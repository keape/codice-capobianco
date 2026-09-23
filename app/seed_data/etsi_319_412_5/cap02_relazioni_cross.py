"""Relazioni cross-fonte ETSI EN 319 412-5 -> eIDAS/eIDAS2/DPCM 22-2-2013 (2026-09-21).

Modulo "capitolo virtuale" (nessuna riga obbligo/principio propria, solo
RELAZIONI) nel senso del contratto di app/seed_data/lib.py:inserisci_capitoli,
usato per collegare i 31 nodi ETSI 412-5 (cap01.py) ai nodi eIDAS/eIDAS2 e
DPCM 22/2/2013 gia' presenti nel registro (fonte_id=1, 2, 4) al momento in
cui questo modulo viene processato (fase 6, ADR-0009).

Pipeline effettivamente utilizzata per questa fonte (diversa da CAD/DPCM/
SPID: qui non serve grep+KNN perche' il testo ufficiale e' breve, 21 pagine,
letto integralmente nella sessione principale, con citazioni esplicite gia'
identificabili a vista):

1. Candidati da citazione testuale esplicita: il documento cita
   pervasivamente Regulation (EU) No 910/2014 [i.8] e Regulation (EU)
   2024/1183 [i.13] (eIDAS2), ma solo in tre punti la citazione e'
   sufficientemente specifica da risolvere un riferimento puntuale a un nodo
   gia' censito invece che un rinvio generico al regolamento nel suo
   complesso: (a) Annex A.1/A.2/A.3, che mappano esplicitamente gli Allegati
   I/III/IV del regolamento sulle clausole ETSI - risolti contro gli
   obblighi eIDAS/eIDAS2 il cui testo cita lo stesso Allegato ("art. 28 §1",
   "art. 38 §1", "art. 45 §1"); (b) clausola 4.3.5 (QCS-4.3.5-01 e clausola
   4.3.5.3), che cita esplicitamente "Article 24" e "Article 24.1a" del
   regolamento come modificato da eIDAS2 - risolta contro l'obbligo eIDAS2
   "art. 24 §1-bis" il cui testo (verifica dell'identita' tramite Wallet,
   certificato qualificato, altri metodi ad alta affidabilita', presenza
   fisica) corrisponde ai metodi elencati nella clausola 4.3.5.3.
2. Nessuna classificazione LLM in batch necessaria data la piccola
   dimensione della fonte (31 nodi contro migliaia di CAD/DPCM/SPID):
   candidati risolti e validati manualmente nella sessione principale,
   confidence assegnata secondo la stessa scala di CAD/DPCM/SPID (0.85-0.9
   per citazione esplicita puntuale con corrispondenza di contenuto diretta,
   0.75 per citazione esplicita ma con corrispondenza per rinvio articolo
   generico non ulteriormente specificato dal testo).
3. Verificato che ogni `riferimento` referenziato esiste realmente nel
   registro (fonte_id=1/2) prima di scrivere questo file.

Verificato (esito, non fase saltata) contro le altre fonti censite: CAD
(fonte_id=3), SPID/DPCM 24-10-2014 (fonte_id=5), DPCM 19-10-2021
(fonte_id=6). Zero citazioni testuali dirette di CAD o del DPCM SPID nel
testo ufficiale ETSI 412-5 (standard tecnico europeo che non cita normativa
italiana di attuazione interna, salvo l'eccezione DPCM 22/2/2013 sotto) -
grep su "CAD", "82/2005", "SPID", "24 ottobre 2014" sul testo ufficiale in
app/.source_cache/etsi-319-412-5/raw.txt conferma zero occorrenze fuori da
questo stesso commento. Nessuna relazione verso Fonte 3/5/6.

Eccezione trovata verso DPCM 22/2/2013 (fonte_id=4): grep sul testo ufficiale
DPCM (app/.source_cache/dpcm/raw.txt) per "319 412"/"QCStatement" rivela due
citazioni testuali dirette ed esplicite dell'OID "id-etsi-qcs-QcSSCD" -
definito in ETSI 412-5 clausola 4.2.2/Annex B - negli artt. 13 c.3 e 42 c.5
del DPCM (entrambi impongono requisiti sulla valorizzazione/assenza di
questa esatta estensione qcStatements). Relazione "richiama" (rinvio
esplicito, non modifica) da DPCM verso ETSI, confidence 0.9 (corrispondenza
letterale dell'identificatore tecnico, non solo tematica).
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI_LOCALE: list[str] = []
MAPPATURA_LOCALE: dict[str, list[str]] = {}

RELAZIONI = [
    {
        "nodo_da": ("principio", None, "Annex A.1 (mapping con Allegato I Reg. 910/2014)"),
        "nodo_a": ("obbligo", 1, "art. 28 §1"),
        "tipo_relazione": "attua",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("principio", None, "Annex A.2 (mapping con Allegato III Reg. 910/2014)"),
        "nodo_a": ("obbligo", 1, "art. 38 §1"),
        "tipo_relazione": "attua",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("principio", None, "Annex A.3 (mapping con Allegato IV Reg. 910/2014)"),
        "nodo_a": ("obbligo", 2, "art. 45 §1 (vigente, eIDAS2)"),
        "tipo_relazione": "attua",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("principio", None, "QCS-4.3.5-01"),
        "nodo_a": ("obbligo", 2, "art. 24 §1-bis (nuovo, eIDAS2 — metodi di verifica dell'identità)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("principio", None, "clausola 4.3.5.3 (metodi di identificazione eIDAS successivi a eIDAS2)"),
        "nodo_a": ("obbligo", 2, "art. 24 §1-bis (nuovo, eIDAS2 — metodi di verifica dell'identità)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", 4, "art. 13 c.3"),
        "nodo_a": ("principio", None, "clausola 4.2.2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", 4, "art. 42 c.5"),
        "nodo_a": ("principio", None, "clausola 4.2.2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
]
