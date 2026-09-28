"""Fase 6 (ADR-0009) di Fonte 25 - ETSI TS 119 312 V2.1.1 (2026-06),
"Electronic Signatures and Trust Infrastructures (ESI); Cryptographic Suites".
Capitolo virtuale: solo RELAZIONI. Nessuna relazione *nativa* in questa fonte:
TS 119 312 non cita nessuna delle fonti gia' censite, cita IETF RFC, FIPS e
ISO/IEC (nessuna censita) e altri standard ETSI non censiti (EN 319 122,
EN 319 132, EN 319 142, TS 101 733, TS 101 903, TS 102 778, TS 102 176-1).

## Il giro che conta e' in direzione inversa (come per il Codice Civile)

Il contributo di questo import non e' quello che la fonte nuova dice delle
vecchie, ma quello che le fonti **gia' censite** dicono di questa: 20 nodi in 7
Fonti richiamano espressamente ETSI TS 119 312. Fino a oggi quei rinvii non
potevano produrre relazioni (nessun nodo controparte) e restavano muti nel
grafo: e' il caso che l'ADR-0009 non copre, perche' la sua pipeline guarda
"fonte nuova -> fonti esistenti". Ricognizione: query su tutti i nodi con
`testo_integrale` contenente "119 312", con etichetta di quale delle tre fonti
in arrivo (119 312, 119 101, 319 102) ciascun nodo cita, per non attribuire a
questa fonte citazioni che appartengono alle altre.

## Esito: 21 relazioni, tutte "richiama" e tutte su citazione letterale

Il bersaglio e' la clausola di TS 119 312 che contiene la risposta alla
domanda del nodo citante, non la clausola il cui numero coincide: le citazioni
piu' vecchie usano la numerazione della V1.x (annessi A.8/A.9, clausola 11),
mentre la versione importata ha rinumerato in clausole 5, 6, 7, 9 e 10. Dove
il numero coincide (l'antica clausola 9.3 per le lunghezze di chiave) la
corrispondenza e' anche numerica; dove non coincide, l'aggancio e' per
contenuto. Mai per numero.

Tipo "richiama" (non "attua" ne' "specifica"): il nodo citante rinvia a una
norma esterna per il parametro tecnico, senza attuarne il contenuto ne'
rendere operative le sue clausole.

| nodo citante (fonte) | -> nodo di TS 119 312 | perche' |
|---|---|---|
| 7 Parte 2 GEN-4.2.2-1 | clausola 7.3 (Signature suites) | algoritmo di firma del certificato: la risposta e' la tabella delle suite |
| 7 Parte 2 GEN-4.2.5-1 | clausola 6.3 (Key generation) | chiave pubblica del soggetto |
| 10 REQ-7.5-05 | clausola 1 (Scope) | rinvio generico agli standard riconosciuti, senza clausola |
| 11 Parte 2 OVR-8.2-02 | clausola 7.3 (Signature suites) | algoritmi crittografici ammessi |
| 17 Parte 1 GEN-6.5.1-06 | clausola 6.3 (Key generation) | generazione della coppia di chiavi della CA |
| 17 Parte 1 GEN-6.5.1-07 | clausola 6.3 (Key generation) | lunghezza della chiave di firma della CA |
| 17 Parte 1 GEN-6.5.1-13B | clausola 6.3 (Key generation) | chiavi pre-generate |
| 17 Parte 1 SDP-6.5.1-18 | clausola 6.3 (Key generation) | chiavi del soggetto generate dalla CA |
| 18 TIS-7.6.2-05 | clausola 6.3 (Key generation) | generazione della chiave della TSU |
| 18 TIS-7.6.7-03 | clausola 9.3 (Time period resistance for signer's key) | "recommended key sizes versus time" (nell'antica numerazione un annesso; qui clausola 9.3) |
| 19 4.1.3 (Hash algorithms to be used) | clausola 5.1 (General) | funzioni di hash, citate come "clause A.8" |
| 19 4.2.3 (Algorithms to be supported) | clausola 7.3 (Signature suites) | algoritmi di firma, citati come "clause A.8" |
| 19 4.2.4 (Key lengths to be supported) | clausola 9.3 (Time period resistance for signer's key) | cita "clause 9.3": numero coincidente |
| 19 5.1.3 (Algorithms to be supported) | clausola 5.1 (General) | idem 4.1.3 |
| 19 5.2.3 (Algorithms to be used) | clausola 5.1 (General) e clausola 7.3 (Signature suites) | la clausola copre hash e algoritmi di firma: due relazioni |
| 19 6.3 (Key lengths requirements) | clausola 9.3 (Time period resistance for signer's key) | cita "clause 9.3" |
| 19 6.5 (Algorithm requirements) | clausola 10.2.4 (Signature algorithms) | algoritmi citati come "clause A.9", che nella V1.x era la tabella degli OID |
| 19 8 (Object identifiers of the cryptographic algorithms) | clausola 10.2.2 (Hash functions) e clausola 10.2.4 (Signature algorithms) | cita "clause 11", la clausola degli OID nella V1.x: due relazioni, hash e firma |
| 21 5.7.1 (Digitally signed Trusted List) | clausola 7.3 (Signature suites) | algoritmo di firma dell'elenco di fiducia |

## Proposte valutate e scartate

- **Direzione diretta (KNN)**: 57 coppie candidate a soglia 0.88. Il resto era
  o lo stesso fatto gia' modellato dalle citazioni inverse (Annex A.10 -> Fonte
  18, clausola 6.2.1 -> Fonte 19, ecc.), o boilerplate ("clausola 3.1 (Terms)"
  contro le clausole dei termini di altri standard), o affinita' tematica
  verificata e scartata: le coppie "Annex B (Signature maintenance)" verso
  Fonte 4 art. 56 c.1 lett.d/e, Fonte 3 art. 35 c.2, Fonte 13 art. 11 - lette
  nel testo, riguardano l'integrita' e l'evidenza della firma al momento
  dell'apposizione, non la manutenzione della validita' nel tempo, che e'
  l'oggetto dell'Annex B.
- **Citazioni lasciate senza relazione perche' prive di bersaglio puntuale**:
  Fonte 11 Parte 2 "Annex C" (tabella informativa di mapping, il rinvio a
  TS 119 312 e' in elenco bibliografico); Fonte 17 Parte 1 "clausola 2.2
  (Informative references)" (bibliografia); Fonte 17 Parte 1 OVR-6.3.5-01
  (menzione dentro un elenco di obblighi del sottoscrittore, senza indicare
  quale parametro crittografico ne dipende).
- **Nessuna relazione verso le fonti censite in direzione diretta**: le
  clausole di TS 119 312 rinviano a IETF RFC, FIPS, ISO/IEC e a standard ETSI
  non censiti (vedi elenco in testa). Sono norme esterne al censimento, non
  relazioni omesse.

## Limite noto

Le 20 citazioni inverse sono state ricostruite sul testo delle fonti gia'
censite, non su quello di TS 119 312: se una clausola della V1.x citata non ha
un corrispondente riconoscibile nella V2.1.1 (rinumerazione del 2026), la
relazione e' agganciata alla clausola piu' vicina per contenuto e la scelta e'
annotata nella tabella qui sopra. Riverificare questo modulo se e quando il
censimento importera' anche la V1.x o gli standard AdES (EN 319 122/132/142),
che sono il bersaglio di gran parte dei rinvii interni di questa fonte.
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = []

MAPPATURA_LOCALE = {}

RELAZIONI = [
    # --- Fonte 7 (ETSI EN 319 412, Parte 2) -------------------------------
    {
        'nodo_da': ('obbligo', 7, 'Parte 2: GEN-4.2.2-1'),
        'nodo_a': ('obbligo', None, 'clausola 7.3 (Signature suites)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.8,
    },
    {
        'nodo_da': ('obbligo', 7, 'Parte 2: GEN-4.2.5-1'),
        'nodo_a': ('obbligo', None, 'clausola 6.3 (Key generation)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.8,
    },
    # --- Fonte 10 (ETSI EN 319 401) ---------------------------------------
    {
        'nodo_da': ('obbligo', 10, 'REQ-7.5-05'),
        'nodo_a': ('principio', None, 'clausola 1 (Scope)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.8,
    },
    # --- Fonte 11 (ETSI TS 119 431, Parte 2) ------------------------------
    {
        'nodo_da': ('obbligo', 11, 'Parte 2: OVR-8.2-02'),
        'nodo_a': ('obbligo', None, 'clausola 7.3 (Signature suites)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.8,
    },
    # --- Fonte 17 (ETSI EN 319 411, Parte 1) ------------------------------
    {
        'nodo_da': ('principio', 17, 'Parte 1: GEN-6.5.1-06'),
        'nodo_a': ('obbligo', None, 'clausola 6.3 (Key generation)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('principio', 17, 'Parte 1: GEN-6.5.1-07'),
        'nodo_a': ('obbligo', None, 'clausola 6.3 (Key generation)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', 17, 'Parte 1: GEN-6.5.1-13B'),
        'nodo_a': ('obbligo', None, 'clausola 6.3 (Key generation)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('principio', 17, 'Parte 1: SDP-6.5.1-18'),
        'nodo_a': ('obbligo', None, 'clausola 6.3 (Key generation)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.8,
    },
    # --- Fonte 18 (ETSI EN 319 421) ---------------------------------------
    {
        'nodo_da': ('obbligo', 18, 'TIS-7.6.2-05'),
        'nodo_a': ('obbligo', None, 'clausola 6.3 (Key generation)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.8,
    },
    {
        'nodo_da': ('obbligo', 18, 'TIS-7.6.7-03'),
        'nodo_a': ('obbligo', None, "clausola 9.3 (Time period resistance for signer's key)"),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    # --- Fonte 19 (ETSI EN 319 422, numerazione V1.x: A.8/A.9/11) ---------
    {
        'nodo_da': ('obbligo', 19, 'clausola 4.1.3 (Hash algorithms to be used)'),
        'nodo_a': ('obbligo', None, 'clausola 5.1 (General)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('obbligo', 19, 'clausola 4.2.3 (Algorithms to be supported)'),
        'nodo_a': ('obbligo', None, 'clausola 7.3 (Signature suites)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('obbligo', 19, 'clausola 4.2.4 (Key lengths to be supported)'),
        'nodo_a': ('obbligo', None, "clausola 9.3 (Time period resistance for signer's key)"),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', 19, 'clausola 5.1.3 (Algorithms to be supported)'),
        'nodo_a': ('obbligo', None, 'clausola 5.1 (General)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('obbligo', 19, 'clausola 5.2.3 (Algorithms to be used)'),
        'nodo_a': ('obbligo', None, 'clausola 5.1 (General)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('obbligo', 19, 'clausola 5.2.3 (Algorithms to be used)'),
        'nodo_a': ('obbligo', None, 'clausola 7.3 (Signature suites)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('obbligo', 19, 'clausola 6.3 (Key lengths requirements)'),
        'nodo_a': ('obbligo', None, "clausola 9.3 (Time period resistance for signer's key)"),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', 19, 'clausola 6.5 (Algorithm requirements)'),
        'nodo_a': ('obbligo', None, 'clausola 10.2.4 (Signature algorithms)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('principio', 19, 'clausola 8 (Object identifiers of the cryptographic algorithms)'),
        'nodo_a': ('obbligo', None, 'clausola 10.2.2 (Hash functions)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('principio', 19, 'clausola 8 (Object identifiers of the cryptographic algorithms)'),
        'nodo_a': ('obbligo', None, 'clausola 10.2.4 (Signature algorithms)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.75,
    },
    # --- Fonte 21 (ETSI TS 119 612) ---------------------------------------
    {
        'nodo_da': ('obbligo', 21, 'clausola 5.7.1 (Digitally signed Trusted List)'),
        'nodo_a': ('obbligo', None, 'clausola 7.3 (Signature suites)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.65,
    },
]
