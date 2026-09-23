"""Relazioni cross-fonte DPCM 24/10/2014 (SPID) -> CAD / eIDAS / eIDAS2 / DPCM 22-2-2013 (2026-09-21).

Modulo "capitolo virtuale" (nessuna riga obbligo/principio propria, solo
RELAZIONI) nel senso del contratto di app/seed_data/lib.py:inserisci_capitoli,
usato per collegare i 118 nodi SPID (cap01-cap03) alle fonti gia' presenti nel
grafo al momento in cui viene processato, secondo ADR-0009 (collegamento
cross-fonte a posteriori).

Pipeline di generazione (non ripetere a mano):
1. candidati da citazione testuale esplicita nel testo ufficiale SPID (8
   citazioni dirette al CAD trovate via grep -- art. 64 e commi derivati
   [istituzione SPID/adesione PA/soggetti privati], art. 1 c.1 lett.u-ter
   [definizione "identificazione informatica"], art. 2 c.2 [definizione PA],
   art. 6-bis e art. 57-bis [indici usati per l'accreditamento di diritto dei
   gestori di attributi qualificati]; zero citazioni testuali dirette a
   eIDAS/eIDAS2/DPCM 22-2-2013, decreto anteriore al regolamento eIDAS del
   2014 e non della stessa materia del DPCM 22-2-2013 sulle firme) +
   candidati da similarita' vettoriale (KNN sugli indici
   idxEmbeddingObbligo/Principio gia' popolati da embed_neo4j.py, soglia
   score >= 0.90 -- soglia alta per il dominio lessicale SPID/CAD/eIDAS
   molto ristretto [identita' digitale, autenticazione, accreditamento],
   326 candidati a 0.85 vs 19 a 0.90) -- zero token LLM per questo stadio.
   Unione: 27 coppie candidate (8 testuali, 19 vettoriali).
2. classificazione LLM in 3 batch da 9 coppie (completion() con schema
   JSON, system prompt con la tassonomia di CONTEXT.md ristretta a
   attua/richiama/specifica/si sovrappone a/modifica/deroga a/definisce/
   si applica a/e condizionato da/recepisce, istruito a essere conservativo
   e a proporre confidence piu' bassa quando il nodo target e' una lettera
   "soppressa"/comma "abrogato") sul solo shortlist dello stadio 1, non sul
   prodotto cartesiano SPID x (CAD+eIDAS+eIDAS2+DPCM 22-2-2013).
3. filtro confidence >= 0.5 (rimosse 4 coppie: nessun nesso normativo
   secondo il classificatore), nessun riferimento proposto e' stato
   corretto (tutti verificati esistenti in Neo4j prima di scrivere questo
   file). Esito finale: 23 relazioni (8 verso CAD con evidence_type
   "textual", 15 verso CAD/eIDAS/eIDAS2/DPCM 22-2-2013 con evidence_type
   "inferred").

Nota di modellazione: alcune relazioni "si sovrappone a" puntano a nodi
eIDAS/eIDAS2 esplicitamente marcati come storici nel loro riferimento
(es. "(abrogato, testo originario 2014)"): la sovrapposizione tematica e'
comunque un'informazione utile (mostra la corrispondenza storica tra la
disciplina SPID e la versione dell'obbligo eIDAS vigente all'epoca del
decreto, 2014), riportata con confidence piu' bassa quando pertinente.

Correzione 2026-09-21 (import DPCM 19/10/2021, Fonte 6): il testo di
art. 16 c.3 lett.d) SPID e' stato aggiornato per riportare il riferimento
CAD vigente (art. 6-ter, non piu' art. 57-bis, abrogato dal d.lgs.
179/2016 - la modifica introdotta dallo stesso DPCM 19/10/2021, art. 5).
Su richiesta esplicita dell'utente, la relazione verso l'art. 57-bis non e'
stata rimossa ma mantenuta accanto a quella verso l'art. 6-ter: il nodo CAD
"art. 57-bis" riporta gia' nel proprio testo "ARTICOLO ABROGATO DAL D.LGS.
26 AGOSTO 2016, N. 179", quindi la relazione stessa segnala l'abrogazione
senza bisogno di un campo dedicato; l'utente puo' cosi' vedere sia il
riferimento storico originario sia quello corretto/vigente.
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI = [
    {
        "nodo_da": ('principio', None, 'art. 1 c.1 lett.n)'),
        "nodo_a": ('principio', 3, 'art. 1 c.1 lett.u-ter)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.6,
    },
    {
        "nodo_da": ('principio', None, 'art. 1 c.1 lett.u)'),
        "nodo_a": ('obbligo', 3, 'art. 64 c.2-bis'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
    {
        "nodo_da": ('principio', None, 'art. 2 c.1'),
        "nodo_a": ('obbligo', 3, 'art. 64 c.2-sexies'),
        "tipo_relazione": 'attua',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ('obbligo', None, 'art. 14 c.1'),
        "nodo_a": ('obbligo', 3, 'art. 64 c.2-quater'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
    {
        "nodo_da": ('obbligo', None, 'art. 14 c.2'),
        "nodo_a": ('principio', 3, 'art. 2 c.2'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.75,
    },
    {
        "nodo_da": ('obbligo', None, 'art. 15 c.2'),
        "nodo_a": ('principio', 3, 'art. 64 c.2-quinquies'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
    {
        "nodo_da": ('principio', None, 'art. 16 c.3 lett.a)'),
        "nodo_a": ('obbligo', 3, 'art. 6-bis c.1'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.7,
    },
    {
        "nodo_da": ('principio', None, 'art. 16 c.3 lett.d)'),
        "nodo_a": ('obbligo', 3, 'art. 6-ter c.1'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.6,
    },
    {
        "nodo_da": ('principio', None, 'art. 16 c.3 lett.d)'),
        "nodo_a": ('principio', 3, 'art. 57-bis'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.55,
    },
    {
        "nodo_da": ('principio', None, 'art. 1 c.1 lett.a)'),
        "nodo_a": ('principio', 4, 'art. 1 c.1 lett.c)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.85,
    },
    {
        "nodo_da": ('principio', None, 'art. 1 c.1 lett.g)'),
        "nodo_a": ('principio', 3, 'art. 1 c.1 lett.u-quater)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ('principio', None, 'art. 1 c.1 lett.o)'),
        "nodo_a": ('principio', 3, 'art. 1 c.1 lett.u-quater)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.85,
    },
    {
        "nodo_da": ('principio', None, 'art. 1 c.1 lett.s)'),
        "nodo_a": ('principio', 3, 'art. 64 c.2-ter'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.75,
    },
    {
        "nodo_da": ('obbligo', None, 'art. 7 c.1'),
        "nodo_a": ('obbligo', 3, 'art. 3-ter c.7'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ('obbligo', None, 'art. 7 c.9'),
        "nodo_a": ('principio', 3, 'art. 2 c.5'),
        "tipo_relazione": 'è condizionato da',
        "evidence_type": 'inferred',
        "confidence": 0.7,
    },
    {
        "nodo_da": ('obbligo', None, 'art. 10 c.3 lett.f)'),
        "nodo_a": ('obbligo', 4, 'art. 58 c.1'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.7,
    },
    {
        "nodo_da": ('obbligo', None, 'art. 10 c.3 lett.f)'),
        "nodo_a": ('obbligo', 1, 'art. 38 §1'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ('obbligo', None, 'art. 10 c.3 lett.h)'),
        "nodo_a": ('obbligo', 4, 'art. 37 c.1'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.7,
    },
    {
        "nodo_da": ('obbligo', None, 'art. 11 c.1 lett.a)'),
        "nodo_a": ('obbligo', 2, 'art. 24 §2(e) (vigente, eIDAS2)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.8,
    },
    {
        "nodo_da": ('obbligo', None, 'art. 11 c.1 lett.a)'),
        "nodo_a": ('obbligo', 2, 'art. 5 bis §12'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ('obbligo', None, 'art. 11 c.1 lett.b)'),
        "nodo_a": ('obbligo', 1, 'art. 24 §2(g) (abrogato, testo originario 2014)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.75,
    },
    {
        "nodo_da": ('obbligo', None, 'art. 11 c.1 lett.f)'),
        "nodo_a": ('obbligo', 4, 'art. 58 c.1'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ('obbligo', None, 'art. 11 c.1 lett.n)'),
        "nodo_a": ('principio', 2, 'art. 24 §2, secondo comma (nuovo, eIDAS2)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.7,
    },
    {
        "nodo_da": ('obbligo', None, 'art. 11 c.1 lett.n)'),
        "nodo_a": ('principio', 1, 'art. 21 §2 (abrogato, testo originario 2014)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
]
