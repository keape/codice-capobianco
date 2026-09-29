"""Fase 6 (ADR-0009 + ADR-0012) di Fonte 32 - ETSI EN 319 132-1 V1.3.1 (2024-07),
"Electronic Signatures and Infrastructures (ESI); XAdES digital signatures; Part 1:
Building blocks and XAdES baseline signatures". Capitolo virtuale: solo RELAZIONI,
nessun nodo proprio.

Le relazioni *interne* di ciascun capitolo (124 in totale) stanno nei moduli cap01-cap10.

## Pipeline eseguita (2026-09-29, sessione principale)

Stadio 1 - candidati a zero token LLM:
(a) citazioni interne di clausola/annesso lette nel `testo_integrale` di ogni riga
    ("clause 5.7", "see clause 4.5", "Annex C", "clause E.1.3"), risolte con la regola di
    miraggio dell'ADR-0012: il nodo della clausola se esiste come riga, altrimenti la
    partizione padre piu' specifica (`clausola 5.5`, `Annex A, clausola A.1`) e in ultima
    istanza l'annesso (`Annex A`). I bersagli interni al modulo citante sono saltati (li
    hanno gia' dichiarati i worker). Esito: 92 relazioni.
(b) direzione inversa (Fonti gia' censite -> questa Fonte): query su Neo4j per i nodi il
    cui `testo_integrale` nomina "319 132" o "XAdES": 53 nodi, ancorati alla
    partizione `clausola 1 (Scope)` perche' il rinvio e' allo standard come insieme.
(c) candidati KNN (`app/tools/fase6_candidati_knn.py`, soglia 0.86) lanciati in
    background sull'intero standard: **esito non ancora incorporato in questo modulo**.
    Per CAdES il giro KNN su 434 coppie aveva prodotto 5 relazioni utili, e gran parte dei
    candidati era rumore da titoli di clausola identici fra standard diversi; le eventuali
    corrispondenze di istituto di XAdES saranno aggiunte in una passata successiva e
    documentate qui.

Stadio 2 - classificazione nella sessione principale, leggendo le controparti in Neo4j
prima di decidere.

Stadio 3 - validazione: ogni `riferimento` proposto risolto contro l'indice delle righe
della Fonte o contro le sue partizioni (`preflight_relazioni.py 32`, che risolve anche i
bersagli di tipo partizione).

## Esito: 150 relazioni

- **92 cross-capitolo o verso annessi** (`richiama`, `textual`, 0.80): citazioni
  letterali di clausole e annessi del medesimo standard. I capitoli piu' citati sono la
  clausola 5 (qualifying properties) e la clausola 4 (sintassi dei container); fra gli
  annessi, l'Annex A (schemi e attributi aggiuntivi) e l'Annex C (elementi obbligatori nei
  profili baseline).
- **53 in direzione inversa** (`richiama`, `textual`, 0.85): nodi gia' censiti che
  nominano questa norma.

## Rinvii lasciati senza relazione (dichiarati, non omessi per svista)

- Norme esterne, citate dallo standard: W3C XML Signature e XML Canonicalization, W3C XML
  Schema, IETF RFC 3161 e 5035, RFC 5280, ISO/IEC 10118, ETSI EN 319 102-1, EN 319 122-1
  (CAdES), EN 319 132-2, TS 119 312, TR 119 100, eIDAS (Reg. UE 910/2014) come quadro
  giuridico. Alcune sono gia' censite (Fonte 27 = EN 319 102-1, Fonte 25 = TS 119 312,
  Fonte 31 = CAdES): i rinvii puntuali a quelle norme sono materia del giro KNN e della
  direzione inversa, non di questo estrattore, che risolve solo i riferimenti interni.
- I riferimenti bibliografici della clausola 2 (18 normativi e 22 informativi) sono
  paratesto escluso dal censimento, non rinvii omessi.
- L'"Annex F (Change History)" e' censito come riga informativa dai moduli di capitolo:
  non genera ne' riceve archi.
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
        "nodo_da": ("principio", None, "clausola 3.4 (Terminology)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.6 (The SignerRoleV2 qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 4.2 (XML Namespaces)"),
        "nodo_a": ("partizione", None, "Annex C"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 4.3.6 (The UnsignedSignatureProperties container)"),
        "nodo_a": ("partizione", None, "clausola 5.5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 4.3.7 (The UnsignedDataObjectProperties container)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.1 (The AnyType data type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.4.3 (The GenericTimeStampType data type)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.4.3 (The GenericTimeStampType data type)"),
        "nodo_a": ("partizione", None, "clausola 5.1.4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.4.4.1 (Semantics and syntax)"),
        "nodo_a": ("partizione", None, "clausola 5.1.4.4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.4.4.2.3 (Processing model for Include element)"),
        "nodo_a": ("partizione", None, "clausola 4.4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.4.4.2.3 (Processing model for Include element)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.1.4.5 (The OtherTimeStampType data type)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.7.2 (Enveloped countersignatures: the CounterSignature qualifying property)"),
        "nodo_a": ("partizione", None, "clausola 5.5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.7.2 (Enveloped countersignatures: the CounterSignature qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.6 (The AnyValidationData qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.8.1 (The AllDataObjectsTimeStamp qualifying property)"),
        "nodo_a": ("partizione", None, "clausola 4.4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.8.1 (The AllDataObjectsTimeStamp qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "clausola 5.1.4.2 (Containers for electronic time-stamps)"),
        "nodo_a": ("partizione", None, "Annex A"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.8.2 (The IndividualDataObjectsTimeStamp qualifying property)"),
        "nodo_a": ("partizione", None, "clausola 4.4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.2.8.2 (The IndividualDataObjectsTimeStamp qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.3 (The SignatureTimeStamp qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.1.2 (Use of URI attribute)"),
        "nodo_a": ("partizione", None, "clausola 4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.1 (Semantics and syntax)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.7.1 (Countersignature identifier in Type attribute of ds:Reference)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.2 (Generation and incorporation of ArchiveTimeStamp)"),
        "nodo_a": ("partizione", None, "clausola 5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.2 (Generation and incorporation of ArchiveTimeStamp)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.3 (Computation of the message digest for not distributed case)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.2 (Generation and incorporation of ArchiveTimeStamp)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.4 (Computation of the message digest for distributed case)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "clausola 5.4.1 (Introduction)"),
        "nodo_a": ("partizione", None, "clausola 5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3 (Computation of the message digest for not distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.2 (Generation and incorporation of ArchiveTimeStamp)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 3), lettera a)"),
        "nodo_a": ("partizione", None, "clausola 4.4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 3), lettera b)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 3), lettera c)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 4)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 5)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 6)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.3, passo 5) sostitutivo in convalida"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.4 (Computation of the message digest for distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.2 (Generation and incorporation of ArchiveTimeStamp)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.4, passo 5)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.2.4, passo 5) sostitutivo in convalida"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3, requisito 1) (NewSDODigestValue)"),
        "nodo_a": ("partizione", None, "clausola 4.4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 5.5.3, convalida della firma, passo 3)"),
        "nodo_a": ("partizione", None, "clausola 4.4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("partizione", None, "clausola 4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 4.4.1 (General requirements)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 4.4.3 (The QualifyingPropertiesReference element)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("partizione", None, "clausola 4.4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.1 (The SigningTime qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.2 (The SigningCertificateV2 qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.4 (The DataObjectFormat qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.6 (The SignerRoleV2 qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.3 (The CommitmentTypeIndication qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.5 (The SignatureProductionPlaceV2 qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.7.2 (Enveloped countersignatures: the CounterSignature qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.8.1 (The AllDataObjectsTimeStamp qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.8.2 (The IndividualDataObjectsTimeStamp qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("partizione", None, "clausola 5.2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.10 (The SignaturePolicyStore qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.3 (The SignatureTimeStamp qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.2 (The CertificateValues qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.6 (The AnyValidationData qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.4 (The AttrAuthoritiesCertValues qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.3 (The RevocationValues qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.5 (The AttributeRevocationValues qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("partizione", None, "clausola 5.5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3, requisito addizionale g)"),
        "nodo_a": ("partizione", None, "clausola 6"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3, requisito addizionale p)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.2 (The CertificateValues qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3, requisito addizionale r)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.4 (The AttrAuthoritiesCertValues qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3, requisito addizionale t)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.3 (The RevocationValues qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "clausola 6.3, requisito addizionale w)"),
        "nodo_a": ("obbligo", None, "clausola 5.4.5 (The AttributeRevocationValues qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "clausola 6.1 (Signature levels)"),
        "nodo_a": ("partizione", None, "Annex C"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.1 (The CompleteCertificateRefsV2 qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.2 (The SigningCertificateV2 qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.2 (The CompleteRevocationRefs qualifying property)"),
        "nodo_a": ("partizione", None, "clausola 4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.5.1.2 (Not distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.5.1.3 (Distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4.4.2.1 (Semantics and syntax)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.5.1.3 (Distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.5.2.2 (Not distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.5.2.3 (Distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4.4.2.1 (Semantics and syntax)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.1.5.2.3 (Distributed case)"),
        "nodo_a": ("obbligo", None, "clausola 4.5 (Managing canonicalization of XML nodesets)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex A, clausola A.2.2 (The RenewedDigests qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
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
        "nodo_da": ("obbligo", None, "Annex D (Deprecated qualifying properties)"),
        "nodo_a": ("obbligo", None, "clausola 6.4 (Legacy XAdES baseline signatures)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D (Deprecated qualifying properties)"),
        "nodo_a": ("partizione", None, "Annex D"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D, punto 1) (The SigningCertificate qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.2 (The SigningCertificateV2 qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D, punto 2) (The SignatureProductionPlace qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.5 (The SignatureProductionPlaceV2 qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("obbligo", None, "Annex D, punto 3) (The SignerRole qualifying property)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.6 (The SignerRoleV2 qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex E (Change history)"),
        "nodo_a": ("obbligo", None, "clausola 5.1.4.3 (The GenericTimeStampType data type)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex E (Change history)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.4 (The DataObjectFormat qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex E (Change history)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.8.1 (The AllDataObjectsTimeStamp qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex E (Change history)"),
        "nodo_a": ("obbligo", None, "clausola 5.2.8.2 (The IndividualDataObjectsTimeStamp qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex E (Change history)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.2 (Generation and incorporation of ArchiveTimeStamp)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex E (Change history)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.3 (The RenewedDigestsV2 qualifying property)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex E (Change history)"),
        "nodo_a": ("obbligo", None, "clausola 6.3 (Requirements on XAdES signature's elements, qualifying properties and services)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex E (Change history)"),
        "nodo_a": ("partizione", None, "clausola 5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex E (Change history)"),
        "nodo_a": ("principio", None, "clausola 5.4.1 (Introduction)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex E (Change history)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.2.1 (Semantics and syntax)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },
    {
        "nodo_da": ("principio", None, "Annex E (Change history)"),
        "nodo_a": ("partizione", None, "Annex E"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.80,
    },

    # --- cross-fonte: candidati KNN giudicati sulla lettura delle controparti --

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
    {
        "nodo_da": ("obbligo", 31, "Annex A.1.3 (The attribute-certificate-references attribute)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 31, "Annex A.1.4 (The attribute-revocation-references attribute)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 31, "Annex A.1.5.2 (The CAdES-C-timestamp attribute)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 31, "Annex B (Alternative mechanisms for long term availability and integrity of validation data)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 31, "Annex D, id-aa-ets-escTimeStamp (CAdES-C-timestamp attribute, clause A.1.5.2)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 31, "Annex D, modulo ETSI-CAdES-19122v121 (intestazione, EXPORTS e IMPORTS)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 31, "Annex D, modulo ETSI-CAdES-ExplicitSyntax97 (intestazione, EXPORTS e IMPORTS)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 31, "Annex E, clause E.2.2 (Using application/pkcs7-mime)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 31, "Annex E, clause E.2.3 (Using multipart/signed and application/pkcs7-signature)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 31, "Annex E, clause E.3 (Use of MIME in the signature)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 31, "Annex F (Change History)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 31, "clausola 1 (Scope)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 31, "clausola 3.1 (Terms)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 31, "clausola 4.1 (General requirements)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 31, "clausola 4.9 (Attributes)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 31, "clausola 5.2.7 (The countersignature attribute)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 31, "clausola 5.5.2 (The ats-hash-index-v3 attribute)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 31, "clausola 5.5.3 (The archive-time-stamp-v3 attribute)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 31, "clausola 6.1 (Signature levels)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", 31, "clausola 6.2.2 (Notation for requirements)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 31, "clausola 6.3 (Requirements on components and services)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 31, "clausola 6.3, requisito addizionale k)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("obbligo", 31, "clausola 6.4 (Legacy CAdES baseline signatures)"),
        "nodo_a": ("principio", None, "clausola 1 (Scope)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
]
