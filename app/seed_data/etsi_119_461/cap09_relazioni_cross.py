"""Relazioni cross-fonte ETSI TS 119 461 V2.1.1 -> eIDAS/eIDAS2/CAD/DPCM 22-2-2013/SPID/
DPCM 19-10-2021/ETSI EN 319 412-5/Reg. UE 2025/1566, e viceversa Reg. UE 2025/1566 -> ETSI
TS 119 461 (2026-09-21).

Modulo "capitolo virtuale" (nessuna riga obbligo/principio propria, solo RELAZIONI) nel senso
del contratto di app/seed_data/lib.py:inserisci_capitoli, agganciato in coda alla lista
capitoli di ETSI TS 119 461 (fonte_id=9) passata a inserisci_capitoli (fase 6, ADR-0009).

Pipeline eseguita nella sessione principale (nessun subagent), in 3 stadi:

1. Candidati a zero token LLM:
   - grep testuale sul testo ufficiale grezzo ETSI TS 119 461
     (app/.source_cache/etsi_119_461/raw.txt) per citazioni esplicite di 910/2014,
     2024/1183, 82/2005, DPCM 22/2/2013, DPCM 24/10/2014, DPCM 19/10/2021, ETSI 319 412-5,
     Reg. 2025/1566: zero citazioni dirette di CAD/DPCM/SPID/ETSI 412-5/Reg. 1566 nel testo
     ufficiale ETSI 119 461 (solo citazioni generiche a eIDAS/eIDAS2, gia' rilevate come
     riferimenti diffusi non puntuali, non risolvibili a un singolo nodo).
   - Grep INVERSO sul testo ufficiale gia' cache di Reg. UE 2025/1566
     (app/.source_cache/reg-ue-2025-1566/raw.txt): l'Allegato del regolamento designa
     esplicitamente "ETSI TS 119 461 V2.1.1 (2025-02)" come norma di riferimento per la
     conformita' all'Allegato C clausola C.3, con 6 punti di adeguamento che citano id di
     requisito precisi (QTS-C.3.4-06, VAL-8.3.3-05X/05A/05B/05C/07A/07X, OVR-7.12-01) o
     intervalli di clausole (C3.1-C3.6, clausola 9.2.3.4) - 9 relazioni "modifica"/"specifica"
     con evidence_type "textual", ancorate al nodo esistente piu' preciso quando l'id citato
     da Reg. 1566 e' esso stesso una disposizione nuova non presente nel testo base ETSI
     (punti 2/4/6: id "QTS-C3-01"/"USE-9.2.3.4-04"/"OVR-7.12-02" sono prescrizioni aggiunte
     da Reg. 1566, non presenti nel testo ETSI - ancorate rispettivamente a QTS-C.3.1-01,
     clausola 9.2.3.4, OVR-7.12-01). Punto 1 (aggiunta bibliografica a clausola 2.1) omesso:
     clausola 2 (References) non genera nodi nel censimento (paratesto bibliografico).
   - KNN sull'indice vettoriale HNSW gia' popolato (idxEmbeddingObbligo/idxEmbeddingPrincipio,
     soglia 0.80, top 8 per indice per nodo, poi top 3 per nodo sorgente): 919 coppie grezze,
     ridotte a 530 dopo deduplica e selezione top-3/nodo sorgente su 220 dei 435 nodi ETSI
     119 461 con almeno un candidato sopra soglia.
2. Classificazione LLM sullo shortlist (mai sul prodotto cartesiano 435 x ~2500 nodi delle
   altre 8 fonti): 45 batch da 12 coppie, chiamate completion() dirette in parallelo con
   wait(), system prompt con tassonomia CONTEXT.md ristretta ai tipi rilevanti, output a
   schema JSON, prompt esplicitamente conservativo (omettere piuttosto che inventare) ->
   114 relazioni proposte.
3. Validazione: 10 proposte scartate (8 per riferimento target allucinato non presente nello
   shortlist fornito al batch, verificato contro l'elenco reale dei candidati passati al
   prompt - anti-allucinazione; 2 per tipo_relazione vuoto/non valido), poi deduplica su
   (rif_src, fonte_target, rif_target) -> 103 relazioni LLM finali, evidence_type "inferred",
   confidence 0.5-0.8 (nessuna sopra 0.8: nessuna coppia ha raggiunto corrispondenza quasi
   letterale/citazione esplicita nello shortlist KNN). Distribuzione per fonte target:
   Reg. 1566 (32), eIDAS2 (28), CAD (17), eIDAS (13), SPID (7), ETSI 412-5 (3),
   DPCM 22/2/2013 (3); zero verso DPCM 19/10/2021 (fonte piccola, 5 sole disposizioni,
   nessuna sopra soglia KNN). Per tipo: specifica (38), si sovrappone a (33), richiama (19),
   attua (8), si applica a (4), modifica (1).

Totale: 9 relazioni esplicite (evidence_type textual) + 103 relazioni classificate
(evidence_type inferred) = 112 relazioni cross-fonte.
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI = [
    {
        "nodo_da": ("obbligo", 8, 'allegato, punto 2 (QTS-C3-01)'),
        "nodo_a": ("obbligo", 9, 'QTS-C.3.1-01'),
        "tipo_relazione": 'modifica',
        "evidence_type": 'textual',
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", 8, 'allegato, punto 3 (QTS-C.3.4-06A)'),
        "nodo_a": ("obbligo", 9, 'QTS-C.3.4-06'),
        "tipo_relazione": 'modifica',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", 8, 'allegato, punto 4 (USE-9.2.3.4-04)'),
        "nodo_a": ("principio", 9, 'clausola 9.2.3.4'),
        "tipo_relazione": 'modifica',
        "evidence_type": 'textual',
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", 8, 'allegato, punto 6 (OVR-7.12-02)'),
        "nodo_a": ("obbligo", 9, 'OVR-7.12-01'),
        "tipo_relazione": 'modifica',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", 8, 'allegato, punto 5 (VAL-8.3.3-21)'),
        "nodo_a": ("obbligo", 9, 'VAL-8.3.3-05X'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", 8, 'allegato, punto 5 (VAL-8.3.3-21)'),
        "nodo_a": ("obbligo", 9, 'VAL-8.3.3-05A'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", 8, 'allegato, punto 5 (VAL-8.3.3-21)'),
        "nodo_a": ("obbligo", 9, 'VAL-8.3.3-05B'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", 8, 'allegato, punto 5 (VAL-8.3.3-21)'),
        "nodo_a": ("obbligo", 9, 'VAL-8.3.3-05C'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", 8, 'allegato, punto 5 (VAL-8.3.3-21)'),
        "nodo_a": ("obbligo", 9, 'VAL-8.3.3-07A'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", 8, 'allegato, punto 5 (VAL-8.3.3-21)'),
        "nodo_a": ("obbligo", 9, 'VAL-8.3.3-07X'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ("principio", None, 'clausola 1 (Scope)'),
        "nodo_a": ("principio", 7, 'QCS-4.3.5-01'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambi trattano identity proofing per certificati qualificati ex art.24 eIDAS ma senza rapporto gerarchico diretto.
    },
    {
        "nodo_da": ("principio", None, 'clausola 4.1 (Identity proofing actors)'),
        "nodo_a": ("principio", 7, 'QCS-4.3.5-01'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
        # Entrambi collegati al metodo di identificazione per certificati qualificati ex art.24 eIDAS.
    },
    {
        "nodo_da": ("principio", None, 'COL-8.2.6-02'),
        "nodo_a": ("principio", 2, 'art. 7'),
        "tipo_relazione": 'si applica a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambi trattano requisiti su regimi/registri nazionali di identificazione, ma senza rapporto gerarchico diretto
    },
    {
        "nodo_da": ("principio", None, 'COL-8.2.8-04'),
        "nodo_a": ("obbligo", 3, 'art. 24 c.1'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambi riguardano l'unicita' e attribuzione della firma digitale come garanzia di autenticita' del documento
    },
    {
        "nodo_da": ("principio", None, 'VAL-8.3.2-00'),
        "nodo_a": ("principio", 3, 'art. 64 c.2-duodecies'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambe trattano la validazione di documenti/identità digitale come equivalente a documento di riconoscimento, ma da prospettive tecniche/normative diverse senza rapporto gerarchico diretto.
    },
    {
        "nodo_da": ("principio", None, 'clausola 8.3.4 (ambito di applicazione)'),
        "nodo_a": ("principio", 2, 'art. 45 septies §5'),
        "tipo_relazione": 'si applica a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
        # Entrambe riguardano l'uso di mezzi eID/attestati come evidenza conforme, ma il rapporto è debole e non diretto.
    },
    {
        "nodo_da": ("principio", None, 'VAL-8.3.4-02'),
        "nodo_a": ("principio", 3, 'art. 64 c.2-duodecies'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # La clausola ETSI specifica operativamente i requisiti di validazione dell'autenticazione eID che il CAD richiama in termini di effetti giuridici della verifica dell'identità digitale.
    },
    {
        "nodo_da": ("principio", None, 'VAL-8.3.4-02'),
        "nodo_a": ("principio", 5, 'art. 1 c.1 lett.f)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # La clausola ETSI specifica operativamente il concetto di autenticazione informatica definito da SPID.
    },
    {
        "nodo_da": ("principio", None, 'clausola 8.3.5 (ambito di applicazione)'),
        "nodo_a": ("obbligo", 3, 'art. 24 c.3'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambe trattano requisiti sulla validità del certificato per firma digitale usata come evidenza.
    },
    {
        "nodo_da": ("principio", None, 'clausola 8.3.5 (ambito di applicazione)'),
        "nodo_a": ("obbligo", 4, 'art. 61 c.4'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambe riguardano la verifica del certificato a supporto della firma digitale.
    },
    {
        "nodo_da": ("principio", None, 'VAL-8.3.5-00'),
        "nodo_a": ("principio", 3, 'art. 64 c.2-duodecies'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
        # Entrambe trattano la validazione degli attributi identificativi associati al richiedente/utente, contesti diversi.
    },
    {
        "nodo_da": ("principio", None, 'VAL-8.3.5-00'),
        "nodo_a": ("obbligo", 2, 'art. 32-bis §1-§2'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.75,
        # La clausola ETSI specifica operativamente i requisiti di validazione della firma elettronica avanzata/qualificata già disciplinati dall'art. 32-bis eIDAS2.
    },
    {
        "nodo_da": ("principio", None, 'clausola 8.3.6 (ambito di applicazione)'),
        "nodo_a": ("principio", 2, 'art. 45 septies §5'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # La clausola ETSI richiama esplicitamente il concetto di fonte autentica definito dal regolamento eIDAS modificato.
    },
    {
        "nodo_da": ("principio", None, 'clausola 8.3.8 (ambito di applicazione)'),
        "nodo_a": ("principio", 2, 'art. 45 septies §5'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # La clausola ETSI specifica requisiti tecnici per l'uso di attestazioni elettroniche di attributi come evidenza supplementare, rendendo operativo il rinvio a norme/specifiche di cui all'art. 45 septies §5 eIDAS2.
    },
    {
        "nodo_da": ("principio", None, 'clausola 8.3.8 (ambito di applicazione)'),
        "nodo_a": ("principio", 2, 'art. 45 septies §1'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # La clausola disciplina l'uso di attestazioni elettroniche qualificate di attributi menzionate nell'art. 45 septies §1, fornendo requisiti tecnici applicativi.
    },
    {
        "nodo_da": ("principio", None, 'clausola C.1'),
        "nodo_a": ("principio", 8, 'art. 1'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # Entrambi trattano norme/specifiche per identity proofing ai fini dell'art.24 eIDAS modificato, ma senza rapporto gerarchico diretto esplicito.
    },
    {
        "nodo_da": ("principio", None, 'QTS-C.4-02'),
        "nodo_a": ("obbligo", 2, 'art. 24 §1 (vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.75,
        # La clausola tecnica specifica operativamente come effettuare l'identity proofing richiesto dall'art. 24 §1 per il rilascio di certificati/attestazioni qualificate.
    },
    {
        "nodo_da": ("principio", None, 'QTS-C.4-03'),
        "nodo_a": ("obbligo", 2, 'art. 24 §1 (vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.7,
        # La clausola tecnica sull'identity proofing dei destinatari del QERDS specifica operativamente l'obbligo generale di verifica identità dell'art.24 §1.
    },
    {
        "nodo_da": ("principio", None, 'Annex D'),
        "nodo_a": ("principio", 1, 'art. 45 §1 (abrogato, testo originario 2014)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.5,
        # Annex D mappa requisiti eIDAS su TS 119 461 ma non riguarda specificamente art.45 abrogato su siti web, bassa pertinenza
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-5-01'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 2 (QTS-C3-01)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.75,
        # Entrambe trattano requisiti di identity proofing conformi a clausole ETSI TS 119 461 C3, con esplicito rinvio incrociato tra i due testi
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-5-02'),
        "nodo_a": ("obbligo", 5, 'art. 11 c.1 lett.d)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # Entrambe impongono un aggiornamento annuale della valutazione/analisi dei rischi relativa ai processi di identificazione
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-5-03'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 4 (USE-9.2.3.4-04)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.7,
        # Il Reg. 2025/1566 specifica operativamente la valutazione dei rischi di sicurezza dei sistemi informativi richiesta genericamente da OVR-5-03, con metriche FAR/FRR concrete
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-5-05'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 4 (USE-9.2.3.4-04)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.7,
        # Il Reg. 2025/1566 rende operativa la procedura di intelligence sulle minacce richiesta da OVR-5-05, definendo metodologia e parametri specifici
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-5-06'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 4 (USE-9.2.3.4-04)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.75,
        # L'obbligo di aggiornamento della valutazione del rischio in base all'intelligence sulle minacce è reso operativo dal Reg. 2025/1566 tramite metodologia specifica ENISA e target FAR/FRR.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-6.1-01'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'modifica',
        "evidence_type": 'inferred',
        "confidence": 0.75,
        # Il Reg. 2025/1566 modifica esplicitamente la clausola 2.1 di ETSI TS 119 461 aggiungendo un riferimento normativo relativo a EN 319 401.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.2-01'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.7,
        # Il regolamento aggiunge esplicitamente ETSI EN 319 401 come riferimento normativo di TS 119 461, corrispondendo al richiamo effettuato dall'obbligo OVR-7.2-01.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.3-01'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.7,
        # Il regolamento aggiunge esplicitamente ETSI EN 319 401 come riferimento normativo di TS 119 461, corrispondendo al richiamo effettuato dall'obbligo OVR-7.3-01.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.4-01'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.7,
        # Il regolamento aggiunge esplicitamente ETSI EN 319 401 come riferimento normativo di TS 119 461, corrispondendo al richiamo effettuato dall'obbligo OVR-7.4-01.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.6-01'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # Il Reg. 2025/1566 aggiunge il riferimento a EN 319 401 nella clausola 2.1 di TS 119 461, correlato al richiamo effettuato dall'obbligo OVR-7.6-01 alla stessa norma.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.7-01'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # Analogamente, il Reg. 2025/1566 introduce formalmente il riferimento a EN 319 401 richiamato dall'obbligo di sicurezza operativa.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.8-01'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # Il Reg. 2025/1566 inserisce il riferimento normativo a EN 319 401 richiamato dall'obbligo di sicurezza di rete.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.8-02'),
        "nodo_a": ("obbligo", 2, 'art. 45 nonies §2'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambe richiedono separazione logica/fisica dei sistemi/dati critici, senza rapporto gerarchico diretto ma sostanziale sovrapposizione di contenuto.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.9-01'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.7,
        # Il Reg. 2025/1566 modifica formalmente ETSI TS 119 461 aggiungendo il riferimento a EN 319 401 richiamato dall'obbligo OVR-7.9-01.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.9-02'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # L'obbligo richiama EN 319 401 il cui riferimento è introdotto formalmente dal Reg. 2025/1566 nella stessa clausola 2.1.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.10-01'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # L'obbligo si basa su EN 319 401 il cui riferimento normativo è aggiunto dal Reg. 2025/1566.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.11-01'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # L'obbligo richiama EN 319 401, riferimento introdotto formalmente dal Reg. 2025/1566.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.11-02'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # Il Reg. 2025/1566 aggiorna il riferimento normativo a ETSI EN 319 401 richiamato dall'obbligo OVR-7.11-02.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.12-01'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # Il Reg. 2025/1566 aggiorna il riferimento normativo a ETSI EN 319 401 richiamato dall'obbligo OVR-7.12-01.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.13-01'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # Il Reg. 2025/1566 aggiorna il riferimento normativo a ETSI EN 319 401 richiamato dall'obbligo OVR-7.13-01.
    },
    {
        "nodo_da": ("obbligo", None, 'OVR-7.14-01'),
        "nodo_a": ("principio", 8, 'allegato, punto 1 (riferimenti normativi)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # Il Reg. 2025/1566 aggiorna il riferimento normativo a ETSI EN 319 401 richiamato dall'obbligo OVR-7.14-01.
    },
    {
        "nodo_da": ("obbligo", None, 'INI-8.1-03X'),
        "nodo_a": ("obbligo", 3, 'art. 32 c.3 lett.e'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # Entrambe impongono l'obbligo di informare chiaramente il richiedente sul processo di verifica/certificazione, con TS 119 461 che rende operativo il principio generale CAD.
    },
    {
        "nodo_da": ("obbligo", None, 'INI-8.1-04'),
        "nodo_a": ("obbligo", 2, 'art. 15 (testo vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.75,
        # La norma ETSI rende operativo l'obbligo di accessibilita' per persone con disabilita' previsto da eIDAS2 art.15.
    },
    {
        "nodo_da": ("obbligo", None, 'INI-8.1-04'),
        "nodo_a": ("obbligo", 1, 'art. 15 (testo originario 2014)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.75,
        # L'obbligo ETSI specifica concretamente il principio di accessibilita' ai disabili gia' previsto da eIDAS art.15.
    },
    {
        "nodo_da": ("obbligo", None, 'INI-8.1-04'),
        "nodo_a": ("obbligo", 3, 'art. 23-ter c.5-bis'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambe trattano l'accessibilita' per persone con disabilita', ma in ambiti diversi (identity proofing vs documenti amministrativi), senza gerarchia diretta.
    },
    {
        "nodo_da": ("obbligo", None, 'COL-8.2.3-06X'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 2 (QTS-C3-01)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.85,
        # Il regolamento richiama esplicitamente la conformità alle clausole C3.1-C3.6 di ETSI TS 119 461, che includono la clausola sui documenti eMRTD, rendendo COL-8.2.3-06X specificazione operativa richiamata dal target.
    },
    {
        "nodo_da": ("obbligo", None, 'COL-8.2.5-01X'),
        "nodo_a": ("principio", 3, 'art. 64 c.2-duodecies'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambe riguardano l'accettazione di evidenze/verifiche di identità digitale ai fini di equipollenza; relazione plausibile ma non certa.
    },
    {
        "nodo_da": ("obbligo", None, 'COL-8.2.5-06X'),
        "nodo_a": ("principio", 4, 'art. 1 c.1 lett.o)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # L'obbligo ETSI sul controllo esclusivo del firmatario specifica operativamente la definizione generale di dispositivo sicuro con controllo esclusivo del DPCM.
    },
    {
        "nodo_da": ("obbligo", None, 'COL-8.2.5-06X'),
        "nodo_a": ("obbligo", 3, 'art. 32 c.1'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # L'obbligo ETSI di garanzia del controllo esclusivo specifica il dovere generale del titolare di custodire e usare personalmente il dispositivo di firma previsto dal CAD.
    },
    {
        "nodo_da": ("obbligo", None, 'COL-8.2.5-06X'),
        "nodo_a": ("obbligo", 4, 'art. 56 c.1 lett.c'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.75,
        # Entrambe le disposizioni richiedono garanzia di controllo esclusivo del firmatario sul sistema di generazione della firma, con formulazione quasi equivalente.
    },
    {
        "nodo_da": ("obbligo", None, 'COL-8.2.6-01A'),
        "nodo_a": ("obbligo", 1, 'art. 24 §2(f)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # L'obbligo ETSI di collegamento affidabile tra attributi e richiedente specifica il requisito eIDAS di verificabilità e autenticità dei dati memorizzati.
    },
    {
        "nodo_da": ("obbligo", None, 'COL-8.2.7-02'),
        "nodo_a": ("principio", 1, 'art. 35 §2'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
        # Entrambe riguardano l'affidabilità/integrità dei dati collegati a un soggetto, ma senza rapporto gerarchico diretto.
    },
    {
        "nodo_da": ("obbligo", None, 'VAL-8.3.2-05'),
        "nodo_a": ("obbligo", 5, 'art. 5 c.1'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # Entrambe richiedono la registrazione di attributi identificativi del documento/identità, senza gerarchia diretta.
    },
    {
        "nodo_da": ("obbligo", None, 'VAL-8.3.2-05'),
        "nodo_a": ("obbligo", 5, 'art. 7 c.5'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # ETSI specifica in dettaglio operativo l'obbligo di conservazione documentale già previsto dall'art.7 c.5 SPID.
    },
    {
        "nodo_da": ("obbligo", None, 'VAL-8.3.4-01X'),
        "nodo_a": ("principio", 1, 'art. 8 §1'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # ETSI specifica operativamente il concetto di livello di garanzia dei mezzi eID definito da eIDAS art.8, richiedendo un protocollo di autenticazione coerente con il LoA.
    },
    {
        "nodo_da": ("obbligo", None, 'VAL-8.3.6-01'),
        "nodo_a": ("obbligo", 2, 'art. 24 §2(e) (vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.75,
        # Il requisito TLS specifica operativamente l'obbligo generale di sistemi affidabili e tecniche crittografiche adeguate.
    },
    {
        "nodo_da": ("obbligo", None, 'VAL-8.3.6-01'),
        "nodo_a": ("obbligo", 5, 'art. 11 c.1 lett.a)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # Requisito tecnico specifico che concretizza l'obbligo generale di sicurezza crittografica dei procedimenti.
    },
    {
        "nodo_da": ("obbligo", None, 'VAL-8.3.7-03'),
        "nodo_a": ("obbligo", 2, 'art. 24 §1-ter (nuovo, eIDAS2 — metodi di verifica degli attributi)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # ETSI dettaglia i requisiti tecnici di validazione dell'integrità e autenticità degli attributi che eIDAS2 richiede genericamente come metodi di verifica affidabili.
    },
    {
        "nodo_da": ("obbligo", None, 'VAL-8.3.7-01'),
        "nodo_a": ("obbligo", 2, 'art. 24 §1-ter (nuovo, eIDAS2 — metodi di verifica degli attributi)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Il protocollo di prova di controllo dell'elemento (es. cellulare, email) è un metodo operativo che concretizza i metodi di verifica degli attributi previsti da eIDAS2.
    },
    {
        "nodo_da": ("obbligo", None, 'BIN-8.4.2-04B'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 5 (VAL-8.3.3-21)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # Entrambe richiedono verifica periodica da laboratorio accreditato di misure anti-frode, ma riferite a controlli diversi (biometria vs documento).
    },
    {
        "nodo_da": ("obbligo", None, 'BIN-8.4.2-04B'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 2 (QTS-C3-01)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # QTS-C3-01 rinvia esplicitamente alle clausole ETSI TS 119 461 C3.1-C3.6 per la verifica dell'identità biometrica.
    },
    {
        "nodo_da": ("obbligo", None, 'BIN-8.4.2-04C'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 5 (VAL-8.3.3-21)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Analoga richiesta di verifica periodica ma su ambiti differenti (biometria vs documento fisico).
    },
    {
        "nodo_da": ("obbligo", None, 'BIN-8.4.2-04C'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 2 (QTS-C3-01)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # QTS-C3-01 rinvia alle clausole ETSI TS 119 461 per la conformità dei processi di identity proofing.
    },
    {
        "nodo_da": ("obbligo", None, 'BIN-8.4.2-07X'),
        "nodo_a": ("principio", 2, 'art. 12 §6 (vigente, eIDAS2)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
        # Entrambe riguardano procedure di valutazione/conformità ma con oggetti diversi (PAD vs peer review); relazione debole.
    },
    {
        "nodo_da": ("obbligo", None, 'BIN-8.4.3-05A'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 4 (USE-9.2.3.4-04)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.75,
        # Entrambe le norme richiedono la definizione di obiettivi FAR/FRR basati su intelligence sulle minacce, con contenuto sostanzialmente coincidente.
    },
    {
        "nodo_da": ("obbligo", None, 'BIN-8.4.3-05B'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 4 (USE-9.2.3.4-04)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.75,
        # Entrambe richiedono l'aggiornamento degli obiettivi FAR/FRR sulla base della procedura di intelligence sulle minacce, contenuto sostanzialmente coincidente.
    },
    {
        "nodo_da": ("obbligo", None, 'BIN-8.4.3-08X'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 5 (VAL-8.3.3-21)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambe richiedono verifica/test dell'efficacia di misure biometriche/identità da parte di enti terzi, ma su ambiti leggermente diversi (facciale vs documento).
    },
    {
        "nodo_da": ("obbligo", None, 'USE-9.2.1.1-01'),
        "nodo_a": ("principio", 2, 'art. 45 quinquies §2'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambi riguardano requisiti di raccolta/verifica attributi per attestati qualificati ma senza rinvio esplicito diretto.
    },
    {
        "nodo_da": ("obbligo", None, 'USE-9.2.1.1-02'),
        "nodo_a": ("principio", 3, 'art. 64 c.2-duodecies'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambi trattano l'uso di identità digitale/documenti come evidenza di identità, ma contesti normativi diversi senza gerarchia chiara.
    },
    {
        "nodo_da": ("obbligo", None, 'USE-9.2.1.2-01'),
        "nodo_a": ("principio", 5, 'art. 1 c.1 lett.r)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambi descrivono il processo di registrazione/identity proofing con raccolta e verifica attributi, sovrapposizione tematica sostanziale.
    },
    {
        "nodo_da": ("obbligo", None, 'USE-9.2.1.4-05X'),
        "nodo_a": ("principio", 3, 'art. 64 c.2-duodecies'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # Entrambi trattano requisiti di verifica dell'identità digitale tramite documenti/evidenze; ETSI specifica operativamente il livello richiesto dal CAD.
    },
    {
        "nodo_da": ("obbligo", None, 'USE-9.2.2.1-01'),
        "nodo_a": ("principio", 5, 'art. 1 c.1 lett.r)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # ETSI dettaglia operativamente il processo di registrazione/identity proofing definito in astratto dal DPCM SPID.
    },
    {
        "nodo_da": ("obbligo", None, 'USE-9.2.2.3-01X'),
        "nodo_a": ("principio", 3, 'art. 64 c.2-duodecies'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # L'obbligo ETSI specifica requisiti tecnici di validazione del documento d'identità digitale usato come evidenza, coerente con la verifica dell'identità digitale di cui all'art. 64 CAD.
    },
    {
        "nodo_da": ("obbligo", None, 'USE-9.3-03A'),
        "nodo_a": ("principio", 2, 'art. 45 septies §2'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # L'obbligo ETSI di raccolta alternativa di attributi per persone giuridiche non registrate specifica il principio generale di equivalente affidabilità richiesto agli organismi pubblici fonte autentica.
    },
    {
        "nodo_da": ("obbligo", None, 'USE-9.3-05X'),
        "nodo_a": ("principio", 3, 'art. 64 c.2-duodecies'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
        # Entrambi trattano l'uso di firme/sigilli qualificati come evidenza per attestare identità/attributi, ma in contesti diversi (identity proofing vs identità digitale SPID/CIE).
    },
    {
        "nodo_da": ("obbligo", None, 'USE-9.4-04'),
        "nodo_a": ("principio", 2, 'art. 45 septies §5'),
        "tipo_relazione": 'si applica a',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # Il requisito ETSI sul registro fidato come fonte autentica richiama il concetto di fonte autentica disciplinato dall'art. 45 septies §5 eIDAS2.
    },
    {
        "nodo_da": ("obbligo", None, 'USE-9.4-04'),
        "nodo_a": ("principio", 2, 'art. 45 septies §1'),
        "tipo_relazione": 'si applica a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Riferimento comune al concetto di fonte autentica, ma senza rapporto gerarchico diretto.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.1-01'),
        "nodo_a": ("principio", 2, 'art. 45 terdecies §2'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # La clausola tecnica potrebbe fornire attuazione operativa alle norme richiamate dall'atto di esecuzione, ma il collegamento è generico.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.1-01'),
        "nodo_a": ("principio", 1, 'art. 24 §5 (abrogato, testo originario 2014)'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.5,
        # Le specifiche tecniche di ETSI TS 119 461 rientrano tra le norme la cui conformità fa presumere il rispetto dei requisiti eIDAS, ma il legame è indiretto.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.1-02'),
        "nodo_a": ("principio", 1, 'art. 24 §5 (abrogato, testo originario 2014)'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.5,
        # Analogo alla coppia precedente, requisiti tecnici di verifica identità come possibile attuazione delle norme presunte.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.2-01'),
        "nodo_a": ("principio", 2, 'art. 24 §5 (vigente, eIDAS2)'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # La clausola sul Baseline LoIP fornisce specifiche tecniche che possono rientrare tra le norme richiamate dall'atto di esecuzione previsto dall'art. 24 §5 vigente.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.2-01'),
        "nodo_a": ("principio", 1, 'art. 24 §5 (abrogato, testo originario 2014)'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.5,
        # Collegamento indiretto tra requisiti tecnici e norme di riferimento richiamate dall'articolo.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.2-02'),
        "nodo_a": ("principio", 1, 'art. 8 §1'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.7,
        # La clausola specifica in modo operativo il requisito di livello di garanzia (substantial/high) previsto in generale dall'art. 8 §1 eIDAS.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.3-01'),
        "nodo_a": ("principio", 2, 'art. 24 §5 (vigente, eIDAS2)'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # La clausola tecnica 9.2.5 richiamata da ETSI da' attuazione operativa alle norme di riferimento previste dall'art. 24 §5 eIDAS2 per il rispetto dei requisiti dei fornitori di servizi fiduciari.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.3-02'),
        "nodo_a": ("principio", 3, 'art. 20 c.1-ter'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambi trattano della qualificazione della firma elettronica qualificata come requisito di attribuzione al titolare, in contesti normativi diversi ma con contenuto sostanziale affine.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.3-03'),
        "nodo_a": ("obbligo", 3, 'art. 25 c.2'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
        # Entrambi riguardano la qualificazione/autenticazione di firme elettroniche per persone giuridiche/rappresentanti, sebbene in ambiti procedurali diversi.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.3-03'),
        "nodo_a": ("obbligo", 3, 'art. 24 c.3'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # Entrambi disciplinano requisiti sul certificato qualificato usato per la firma/sigillo del richiedente persona giuridica, ETSI specifica il tipo di firma richiesto.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.3-04'),
        "nodo_a": ("obbligo", 1, 'art. 24 §1 (abrogato, testo originario 2014)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.85,
        # ETSI rende operativo il requisito generale eIDAS di identity proofing mediante presenza fisica o eID equivalente.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.3-04'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 2 (QTS-C3-01)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'inferred',
        "confidence": 0.85,
        # Il Reg. UE 2025/1566 cita esplicitamente le clausole C3.1-C3.6 di ETSI TS 119 461 come alternativa di conformità.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.3-04'),
        "nodo_a": ("obbligo", 2, 'art. 24 §1 (vigente, eIDAS2)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.8,
        # ETSI specifica in dettaglio i metodi di identity proofing richiamati genericamente dall'art. 24 eIDAS2.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.3-05'),
        "nodo_a": ("obbligo", 1, 'art. 28 §1'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
        # Entrambi riguardano requisiti sui certificati qualificati per firme, ma con oggetto diverso (convalida vs allegato I).
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.4-05'),
        "nodo_a": ("obbligo", 2, 'art. 24 §1-bis (nuovo, eIDAS2 — metodi di verifica dell\'identità)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.7,
        # ETSI specifica il riconoscimento nazionale dei metodi di identity proofing elencati nell'art. 24 §1-bis.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.4-06'),
        "nodo_a": ("obbligo", 2, 'art. 24 §1-bis (nuovo, eIDAS2 — metodi di verifica dell\'identità)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.7,
        # ETSI specifica il livello di garanzia equivalente alla presenza fisica richiesto dai metodi indicati nell'art. 24 §1-bis.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.4-06'),
        "nodo_a": ("obbligo", 2, 'art. 24 §1-ter (nuovo, eIDAS2 — metodi di verifica degli attributi)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.75,
        # L'obbligo ETSI specifica il livello di garanzia equivalente alla presenza fisica richiesto dai metodi di identity proofing previsti dall'art. 24 §1-ter eIDAS2.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.2.4-07'),
        "nodo_a": ("obbligo", 2, 'art. 45 §1 (vigente, eIDAS2)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
        # Entrambi richiedono valutazione di conformità ma su ambiti diversi (identity proofing vs QWAC), relazione debole.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.3.2-02'),
        "nodo_a": ("principio", 1, 'art. 8 §1'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.65,
        # Il requisito eIDAS high eID concretizza il livello di garanzia elevato previsto dall'art.8 eIDAS.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.3.2-03'),
        "nodo_a": ("principio", 1, 'art. 8 §1'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.6,
        # L'obbligo di eID notificato eIDAS specifica il regime di notificazione previsto dall'art.8.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.3.3-02'),
        "nodo_a": ("principio", 3, 'art. 20 c.1-ter'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # Entrambi trattano l'efficacia della firma elettronica qualificata riconducibile al titolare.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.3.3-04'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 2 (QTS-C3-01)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.8,
        # Il Reg. UE 2025/1566 richiama esplicitamente le clausole C3.1-C3.6 di ETSI TS 119 461 come requisito alternativo per la verifica dell'identità, corrispondenza diretta di contenuto.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.3.4-08'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 3 (QTS-C.3.4-06A)'),
        "tipo_relazione": 'specifica',
        "evidence_type": 'inferred',
        "confidence": 0.75,
        # Il Reg. UE 2025/1566 dettaglia i requisiti dell'organismo di valutazione della conformità menzionato in modo generico dalla clausola ETSI, specificandone accreditamento e processo certificativo.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.3.4-08'),
        "nodo_a": ("obbligo", 8, 'allegato, punto 2 (QTS-C3-01)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.8,
        # Entrambi richiedono valutazione di conformità da organismo accreditato per il processo di identity proofing, con riferimento esplicito reciproco alle clausole C3.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.3.4-08'),
        "nodo_a": ("principio", 2, 'art. 12-bis §1'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.55,
        # La clausola tecnica ETSI da attuazione operativa al principio generale eIDAS2 sulla certificazione della conformità da parte di organismi di valutazione.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.3.6-01'),
        "nodo_a": ("principio", 7, 'Annex A.1 (mapping con Allegato I Reg. 910/2014)'),
        "tipo_relazione": 'si sovrappone a',
        "evidence_type": 'inferred',
        "confidence": 0.5,
        # Entrambi trattano requisiti tecnici di livello di garanzia per certificati qualificati, ma senza rinvio esplicito reciproco.
    },
    {
        "nodo_da": ("obbligo", None, 'QTS-C.4-01'),
        "nodo_a": ("obbligo", 2, 'art. 24 §1 (vigente, eIDAS2)'),
        "tipo_relazione": 'attua',
        "evidence_type": 'inferred',
        "confidence": 0.75,
        # La clausola tecnica ETSI specifica in dettaglio le modalità operative di verifica dell'identità richieste dall'art. 24 §1 eIDAS2 per il rilascio di certificati qualificati/QEAA, applicandole al caso QERDS.
    },
]