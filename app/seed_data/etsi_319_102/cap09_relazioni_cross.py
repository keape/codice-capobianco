"""Fase 6 (ADR-0009) di Fonte 27 - ETSI EN 319 102-1 V1.4.1 (2024-06),
"Electronic Signatures and Infrastructures (ESI); Procedures for Creation and
Validation of AdES Digital Signatures; Part 1: Creation and Validation".
Capitolo virtuale: solo RELAZIONI.

Nessuna relazione *nativa*: il documento cita IETF RFC, ISO/IEC, FIPS, altri
standard ETSI (EN 319 122/132/142, TS 119 172, EN 319 401, TS 119 612) e
nessuna fonte censita in modo diretto... con una eccezione importante e
verificata: le fonti gia' censite che citano *questa*, vedi sotto.

## Il giro che conta e' in direzione inversa (terzo caso del lotto)

Ricognizione: query su tutti i nodi con `testo_integrale` contenente "319 102",
con etichetta di quale delle tre fonti ETSI in arrivo ciascun nodo cita. Nove
nodi in tre Fonti (9, 19, 20) richiamano EN 319 102-1; i rinvii restavano muti
per assenza di nodo controparte. E' lo stesso fenomeno gia' trattato per Fonte
25 (ETSI TS 119 312, 21 relazioni) e Fonte 26 (ETSI TS 119 101, 14): la
pipeline di ADR-0009 guarda solo "fonte nuova -> fonti esistenti".

## Esito: 9 relazioni, tutte "richiama" su citazione letterale

| nodo citante | -> nodo di EN 319 102-1 | citazione |
|---|---|---|
| 9 VAL-8.3.2-02 (O) | clausola 5.1.3 (Status indication ...) | "the validation result is TOTAL-PASSED as defined by ETSI EN 319 102-1" |
| 9 VAL-8.3.5-00 (P) | clausola 5.1.3 (Status indication ...) | idem: il risultato di convalida e' quello definito da questo standard |
| 19 clausola 1 (Scope) (P) | clausola 1 (Scope) | menzione della norma nell'ambito di EN 319 422 |
| 20 clausola 1 (Scope) (P) | clausola 4.1 (Signature creation model) | "the process of creating AdES digital signatures as defined by ETSI EN 319 102-1" |
| 20 clausola 4.1 (Signature creation process steps and data elements) (P) | clausola 4.2.1 (Introduction) | "Figure 1 (derived from ETSI EN 319 102-1 [i.12], clause 4.2.1)" - citazione di sottoclavola esatta |
| 20 Annex A.1 (Overview) (P) | clausola 4.1 (Signature creation model) | "This profile assumes AdES signature creation processing (PAdES/XAdES/CAdES/JAdES) per ETSI EN 319 102-1" |
| 20 Annex A.7.3 (EUDIW processing) (P) | clausola 4.2.6 (Data To Be Signed (DTBS)) | "DTBS/DTBSR definitions according to ETSI EN 319 102.1" |
| 20 Annex A.7.3 (EUDIW processing) (P) | clausola 4.2.8 (Data To Be Signed Representation (DTBSR)) | idem: la citazione nomina entrambe le definizioni |
| 20 Annex A.10 (Security & privacy requirements) (O) | clausola 1 (Scope) | "AdES: signature formats and conformance levels follow ETSI EN 319 102-1" - rinvio alla norma nel suo insieme, non a una clausola |

Le due relazioni da "clausola 4.1" di TS 119 432 (Fonte 20) sono un caso di
**citazione di sottoclavola** ("clause 4.2.1"): il bersaglio e' la clausola
citata, non quella che si chiama allo stesso modo. Il resto sono rinvii alla
norma nel suo insieme, agganciati alla clausola 1 (Scope) come capostipite -
stesso criterio usato per le citazioni generiche di Fonte 25.

## Proposte valutate e scartate

- Fonte 20 "Annex A.12.2 (Example 'qesRequest')" e "Annex B.1 (Overview)":
  la menzione di EN 319 102-1 cade dentro un esempio di payload JSON o in un
  elenco di allineamenti (CSC DM, EN 419 241-1), senza indicare quale
  requisito ne dipende. Scartate: agganciarle a una clausola sarebbe una
  scelta arbitraria.
- Nessuna relazione in direzione diretta in questo modulo: vedi sotto.

## Nota sul giro KNN

Il giro in direzione diretta su questa Fonte (oltre 200 nodi) produce uno
shortlist dominato dal lessico comune degli standard ETSI (DTBS, SDO,
certificato, convalida) e va classificato con lo stesso criterio restrittivo
usato per le altre fonti del lotto: sono state accettate solo le coppie in cui
le due prescrizioni hanno lo stesso oggetto, non quelle in cui il vocabolario
coincide. L'esito e' riportato nel rapporto di import; le corrispondenze
sostanziali di questa Fonte sono quelle per citazione letterale elencate sopra.

## Limite noto

EN 319 102-1 e' un deliverable multi-parte: il censimento copre oggi la sola
Parte 1 (Creation and Validation). I `riferimento` di questa Fonte non portano
prefisso di parte (decisione documentata in
docs/plan-import-lotto-eidas2-standard.md, sezione "Decisione presa in corso
d'import"): se si importera' TS 119 102-2 nella stessa Fonte, il prefisso
"Parte 1: "/"Parte 2: " va aggiunto anche ai nodi citati dalle relazioni di
questo modulo, altrimenti le due Parti diventano indistinguibili.
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = []

MAPPATURA_LOCALE = {}

RELAZIONI = [
    # --- Fonte 9 (ETSI TS 119 461): il risultato di convalida e' quello
    #     definito da questo standard ----------------------------------------
    {
        'nodo_da': ('obbligo', 9, 'VAL-8.3.2-02'),
        'nodo_a': ('obbligo', None, 'clausola 5.1.3 (Status indication of the signature validation process and signature validation report)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('principio', 9, 'VAL-8.3.5-00'),
        'nodo_a': ('obbligo', None, 'clausola 5.1.3 (Status indication of the signature validation process and signature validation report)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    # --- Fonte 19 (ETSI EN 319 422) ---------------------------------------
    {
        'nodo_da': ('principio', 19, 'clausola 1 (Scope)'),
        'nodo_a': ('principio', None, 'clausola 1 (Scope)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.6,
    },
    # --- Fonte 20 (ETSI TS 119 432) ---------------------------------------
    {
        'nodo_da': ('principio', 20, 'clausola 1 (Scope)'),
        'nodo_a': ('obbligo', None, 'clausola 4.1 (Signature creation model)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.8,
    },
    {
        'nodo_da': ('principio', 20, 'clausola 4.1 (Signature creation process steps and data elements)'),
        'nodo_a': ('principio', None, 'clausola 4.2.1 (Introduction)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('principio', 20, 'Annex A.1 (Overview)'),
        'nodo_a': ('obbligo', None, 'clausola 4.1 (Signature creation model)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('principio', 20, 'Annex A.7.3 (EUDIW processing)'),
        'nodo_a': ('obbligo', None, 'clausola 4.2.6 (Data To Be Signed (DTBS))'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.8,
    },
    {
        'nodo_da': ('principio', 20, 'Annex A.7.3 (EUDIW processing)'),
        'nodo_a': ('obbligo', None, 'clausola 4.2.8 (Data To Be Signed Representation (DTBSR))'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.8,
    },
    {
        'nodo_da': ('obbligo', 20, 'Annex A.10 (Security & privacy requirements)'),
        'nodo_a': ('principio', None, 'clausola 1 (Scope)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.6,
    },
]
