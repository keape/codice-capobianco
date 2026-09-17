"""Pipeline di embedding per la vector index Neo4j (docs/plan-migrazione-neo4j.md, Fase 4).

Decisione di design (presa qui, non assunta a priori): **1 vettore per nodo**, calcolato sul
campo `testo` (sintesi densa, già pensata per essere breve e rappresentativa), non su
`testo_integrale` chunkato. Motivo: 1 vettore per nodo è coerente con la vector index dichiarata
in Fase 2 come proprietà singola (`Obbligo.embedding`/`Principio.embedding`); N vettori per nodo
richiederebbe nodi satellite `:TextUnit` (un pezzo di SAT-Graph mai deciso per questo censimento,
vedi ADR-0006 "Chiarimento"). Si perde granularità sui pochi nodi con `testo_integrale` molto
lungo, ma la ricerca full-text Lucene (Fase 2) copre già `testo_integrale` per intero: il vettore
serve al match semantico sulla sintesi, non a sostituire il full-text sul testo esteso.

Separato da `migrate_to_neo4j.py` (Fase 3): il calcolo embedding è la parte più lenta/con
dipendenza da modello — separare le fasi rende ripetibile la sola migrazione strutturale senza
ricalcolare vettori ogni volta. Rieseguibile in autonomia dopo ogni `migrate_to_neo4j.py`.

    app/.venv/bin/python app/embed_neo4j.py
"""

from sentence_transformers import SentenceTransformer

from neo4j_common import EMBEDDING_DIMENSIONS, EMBEDDING_MODEL_NAME, get_database, get_driver

BATCH_SIZE = 32


def _embed_label(session, model: SentenceTransformer, label: str) -> int:
    rows = session.run(f"MATCH (n:{label}) RETURN n.id AS id, n.testo AS testo").data()
    if not rows:
        return 0
    testi = [r["testo"] or "" for r in rows]
    vettori = model.encode(testi, batch_size=BATCH_SIZE, show_progress_bar=False, normalize_embeddings=True)
    payload = [{"id": r["id"], "embedding": vettori[i].tolist()} for i, r in enumerate(rows)]
    session.run(
        f"UNWIND $rows AS row MATCH (n:{label} {{id: row.id}}) SET n.embedding = row.embedding",
        rows=payload,
    )
    return len(payload)


def embed() -> None:
    model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    dim = model.get_embedding_dimension()
    if dim != EMBEDDING_DIMENSIONS:
        raise SystemExit(
            f"Il modello {EMBEDDING_MODEL_NAME} produce vettori a {dim} dimensioni, "
            f"ma la vector index in neo4j_schema.cypher è dichiarata a {EMBEDDING_DIMENSIONS}. "
            "Aggiornare lo schema (Fase 2) prima di procedere."
        )

    driver = get_driver()
    database = get_database()
    with driver.session(database=database) as session:
        n_obblighi = _embed_label(session, model, "Obbligo")
        n_principi = _embed_label(session, model, "Principio")
    driver.close()
    print(f"Embedding scritto: {n_obblighi} Obbligo, {n_principi} Principio (dim={dim}).")


if __name__ == "__main__":
    embed()
