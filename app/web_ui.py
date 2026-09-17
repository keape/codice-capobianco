"""UI web del censimento obblighi QTSP (nata come mockup nel ticket 07, ora in produzione).

Copre le tre funzioni previste dal ticket: consultazione/ricerca con le relazioni tipizzate
del grafo, coda di revisione delle bozze generate dall'estrazione (valida/correggi/rifiuta),
badge di notifica per le fonti con modifiche rilevate dal monitoraggio (ticket 05).

Storage: Neo4j (migrazione ADR-0006 / docs/plan-migrazione-neo4j.md), non più SQLite —
`censimento.db` resta come backup storico/fonte di export una tantum (Fase 3), non è più
letto da questa UI. Unica eccezione: `modifiche_rilevate` (monitoraggio automatico delle
Fonti) resta su un piccolo DB SQLite dedicato (`app/monitoraggio.db`, Fase 2) perché non fa
parte del grafo.

Ricerca: faceted + full-text Lucene su `/api/obblighi`/`/api/principi` (sostituisce lo scan
Python case-insensitive pre-migrazione), più un endpoint di ricerca ibrida a fusione WRRF
(lessicale + semantico, ADR-0006) su `/api/ricerca`.

    app/.venv/bin/python app/seed.py       # una tantum / per ripartire puliti (scrive su Neo4j)
    app/.venv/bin/python app/migrate_to_neo4j.py   # se si riparte invece da censimento.db
    app/.venv/bin/python app/embed_neo4j.py        # (ri)calcola gli embedding per la ricerca semantica
    app/.venv/bin/python app/web_ui.py
    -> http://127.0.0.1:8010
"""

import argparse
from datetime import date
from functools import lru_cache

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel

from neo4j_common import (
    DIRETTEZZA_PESO,
    EMBEDDING_MODEL_NAME,
    STATI_NORMA,
    TIPI_OBBLIGO,
    TIPI_PRINCIPIO,
    TIPI_RELAZIONE_INVERSO,
    TIPO_RELAZIONE_TO_ARCO,
    get_database,
    get_driver,
    mon_conn,
)

app = FastAPI(title="Censimento Obblighi QTSP", docs_url=None, redoc_url=None)

_driver = None
_database = None

# Pesi WRRF (ADR-0006 § "Pesi WRRF: lessicale vs semantico") — costanti nominate, non magic
# number sparso nella logica di fusione.
PESO_LESSICALE = 0.55
PESO_SEMANTICO = 0.45

ARCHI_RELAZIONE = list(TIPO_RELAZIONE_TO_ARCO.values())


@app.on_event("startup")
def _startup():
    global _driver, _database
    _driver = get_driver()
    _database = get_database()


@app.on_event("shutdown")
def _shutdown():
    if _driver is not None:
        _driver.close()


def _session():
    if _driver is None:
        raise HTTPException(503, "Driver Neo4j non inizializzato")
    return _driver.session(database=_database)


@lru_cache(maxsize=1)
def _embedding_model():
    """Modello caricato pigramente: solo /api/ricerca lo usa, non serve al boot dell'app."""
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(EMBEDDING_MODEL_NAME)


# --------------------------------------------------------------- costruzione righe

def _riga_obbligo(rec) -> dict:
    n = rec["n"]
    return {
        "tipo_nodo": "obbligo",
        "obbligo_id": n["id"],
        "fonte_id": n["fonte_id"],
        "fonte": rec["fonte"],
        "riferimento": n["riferimento"],
        "testo": n["testo"],
        "testo_integrale": n.get("testo_integrale"),
        "tipo_obbligo": n["tipo_obbligo"],
        "stato_obbligo": n["stato_obbligo"],
        "data_inizio_vigore": n.get("data_inizio_vigore"),
        "data_fine_vigore": n.get("data_fine_vigore"),
        "severita": n.get("severita"),
        "sanzioni": n.get("sanzioni"),
        "condizione_applicabilita": n.get("condizione_applicabilita"),
        "stato_validazione": n["stato_validazione"],
        "validato_da": n.get("validato_da"),
        "data_validazione": n.get("data_validazione"),
        "soggetti_obbligati": rec["soggetti_obbligati"],
        "destinatari": rec["destinatari"],
    }


def _riga_principio(rec) -> dict:
    n = rec["n"]
    return {
        "tipo_nodo": "principio",
        "principio_id": n["id"],
        "fonte_id": n["fonte_id"],
        "fonte": rec["fonte"],
        "riferimento": n["riferimento"],
        "testo": n["testo"],
        "testo_integrale": n.get("testo_integrale"),
        "tipo_principio": n["tipo_principio"],
        "stato_obbligo": n["stato_obbligo"],
        "data_inizio_vigore": n.get("data_inizio_vigore"),
        "data_fine_vigore": n.get("data_fine_vigore"),
        "condizione_applicabilita": n.get("condizione_applicabilita"),
        "stato_validazione": n["stato_validazione"],
        "validato_da": n.get("validato_da"),
        "data_validazione": n.get("data_validazione"),
        "oggetti_giuridici": rec["oggetti_giuridici"],
    }


_OBBLIGHI_QUERY = """
    MATCH (o:Obbligo)-[:DA_FONTE]->(f:Fonte)
    OPTIONAL MATCH (o)-[hs:HA_SOGGETTO]->(cs:CategoriaSoggetto)
    WITH o, f, collect(DISTINCT CASE WHEN hs.ruolo = 'obbligato' THEN cs.nome END) AS obbligati,
               collect(DISTINCT CASE WHEN hs.ruolo = 'destinatario' THEN cs.nome END) AS destinatari
    RETURN o AS n, f.nome AS fonte,
           [x IN obbligati WHERE x IS NOT NULL] AS soggetti_obbligati,
           [x IN destinatari WHERE x IS NOT NULL] AS destinatari
    ORDER BY o.id
"""

_PRINCIPI_QUERY = """
    MATCH (p:Principio)-[:DA_FONTE]->(f:Fonte)
    OPTIONAL MATCH (p)-[:HA_OGGETTO]->(og:OggettoGiuridico)
    WITH p, f, collect(DISTINCT og.nome) AS oggetti
    RETURN p AS n, f.nome AS fonte, oggetti AS oggetti_giuridici
    ORDER BY p.id
"""


def _obblighi_all(session) -> list[dict]:
    return [_riga_obbligo(r) for r in session.run(_OBBLIGHI_QUERY).data()]


def _principi_all(session) -> list[dict]:
    return [_riga_principio(r) for r in session.run(_PRINCIPI_QUERY).data()]


# ------------------------------------------------------------------- vicini (Fase 5+7)

_LABEL_DI_TIPO = {"obbligo": "Obbligo", "principio": "Principio"}
_TIPO_DI_LABEL = {"Obbligo": "obbligo", "Principio": "principio"}
_TIPI_ARCO_PATTERN = "|".join(ARCHI_RELAZIONE)


def _vicini_di(session, tipo_nodo: str, nodo_id: int, profondita: int = 1) -> list[dict]:
    """Vicini di un nodo del grafo (Obbligo o Principio, ADR-0004) via traversal Cypher nativo.

    Multi-hop pesato (ADR-0006/Fase 7): profondita=1 riproduce esattamente il comportamento
    1-hop pre-Fase-7 (nessun cambio di comportamento salvo richiesta esplicita). Per hop > 1,
    il ranking ordina per distanza (hop count) crescente e, a parità di hop, per direttezza del
    tipo di relazione decrescente (peso dell'ultimo arco del percorso, DIRETTEZZA_PESO — la
    direttezza è una proprietà del tipo di relazione, non della direzione di attraversamento).
    Se un nodo è raggiungibile con più percorsi, si tiene il migliore (hop minore, poi peso
    maggiore).
    """
    label = _LABEL_DI_TIPO[tipo_nodo]
    query = f"""
        MATCH (start:{label} {{id: $nodo_id}})
        MATCH path = (start)-[rels:{_TIPI_ARCO_PATTERN}*1..{int(profondita)}]-(other)
        WHERE other <> start AND (other:Obbligo OR other:Principio)
        WITH other, rels[-1] AS ultimo, length(path) AS hop
        RETURN DISTINCT other AS n, labels(other) AS other_labels, hop,
               ultimo.relazione_id AS relazione_id, ultimo.tipo_relazione AS tipo_relazione_base,
               ultimo.evidence_type AS evidence_type, ultimo.confidence AS confidence,
               (endNode(ultimo) = other) AS forward
    """
    rows = session.run(query, nodo_id=nodo_id).data()

    fonti_cache: dict[int, str] = {}

    def _fonte_di(fonte_id: int) -> str:
        if fonte_id not in fonti_cache:
            rec = session.run("MATCH (f:Fonte {id: $id}) RETURN f.nome AS nome", id=fonte_id).single()
            fonti_cache[fonte_id] = rec["nome"] if rec else "?"
        return fonti_cache[fonte_id]

    migliori: dict[tuple[str, int], dict] = {}
    for r in rows:
        altro_label = "Obbligo" if "Obbligo" in r["other_labels"] else "Principio"
        altro_tipo = _TIPO_DI_LABEL[altro_label]
        chiave = (altro_tipo, r["n"]["id"])
        peso = DIRETTEZZA_PESO.get(r["tipo_relazione_base"], 0)
        candidato_rank = (r["hop"], -peso)
        esistente = migliori.get(chiave)
        if esistente is not None and esistente["_rank"] <= candidato_rank:
            continue
        tipo_relazione = r["tipo_relazione_base"] if r["forward"] else TIPI_RELAZIONE_INVERSO[r["tipo_relazione_base"]]
        n = r["n"]
        migliori[chiave] = {
            "_rank": candidato_rank,
            "tipo_nodo": altro_tipo,
            ("obbligo_id" if altro_tipo == "obbligo" else "principio_id"): n["id"],
            "relazione_id": r["relazione_id"],
            "tipo_relazione": tipo_relazione,
            "hop": r["hop"],
            "evidence_type": r["evidence_type"],
            "confidence": r["confidence"],
            "fonte": _fonte_di(n["fonte_id"]),
            "riferimento": n["riferimento"],
            "testo": n["testo"],
            "stato_validazione": n["stato_validazione"],
        }

    vicini = list(migliori.values())
    vicini.sort(key=lambda v: v["_rank"])
    for v in vicini:
        del v["_rank"]
    return vicini


# --------------------------------------------------------------- lookup/stats

@app.get("/api/lookup")
def lookup():
    with _session() as session:
        fonti = session.run(
            "MATCH (f:Fonte) RETURN f.id AS fonte_id, f.nome AS nome, f.versione AS versione, "
            "f.url_sorgente AS url_sorgente, f.urn AS urn, f.stato AS stato ORDER BY f.id"
        ).data()
        categorie = [r["nome"] for r in session.run("MATCH (c:CategoriaSoggetto) RETURN c.nome AS nome ORDER BY nome")]
        oggetti = [r["nome"] for r in session.run("MATCH (o:OggettoGiuridico) RETURN o.nome AS nome ORDER BY nome")]
    return {
        "status": "ok",
        "fonti": fonti,
        "tipi_obbligo": TIPI_OBBLIGO,
        "stati_obbligo": STATI_NORMA,
        "categorie_soggetto": categorie,
        "tipi_principio": TIPI_PRINCIPIO,
        "oggetti_giuridici": oggetti,
        "tipi_relazione": [{"nome": n, "nome_inverso": i} for n, i in TIPI_RELAZIONE_INVERSO.items()],
    }


@app.get("/api/stats")
def stats():
    with _session() as session:
        obblighi_counts = session.run(
            "MATCH (o:Obbligo) RETURN o.stato_validazione AS stato, count(*) AS c"
        ).data()
        counts = {r["stato"]: r["c"] for r in obblighi_counts}
        n_principi = session.run("MATCH (p:Principio) RETURN count(p) AS c").single()["c"]
        n_fonti = session.run("MATCH (f:Fonte) RETURN count(f) AS c").single()["c"]
        n_relazioni = session.run(
            "MATCH ()-[r]->() WHERE r.relazione_id IS NOT NULL RETURN count(r) AS c"
        ).single()["c"]
    with mon_conn() as mconn:
        n_modifiche = mconn.execute(
            "SELECT COUNT(*) c FROM modifiche_rilevate WHERE esaminata = 0"
        ).fetchone()["c"]
    return {
        "fonti": n_fonti,
        "obblighi_validati": counts.get("validato", 0),
        "obblighi_bozza": counts.get("bozza", 0),
        "principi": n_principi,
        "relazioni": n_relazioni,
        "modifiche_da_esaminare": n_modifiche,
    }


# ------------------------------------------------------------- consultazione

@app.get("/api/obblighi")
def cerca_obblighi(
    q: str = "",
    fonte_id: list[int] = Query(default=[]),
    tipo_obbligo: list[str] = Query(default=[]),
    stato_obbligo: list[str] = Query(default=[]),
    categoria_soggetto: list[str] = Query(default=[]),
    ruolo: str = Query("", pattern="^(|obbligato|destinatario)$"),
    solo_validati: bool = True,
):
    with _session() as session:
        righe = _obblighi_all(session)
        id_lessicali = _fulltext_ids(session, "idxTestoObbligo", q) if q.strip() else None

    risultati = []
    for r in righe:
        if solo_validati and r["stato_validazione"] != "validato":
            continue
        if fonte_id and r["fonte_id"] not in fonte_id:
            continue
        if tipo_obbligo and r["tipo_obbligo"] not in tipo_obbligo:
            continue
        if stato_obbligo and r["stato_obbligo"] not in stato_obbligo:
            continue
        if id_lessicali is not None and r["obbligo_id"] not in id_lessicali:
            continue
        if categoria_soggetto:
            pool = (
                r["soggetti_obbligati"] if ruolo == "obbligato"
                else r["destinatari"] if ruolo == "destinatario"
                else r["soggetti_obbligati"] + r["destinatari"]
            )
            if not any(c in pool for c in categoria_soggetto):
                continue
        risultati.append(r)

    return {"status": "ok", "totale": len(risultati), "risultati": risultati}


@app.get("/api/obblighi/{obbligo_id}")
def dettaglio_obbligo(obbligo_id: int, profondita: int = Query(default=1, ge=1, le=4)):
    with _session() as session:
        rec = session.run(
            _OBBLIGHI_QUERY.split("ORDER BY")[0].replace("MATCH (o:Obbligo)", "MATCH (o:Obbligo {id: $id})"),
            id=obbligo_id,
        ).data()
        if not rec:
            raise HTTPException(404, "Obbligo non trovato")
        obbligo = _riga_obbligo(rec[0])
        vicini = _vicini_di(session, "obbligo", obbligo_id, profondita=profondita)
    return {"status": "ok", "obbligo": obbligo, "vicini": vicini}


@app.get("/api/principi")
def cerca_principi(
    q: str = "",
    fonte_id: list[int] = Query(default=[]),
    tipo_principio: list[str] = Query(default=[]),
    oggetto_giuridico: list[str] = Query(default=[]),
    solo_validati: bool = True,
):
    with _session() as session:
        righe = _principi_all(session)
        id_lessicali = _fulltext_ids(session, "idxTestoPrincipio", q) if q.strip() else None

    risultati = []
    for r in righe:
        if solo_validati and r["stato_validazione"] != "validato":
            continue
        if fonte_id and r["fonte_id"] not in fonte_id:
            continue
        if tipo_principio and r["tipo_principio"] not in tipo_principio:
            continue
        if id_lessicali is not None and r["principio_id"] not in id_lessicali:
            continue
        if oggetto_giuridico and not any(o in r["oggetti_giuridici"] for o in oggetto_giuridico):
            continue
        risultati.append(r)

    return {"status": "ok", "totale": len(risultati), "risultati": risultati}


@app.get("/api/principi/{principio_id}")
def dettaglio_principio(principio_id: int, profondita: int = Query(default=1, ge=1, le=4)):
    with _session() as session:
        rec = session.run(
            _PRINCIPI_QUERY.split("ORDER BY")[0].replace("MATCH (p:Principio)", "MATCH (p:Principio {id: $id})"),
            id=principio_id,
        ).data()
        if not rec:
            raise HTTPException(404, "Principio non trovato")
        principio = _riga_principio(rec[0])
        vicini = _vicini_di(session, "principio", principio_id, profondita=profondita)
    return {"status": "ok", "principio": principio, "vicini": vicini}


def _query_lucene(termine: str) -> str:
    """Query Lucene a frase, con boost sul campo `riferimento` (ADR-0006): un match esatto sul
    riferimento normativo ("Art. 32") deve premiare l'articolo corrispondente, non un articolo
    qualunque che condivide solo alcuni termini nel testo esteso."""
    pulito = termine.strip().replace('"', '\\"')
    if not pulito:
        return ""
    return f'riferimento:"{pulito}"^3 OR testo:"{pulito}" OR testo_integrale:"{pulito}"'


def _fulltext_ids(session, index_name: str, q: str) -> set[int]:
    """ID dei nodi che matchano `q` sull'indice full-text Lucene indicato (ADR-0006:
    sostituisce lo scan Python case-insensitive)."""
    query_lucene = _query_lucene(q)
    if not query_lucene:
        return set()
    rows = session.run(
        f"CALL db.index.fulltext.queryNodes('{index_name}', $q) YIELD node RETURN node.id AS id",
        q=query_lucene,
    ).data()
    return {r["id"] for r in rows}


# ---------------------------------------------------------- Fase 6: ricerca ibrida WRRF

def _candidati_pre_filtrati(
    session, label: str, fonte_id: list[int], stato_validazione: list[str],
    tipo_obbligo: list[str], tipo_principio: list[str], categoria_soggetto: list[str],
    data_riferimento: str | None,
) -> set[int]:
    """Pre-filtro (ADR-0006): facet + range temporale come WHERE prima del retrieval, mai come
    termine pesato nella fusione — un nodo non vigente alla data di riferimento non deve mai
    comparire, indipendentemente dalla rilevanza lessicale/semantica."""
    clausole = ["true"]
    params: dict = {}
    if fonte_id:
        clausole.append("n.fonte_id IN $fonte_id")
        params["fonte_id"] = fonte_id
    if stato_validazione:
        clausole.append("n.stato_validazione IN $stato_validazione")
        params["stato_validazione"] = stato_validazione
    if label == "Obbligo" and tipo_obbligo:
        clausole.append("n.tipo_obbligo IN $tipo_obbligo")
        params["tipo_obbligo"] = tipo_obbligo
    if label == "Principio" and tipo_principio:
        clausole.append("n.tipo_principio IN $tipo_principio")
        params["tipo_principio"] = tipo_principio
    if data_riferimento:
        clausole.append(
            "(n.data_inizio_vigore IS NULL OR n.data_inizio_vigore <= $data_riferimento) "
            "AND (n.data_fine_vigore IS NULL OR n.data_fine_vigore >= $data_riferimento)"
        )
        params["data_riferimento"] = data_riferimento

    match_extra = ""
    if label == "Obbligo" and categoria_soggetto:
        match_extra = "MATCH (n)-[:HA_SOGGETTO]->(cs:CategoriaSoggetto) WHERE cs.nome IN $categoria_soggetto WITH DISTINCT n"
        params["categoria_soggetto"] = categoria_soggetto

    query = f"MATCH (n:{label}) {match_extra} WHERE {' AND '.join(clausole)} RETURN n.id AS id"
    return {r["id"] for r in session.run(query, **params).data()}


def _wrrf(lessicali: list[int], semantici: list[int]) -> dict[int, float]:
    """Weighted Reciprocal Rank Fusion (ADR-0006): 0.55/rank_lucene + 0.45/rank_vector."""
    punteggi: dict[int, float] = {}
    for rank, node_id in enumerate(lessicali, start=1):
        punteggi[node_id] = punteggi.get(node_id, 0.0) + PESO_LESSICALE / rank
    for rank, node_id in enumerate(semantici, start=1):
        punteggi[node_id] = punteggi.get(node_id, 0.0) + PESO_SEMANTICO / rank
    return punteggi


@app.get("/api/ricerca")
def ricerca_ibrida(
    q: str,
    n: int = 10,
    fonte_id: list[int] = Query(default=[]),
    tipo_obbligo: list[str] = Query(default=[]),
    tipo_principio: list[str] = Query(default=[]),
    categoria_soggetto: list[str] = Query(default=[]),
    stato_validazione: list[str] = Query(default=[]),
    data_riferimento: str | None = None,
):
    """Ricerca ibrida a fusione WRRF (lessicale Lucene + semantico vettoriale, ADR-0006):
    rilevanza per rango, non solo presenza/assenza, su indici nativi Neo4j.
    """
    if not q.strip():
        return {"status": "ok", "risultati": []}

    with _session() as session:
        candidati_obbligo = _candidati_pre_filtrati(
            session, "Obbligo", fonte_id, stato_validazione, tipo_obbligo, [], categoria_soggetto,
            data_riferimento,
        )
        candidati_principio = _candidati_pre_filtrati(
            session, "Principio", fonte_id, stato_validazione, [], tipo_principio, [],
            data_riferimento,
        )

        risultati_finali = []
        for label, index_testo, index_vettore, candidati, tipo_nodo in (
            ("Obbligo", "idxTestoObbligo", "idxEmbeddingObbligo", candidati_obbligo, "obbligo"),
            ("Principio", "idxTestoPrincipio", "idxEmbeddingPrincipio", candidati_principio, "principio"),
        ):
            if not candidati:
                continue
            id_lessicali_ordinati = [
                r["id"] for r in session.run(
                    f"CALL db.index.fulltext.queryNodes('{index_testo}', $q) YIELD node, score "
                    "RETURN node.id AS id ORDER BY score DESC",
                    q=_query_lucene(q),
                ).data()
                if r["id"] in candidati
            ]

            vettore_query = _embedding_model().encode(q, normalize_embeddings=True).tolist()
            k = max(50, n * 5)
            id_semantici_ordinati = [
                r["id"] for r in session.run(
                    f"CALL db.index.vector.queryNodes('{index_vettore}', $k, $vec) YIELD node, score "
                    "RETURN node.id AS id ORDER BY score DESC",
                    k=k, vec=vettore_query,
                ).data()
                if r["id"] in candidati
            ]

            punteggi = _wrrf(id_lessicali_ordinati, id_semantici_ordinati)
            for node_id, score in punteggi.items():
                risultati_finali.append((score, tipo_nodo, node_id))

        risultati_finali.sort(key=lambda t: t[0], reverse=True)
        risultati_finali = risultati_finali[:n]

        righe = []
        for score, tipo_nodo, node_id in risultati_finali:
            if tipo_nodo == "obbligo":
                rec = session.run(
                    _OBBLIGHI_QUERY.split("ORDER BY")[0].replace("MATCH (o:Obbligo)", "MATCH (o:Obbligo {id: $id})"),
                    id=node_id,
                ).data()
                riga = _riga_obbligo(rec[0])
            else:
                rec = session.run(
                    _PRINCIPI_QUERY.split("ORDER BY")[0].replace("MATCH (p:Principio)", "MATCH (p:Principio {id: $id})"),
                    id=node_id,
                ).data()
                riga = _riga_principio(rec[0])
            riga["score"] = round(score, 4)
            righe.append(riga)

    return {"status": "ok", "risultati": righe}


# ---------------------------------------------------------------- revisione

@app.get("/api/revisione")
def coda_revisione():
    with _session() as session:
        rows = session.run(
            _OBBLIGHI_QUERY.split("ORDER BY")[0].replace(
                "MATCH (o:Obbligo)", "MATCH (o:Obbligo {stato_validazione: 'bozza'})"
            ) + " ORDER BY o.id",
        ).data()
        bozze = [_riga_obbligo(r) for r in rows]
    return {"status": "ok", "bozze": bozze}


class CorrezioneBozza(BaseModel):
    riferimento: str
    testo: str
    tipo_obbligo: str
    stato_obbligo: str
    data_inizio_vigore: str | None = None
    data_fine_vigore: str | None = None
    severita: str | None = None
    sanzioni: str | None = None
    condizione_applicabilita: str | None = None
    soggetti_obbligati: list[str] = []
    destinatari: list[str] = []
    validato_da: str = "sistema"


@app.post("/api/revisione/{obbligo_id}/valida")
def valida_bozza(obbligo_id: int, body: CorrezioneBozza):
    if body.tipo_obbligo not in TIPI_OBBLIGO or body.stato_obbligo not in STATI_NORMA:
        raise HTTPException(400, "Valore di lookup sconosciuto (tipo_obbligo/stato_obbligo)")

    with _session() as session:
        esiste = session.run(
            "MATCH (o:Obbligo {id: $id, stato_validazione: 'bozza'}) RETURN o.id AS id", id=obbligo_id
        ).single()
        if esiste is None:
            raise HTTPException(404, "Bozza non trovata (già validata/rifiutata?)")

        categorie_esistenti = {
            r["nome"] for r in session.run("MATCH (c:CategoriaSoggetto) RETURN c.nome AS nome")
        }
        for nome in [*body.soggetti_obbligati, *body.destinatari]:
            if nome not in categorie_esistenti:
                raise HTTPException(400, f"Categoria di soggetto sconosciuta: {nome}")

        session.run(
            """
            MATCH (o:Obbligo {id: $id})
            SET o.riferimento = $riferimento, o.testo = $testo, o.tipo_obbligo = $tipo_obbligo,
                o.stato_obbligo = $stato_obbligo, o.data_inizio_vigore = $data_inizio_vigore,
                o.data_fine_vigore = $data_fine_vigore, o.severita = $severita, o.sanzioni = $sanzioni,
                o.condizione_applicabilita = $condizione_applicabilita, o.stato_validazione = 'validato',
                o.validato_da = $validato_da, o.data_validazione = $data_validazione
            """,
            id=obbligo_id, riferimento=body.riferimento, testo=body.testo, tipo_obbligo=body.tipo_obbligo,
            stato_obbligo=body.stato_obbligo, data_inizio_vigore=body.data_inizio_vigore,
            data_fine_vigore=body.data_fine_vigore, severita=body.severita, sanzioni=body.sanzioni,
            condizione_applicabilita=body.condizione_applicabilita, validato_da=body.validato_da,
            data_validazione=date.today().isoformat(),
        )

        session.run("MATCH (:Obbligo {id: $id})-[r:HA_SOGGETTO]->() DELETE r", id=obbligo_id)
        for nome in body.soggetti_obbligati:
            session.run(
                "MATCH (o:Obbligo {id: $id}), (c:CategoriaSoggetto {nome: $nome}) "
                "CREATE (o)-[:HA_SOGGETTO {ruolo: 'obbligato'}]->(c)",
                id=obbligo_id, nome=nome,
            )
        for nome in body.destinatari:
            session.run(
                "MATCH (o:Obbligo {id: $id}), (c:CategoriaSoggetto {nome: $nome}) "
                "CREATE (o)-[:HA_SOGGETTO {ruolo: 'destinatario'}]->(c)",
                id=obbligo_id, nome=nome,
            )

    return {"status": "ok", "obbligo_id": obbligo_id}


@app.post("/api/revisione/{obbligo_id}/rifiuta")
def rifiuta_bozza(obbligo_id: int):
    # Decisione ticket 03: le bozze rifiutate vengono eliminate, nessuna traccia storica.
    with _session() as session:
        rec = session.run(
            "MATCH (o:Obbligo {id: $id, stato_validazione: 'bozza'}) DETACH DELETE o RETURN count(o) AS c",
            id=obbligo_id,
        ).single()
        if rec["c"] == 0:
            raise HTTPException(404, "Bozza non trovata (già validata/rifiutata?)")
    return {"status": "ok"}


# -------------------------------------------------------------- monitoraggio

@app.get("/api/monitoraggio")
def monitoraggio_stato():
    with mon_conn() as mconn:
        righe = mconn.execute(
            "SELECT * FROM modifiche_rilevate WHERE esaminata = 0 ORDER BY fonte_id, data_rilevamento"
        ).fetchall()

    if not righe:
        return {"status": "ok", "fonti_con_modifiche": []}

    with _session() as session:
        fonti = {
            r["id"]: r["nome"] for r in session.run("MATCH (f:Fonte) RETURN f.id AS id, f.nome AS nome").data()
        }
        per_fonte: dict[int, dict] = {}
        for r in righe:
            impattati = [
                rec["id"] for rec in session.run(
                    "MATCH (o:Obbligo {fonte_id: $fonte_id, riferimento: $riferimento}) RETURN o.id AS id",
                    fonte_id=r["fonte_id"], riferimento=r["riferimento"],
                ).data()
            ]
            entry = per_fonte.setdefault(r["fonte_id"], {
                "fonte_id": r["fonte_id"], "nome": fonti.get(r["fonte_id"], "?"), "modifiche": [],
            })
            entry["modifiche"].append({
                "modifica_id": r["id"],
                "riferimento": r["riferimento"],
                "data_rilevamento": r["data_rilevamento"],
                "testo_precedente": r["testo_precedente"],
                "testo_nuovo": r["testo_nuovo"],
                "obblighi_impattati": impattati,
            })
    return {"status": "ok", "fonti_con_modifiche": list(per_fonte.values())}


@app.post("/api/monitoraggio/{modifica_id}/esamina")
def segna_esaminata(modifica_id: int):
    with mon_conn() as mconn:
        cur = mconn.execute("UPDATE modifiche_rilevate SET esaminata = 1 WHERE id = ?", (modifica_id,))
        if cur.rowcount == 0:
            raise HTTPException(404, "Modifica non trovata")
        mconn.commit()
    return {"status": "ok"}


# ------------------------------------------------------------------ frontend

@app.get("/", response_class=HTMLResponse)
def index():
    return HTMLResponse(INDEX_HTML)


@app.exception_handler(HTTPException)
def _http_error(request, exc: HTTPException):
    return JSONResponse({"error": exc.detail}, status_code=exc.status_code)


INDEX_HTML = r"""<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Censimento Obblighi QTSP</title>
<style>
:root{
  --bg:#f7f7f5; --panel:#fff; --ink:#1a1a18; --muted:#6b6b66; --line:#e3e3df;
  --accent:#3a5bb8; --accent-soft:#eaefff; --warn:#8a5a00; --warn-soft:#fff4e0;
  --ok:#1a7a4a; --ok-soft:#e6f5ec; --bad:#a3312a; --bad-soft:#fbe9e8;
  --mono:ui-monospace,"Cascadia Mono",Consolas,monospace;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 -apple-system,"Segoe UI",Roboto,sans-serif}
header{background:var(--panel);border-bottom:1px solid var(--line);padding:12px 20px;display:flex;align-items:baseline;gap:16px;flex-wrap:wrap;position:sticky;top:0;z-index:5}
header h1{font-size:15px;margin:0;font-weight:650}
header .sub{color:var(--muted);font-size:12px;font-family:var(--mono)}
nav{display:flex;gap:4px;margin-left:auto}
nav button{background:none;border:1px solid transparent;border-radius:6px;padding:6px 12px;font:inherit;color:var(--muted);cursor:pointer;position:relative}
nav button:hover{background:var(--bg)}
nav button.on{background:var(--accent-soft);color:var(--accent);border-color:#cdd8f5;font-weight:600}
nav button .badge{background:var(--bad);color:#fff;border-radius:20px;font-size:10px;padding:1px 6px;margin-left:6px}
main{padding:20px;max-width:1100px;margin:0 auto}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:16px;margin-bottom:16px}
.panel h2{font-size:13px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);margin:0 0 12px}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:16px}
.tile{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px}
.tile .v{font-size:24px;font-weight:650;font-variant-numeric:tabular-nums}
.tile .k{color:var(--muted);font-size:12px;margin-top:2px}
.controls{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:12px}
input[type=text],input[type=date],select{font:inherit;padding:6px 9px;border:1px solid var(--line);border-radius:6px;background:var(--panel);color:var(--ink)}
input[type=text]{min-width:240px;flex:1}
textarea{font:inherit;padding:6px 9px;border:1px solid var(--line);border-radius:6px;width:100%;resize:vertical}
input:focus,select:focus,textarea:focus{outline:2px solid var(--accent-soft);border-color:var(--accent)}
button.act{font:inherit;padding:6px 12px;border:1px solid var(--line);border-radius:6px;background:var(--panel);cursor:pointer}
button.act:hover{background:var(--bg)}
button.primary{background:var(--accent);color:#fff;border-color:var(--accent)}
button.primary:hover{filter:brightness(1.08)}
button.danger{background:var(--bad-soft);color:var(--bad);border-color:#f0c9c6}
button.danger:hover{filter:brightness(0.97)}
.facets{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:12px}
.facet{display:flex;flex-direction:column;gap:4px}
.facet .lbl{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.03em}
.chip{display:inline-flex;align-items:center;gap:4px;font-size:12px;padding:3px 9px;border-radius:20px;border:1px solid var(--line);cursor:pointer;background:var(--panel)}
.chip.on{background:var(--accent-soft);color:var(--accent);border-color:#cdd8f5}
.chiprow{display:flex;gap:6px;flex-wrap:wrap;max-width:260px}
.card{border:1px solid var(--line);border-radius:8px;padding:12px;margin-bottom:10px}
.card:hover{cursor:pointer;background:var(--accent-soft)}
.card .hd{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:6px}
.tag{display:inline-block;font-size:11px;padding:1px 7px;border-radius:20px;background:var(--bg);color:var(--muted);border:1px solid var(--line);white-space:nowrap}
.tag.ok{background:var(--ok-soft);color:var(--ok);border-color:#c3e8d3}
.tag.warn{background:var(--warn-soft);color:var(--warn);border-color:#f0dcb4}
.tag.bad{background:var(--bad-soft);color:var(--bad);border-color:#f0c9c6}
.muted{color:var(--muted)}
.ref{font-family:var(--mono);font-weight:650;color:var(--accent)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.field{margin-bottom:8px}
.field label{display:block;font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.03em;margin-bottom:3px}
.err{background:var(--bad-soft);border:1px solid #f0c9c6;color:var(--bad);border-radius:8px;padding:10px 12px;margin-bottom:12px}
.spin{color:var(--muted);padding:12px 0}
.diff .old{background:#fbe9e8;text-decoration:line-through;color:#8a4a46;padding:6px 8px;border-radius:6px;margin-bottom:4px}
.diff .new{background:#e6f5ec;color:#1a5a3a;padding:6px 8px;border-radius:6px}
a{color:var(--accent)}
</style></head><body>
<header>
  <h1>Censimento Obblighi QTSP</h1>
  <span class="sub">dati di esempio, non vincolante</span>
  <nav id="nav">
    <button data-tab="consultazione" class="on">Consultazione</button>
    <button data-tab="revisione">Coda di revisione</button>
    <button data-tab="monitoraggio">Monitoraggio</button>
  </nav>
</header>
<main>
  <div id="err"></div>
  <div id="view"></div>
</main>
<script>
const $ = s => document.querySelector(s);
const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const state = {
  tab: "consultazione", stats:null, lookup:null,
  filtri: { q:"", fonte_id:new Set(), tipo_obbligo:new Set(), stato_obbligo:new Set(), categoria_soggetto:new Set(),
            tipo_principio:new Set(), oggetto_giuridico:new Set(), solo_validati:true },
  risultati:null, dettaglio:null,
  bozze:null, monitoraggio:null,
  validazioneInCorso:false,
};

function showErr(m){ $("#err").innerHTML = m ? `<div class="err">${esc(m)}</div>` : ""; }
async function api(url, opts){
  const r = await fetch(url, opts);
  const j = await r.json().catch(() => ({error:`Risposta non valida (HTTP ${r.status})`}));
  if(!r.ok) throw new Error(j.error || `HTTP ${r.status}`);
  return j;
}
function loading(msg){ $("#view").innerHTML = `<div class="panel spin">${esc(msg)}</div>`; }

document.querySelectorAll("nav button").forEach(b => b.onclick = () => {
  state.tab = b.dataset.tab; state.dettaglio = null;
  document.querySelectorAll("nav button").forEach(x => x.classList.toggle("on", x===b));
  render();
});

async function refreshBadges(){
  try{ state.stats = await api("/api/stats"); }catch(e){ return; }
  const badge = state.stats.modifiche_da_esaminare;
  const b = document.querySelector('nav button[data-tab="monitoraggio"]');
  b.innerHTML = "Monitoraggio" + (badge ? `<span class="badge">${badge}</span>` : "");
}

async function boot(){
  try{ state.lookup = await api("/api/lookup"); }catch(e){ showErr(e.message); }
  await refreshBadges();
  render();
}

function render(){
  showErr("");
  if(state.tab === "consultazione") return state.dettaglio ? renderDettaglio() : renderConsultazione();
  if(state.tab === "revisione") return renderRevisione();
  return renderMonitoraggio();
}

/* ------------------------------------------------------------- consultazione */
function chipRow(id, values, selectedSet){
  return `<div class="chiprow" id="${id}">` + values.map(v =>
    `<span class="chip ${selectedSet.has(v)?"on":""}" data-v="${esc(v)}">${esc(v)}</span>`).join("") + `</div>`;
}
function bindChips(id, set){
  document.querySelectorAll(`#${id} .chip`).forEach(c => c.onclick = () => {
    const v = c.dataset.v;
    if(set.has(v)) set.delete(v); else set.add(v);
    c.classList.toggle("on");
    searchNow();
  });
}

async function renderConsultazione(){
  const f = state.filtri, lk = state.lookup;
  const s = state.stats;
  $("#view").innerHTML = `
  <div class="tiles">
    <div class="tile"><div class="v">${s?s.fonti:"—"}</div><div class="k">fonti</div></div>
    <div class="tile"><div class="v">${s?s.obblighi_validati:"—"}</div><div class="k">obblighi validati</div></div>
    <div class="tile"><div class="v">${s?s.principi:"—"}</div><div class="k">principi</div></div>
    <div class="tile"><div class="v">${s?s.obblighi_bozza:"—"}</div><div class="k">bozze in coda</div></div>
    <div class="tile"><div class="v">${s?s.relazioni:"—"}</div><div class="k">relazioni tipizzate</div></div>
  </div>
  <div class="panel">
    <h2>Ricerca ibrida <span class="muted" style="font-weight:normal;font-size:12px">(lessicale + semantica, Neo4j)</span></h2>
    <div class="controls">
      <input type="text" id="qsem" placeholder="descrivi cosa cerchi, anche senza parole esatte del testo…">
      <label style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--muted)">alla data
        <input type="date" id="qsem-data">
      </label>
      <button id="btnsem">Cerca</button>
    </div>
    <div id="ressem"></div>
  </div>
  <div class="panel">
    <div class="controls">
      <input type="text" id="q" placeholder="cerca nel testo o nel riferimento…" value="${esc(f.q)}">
      <label style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--muted)">
        <input type="checkbox" id="solovalidati" ${f.solo_validati?"checked":""}> solo validati
      </label>
    </div>
  </div>
  <div class="panel">
    <div class="facets">
      <div class="facet"><div class="lbl">Fonte</div>${chipRow("f-fonte", lk.fonti.map(x=>x.nome), new Set([...f.fonte_id].map(id => lk.fonti.find(x=>x.fonte_id===id)?.nome)))}</div>
      <div class="facet"><div class="lbl">Tipo obbligo</div>${chipRow("f-tipo", lk.tipi_obbligo, f.tipo_obbligo)}</div>
      <div class="facet"><div class="lbl">Stato norma</div>${chipRow("f-stato", lk.stati_obbligo, f.stato_obbligo)}</div>
      <div class="facet"><div class="lbl">Categoria soggetto</div>${chipRow("f-cat", lk.categorie_soggetto, f.categoria_soggetto)}</div>
      <div class="facet"><div class="lbl">Tipo principio</div>${chipRow("f-tprinc", lk.tipi_principio, f.tipo_principio)}</div>
      <div class="facet"><div class="lbl">Oggetto giuridico</div>${chipRow("f-ogg", lk.oggetti_giuridici, f.oggetto_giuridico)}</div>
    </div>
  </div>
  <div class="panel"><h2>Risultati</h2><div id="reslist" class="spin">Caricamento…</div></div>`;

  $("#q").oninput = () => { clearTimeout($("#q")._t); $("#q")._t = setTimeout(() => { f.q = $("#q").value; searchNow(); }, 250); };
  $("#solovalidati").onchange = () => { f.solo_validati = $("#solovalidati").checked; searchNow(); };
  document.querySelectorAll("#f-fonte .chip").forEach(c => c.onclick = () => {
    const nome = c.dataset.v; const fonte = lk.fonti.find(x=>x.nome===nome);
    if(f.fonte_id.has(fonte.fonte_id)) f.fonte_id.delete(fonte.fonte_id); else f.fonte_id.add(fonte.fonte_id);
    c.classList.toggle("on"); searchNow();
  });
  bindChips("f-tipo", f.tipo_obbligo);
  bindChips("f-stato", f.stato_obbligo);
  bindChips("f-cat", f.categoria_soggetto);
  bindChips("f-tprinc", f.tipo_principio);
  bindChips("f-ogg", f.oggetto_giuridico);

  $("#btnsem").onclick = ricercaIbrida;
  $("#qsem").addEventListener("keydown", e => { if(e.key === "Enter") ricercaIbrida(); });

  await searchNow(true);
}

async function ricercaIbrida(){
  const q = $("#qsem").value.trim();
  const data_riferimento = $("#qsem-data").value;
  const box = document.getElementById("ressem");
  if(!q){ box.innerHTML = ""; return; }
  box.innerHTML = `<div class="spin">Ricerca in corso…</div>`;
  let data;
  const params = {q, n: 10};
  if(data_riferimento) params.data_riferimento = data_riferimento;
  try{ data = await api("/api/ricerca?" + new URLSearchParams(params).toString()); }
  catch(e){ box.innerHTML = `<div class="muted">Ricerca non disponibile: ${esc(e.message)}</div>`; return; }
  if(!data.risultati || !data.risultati.length){ box.innerHTML = `<div class="muted">Nessun risultato.</div>`; return; }
  box.innerHTML = data.risultati.map(o => (o.tipo_nodo === "principio" ? cardPrincipio(o) : cardObbligo(o))
    .replace('<div class="hd">', `<div class="hd"><span class="tag" title="punteggio di rilevanza ibrida (WRRF)">score ${o.score.toFixed(3)}</span>`)
  ).join("");
}

async function searchNow(first){
  const f = state.filtri;
  const qsObblighi = new URLSearchParams();
  const qsPrincipi = new URLSearchParams();
  if(f.q){ qsObblighi.set("q", f.q); qsPrincipi.set("q", f.q); }
  qsObblighi.set("solo_validati", f.solo_validati);
  qsPrincipi.set("solo_validati", f.solo_validati);
  f.fonte_id.forEach(v => { qsObblighi.append("fonte_id", v); qsPrincipi.append("fonte_id", v); });
  f.tipo_obbligo.forEach(v => qsObblighi.append("tipo_obbligo", v));
  f.stato_obbligo.forEach(v => qsObblighi.append("stato_obbligo", v));
  f.categoria_soggetto.forEach(v => qsObblighi.append("categoria_soggetto", v));
  f.tipo_principio.forEach(v => qsPrincipi.append("tipo_principio", v));
  f.oggetto_giuridico.forEach(v => qsPrincipi.append("oggetto_giuridico", v));
  const box = document.getElementById("reslist");
  if(!first && box) box.innerHTML = `<div class="spin">Ricerca…</div>`;
  // Faceted + full-text Lucene (ADR-0006): se sono attivi filtri specifici di un solo tipo di
  // nodo, l'altro tipo di ricerca resta comunque eseguito (i suoi filtri semplicemente non si
  // applicano), così un principio può emergere anche filtrando per categoria soggetto e viceversa.
  try{
    const [obblighi, principi] = await Promise.all([
      api("/api/obblighi?" + qsObblighi.toString()),
      api("/api/principi?" + qsPrincipi.toString()),
    ]);
    state.risultati = { totale: obblighi.totale + principi.totale, risultati: [...obblighi.risultati, ...principi.risultati] };
  }catch(e){ showErr(e.message); return; }
  paintResults();
}

function paintResults(){
  const box = document.getElementById("reslist");
  if(!box) return;
  const r = state.risultati;
  if(!r.totale){ box.innerHTML = `<div class="muted">Nessun risultato con questi filtri.</div>`; return; }
  box.innerHTML = `<div class="muted" style="margin-bottom:8px">${r.totale} risultati</div>` + r.risultati.map(o =>
    o.tipo_nodo === "principio" ? cardPrincipio(o) : cardObbligo(o)).join("");
}

function cardObbligo(o){
  return `
    <div class="card" onclick="openNodo('obbligo', ${o.obbligo_id})">
      <div class="hd">
        <span class="tag">obbligo</span>
        <span class="ref">${esc(o.fonte)} — ${esc(o.riferimento)}</span>
        <span class="tag">${esc(o.tipo_obbligo)}</span>
        <span class="tag ${o.stato_obbligo.includes('abrogat')?'bad':o.stato_obbligo.includes('transizione')?'warn':'ok'}">${esc(o.stato_obbligo)}</span>
        ${o.stato_validazione!=='validato' ? `<span class="tag warn">${esc(o.stato_validazione)}</span>` : ""}
        ${o.severita ? `<span class="tag">severità: ${esc(o.severita)}</span>` : ""}
      </div>
      <div>${esc(o.testo)}</div>
      <div class="muted" style="margin-top:6px;font-size:12px">obbligato: ${o.soggetti_obbligati.map(esc).join(", ")||"—"} · destinatario: ${o.destinatari.map(esc).join(", ")||"—"}</div>
    </div>`;
}

function cardPrincipio(o){
  return `
    <div class="card" onclick="openNodo('principio', ${o.principio_id})">
      <div class="hd">
        <span class="tag ok">principio</span>
        <span class="ref">${esc(o.fonte)} — ${esc(o.riferimento)}</span>
        <span class="tag">${esc(o.tipo_principio)}</span>
        <span class="tag ${o.stato_obbligo.includes('abrogat')?'bad':o.stato_obbligo.includes('transizione')?'warn':'ok'}">${esc(o.stato_obbligo)}</span>
        ${o.stato_validazione!=='validato' ? `<span class="tag warn">${esc(o.stato_validazione)}</span>` : ""}
      </div>
      <div>${esc(o.testo)}</div>
      <div class="muted" style="margin-top:6px;font-size:12px">oggetto giuridico: ${o.oggetti_giuridici.map(esc).join(", ")||"—"}</div>
    </div>`;
}

async function openNodo(tipoNodo, id){
  loading("Caricamento…");
  try{ state.dettaglio = await api(tipoNodo === "principio" ? `/api/principi/${id}` : `/api/obblighi/${id}`); }
  catch(e){ showErr(e.message); state.dettaglio = null; return render(); }
  renderDettaglio();
}

function renderVicini(vicini){
  return `<div class="panel"><h2>Relazioni tipizzate (grafo, multi-hop)</h2>
    ${vicini.length ? vicini.map(v => `
      <div class="card" onclick="openNodo('${v.tipo_nodo}', ${v.tipo_nodo==='principio'?v.principio_id:v.obbligo_id})">
        <div class="hd"><span class="tag">${esc(v.tipo_relazione)}</span>
          <span class="tag" title="numero di salti dal nodo di partenza">${v.hop} hop</span>
          <span class="tag ${v.evidence_type==='human-curated'?'ok':v.evidence_type==='textual'?'':'warn'}">${esc(v.evidence_type)}${v.confidence!=null?` ${Math.round(v.confidence*100)}%`:''}</span>
          <span class="tag ${v.tipo_nodo==='principio'?'ok':''}">${v.tipo_nodo}</span>
          <span class="ref">${esc(v.fonte)} — ${esc(v.riferimento)}</span>
          ${v.stato_validazione!=='validato' ? `<span class="tag warn">${esc(v.stato_validazione)}</span>` : ""}</div>
        <div class="muted">${esc(v.testo)}</div>
      </div>`).join("") : `<div class="muted">Nessuna relazione tipizzata verso altri nodi.</div>`}
  </div>`;
}

function renderDettaglio(){
  if(state.dettaglio.principio) return renderDettaglioPrincipio();
  const { obbligo: o, vicini } = state.dettaglio;
  $("#view").innerHTML = `
  <button class="act" onclick="state.dettaglio=null;render()">‹ indietro ai risultati</button>
  <div class="panel" style="margin-top:14px">
    <div class="hd">
      <span class="ref" style="font-size:16px">${esc(o.fonte)} — ${esc(o.riferimento)}</span>
      <span class="tag">${esc(o.tipo_obbligo)}</span>
      <span class="tag ${o.stato_obbligo.includes('abrogat')?'bad':o.stato_obbligo.includes('transizione')?'warn':'ok'}">${esc(o.stato_obbligo)}</span>
      <span class="tag ${o.stato_validazione==='validato'?'ok':'warn'}">${esc(o.stato_validazione)}</span>
    </div>
    <p style="font-size:15px">${esc(o.testo)}</p>
    <table style="width:100%;font-size:13px;border-collapse:collapse">
      <tr><td class="muted" style="width:180px;padding:4px 0">Soggetti obbligati</td><td>${o.soggetti_obbligati.map(esc).join(", ")||"—"}</td></tr>
      <tr><td class="muted" style="padding:4px 0">Destinatari</td><td>${o.destinatari.map(esc).join(", ")||"—"}</td></tr>
      <tr><td class="muted" style="padding:4px 0">Severità</td><td>${esc(o.severita||"—")}</td></tr>
      <tr><td class="muted" style="padding:4px 0">Sanzioni</td><td>${esc(o.sanzioni||"—")}</td></tr>
      <tr><td class="muted" style="padding:4px 0">Condizione di applicabilità</td><td>${esc(o.condizione_applicabilita||"—")}</td></tr>
      <tr><td class="muted" style="padding:4px 0">Vigenza</td><td>${o.data_inizio_vigore||o.data_fine_vigore ? `dal ${esc(o.data_inizio_vigore||"—")} al ${esc(o.data_fine_vigore||"in corso")}` : "—"}</td></tr>
      <tr><td class="muted" style="padding:4px 0">Validato da</td><td>${esc(o.validato_da||"—")} ${o.data_validazione?`(${esc(o.data_validazione)})`:""}</td></tr>
    </table>
    ${renderTestoIntegrale(o.testo_integrale)}
  </div>
  ${renderVicini(vicini)}`;
}

function renderTestoIntegrale(testo){
  if(!testo) return `<p class="muted" style="font-size:13px;margin-top:10px">Testo normativo integrale non disponibile.</p>`;
  return `
    <details style="margin-top:10px">
      <summary style="cursor:pointer;font-size:13px;color:#555">Testo normativo integrale</summary>
      <p style="font-size:13px;white-space:pre-wrap;margin-top:8px">${esc(testo)}</p>
    </details>`;
}

function renderDettaglioPrincipio(){
  const { principio: o, vicini } = state.dettaglio;
  $("#view").innerHTML = `
  <button class="act" onclick="state.dettaglio=null;render()">‹ indietro ai risultati</button>
  <div class="panel" style="margin-top:14px">
    <div class="hd">
      <span class="tag ok">principio</span>
      <span class="ref" style="font-size:16px">${esc(o.fonte)} — ${esc(o.riferimento)}</span>
      <span class="tag">${esc(o.tipo_principio)}</span>
      <span class="tag ${o.stato_obbligo.includes('abrogat')?'bad':o.stato_obbligo.includes('transizione')?'warn':'ok'}">${esc(o.stato_obbligo)}</span>
      <span class="tag ${o.stato_validazione==='validato'?'ok':'warn'}">${esc(o.stato_validazione)}</span>
    </div>
    <p style="font-size:15px">${esc(o.testo)}</p>
    <table style="width:100%;font-size:13px;border-collapse:collapse">
      <tr><td class="muted" style="width:180px;padding:4px 0">Oggetto giuridico</td><td>${o.oggetti_giuridici.map(esc).join(", ")||"—"}</td></tr>
      <tr><td class="muted" style="padding:4px 0">Condizione di applicabilità</td><td>${esc(o.condizione_applicabilita||"—")}</td></tr>
      <tr><td class="muted" style="padding:4px 0">Vigenza</td><td>${o.data_inizio_vigore||o.data_fine_vigore ? `dal ${esc(o.data_inizio_vigore||"—")} al ${esc(o.data_fine_vigore||"in corso")}` : "—"}</td></tr>
      <tr><td class="muted" style="padding:4px 0">Validato da</td><td>${esc(o.validato_da||"—")} ${o.data_validazione?`(${esc(o.data_validazione)})`:""}</td></tr>
    </table>
    ${renderTestoIntegrale(o.testo_integrale)}
  </div>
  ${renderVicini(vicini)}`;
}

/* ---------------------------------------------------------------- revisione */
async function renderRevisione(){
  loading("Caricamento coda di revisione…");
  try{ state.bozze = await api("/api/revisione"); }
  catch(e){ showErr(e.message); return; }
  paintRevisione();
}

function paintRevisione(){
  const lk = state.lookup;
  const b = state.bozze.bozze;
  const opt = (values, cur) => values.map(v => `<option value="${esc(v)}" ${v===cur?"selected":""}>${esc(v)}</option>`).join("");
  const catCheckboxes = (name, obbligoId, selected) => lk.categorie_soggetto.map(c => `
    <label style="display:inline-flex;gap:4px;align-items:center;margin-right:10px;font-size:12px">
      <input type="checkbox" data-role="${name}" data-cat="${esc(c)}" ${selected.includes(c)?"checked":""}> ${esc(c)}
    </label>`).join("");

  $("#view").innerHTML = `<div class="panel">
    <div class="hd" style="justify-content:space-between">
      <h2 style="margin:0">Coda di revisione (${b.length} bozze)</h2>
      ${b.length ? `<button class="act primary" onclick="validaTutte()" ${state.validazioneInCorso?"disabled":""}>Valida tutte</button>` : ""}
    </div>
    ${b.length ? "" : '<div class="muted">Nessuna bozza in attesa di revisione.</div>'}
    ${b.map(o => `
    <div class="card" id="bozza-${o.obbligo_id}" style="cursor:default">
      <div class="hd"><span class="ref">${esc(o.fonte)}</span><span class="tag warn">bozza</span></div>
      <div class="grid2">
        <div class="field"><label>Riferimento</label><input type="text" id="rif-${o.obbligo_id}" value="${esc(o.riferimento)}"></div>
        <div class="field"><label>Tipo obbligo</label><select id="tipo-${o.obbligo_id}">${opt(lk.tipi_obbligo, o.tipo_obbligo)}</select></div>
        <div class="field"><label>Stato obbligo</label><select id="stato-${o.obbligo_id}">${opt(lk.stati_obbligo, o.stato_obbligo)}</select></div>
        <div class="field"><label>Severità</label><input type="text" id="sev-${o.obbligo_id}" value="${esc(o.severita||"")}"></div>
      </div>
      <div class="field"><label>Testo</label><textarea id="testo-${o.obbligo_id}" rows="2">${esc(o.testo)}</textarea></div>
      <div class="grid2">
        <div class="field"><label>Sanzioni</label><input type="text" id="san-${o.obbligo_id}" value="${esc(o.sanzioni||"")}"></div>
        <div class="field"><label>Condizione di applicabilità</label><input type="text" id="cond-${o.obbligo_id}" value="${esc(o.condizione_applicabilita||"")}"></div>
        <div class="field"><label>Vigore dal</label><input type="date" id="vig-da-${o.obbligo_id}" value="${esc(o.data_inizio_vigore||"")}"></div>
        <div class="field"><label>Vigore al</label><input type="date" id="vig-a-${o.obbligo_id}" value="${esc(o.data_fine_vigore||"")}"></div>
      </div>
      <div class="field"><label>Soggetti obbligati</label>${catCheckboxes("obbligato", o.obbligo_id, o.soggetti_obbligati)}</div>
      <div class="field"><label>Destinatari</label>${catCheckboxes("destinatario", o.obbligo_id, o.destinatari)}</div>
      <div style="display:flex;gap:8px;margin-top:8px">
        <button class="act primary" onclick="valida(${o.obbligo_id})">Valida</button>
        <button class="act danger" onclick="rifiuta(${o.obbligo_id})">Rifiuta (elimina)</button>
      </div>
    </div>`).join("")}
  </div>`;
}

function checkedCats(role, obbligoId){
  return [...document.querySelectorAll(`#bozza-${obbligoId} input[data-role="${role}"]:checked`)].map(x => x.dataset.cat);
}

async function valida(id, opts){
  const silent = opts && opts.silent;
  const body = {
    riferimento: document.getElementById(`rif-${id}`).value,
    testo: document.getElementById(`testo-${id}`).value,
    tipo_obbligo: document.getElementById(`tipo-${id}`).value,
    stato_obbligo: document.getElementById(`stato-${id}`).value,
    severita: document.getElementById(`sev-${id}`).value || null,
    sanzioni: document.getElementById(`san-${id}`).value || null,
    condizione_applicabilita: document.getElementById(`cond-${id}`).value || null,
    data_inizio_vigore: document.getElementById(`vig-da-${id}`).value || null,
    data_fine_vigore: document.getElementById(`vig-a-${id}`).value || null,
    soggetti_obbligati: checkedCats("obbligato", id),
    destinatari: checkedCats("destinatario", id),
    validato_da: "sistema",
  };
  try{
    await api(`/api/revisione/${id}/valida`, {method:"POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify(body)});
    if(!silent){ await refreshBadges(); await renderRevisione(); }
  }catch(e){
    if(silent) throw e;
    showErr(e.message);
  }
}

async function validaTutte(){
  if(state.validazioneInCorso) return;
  state.validazioneInCorso = true;
  const ids = state.bozze.bozze.map(o => o.obbligo_id);
  const errori = [];
  for(const id of ids){
    if(!document.getElementById(`bozza-${id}`)) continue; // già rimossa dal DOM (validata/rifiutata altrove)
    try{ await valida(id, {silent:true}); }
    catch(e){ errori.push(`#${id}: ${e.message}`); }
  }
  state.validazioneInCorso = false;
  await refreshBadges();
  await renderRevisione();
  if(errori.length) showErr(`Alcune bozze non sono state validate — ${errori.join("; ")}`);
}

async function rifiuta(id){
  try{
    await api(`/api/revisione/${id}/rifiuta`, {method:"POST"});
    await refreshBadges();
    await renderRevisione();
  }catch(e){ showErr(e.message); }
}

/* ------------------------------------------------------------- monitoraggio */
async function renderMonitoraggio(){
  loading("Caricamento monitoraggio…");
  try{ state.monitoraggio = await api("/api/monitoraggio"); }
  catch(e){ showErr(e.message); return; }
  const fonti = state.monitoraggio.fonti_con_modifiche;
  $("#view").innerHTML = `<div class="panel"><h2>Fonti con modifiche rilevate</h2>
    ${fonti.length ? "" : '<div class="muted">Nessuna modifica in attesa di esame.</div>'}
    ${fonti.map(f => `
    <div class="panel" style="background:var(--bg)">
      <div class="hd" style="margin-bottom:10px"><b>${esc(f.nome)}</b><span class="tag warn">${f.modifiche.length} modifiche</span></div>
      ${f.modifiche.map(m => `
        <div class="card" style="cursor:default">
          <div class="hd"><span class="ref">${esc(m.riferimento)}</span><span class="muted" style="font-size:12px">rilevata il ${esc(m.data_rilevamento)}</span></div>
          <div class="diff">
            <div class="old">${esc(m.testo_precedente)}</div>
            <div class="new">${esc(m.testo_nuovo)}</div>
          </div>
          <div class="muted" style="margin:8px 0;font-size:12px">Obblighi impattati: ${m.obblighi_impattati.length ? m.obblighi_impattati.map(id => `<a href="#" onclick="event.preventDefault();document.querySelector('nav button[data-tab=consultazione]').click();setTimeout(()=>openNodo('obbligo', ${id}),50)">#${id}</a>`).join(", ") : "nessuno"}</div>
          <button class="act" onclick="esamina(${m.modifica_id})">Segna come esaminata</button>
        </div>`).join("")}
    </div>`).join("")}
  </div>`;
}

async function esamina(id){
  try{
    await api(`/api/monitoraggio/${id}/esamina`, {method:"POST"});
    await refreshBadges();
    await renderMonitoraggio();
  }catch(e){ showErr(e.message); }
}

boot();
</script></body></html>
"""


def main():
    ap = argparse.ArgumentParser(description="UI web del censimento obblighi QTSP")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8010)
    args = ap.parse_args()

    import uvicorn
    uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
