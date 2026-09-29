"""Utilità condivise per gli script di migrazione/embedding Neo4j.

Centralizza connessione al driver (credenziali da `.env`, mai hardcoded) e la mappatura
dei 14 tipi di relazione tipizzata (ADR-0004/0005/0008) verso nomi di arco Cypher validi
(UPPER_SNAKE_CASE, ASCII — i nomi originali contengono spazi e accenti).
"""

import os
import re
import sqlite3
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from neo4j import GraphDatabase

APP_DIR = Path(__file__).parent
DB_PATH = APP_DIR / "censimento.db"
SCHEMA_CYPHER_PATH = APP_DIR / "neo4j_schema.cypher"

EMBEDDING_MODEL_NAME = "paraphrase-multilingual-mpnet-base-v2"
EMBEDDING_DIMENSIONS = 768

# Tabelle di lookup puramente enumerative (schema.sql: tipi_obbligo, tipi_principio, stati_norma,
# stati_fonte): decisione di Fase 2 — NON diventano nodi Neo4j (nessun attributo oltre al nome),
# restano costanti Python condivise da seed.py (scrittura) e web_ui.py (lettura/validazione).
TIPI_OBBLIGO = [
    "organizzativo", "tecnico/sicurezza", "informativo/trasparenza",
    "procedurale", "di conservazione", "sanzionatorio",
]
TIPI_PRINCIPIO = [
    "non discriminazione", "equivalenza giuridica", "valore probatorio", "presunzione legale",
    "scopo/ambito di applicazione", "definitorio", "altro",
]
STATI_NORMA = ["vigente", "abrogato", "in transizione eIDAS->eIDAS2"]
STATI_FONTE = ["vigente", "abrogata", "in transizione"]

# nome -> nome_inverso, per etichettare i vicini raggiunti in direzione "a ritroso" (_vicini_di).
TIPI_RELAZIONE_INVERSO = {
    "sostituisce": "è sostituito da",
    "specifica": "è specificato da",
    "si sovrappone a": "si sovrappone a",
    "richiede come precondizione": "è precondizione di",
    "è condizionato da": "condiziona",
    "attua": "è attuato da",
    "richiama": "è richiamato da",
    "si applica a": "gli si applica",
    "modifica": "è modificato da",
    "abroga": "è abrogato da",
    "definisce": "è definito da",
    "sanziona": "è sanzionato da",
    "deroga a": "è derogato da",
    "recepisce": "è recepito da",
}

# modifiche_rilevate (monitoraggio automatico delle Fonti) resta fuori dal grafo Neo4j
# (decisione Fase 2, vedi commento in neo4j_schema.cypher): coda di lavoro relazionale minima,
# non referenziata da altre entità del grafo, in un DB SQLite separato e dedicato.
MONITORAGGIO_DB_PATH = APP_DIR / "monitoraggio.db"

# Fase 2: nome tipo_relazione (schema.sql/seed.py) -> nome arco Cypher.
TIPO_RELAZIONE_TO_ARCO = {
    "sostituisce": "SOSTITUISCE",
    "specifica": "SPECIFICA",
    "si sovrappone a": "SI_SOVRAPPONE_A",
    "richiede come precondizione": "RICHIEDE_COME_PRECONDIZIONE",
    "è condizionato da": "E_CONDIZIONATO_DA",
    "attua": "ATTUA",
    "richiama": "RICHIAMA",
    "si applica a": "SI_APPLICA_A",
    "modifica": "MODIFICA",
    "abroga": "ABROGA",
    "definisce": "DEFINISCE",
    "sanziona": "SANZIONA",
    "deroga a": "DEROGA_A",
    "recepisce": "RECEPISCE",
}

# Fase 7 (ADR-0006): peso di direttezza per tipo di relazione, dal più diretto (5) al meno
# diretto (1). "definisce" non è nell'ordine esplicito dell'ADR: trattato come collegamento
# puramente referenziale/descrittivo, stesso livello di richiama/si sovrappone a (2).
DIRETTEZZA_PESO = {
    "sostituisce": 5, "abroga": 5,
    "modifica": 4, "specifica": 4, "deroga a": 4,
    "si applica a": 3, "attua": 3, "sanziona": 3, "recepisce": 3,
    "richiama": 2, "si sovrappone a": 2, "definisce": 2,
    "richiede come precondizione": 1, "è condizionato da": 1,
}


def load_env() -> dict:
    """Legge app/.env (KEY=VALUE per riga, niente dipendenza da python-dotenv)."""
    env_path = APP_DIR / ".env"
    values = dict(os.environ)
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            values.setdefault(key.strip(), val.strip())
    return values


VERSIONE_DRIVER_ATTESA = "5.28.1"


def _verifica_versione_driver() -> None:
    """Guardia esplicita contro la regressione nota: neo4j==6.3.0 installato in
    app/.venv si blocca indefinitamente (query mai completate, nessun errore)
    contro il server Neo4j Desktop 2026.08.1 in uso in questo progetto — la
    causa e' stata isolata solo dopo una sessione di debug con socket raw e
    cypher-shell (vedi docs/runbook-neo4j-import.md). Fallire subito con un
    messaggio chiaro costa una riga; lasciare che la query si blocchi a tempo
    indeterminato costa ore di diagnosi alla cieca.
    """
    try:
        installata = version("neo4j")
    except PackageNotFoundError:
        return
    if installata != VERSIONE_DRIVER_ATTESA:
        raise RuntimeError(
            f"Driver neo4j installato: {installata}, atteso {VERSIONE_DRIVER_ATTESA}. "
            "Versioni diverse (es. 6.3.0) sono note per bloccarsi indefinitamente contro "
            "questa istanza Neo4j Desktop (server risponde, il driver Python no). "
            f"Fix: pip install 'neo4j=={VERSIONE_DRIVER_ATTESA}'. "
            "Dettagli: docs/runbook-neo4j-import.md."
        )


def get_driver():
    _verifica_versione_driver()
    env = load_env()
    uri = env.get("NEO4J_URI", "bolt://127.0.0.1:7687")
    user = env.get("NEO4J_USER", "neo4j")
    password = env.get("NEO4J_PASSWORD")
    if not password:
        raise RuntimeError(
            "NEO4J_PASSWORD non impostata: copiare app/.env.example in app/.env e valorizzarla "
            "con la password dell'istanza Neo4j Desktop."
        )
    return GraphDatabase.driver(uri, auth=(user, password))


def get_database() -> str:
    return load_env().get("NEO4J_DATABASE", "neo4j")


def mon_conn() -> sqlite3.Connection:
    """Connessione al DB SQLite dedicato a modifiche_rilevate (monitoraggio automatico)."""
    conn = sqlite3.connect(MONITORAGGIO_DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("""
        CREATE TABLE IF NOT EXISTS modifiche_rilevate (
            id INTEGER PRIMARY KEY,
            fonte_id INTEGER NOT NULL,
            riferimento TEXT NOT NULL,
            data_rilevamento TEXT NOT NULL,
            testo_precedente TEXT NOT NULL,
            testo_nuovo TEXT NOT NULL,
            esaminata INTEGER NOT NULL DEFAULT 0 CHECK (esaminata IN (0,1))
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_modifiche_fonte ON modifiche_rilevate(fonte_id, esaminata)")
    return conn


# --------------------------------------------------------------------- partizioni
# Livello strutturale intermedio fra il nodo di prescrizione (unità di censimento:
# comma, lettera, punto di allegato) e la Fonte: un nodo `:Partizione` per ciascuna
# unità indivisa citabile "in blocco" - articolo, sezione di allegato, clausola di
# standard. Serve perché molti rinvii normativi hanno per bersaglio l'unità indivisa
# e non un singolo comma ("in conformità degli articoli 13 e 19", "si applica
# l'allegato IV", "clausola 6.8.5"): senza un nodo di partizione quei rinvii
# restavano senza arco, o venivano agganciati a un comma scelto a mano.
# La partizione non porta testo normativo (nessuna duplicazione) e la regola
# ADR-0007 "un nodo di prescrizione per articolo/comma" resta intatta.
#
# Generazione deterministica dai riferimenti già normalizzati dei moduli (mai a mano):
# vedi `partizioni_di`. L'arco strutturale è (nodo di prescrizione)-[:PARTE_DI]->
# (partizione), e fra partizioni (sezione -> allegato, clausola figlia -> clausola
# padre), generato in `migrate_to_neo4j.migrate_from_connection`.

TIPO_PARTIZIONE_ARTICOLO = "articolo"
TIPO_PARTIZIONE_ALLEGATO = "allegato"
TIPO_PARTIZIONE_SEZIONE = "sezione"
TIPO_PARTIZIONE_CLAUSOLA = "clausola"
TIPO_PARTIZIONE_PARAGRAFO = "paragrafo"


def partizioni_di(riferimento: str) -> list[tuple[str, str]]:
    """Catena delle partizioni a cui appartiene un riferimento, dalla più specifica
    alla radice: lista di `(riferimento_partizione, tipo_partizione)`.

    Regole (deterministiche, documentate in docs/adr/0012-*.md):
    - `art. 13 §1`, `art. 5 bis §4(a)`, `art. 2, punto 3` -> `art. 13` / `art. 5 bis` / `art. 2`;
    - `allegato IV, sezione IV.3, punto 5` -> `allegato IV, sezione IV.3` e `allegato IV`;
      `allegato III, punto 2` o `allegato, adeguamento a) ...` -> `allegato III` / `allegato`;
    - `clausola 5.2.2 (titolo)` -> `clausola 5.2` e `clausola 5` (la clausola di primo
      livello è già il nodo stesso: nessuna partizione);
    - id di requisito ETSI con la clausola nel nome (`REQ-7.8-13`, `GEN-6.5.1-06`,
      `ISS-8.5.1-01`, `QTS-C.2.3-03`) -> `clausola 7.8` (o `clausola 6.5.1`, `clausola
      8.5.1`, `clausola C.2.3`) e le sue radici (`clausola 7`, ...);
    - prefisso di parte (`Parte 2: REQ-7.8-13`) conservato nella partizione
      (`Parte 2: clausola 7.8`), perché le parti sono censite come Fonte unica.

    Riferimenti senza struttura riconoscibile (es. id di controllo di ETSI TS 119 101
    come `SCP 13`, sigle prive di numerazione di clausola) restituiscono lista vuota:
    la guardia `tests`/report di seed li elenca e restano senza partizione, invece di
    produrre un nodo inventato.
    """
    rif = riferimento.strip()
    prefisso = ""
    m = re.match(r"^(Parte \d+):\s*(.+)$", rif)
    if m:
        prefisso, rif = m.group(1) + ": ", m.group(2).strip()

    # clausola (o "par." di una fonte che numera così): se il riferimento scende a
    # un'unità più fine (comma, punto, lettera) la partizione è la clausola che la
    # contiene; se il riferimento È la clausola, la partizione è la sua clausola padre
    # (la clausola stessa è già un nodo del censimento).
    m = re.match(r"^(clausola|par\.)\s+(\d+(?:\.\d+)*)", rif)
    if m:
        etichetta, numerazione = m.group(1), m.group(2)
        tipo = TIPO_PARTIZIONE_CLAUSOLA if etichetta == "clausola" else TIPO_PARTIZIONE_PARAGRAFO
        segmenti = numerazione.split(".")
        catena: list[tuple[str, str]] = []
        if re.search(r"§|punto|comma|lett\.", rif[m.end():]):
            catena.append((f"{prefisso}{etichetta} {numerazione}", tipo))
        while len(segmenti) > 1:
            segmenti = segmenti[:-1]
            catena.append((f"{prefisso}{etichetta} " + ".".join(segmenti), tipo))
        return catena

    # id di requisito con la clausola nel nome (ES: REQ-7.8-13, VAL-8.3.7-04, QTS-C.2.3-03)
    m = re.match(r"^[A-Za-z]+-([0-9A-Z][0-9A-Z.]*)-[0-9A-Za-z]+$", rif)
    if m:
        segmenti = m.group(1).split(".")
        catena = [(prefisso + "clausola " + ".".join(segmenti), TIPO_PARTIZIONE_CLAUSOLA)]
        while len(segmenti) > 1:
            segmenti = segmenti[:-1]
            catena.append((prefisso + "clausola " + ".".join(segmenti), TIPO_PARTIZIONE_CLAUSOLA))
        return catena

    # allegati, con o senza numero romano e con o senza sezione
    m = re.match(r"^allegato(?:\s+([IVXL]+))?(?:,\s*sezione\s+([IVXL0-9]+(?:\.[0-9]+)*))?", rif)
    if m and (m.group(1) or m.group(2) or rif.startswith("allegato")):
        catena = []
        if m.group(2):
            etichetta = f"allegato {m.group(1)}" if m.group(1) else "allegato"
            catena.append((f"{etichetta}, sezione {m.group(2)}", TIPO_PARTIZIONE_SEZIONE))
        catena.append((f"allegato {m.group(1)}" if m.group(1) else "allegato", TIPO_PARTIZIONE_ALLEGATO))
        return catena

    # annessi in forma inglese degli standard ETSI ("Annex A.1.1.1 (titolo)",
    # "Annex D (normative), premessa (...)", "Annex D, modulo ..."): la catena dei padri e'
    # "Annex X, clausola X.a.b" -> "Annex X, clausola X.a" -> "Annex X".
    m = re.match(r"^Annex\s+([A-Z])(?:\.(\d+(?:\.\d+)*))?", rif)
    if m:
        lettera, numerazione = m.group(1), m.group(2)
        if not numerazione:
            # forma "Annex E, clause E.1.1 (...)" usata dalle Fonti ETSI multi-annesso
            m2 = re.match(r"^Annex\s+[A-Z],\s*(?:clause|clausola)\s+[A-Z]\.(\d+(?:\.\d+)*)", rif, re.I)
            if m2:
                numerazione = m2.group(1)
        catena = []
        if numerazione:
            segmenti = numerazione.split(".")
            while len(segmenti) > 1:
                segmenti = segmenti[:-1]
                catena.append((f"Annex {lettera}, clausola {lettera}." + ".".join(segmenti), TIPO_PARTIZIONE_CLAUSOLA))
        catena.append((f"Annex {lettera}", TIPO_PARTIZIONE_ALLEGATO))
        return catena

    # articoli (con eventuale suffisso bis/ter/quater/...)
    m = re.match(r"^(art\.\s*\d+(?:\s*-?\s*(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|undecies|duodecies|terdecies))?)", rif)
    if m:
        return [(re.sub(r"\s*-\s*", "-", m.group(1).strip()), TIPO_PARTIZIONE_ARTICOLO)]

    return []
