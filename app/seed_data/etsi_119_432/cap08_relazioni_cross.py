"""ETSI TS 119 432 V1.3.1 (2026-03) - Electronic Signatures and Trust
Infrastructures (ESI); Protocols for remote digital signature creation.
Fonte 20. Capitolo 8 = "capitolo virtuale" di sole relazioni cross-fonte
(Fase 6, ADR-0009): RIGHE_OBBLIGHI/RIGHE_PRINCIPI/INDICE_ARTICOLI_LOCALE/
MAPPATURA_LOCALE vuoti, nessun nodo nuovo - solo archi verso nodi delle altre
Fonti gia' censite. Stesso formato di app/seed_data/cad/cap08_relazioni_eidas.py
e app/seed_data/etsi_319_422/cap05_relazioni_cross.py.

Pipeline usata per generarlo (3 stadi, mai il prodotto cartesiano fonte x fonte):

1. Candidati a zero token LLM (`app/tools/fase6_candidati_432.py`):
   - grep sul testo ufficiale grezzo (`app/.source_cache/etsi_119_432/raw.txt`)
     per citazioni esplicite delle altre Fonti: trovate citazioni di eIDAS
     (910/2014, 11 estratti), eIDAS2 (2024/1183, 2), ETSI TS 119 431-1/-2
     (4, solo bibliografiche: il rinvio e' nella clausola 2 References,
     esclusa dal censimento), nessun'altra Fonte censita;
   - KNN sugli embedding (`idxEmbeddingObbligo`/`idxEmbeddingPrincipio`,
     soglia 0.80, k=8): 164 coppie candidate su 60 nodi di partenza.
   I due insiemi sono stati uniti; ai 10 nodi che citano eIDAS/eIDAS2 sono
   stati aggiunti come candidati 21 nodi eIDAS/eIDAS2 degli istituti
   pertinenti (artt. 24, 25, 26, 29, 29-bis, 5 bis).

2. Classificazione LLM sullo shortlist (mai sul prodotto cartesiano):
   `completion()` dirette in batch di ~8 nodi di partenza, prompt
   esplicitamente conservativo, output a schema JSON, tassonomia ristretta;
   una seconda passata focalizzata sui 10 nodi che citano eIDAS/eIDAS2, con
   gli estratti testuali delle citazioni. 33 proposte grezze.

3. Validazione: verifica che ogni `riferimento` proposto esista davvero in
   Neo4j con la propria `fonte_id` (anti-allucinazione, necessaria perche' le
   stringhe "Parte 1/2: ..." sono condivise fra Fonte 11 e Fonte 17 e "art. 26"
   fra Fonte 1 e altre), soglia di confidence >= 0.5, deduplica per coppia,
   esclusione di 5 proposte senza contenuto normativo proprio o duplicative
   (le due clausole 3.2 Symbols vuote "Void." a confronto fra loro, le due
   clausole di scope a confronto fra loro, le due clausole 3.1 Terms a
   confronto fra loro, il rinvio generico di clausola 6.4.1 all'art. 5 bis §1,
   e il fan-out di clausola 6.4.1 su due lettere dello stesso art. 5 bis §5).
   Esito: 24 relazioni, tutte `inferred` tranne 3 `textual` (Annex B.9,
   Annex A.12.2, Annex A.6.4 -> art. 5 bis §4(e): i loro estratti nominano
   letteralmente il regolamento eIDAS e la resa della QES da parte dell'EUDIW).

Nessuna relazione verso ETSI TS 119 431 e' `textual`: il rinvio a quelle Parti
sta nella sola clausola 2 (References, fuori perimetro); le 4 relazioni verso
Fonte 11 derivano da sovrapposizione concettuale specifica (architettura e
componenti di servizio sovrapponibili fra TS 119 432 e TS 119 431-2, ruolo del
Remote Signing Server rispetto allo scope di TS 119 431-1). Le citazioni a
standard NON censiti nel grafo (CSC API/CSC DM — 130 occorrenze, IETF RFC,
OASIS DSS-X, ETSI EN 419 241, EUDI ARF) non producono relazioni per assenza di
nodo controparte. Nessuna relazione verso CAD/SPID/DPCM 24-10-2014/
DPCM 19-10-2021/Reg. AgID SPID/Regole Tecniche AgID/Reg. (UE) 2025/1566/
Reg. (UE) 2015/1502/Codice Civile/altri standard ETSI non citati.

`evidence_type`/`confidence` per-arco (ADR-0005): valori prodotti dallo stadio
2 e filtrati dallo stadio 3, mai `NULL` per default e mai inventati. La
costruzione e' demandata a questa Fase 6 della sessione principale (ADR-0009).
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, 'Annex B.6.2 (qesApprovalRequest)'),
        "nodo_a": ("obbligo", 2, 'art. 29 §1-bis'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ("principio", None, 'clausola 4.4.1.2 (Signature activation)'),
        "nodo_a": ("obbligo", 2, 'art. 29-bis §1'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.68,
    },
    {
        "nodo_da": ("principio", None, 'Annex A.11 (Conformance checklist (RP))'),
        "nodo_a": ("obbligo", 2, 'art. 29 §1-bis'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.62,
    },
    {
        "nodo_da": ("principio", None, 'Annex B.9 (Processing & rendering requirements (EUDIW))'),
        "nodo_a": ("obbligo", 2, 'art. 5 bis §4(e)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.62,
    },
    {
        "nodo_da": ("principio", None, 'clausola 4.4.1.2 (Signature activation)'),
        "nodo_a": ("obbligo", 2, 'art. 29 §1-bis'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.62,
    },
    {
        "nodo_da": ("principio", None, 'clausola 6.2 (Architectures for creating remote signatures with a credential protected by signature creation service-managed authorization)'),
        "nodo_a": ("obbligo", 2, 'art. 29-bis §1'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.62,
    },
    {
        "nodo_da": ("obbligo", None, 'Annex A.8 (Transaction data processing & UX rendering (EUDIW))'),
        "nodo_a": ("obbligo", 2, 'art. 5 bis §4(e)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ("principio", None, 'clausola 6.2 (Architectures for creating remote signatures with a credential protected by signature creation service-managed authorization)'),
        "nodo_a": ("obbligo", 2, 'art. 29 §1-bis'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.56,
    },
    {
        "nodo_da": ("obbligo", None, 'Annex B.6.2 (qesApprovalRequest)'),
        "nodo_a": ("principio", 1, 'art. 26'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ("obbligo", None, 'clausola 6.4.1 (Overview)'),
        "nodo_a": ("obbligo", 2, 'art. 5 bis §4(e)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ("principio", None, 'clausola 1 (Scope)'),
        "nodo_a": ("obbligo", 2, 'art. 29-bis §1'),
        "tipo_relazione": 'si applica a',
        "evidence_type": 'inferred',
        "confidence": 0.72,
    },
    {
        "nodo_da": ("obbligo", None, 'clausola 6.4.1 (Overview)'),
        "nodo_a": ("obbligo", 2, 'art. 29-bis §1'),
        "tipo_relazione": 'si applica a',
        "evidence_type": 'inferred',
        "confidence": 0.62,
    },
    {
        "nodo_da": ("principio", None, "Annex A.12.2 (Example 'qesRequest' (transaction_data before base64url encoding))"),
        "nodo_a": ("obbligo", 2, 'art. 5 bis §4(e)'),
        "tipo_relazione": 'si applica a',
        "evidence_type": 'textual',
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, 'Annex A.6.4 (transaction_data (the QES transaction))'),
        "nodo_a": ("obbligo", 2, 'art. 29-bis §1'),
        "tipo_relazione": 'si applica a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, 'Annex A.6.4 (transaction_data (the QES transaction))'),
        "nodo_a": ("obbligo", 2, 'art. 5 bis §4(e)'),
        "tipo_relazione": 'si applica a',
        "evidence_type": 'textual',
        "confidence": 0.6,
    },
    {
        "nodo_da": ("principio", None, 'clausola 1 (Scope)'),
        "nodo_a": ("obbligo", 1, 'art. 29 §1'),
        "tipo_relazione": 'si applica a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
    },
    {
        "nodo_da": ("principio", None, 'Annex A.11 (Conformance checklist (RP))'),
        "nodo_a": ("obbligo", 2, 'art. 5 bis §5(g)'),
        "tipo_relazione": 'si applica a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ("principio", None, "Annex A.12.2 (Example 'qesRequest' (transaction_data before base64url encoding))"),
        "nodo_a": ("obbligo", 2, 'art. 29-bis §1'),
        "tipo_relazione": 'si applica a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ("principio", None, 'clausola 4.4.1.2 (Signature activation)'),
        "nodo_a": ("principio", 1, 'art. 26'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
    },
    {
        "nodo_da": ("principio", None, 'Annex B.2 (Roles and architecture)'),
        "nodo_a": ("principio", 11, 'Parte 1: clausola 1 (Scope)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("principio", None, 'clausola 4.2 (Service main components and interfaces)'),
        "nodo_a": ("principio", 11, 'Parte 2: clausola 4.3 (Architecture)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("principio", None, "clausola 4.3.1 (Signer's document and hashing)"),
        "nodo_a": ("principio", 11, 'Parte 2: clausola 4.3 (Architecture)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("obbligo", None, 'clausola 5.1 (Introduction)'),
        "nodo_a": ("obbligo", 4, 'art. 11 c.2'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
    {
        "nodo_da": ("obbligo", None, 'clausola 7.6.1 (Description)'),
        "nodo_a": ("obbligo", 11, 'Parte 2: OVR-B.1-03'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
    },
]


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_completezza_testo_integrale, verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    verifica_completezza_testo_integrale([sys.modules[__name__]])
    print(f"OK: 0 obblighi, 0 principi, 0 item di indice, {len(RELAZIONI)} relazioni cross-fonte.")
