"""Migrazione dati SQLite (`censimento.db`) -> Neo4j (docs/plan-migrazione-neo4j.md, Fase 3).

Standalone, idempotente: droppa e ricrea i nodi/archi del censimento (stesso spirito di
seed.py — "una tantum / per ripartire puliti"). Non calcola embedding (quello è
`embed_neo4j.py`, Fase 4, separato perché più lento e con dipendenza da modello — separare
le fasi rende ripetibile la sola migrazione strutturale senza ricalcolare vettori ogni volta).

`modifiche_rilevate` non entra nel grafo Neo4j (decisione Fase 2, `neo4j_schema.cypher`): viene
invece copiata in `app/monitoraggio.db`, il DB SQLite dedicato che `web_ui.py` usa per il
monitoraggio (stesso spirito "una tantum" — ripetibile senza duplicare righe).

    app/.venv/bin/python app/migrate_to_neo4j.py
"""

import sqlite3
from collections import defaultdict

from neo4j_common import DB_PATH, TIPO_RELAZIONE_TO_ARCO, get_database, get_driver, mon_conn

LABEL_DI_TIPO = {"obbligo": "Obbligo", "principio": "Principio"}


def _sqlite_conn() -> sqlite3.Connection:
    if not DB_PATH.exists():
        raise SystemExit(f"Database non trovato: {DB_PATH}. Esegui prima seed.py (branch SQLite storico).")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _lookup(conn: sqlite3.Connection, table: str) -> dict[int, str]:
    return {r["id"]: r["nome"] for r in conn.execute(f"SELECT id, nome FROM {table}")}



def _migra_modifiche_rilevate(sconn: sqlite3.Connection) -> None:
    righe = [dict(r) for r in sconn.execute("SELECT * FROM modifiche_rilevate")]
    with mon_conn() as mconn:
        mconn.execute("DELETE FROM modifiche_rilevate")
        mconn.executemany(
            "INSERT INTO modifiche_rilevate (id, fonte_id, riferimento, data_rilevamento, "
            "testo_precedente, testo_nuovo, esaminata) VALUES (:id, :fonte_id, :riferimento, "
            ":data_rilevamento, :testo_precedente, :testo_nuovo, :esaminata)",
            righe,
        )
        mconn.commit()
    print(f"[OK] modifiche_rilevate: {len(righe)} righe copiate in app/monitoraggio.db")

def migrate_from_connection(sconn: sqlite3.Connection, driver, database: str) -> None:
    """Nucleo della migrazione strutturale: legge da una connessione sqlite3 già aperta (con
    `row_factory = sqlite3.Row`) e scrive su Neo4j. Riusata sia da `migrate()` (legge da
    `censimento.db` su disco) sia da `seed.py` (scrive su una connessione sqlite in-memory,
    eliminando il file intermedio — Fase 0/Fase 8 decisione utente)."""
    tipi_obbligo = _lookup(sconn, "tipi_obbligo")
    tipi_principio = _lookup(sconn, "tipi_principio")
    stati_norma = _lookup(sconn, "stati_norma")
    stati_fonte = _lookup(sconn, "stati_fonte")
    categorie = _lookup(sconn, "categorie_soggetto")
    oggetti = _lookup(sconn, "oggetti_giuridici")
    tipi_relazione = {
        r["id"]: r["nome"] for r in sconn.execute("SELECT id, nome, nome_inverso FROM tipi_relazione")
    }

    fonti_rows = [dict(r) for r in sconn.execute("SELECT * FROM fonti")]
    obblighi_rows = [dict(r) for r in sconn.execute("SELECT * FROM obblighi")]
    principi_rows = [dict(r) for r in sconn.execute("SELECT * FROM principi")]
    obbligo_soggetti_rows = [dict(r) for r in sconn.execute("SELECT * FROM obbligo_soggetti")]
    principio_oggetti_rows = [dict(r) for r in sconn.execute("SELECT * FROM principio_oggetti")]
    relazioni_rows = [dict(r) for r in sconn.execute("SELECT * FROM relazioni")]

    with driver.session(database=database) as session:
        # Ripartenza pulita: rimuove solo i nodi/archi di nostra competenza (idempotente).
        session.run(
            "MATCH (n) WHERE n:Obbligo OR n:Principio OR n:Fonte OR n:CategoriaSoggetto OR n:OggettoGiuridico "
            "DETACH DELETE n"
        )

        session.run(
            "UNWIND $rows AS row CREATE (f:Fonte) SET f = row",
            rows=[{
                "id": r["id"], "nome": r["nome"], "url_sorgente": r["url_sorgente"], "urn": r["urn"],
                "versione": r["versione"], "data_entrata_vigore": r["data_entrata_vigore"],
                "stato": stati_fonte.get(r["stato_id"], "?"),
            } for r in fonti_rows],
        )

        session.run("UNWIND $nomi AS nome MERGE (:CategoriaSoggetto {nome: nome})", nomi=list(categorie.values()))
        session.run("UNWIND $nomi AS nome MERGE (:OggettoGiuridico {nome: nome})", nomi=list(oggetti.values()))

        session.run(
            "UNWIND $rows AS row CREATE (o:Obbligo) SET o = row",
            rows=[{
                "id": r["id"], "fonte_id": r["fonte_id"], "riferimento": r["riferimento"], "testo": r["testo"],
                "testo_integrale": r["testo_integrale"], "tipo_obbligo": tipi_obbligo.get(r["tipo_obbligo_id"], "?"),
                "stato_obbligo": stati_norma.get(r["stato_id"], "?"),
                "data_inizio_vigore": r["data_inizio_vigore"], "data_fine_vigore": r["data_fine_vigore"],
                "severita": r["severita"], "sanzioni": r["sanzioni"],
                "condizione_applicabilita": r["condizione_applicabilita"],
                "stato_validazione": r["stato_validazione"], "validato_da": r["validato_da"],
                "data_validazione": r["data_validazione"],
            } for r in obblighi_rows],
        )

        session.run(
            "UNWIND $rows AS row CREATE (p:Principio) SET p = row",
            rows=[{
                "id": r["id"], "fonte_id": r["fonte_id"], "riferimento": r["riferimento"], "testo": r["testo"],
                "testo_integrale": r["testo_integrale"],
                "tipo_principio": tipi_principio.get(r["tipo_principio_id"], "?"),
                "stato_obbligo": stati_norma.get(r["stato_id"], "?"),
                "data_inizio_vigore": r["data_inizio_vigore"], "data_fine_vigore": r["data_fine_vigore"],
                "condizione_applicabilita": r["condizione_applicabilita"],
                "stato_validazione": r["stato_validazione"], "validato_da": r["validato_da"],
                "data_validazione": r["data_validazione"],
            } for r in principi_rows],
        )

        session.run(
            "UNWIND $rows AS r MATCH (o:Obbligo {id: r.id}), (f:Fonte {id: r.fonte_id}) CREATE (o)-[:DA_FONTE]->(f)",
            rows=[{"id": r["id"], "fonte_id": r["fonte_id"]} for r in obblighi_rows],
        )
        session.run(
            "UNWIND $rows AS r MATCH (p:Principio {id: r.id}), (f:Fonte {id: r.fonte_id}) CREATE (p)-[:DA_FONTE]->(f)",
            rows=[{"id": r["id"], "fonte_id": r["fonte_id"]} for r in principi_rows],
        )

        session.run(
            "UNWIND $rows AS r MATCH (o:Obbligo {id: r.obbligo_id}), (c:CategoriaSoggetto {nome: r.nome}) "
            "CREATE (o)-[:HA_SOGGETTO {ruolo: r.ruolo}]->(c)",
            rows=[{
                "obbligo_id": r["obbligo_id"], "nome": categorie[r["categoria_soggetto_id"]], "ruolo": r["ruolo"],
            } for r in obbligo_soggetti_rows],
        )
        session.run(
            "UNWIND $rows AS r MATCH (p:Principio {id: r.principio_id}), (o:OggettoGiuridico {nome: r.nome}) "
            "CREATE (p)-[:HA_OGGETTO]->(o)",
            rows=[{
                "principio_id": r["principio_id"], "nome": oggetti[r["oggetto_giuridico_id"]],
            } for r in principio_oggetti_rows],
        )

        # Archi tipizzati (ADR-0004/0005): il tipo di arco Cypher non è parametrizzabile, quindi
        # si raggruppano le righe per (label_da, label_a, arco) ed emette una query per gruppo.
        gruppi: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
        for r in relazioni_rows:
            nome_tipo = tipi_relazione[r["tipo_relazione_id"]]
            arco = TIPO_RELAZIONE_TO_ARCO[nome_tipo]
            chiave = (LABEL_DI_TIPO[r["nodo_da_tipo"]], LABEL_DI_TIPO[r["nodo_a_tipo"]], arco)
            gruppi[chiave].append({
                "relazione_id": r["id"], "da_id": r["nodo_da_id"], "a_id": r["nodo_a_id"],
                "evidence_type": r["evidence_type"], "confidence": r["confidence"],
                "tipo_relazione": nome_tipo,
            })
        for (label_da, label_a, arco), righe in gruppi.items():
            session.run(
                f"UNWIND $rows AS r MATCH (a:{label_da} {{id: r.da_id}}), (b:{label_a} {{id: r.a_id}}) "
                f"CREATE (a)-[rel:{arco} {{relazione_id: r.relazione_id, evidence_type: r.evidence_type, "
                f"confidence: r.confidence, tipo_relazione: r.tipo_relazione}}]->(b)",
                rows=righe,
            )

    _migra_modifiche_rilevate(sconn)


def migrate() -> None:
    sconn = _sqlite_conn()
    driver = get_driver()
    database = get_database()

    migrate_from_connection(sconn, driver, database)
    _verifica(sconn, driver, database)
    driver.close()
    sconn.close()



def _verifica(sconn: sqlite3.Connection, driver, database: str) -> None:
    with driver.session(database=database) as session:
        neo4j_counts = {
            "obblighi": session.run("MATCH (n:Obbligo) RETURN count(n) AS c").single()["c"],
            "principi": session.run("MATCH (n:Principio) RETURN count(n) AS c").single()["c"],
            "relazioni": session.run(
                "MATCH ()-[r]->() WHERE r.relazione_id IS NOT NULL RETURN count(r) AS c"
            ).single()["c"],
            "obbligo_soggetti": session.run("MATCH ()-[r:HA_SOGGETTO]->() RETURN count(r) AS c").single()["c"],
            "principio_oggetti": session.run("MATCH ()-[r:HA_OGGETTO]->() RETURN count(r) AS c").single()["c"],
        }
    sqlite_counts = {
        table: sconn.execute(f"SELECT COUNT(*) c FROM {table}").fetchone()["c"]
        for table in ("obblighi", "principi", "relazioni", "obbligo_soggetti", "principio_oggetti")
    }

    tutto_ok = True
    for tabella, atteso in sqlite_counts.items():
        ottenuto = neo4j_counts[tabella]
        combacia = atteso == ottenuto
        tutto_ok = tutto_ok and combacia
        esito = "OK" if combacia else "MISMATCH"
        print(f"[{esito}] {tabella}: sqlite={atteso} neo4j={ottenuto}")

    if not tutto_ok:
        raise SystemExit(1)
    print("Migrazione completata: conteggi sqlite/neo4j combacianti.")


if __name__ == "__main__":
    migrate()
