"""Utilità condivise per gli script di migrazione/embedding Neo4j.

Centralizza connessione al driver (credenziali da `.env`, mai hardcoded) e la mappatura
dei 14 tipi di relazione tipizzata (ADR-0004/0005/0008) verso nomi di arco Cypher validi
(UPPER_SNAKE_CASE, ASCII — i nomi originali contengono spazi e accenti).
"""

import os
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
