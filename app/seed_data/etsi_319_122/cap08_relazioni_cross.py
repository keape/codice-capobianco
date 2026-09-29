"""Fase 6 (ADR-0009 + ADR-0012) di Fonte 31 - ETSI EN 319 122-1 V1.3.1 (2023-06),
"Electronic Signatures and Infrastructures (ESI); CAdES digital signatures; Part 1:
Building blocks and CAdES baseline signatures". Capitolo virtuale: solo RELAZIONI,
nessun nodo proprio.

Le relazioni *interne* di ciascun capitolo (50 in totale, tutte fra righe dello stesso
modulo) stanno nei moduli cap01-cap07.

## Pipeline eseguita (2026-09-29, sessione principale)

Stadio 1 - candidati a zero token LLM:
(a) citazioni interne di clausola/annesso lette nel `testo_integrale` di ogni riga
    ("clause 5.4.2", "see clause 4.7.1", "Annex A.1.1.1", "Annex E"), risolte con la
    regola di miraggio dell'ADR-0012: se la clausola citata esiste come riga il
    bersaglio e' il nodo, altrimenti la partizione padre piu' specifica
    (`clausola 5.4`, `Annex A, clausola A.1`) e in ultima istanza l'annesso (`Annex A`).
    I bersagli interni al modulo che dichiara la citazione sono saltati: li hanno gia'
    dichiarati i worker nelle loro RELAZIONI. Esito: 100 relazioni.
(b) direzione inversa (Fonti gia' censite -> questa Fonte), con query su Neo4j per i
    nodi il cui `testo_integrale` nomina "319 122" o "CAdES": 30 nodi.
(c) candidati KNN (`app/tools/fase6_candidati_knn.py`, 434 coppie a soglia 0.84) letti
    e filtrati a mano. La maggioranza e' rumore da titoli di clausola identici fra
    standard diversi ("clausola 3.2 (Symbols)", "clausola 3.1 (Terms)": il lessico di
    cornice si ripete identico in ogni standard ETSI). Sono state tenute le cinque
    coppie che descrivono lo stesso istituto tecnico, verificate leggendo entrambe le
    parti (attributi CAdES definiti qui e elencati come attributi da elaborare nella
    convalida di Fonte 27; CRL in Fonte 25; moduli ASN.1 di dichiarazioni in Fonte 7).

Stadio 2 - classificazione nella sessione principale, leggendo le controparti in Neo4j
prima di decidere.

Stadio 3 - validazione: ogni `riferimento` proposto risolto contro l'indice delle righe
della Fonte o contro le sue partizioni (`preflight_relazioni.py 31`, che ora risolve
anche i bersagli di tipo partizione).

## Esito: 135 relazioni

- **100 cross-capitolo o verso annessi** (`richiama`, `textual`, 0.80): citazioni
  letterali di clausole e annessi del medesimo standard. Il capitolo piu' citato e' la
  clausola 5 (semantica e sintassi degli attributi) e la clausola 6 (requisiti delle
  firme baseline); fra gli annessi, il piu' citato e' l'Annex D (definizioni ASN.1 e
  OID), che e' il dizionario dei tipi usati da tutto il documento.
- **5 cross-fonte** (`si sovrappone a`, `inferred`, 0.65-0.70): attributi CAdES definiti
  qui e richiamati come attributi da elaborare in fase di convalida da ETSI EN 319 102-1
  (commitment-type-indication, signature-policy-store, signer-attributes-v2), la sezione
  sulle CRL di ETSI TS 119 312, i moduli ASN.1 di dichiarazioni di ETSI EN 319 412-5.
  Nessuna e' una citazione: sono corrispondenze di istituto, quindi `inferred`.
- **30 in direzione inversa** (`richiama`, `textual`, 0.85): nodi gia' censiti che
  nominano questa norma. Il bersaglio e' la partizione dell'oggetto e dell'ambito
  (`clausola 1 (Scope)`), perche' quei rinvii indicano lo standard come insieme e non una
  sua clausola.

## Rinvii lasciati senza relazione (dichiarati, non omessi per svista)

- Norme esterne non censite, citate dallo standard: IETF RFC 5652 (CMS), RFC 3161 e 5816
  (marca temporale e TSA), RFC 5280 e 4998, RFC 5035, ITU-T X.680/X.690, ISO/IEC 10118,
  ETSI TS 101 733 e TR 119 001/119 100, ETSI EN 319 122-2, eIDAS (Reg. UE 910/2014) come
  quadro giuridico. Nessuna ha un nodo controparte.
- I riferimenti bibliografici della clausola 2 (39 voci fra normative e informative) sono
  esclusi dal censimento come paratesto, non come rinvii omessi: sono l'elenco delle opere
  citate, non disposizioni.
- Il "Change History" (Annex F) e' censito come riga informativa (scelta del worker,
  documentata nel modulo): non genera ne' riceve archi.
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = []

MAPPATURA_LOCALE = {}

RELAZIONI = []

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = []

MAPPATURA_LOCALE = {}

RELAZIONI = [
    # --- cross-capitolo e annessi (ADR-0012: nodo se la clausola esiste come riga,
    # --- altrimenti partizione padre piu' specifica) -------------------
    {
        "nodo_da": ("principio", None, "clausola 3.3 (Abbreviations)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (The archive-time-stamp-v3 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 4.1 (General requirements)"),
        "nodo_a": ("partizione", None, "clausola 5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 4.4 (The SignedData type)"),
        "nodo_a": ("partizione", None, "clausola 5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 4.5 (The EncapsulatedContentInfo type)"),
        "nodo_a": ("partizione", None, "clausola 5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 4.6 (The SignerInfo type)"),
        "nodo_a": ("obbligo", None, "clausola 5.3 (The signature-time-stamp attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "clausola 4.9 (Attributes)"),
        "nodo_a": ("obbligo", None, "clausola 5.3 (The signature-time-stamp attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.2 (The message-digest attribute)"),
        "nodo_a": ("partizione", None, "clausola 5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.2.2 (ESS signing-certificate attribute)"),
        "nodo_a": ("partizione", None, "clausola 5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.3 (The commitment-type-indication attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.4.1 (The content-hints attribute)"),
        "nodo_a": ("obbligo", None, "clausola 4.2 (The data content type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.4.1 (The content-hints attribute)"),
        "nodo_a": ("partizione", None, "Annex E"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.4.2 (The mime-type attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.4.2 (The mime-type attribute)"),
        "nodo_a": ("partizione", None, "Annex E"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.5 (The signer-location attribute)"),
        "nodo_a": ("partizione", None, "clausola 6"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.5 (The signer-location attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.6.1 (The signer-attributes-v2 attribute)"),
        "nodo_a": ("obbligo", None, "clausola 4.8.2 (Additional types)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.6.1 (The signer-attributes-v2 attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.6.2 (claimed-SAML-assertion)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.6.3 (signed-SAML-assertion)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.8 (The content-time-stamp attribute)"),
        "nodo_a": ("obbligo", None, "clausola 4.8.1 (Time-stamp token format)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.8 (The content-time-stamp attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.9.1 (The signature-policy-identifier attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.9.2 (The SigPolicyQualifierInfo type)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.10 (The signature-policy-store attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3 (The signature-time-stamp attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.2.1 (OCSP response types)"),
        "nodo_a": ("obbligo", None, "clausola 4.8.2 (Additional types)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.2.2 (OCSP responses within RevocationInfoChoices)"),
        "nodo_a": ("obbligo", None, "clausola 4.8.2 (Additional types)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2 (The ats-hash-index-v3 attribute)"),
        "nodo_a": ("obbligo", None, "clausola 4.7.1 (DER)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2 (The ats-hash-index-v3 attribute)"),
        "nodo_a": ("obbligo", None, "clausola 4.4 (The SignedData type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2 (The ats-hash-index-v3 attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The archive-time-stamp-v3 attribute)"),
        "nodo_a": ("obbligo", None, "clausola 4.4 (The SignedData type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The archive-time-stamp-v3 attribute)"),
        "nodo_a": ("partizione", None, "clausola 5.4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The archive-time-stamp-v3 attribute)"),
        "nodo_a": ("obbligo", None, "clausola 4.7.1 (DER)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The archive-time-stamp-v3 attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3 (The archive-time-stamp-v3 attribute)"),
        "nodo_a": ("partizione", None, "Annex B"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 4.4 (The SignedData type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.1 (The content-type attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.2 (The message-digest attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("partizione", None, "clausola 5.2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.2.2 (ESS signing-certificate attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.2.3 (ESS signing-certificate-v2 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.1 (The signing-time attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.3 (The commitment-type-indication attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.4.1 (The content-hints attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.4.2 (The mime-type attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.5 (The signer-location attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.6.1 (The signer-attributes-v2 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.7 (The countersignature attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.8 (The content-time-stamp attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.9.1 (The signature-policy-identifier attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.10 (The signature-policy-store attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.11 (The content-reference attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.12 (The content-identifier attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.13 (The cms-algorithm-protection attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.3 (The signature-time-stamp attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (The archive-time-stamp-v3 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3, requisito addizionale f)"),
        "nodo_a": ("obbligo", None, "clausola 4.2 (The data content type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3, requisito addizionale l)"),
        "nodo_a": ("obbligo", None, "clausola 4.7.1 (DER)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3, requisito addizionale n)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.6.1 (The signer-attributes-v2 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "clausola 6.1 (Signature levels)"),
        "nodo_a": ("partizione", None, "Annex B"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.1.1 (The complete-certificate-references attribute)"),
        "nodo_a": ("partizione", None, "clausola 5.2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.1.1 (The complete-certificate-references attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.1.2 (The certificate-values attribute)"),
        "nodo_a": ("partizione", None, "clausola 5.2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.1.2 (The certificate-values attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.2.1 (The complete-revocation-references attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.2.1 (OCSP response types)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.2.1 (The complete-revocation-references attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.2.2 (The revocation-values attribute)"),
        "nodo_a": ("obbligo", None, "clausola 4.8.2 (Additional types)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.2.2 (The revocation-values attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.2.1 (OCSP response types)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.2.2 (The revocation-values attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.3 (The attribute-certificate-references attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.6.1 (The signer-attributes-v2 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.3 (The attribute-certificate-references attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.4 (The attribute-revocation-references attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.5.1 (The time-stamped-certs-crls-references attribute)"),
        "nodo_a": ("obbligo", None, "clausola 4.7.1 (DER)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.5.1 (The time-stamped-certs-crls-references attribute)"),
        "nodo_a": ("obbligo", None, "clausola 4.8.1 (Time-stamp token format)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.5.1 (The time-stamped-certs-crls-references attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.5.2 (The CAdES-C-timestamp attribute)"),
        "nodo_a": ("obbligo", None, "clausola 4.7.1 (DER)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.5.2 (The CAdES-C-timestamp attribute)"),
        "nodo_a": ("obbligo", None, "clausola 4.8.1 (Time-stamp token format)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.1.5.2 (The CAdES-C-timestamp attribute)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.2.2 (The other-signing-certificate attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.2.3 (ESS signing-certificate-v2 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.2.3 (The signer-attributes attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.6.1 (The signer-attributes-v2 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.2.4 (The archive-time-stamp attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (The archive-time-stamp-v3 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.2.5 (The long-term-validation attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (The archive-time-stamp-v3 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A.2.6 (The ats-hash-index attribute)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2 (The ats-hash-index-v3 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex B (Alternative mechanisms for long term availability and integrity of validation data)"),
        "nodo_a": ("partizione", None, "clausola 5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex B (Alternative mechanisms for long term availability and integrity of validation data)"),
        "nodo_a": ("partizione", None, "Annex A"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D (normative), premessa (precedenza dei moduli ASN.1 e sintassi di interpretazione)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-commitmentType (commitment-type attribute, clause 5.2.3)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.3 (The commitment-type-indication attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-mimeType (mime-type attribute, clause 5.2.4.2)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.4.2 (The mime-type attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-signerLocation (signer-location attribute, clause 5.2.5)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.5 (The signer-location attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-signerAttrV2 (signer-attributes-v2 attribute, clause 5.2.6.1)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.6.1 (The signer-attributes-v2 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-claimedSAML (claimed-SAML-assertion attribute, clause 5.2.6.2)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.6.2 (claimed-SAML-assertion)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-contentTimestamp (content-timestamp attribute, clause 5.2.8)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.8 (The content-time-stamp attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-sigPolicyId (signature-policy-identifier attribute, clause 5.2.9.1)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.9.1 (The signature-policy-identifier attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-sigPolicyStore (signature-policy-store attribute, clause 5.2.10)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.10 (The signature-policy-store attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-signatureTimeStampToken (signature-timestamp attribute, clause 5.3)"),
        "nodo_a": ("obbligo", None, "clausola 5.3 (The signature-time-stamp attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ATSHashIndex-v3 (ats-hash-index-v3 attribute, clause 5.5.2)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2 (The ats-hash-index-v3 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex D, id-aa-ets-archiveTimestampV3 (archive-time-stamp-v3 attribute, clause 5.5.3)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (The archive-time-stamp-v3 attribute)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex E, clause E.2.2 (Using application/pkcs7-mime)"),
        "nodo_a": ("partizione", None, "clausola 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex E, clause E.2.3 (Using multipart/signed and application/pkcs7-signature)"),
        "nodo_a": ("partizione", None, "clausola 3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex F (Change History)"),
        "nodo_a": ("partizione", None, "Annex F"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },

    # --- cross-fonte: candidati KNN giudicati sulla lettura delle controparti --
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.3 (The commitment-type-indication attribute)"),
        "nodo_a": ("obbligo", 27, "clausola 4.2.5.6 (Commitment type indication)"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.70,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.10 (The signature-policy-store attribute)"),
        "nodo_a": ("obbligo", 27, "clausola 4.2.5.4 (Signature policy store)"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.70,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.6.1 (The signer-attributes-v2 attribute)"),
        "nodo_a": ("obbligo", 27, "clausola 4.2.5.10 (Signer's attributes)"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.70,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.4.3 (CRLs)"),
        "nodo_a": ("obbligo", 25, "Annex A.5 (CRLs)"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.70,
    },
    {
        "nodo_da": ("principio", None, "Annex D, modulo ETSI-CAdES-19122v121 (intestazione, EXPORTS e IMPORTS)"),
        "nodo_a": ("principio", 7, "Parte 5: Annex B (dichiarazioni ASN.1)"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "inferred",
        "confidence": 0.65,
    },

    # --- direzione inversa: nodi gia' censiti che citano questa Fonte ----------
    {
        "nodo_da": ("obbligo", 11, "Parte 2: OVR-6.2-07"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 11, "Parte 2: clausola 3.1 (Terms)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 18, "OVR-5.3-01"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 20, "Annex A.1 (Overview)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 20, "Annex A.12.2 (Example 'qesRequest' (transaction_data before base64url encoding))"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 20, "clausola 3.1 (Terms)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 20, "clausola 4.3.2 (DTBS composition and formatting)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 20, "clausola 4.3.4 (SDO composer)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 20, "clausola 5.2.4 (Other authentication mechanisms)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 23, "allegato, punto 3(a), 7.5 REQ-7.5-03"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 25, "Annex A.1 (Introduction)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 25, "Annex A.2 (CAdES and PAdES)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 25, "Annex B (Signature maintenance)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 25, "clausola 3.1 (Terms)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 25, "clausola 6.2.2.6 (SLH-DSA)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 25, "clausola 6.4.2 (Recommended Hybrid Suites)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 25, "clausola 9.1 (General notes)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 25, "clausola 9.4 (Time period resistance for trust anchors)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 26, "SCP 1"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 26, "SVP 1"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 26, "TC 1"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 26, "clausola 3.1 (Definitions)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 27, "Annex B (Signature Classes and AdES Signatures)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 27, "Annex C.2 (Format conformance)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 27, "clausola 1 (Scope)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 27, "clausola 4.1 (Signature creation model)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 27, "clausola 4.2.5.1 (General requirements)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 27, "clausola 4.3.2.4.2 (Signature attribute and parameters selection)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 27, "clausola 5.2.7.4 (Processing)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 28, "allegato IV, punto 2"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
]
