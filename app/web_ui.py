"""UI web del censimento obblighi QTSP (nata come mockup nel ticket 07, ora in produzione).

Copre le tre funzioni previste dal ticket: consultazione/ricerca con le
relazioni tipizzate del grafo, coda di revisione delle bozze generate
dall'estrazione (valida/correggi/rifiuta), badge di notifica per le fonti
con modifiche rilevate dal monitoraggio (ticket 05).

Legge/scrive `censimento.db`; non e' ancora collegata a Qdrant ne' a un vero
LLM — la ricerca qui e' solo faceted + full-text, non semantica (quella
arriva con l'implementazione reale, dietro `interroga_obblighi`, ticket 04).

    .venv\\Scripts\\python.exe seed.py       # una tantum / per ripartire puliti
    .venv\\Scripts\\python.exe web_ui.py
    -> http://127.0.0.1:8010
"""

import argparse
import sqlite3
from datetime import date
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel

import qmd_search

DB_PATH = Path(__file__).parent / "censimento.db"

app = FastAPI(title="Censimento Obblighi QTSP", docs_url=None, redoc_url=None)


def _conn() -> sqlite3.Connection:
    if not DB_PATH.exists():
        raise HTTPException(503, f"Database non trovato: {DB_PATH}. Esegui prima seed.py.")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _lookup_maps(conn):
    tipi_obbligo = {r["id"]: r["nome"] for r in conn.execute("SELECT id, nome FROM tipi_obbligo")}
    stati_norma = {r["id"]: r["nome"] for r in conn.execute("SELECT id, nome FROM stati_norma")}
    categorie = {r["id"]: r["nome"] for r in conn.execute("SELECT id, nome FROM categorie_soggetto")}
    fonti = {r["id"]: r["nome"] for r in conn.execute("SELECT id, nome FROM fonti")}
    return tipi_obbligo, stati_norma, categorie, fonti


def _tipi_principio_map(conn):
    return {r["id"]: r["nome"] for r in conn.execute("SELECT id, nome FROM tipi_principio")}


def _oggetti_giuridici_map(conn):
    return {r["id"]: r["nome"] for r in conn.execute("SELECT id, nome FROM oggetti_giuridici")}


def _soggetti_di(conn, obbligo_id: int):
    rows = conn.execute("""
        SELECT cs.nome, os.ruolo FROM obbligo_soggetti os
        JOIN categorie_soggetto cs ON cs.id = os.categoria_soggetto_id
        WHERE os.obbligo_id = ?
    """, (obbligo_id,)).fetchall()
    obbligati = [r["nome"] for r in rows if r["ruolo"] == "obbligato"]
    destinatari = [r["nome"] for r in rows if r["ruolo"] == "destinatario"]
    return obbligati, destinatari


def _oggetti_di_principio(conn, principio_id: int):
    rows = conn.execute("""
        SELECT og.nome FROM principio_oggetti po
        JOIN oggetti_giuridici og ON og.id = po.oggetto_giuridico_id
        WHERE po.principio_id = ?
    """, (principio_id,)).fetchall()
    return [r["nome"] for r in rows]


def _riga_obbligo(conn, row, tipi_obbligo, stati_norma, fonti):
    obbligati, destinatari = _soggetti_di(conn, row["id"])
    return {
        "tipo_nodo": "obbligo",
        "obbligo_id": row["id"],
        "fonte_id": row["fonte_id"],
        "fonte": fonti.get(row["fonte_id"], "?"),
        "riferimento": row["riferimento"],
        "testo": row["testo"],
        "testo_integrale": row["testo_integrale"],
        "tipo_obbligo": tipi_obbligo.get(row["tipo_obbligo_id"], "?"),
        "stato_obbligo": stati_norma.get(row["stato_id"], "?"),
        "severita": row["severita"],
        "sanzioni": row["sanzioni"],
        "condizione_applicabilita": row["condizione_applicabilita"],
        "stato_validazione": row["stato_validazione"],
        "validato_da": row["validato_da"],
        "data_validazione": row["data_validazione"],
        "soggetti_obbligati": obbligati,
        "destinatari": destinatari,
    }


def _riga_principio(conn, row, tipi_principio, stati_norma, fonti):
    oggetti = _oggetti_di_principio(conn, row["id"])
    return {
        "tipo_nodo": "principio",
        "principio_id": row["id"],
        "fonte_id": row["fonte_id"],
        "fonte": fonti.get(row["fonte_id"], "?"),
        "riferimento": row["riferimento"],
        "testo": row["testo"],
        "testo_integrale": row["testo_integrale"],
        "tipo_principio": tipi_principio.get(row["tipo_principio_id"], "?"),
        "stato_obbligo": stati_norma.get(row["stato_id"], "?"),
        "condizione_applicabilita": row["condizione_applicabilita"],
        "stato_validazione": row["stato_validazione"],
        "validato_da": row["validato_da"],
        "data_validazione": row["data_validazione"],
        "oggetti_giuridici": oggetti,
    }


# ------------------------------------------------------- ricerca semantica

@app.get("/api/ricerca-semantica")
def ricerca_semantica(q: str, n: int = 10):
    """Ricerca per significato via qmd (locale, `qmd query` con reranking).

    Additiva rispetto alla ricerca full-text di /api/obblighi e /api/principi,
    non la sostituisce. Vedi docs/qmd-semantic-search-spec.md.
    """
    if not q.strip():
        return {"status": "ok", "risultati": []}

    trovati, errore = qmd_search.ricerca_semantica(q, n)
    if errore is not None:
        return JSONResponse(status_code=503, content={"status": "errore", "messaggio": errore})

    with _conn() as conn:
        tipi_obbligo_map, stati_obbligo_map, _, fonti = _lookup_maps(conn)
        tipi_principio_map = _tipi_principio_map(conn)
        risultati = []
        for r in trovati:
            if r["tipo_nodo"] == "obbligo":
                row = conn.execute("SELECT * FROM obblighi WHERE id = ?", (r["id"],)).fetchone()
                if row is None:
                    continue
                riga = _riga_obbligo(conn, row, tipi_obbligo_map, stati_obbligo_map, fonti)
            else:
                row = conn.execute("SELECT * FROM principi WHERE id = ?", (r["id"],)).fetchone()
                if row is None:
                    continue
                riga = _riga_principio(conn, row, tipi_principio_map, stati_obbligo_map, fonti)
            riga["score"] = r["score"]
            riga["snippet"] = r["snippet"]
            risultati.append(riga)

    return {"status": "ok", "risultati": risultati}


# --------------------------------------------------------------- lookup/stats

@app.get("/api/lookup")
def lookup():
    with _conn() as conn:
        return {
            "status": "ok",
            "fonti": [dict(r) for r in conn.execute(
                "SELECT f.id AS fonte_id, f.nome, f.versione, f.url_sorgente, sf.nome AS stato "
                "FROM fonti f JOIN stati_fonte sf ON sf.id = f.stato_id")],
            "tipi_obbligo": [r["nome"] for r in conn.execute("SELECT nome FROM tipi_obbligo")],
            "stati_obbligo": [r["nome"] for r in conn.execute("SELECT nome FROM stati_norma")],
            "categorie_soggetto": [r["nome"] for r in conn.execute("SELECT nome FROM categorie_soggetto")],
            "tipi_principio": [r["nome"] for r in conn.execute("SELECT nome FROM tipi_principio")],
            "oggetti_giuridici": [r["nome"] for r in conn.execute("SELECT nome FROM oggetti_giuridici")],
            "tipi_relazione": [dict(r) for r in conn.execute("SELECT nome, nome_inverso FROM tipi_relazione")],
        }


@app.get("/api/stats")
def stats():
    with _conn() as conn:
        obblighi = conn.execute("SELECT stato_validazione, COUNT(*) c FROM obblighi GROUP BY stato_validazione").fetchall()
        counts = {r["stato_validazione"]: r["c"] for r in obblighi}
        n_principi = conn.execute("SELECT COUNT(*) c FROM principi").fetchone()["c"]
        n_fonti = conn.execute("SELECT COUNT(*) c FROM fonti").fetchone()["c"]
        n_relazioni = conn.execute("SELECT COUNT(*) c FROM relazioni").fetchone()["c"]
        n_modifiche = conn.execute("SELECT COUNT(*) c FROM modifiche_rilevate WHERE esaminata = 0").fetchone()["c"]
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
    with _conn() as conn:
        tipi_obbligo_map, stati_obbligo_map, categorie_map, fonti = _lookup_maps(conn)
        rows = conn.execute("SELECT * FROM obblighi").fetchall()

    needle = q.strip().lower()
    tipo_ids = {k for k, v in tipi_obbligo_map.items() if v in tipo_obbligo} if tipo_obbligo else None
    stato_ids = {k for k, v in stati_obbligo_map.items() if v in stato_obbligo} if stato_obbligo else None

    risultati = []
    with _conn() as conn:
        for row in rows:
            if solo_validati and row["stato_validazione"] != "validato":
                continue
            if fonte_id and row["fonte_id"] not in fonte_id:
                continue
            if tipo_ids is not None and row["tipo_obbligo_id"] not in tipo_ids:
                continue
            if stato_ids is not None and row["stato_id"] not in stato_ids:
                continue
            if needle and needle not in row["testo"].lower() and needle not in row["riferimento"].lower() \
                    and needle not in (row["testo_integrale"] or "").lower():
                continue
            obbligati, destinatari = _soggetti_di(conn, row["id"])
            if categoria_soggetto:
                pool = obbligati if ruolo == "obbligato" else destinatari if ruolo == "destinatario" else obbligati + destinatari
                if not any(c in pool for c in categoria_soggetto):
                    continue
            risultati.append(_riga_obbligo(conn, row, tipi_obbligo_map, stati_obbligo_map, fonti))

    return {"status": "ok", "totale": len(risultati), "risultati": risultati}


def _vicini_di(conn, tipo_nodo: str, nodo_id: int, fonti):
    """Vicini di un nodo del grafo (Obbligo o Principio, ADR-0004), a prescindere
    dal tipo di nodo all'altra estremità della relazione."""
    vicini_rows = conn.execute("""
        SELECT r.id AS relazione_id, r.nodo_a_tipo AS altro_tipo, r.nodo_a_id AS altro_id, tr.nome AS tipo
        FROM relazioni r JOIN tipi_relazione tr ON tr.id = r.tipo_relazione_id
        WHERE r.nodo_da_tipo = ? AND r.nodo_da_id = ?
        UNION ALL
        SELECT r.id AS relazione_id, r.nodo_da_tipo AS altro_tipo, r.nodo_da_id AS altro_id, tr.nome_inverso AS tipo
        FROM relazioni r JOIN tipi_relazione tr ON tr.id = r.tipo_relazione_id
        WHERE r.nodo_a_tipo = ? AND r.nodo_a_id = ?
    """, (tipo_nodo, nodo_id, tipo_nodo, nodo_id)).fetchall()
    vicini = []
    for v in vicini_rows:
        tabella = "obblighi" if v["altro_tipo"] == "obbligo" else "principi"
        altro = conn.execute(f"SELECT * FROM {tabella} WHERE id = ?", (v["altro_id"],)).fetchone()
        if altro is None:
            continue  # estremità inesistente: nessun FK a livello DB (ADR-0004), la si ignora in lettura
        vicini.append({
            "tipo_nodo": v["altro_tipo"],
            "obbligo_id" if v["altro_tipo"] == "obbligo" else "principio_id": v["altro_id"],
            "relazione_id": v["relazione_id"],
            "tipo_relazione": v["tipo"],
            "fonte": fonti.get(altro["fonte_id"], "?"),
            "riferimento": altro["riferimento"],
            "testo": altro["testo"],
            "stato_validazione": altro["stato_validazione"],
        })
    return vicini


@app.get("/api/obblighi/{obbligo_id}")
def dettaglio_obbligo(obbligo_id: int):
    with _conn() as conn:
        tipi_obbligo_map, stati_norma_map, categorie_map, fonti = _lookup_maps(conn)
        row = conn.execute("SELECT * FROM obblighi WHERE id = ?", (obbligo_id,)).fetchone()
        if row is None:
            raise HTTPException(404, "Obbligo non trovato")
        obbligo = _riga_obbligo(conn, row, tipi_obbligo_map, stati_norma_map, fonti)
        vicini = _vicini_di(conn, "obbligo", obbligo_id, fonti)

    return {"status": "ok", "obbligo": obbligo, "vicini": vicini}


@app.get("/api/principi/{principio_id}")
def dettaglio_principio(principio_id: int):
    with _conn() as conn:
        _, stati_norma_map, _, fonti = _lookup_maps(conn)
        tipi_principio_map = _tipi_principio_map(conn)
        row = conn.execute("SELECT * FROM principi WHERE id = ?", (principio_id,)).fetchone()
        if row is None:
            raise HTTPException(404, "Principio non trovato")
        principio = _riga_principio(conn, row, tipi_principio_map, stati_norma_map, fonti)
        vicini = _vicini_di(conn, "principio", principio_id, fonti)

    return {"status": "ok", "principio": principio, "vicini": vicini}


@app.get("/api/principi")
def cerca_principi(
    q: str = "",
    fonte_id: list[int] = Query(default=[]),
    tipo_principio: list[str] = Query(default=[]),
    oggetto_giuridico: list[str] = Query(default=[]),
    solo_validati: bool = True,
):
    with _conn() as conn:
        tipi_principio_map = _tipi_principio_map(conn)
        _, stati_norma_map, _, fonti = _lookup_maps(conn)
        rows = conn.execute("SELECT * FROM principi").fetchall()

    needle = q.strip().lower()
    tipo_ids = {k for k, v in tipi_principio_map.items() if v in tipo_principio} if tipo_principio else None

    risultati = []
    with _conn() as conn:
        for row in rows:
            if solo_validati and row["stato_validazione"] != "validato":
                continue
            if fonte_id and row["fonte_id"] not in fonte_id:
                continue
            if tipo_ids is not None and row["tipo_principio_id"] not in tipo_ids:
                continue
            if needle and needle not in row["testo"].lower() and needle not in row["riferimento"].lower() \
                    and needle not in (row["testo_integrale"] or "").lower():
                continue
            oggetti = _oggetti_di_principio(conn, row["id"])
            if oggetto_giuridico and not any(o in oggetti for o in oggetto_giuridico):
                continue
            risultati.append(_riga_principio(conn, row, tipi_principio_map, stati_norma_map, fonti))

    return {"status": "ok", "totale": len(risultati), "risultati": risultati}


# ---------------------------------------------------------------- revisione

@app.get("/api/revisione")
def coda_revisione():
    with _conn() as conn:
        tipi_obbligo_map, stati_obbligo_map, categorie_map, fonti = _lookup_maps(conn)
        rows = conn.execute("SELECT * FROM obblighi WHERE stato_validazione = 'bozza' ORDER BY id").fetchall()
        bozze = [_riga_obbligo(conn, r, tipi_obbligo_map, stati_obbligo_map, fonti) for r in rows]
    return {"status": "ok", "bozze": bozze}


class CorrezioneBozza(BaseModel):
    riferimento: str
    testo: str
    tipo_obbligo: str
    stato_obbligo: str
    severita: str | None = None
    sanzioni: str | None = None
    condizione_applicabilita: str | None = None
    soggetti_obbligati: list[str] = []
    destinatari: list[str] = []
    validato_da: str = "sistema"


@app.post("/api/revisione/{obbligo_id}/valida")
def valida_bozza(obbligo_id: int, body: CorrezioneBozza):
    with _conn() as conn:
        tipo_row = conn.execute("SELECT id FROM tipi_obbligo WHERE nome = ?", (body.tipo_obbligo,)).fetchone()
        stato_row = conn.execute("SELECT id FROM stati_norma WHERE nome = ?", (body.stato_obbligo,)).fetchone()
        if tipo_row is None or stato_row is None:
            raise HTTPException(400, "Valore di lookup sconosciuto (tipo_obbligo/stato_obbligo)")
        cur = conn.execute("SELECT id FROM obblighi WHERE id = ? AND stato_validazione = 'bozza'", (obbligo_id,))
        if cur.fetchone() is None:
            raise HTTPException(404, "Bozza non trovata (già validata/rifiutata?)")

        conn.execute("""
            UPDATE obblighi SET riferimento = ?, testo = ?, tipo_obbligo_id = ?, stato_id = ?,
                severita = ?, sanzioni = ?, condizione_applicabilita = ?,
                stato_validazione = 'validato', validato_da = ?, data_validazione = ?
            WHERE id = ?
        """, (body.riferimento, body.testo, tipo_row["id"], stato_row["id"],
              body.severita, body.sanzioni, body.condizione_applicabilita,
              body.validato_da, date.today().isoformat(), obbligo_id))

        conn.execute("DELETE FROM obbligo_soggetti WHERE obbligo_id = ?", (obbligo_id,))
        cats = {r["nome"]: r["id"] for r in conn.execute("SELECT id, nome FROM categorie_soggetto")}
        for nome in body.soggetti_obbligati:
            if nome not in cats:
                raise HTTPException(400, f"Categoria di soggetto sconosciuta: {nome}")
            conn.execute("INSERT INTO obbligo_soggetti (obbligo_id, categoria_soggetto_id, ruolo) VALUES (?,?,?)",
                         (obbligo_id, cats[nome], "obbligato"))
        for nome in body.destinatari:
            if nome not in cats:
                raise HTTPException(400, f"Categoria di soggetto sconosciuta: {nome}")
            conn.execute("INSERT INTO obbligo_soggetti (obbligo_id, categoria_soggetto_id, ruolo) VALUES (?,?,?)",
                         (obbligo_id, cats[nome], "destinatario"))
        conn.commit()
    qmd_search.sync_qmd()
    return {"status": "ok", "obbligo_id": obbligo_id}


@app.post("/api/revisione/{obbligo_id}/rifiuta")
def rifiuta_bozza(obbligo_id: int):
    # Decisione ticket 03: le bozze rifiutate vengono eliminate, nessuna traccia storica.
    with _conn() as conn:
        cur = conn.execute("DELETE FROM obblighi WHERE id = ? AND stato_validazione = 'bozza'", (obbligo_id,))
        if cur.rowcount == 0:
            raise HTTPException(404, "Bozza non trovata (già validata/rifiutata?)")
        conn.commit()
    qmd_search.sync_qmd()
    return {"status": "ok"}


# -------------------------------------------------------------- monitoraggio

@app.get("/api/monitoraggio")
def monitoraggio_stato():
    with _conn() as conn:
        fonti = {r["id"]: r["nome"] for r in conn.execute("SELECT id, nome FROM fonti")}
        rows = conn.execute("""
            SELECT * FROM modifiche_rilevate WHERE esaminata = 0 ORDER BY fonte_id, data_rilevamento
        """).fetchall()
        per_fonte: dict[int, dict] = {}
        for r in rows:
            impattati = [row["id"] for row in conn.execute(
                "SELECT id FROM obblighi WHERE fonte_id = ? AND riferimento = ?", (r["fonte_id"], r["riferimento"]))]
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
    with _conn() as conn:
        cur = conn.execute("UPDATE modifiche_rilevate SET esaminata = 1 WHERE id = ?", (modifica_id,))
        if cur.rowcount == 0:
            raise HTTPException(404, "Modifica non trovata")
        conn.commit()
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
input[type=text],select{font:inherit;padding:6px 9px;border:1px solid var(--line);border-radius:6px;background:var(--panel);color:var(--ink)}
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
    <div class="controls">
      <input type="text" id="q" placeholder="cerca nel testo o nel riferimento…" value="${esc(f.q)}">
      <label style="display:flex;align-items:center;gap:6px;font-size:12px;color:var(--muted)">
        <input type="checkbox" id="solovalidati" ${f.solo_validati?"checked":""}> solo validati
      </label>
    </div>
    <div class="facets">
      <div class="facet"><div class="lbl">Fonte</div>${chipRow("f-fonte", lk.fonti.map(x=>x.nome), new Set([...f.fonte_id].map(id => lk.fonti.find(x=>x.fonte_id===id)?.nome)))}</div>
      <div class="facet"><div class="lbl">Tipo obbligo</div>${chipRow("f-tipo", lk.tipi_obbligo, f.tipo_obbligo)}</div>
      <div class="facet"><div class="lbl">Stato norma</div>${chipRow("f-stato", lk.stati_obbligo, f.stato_obbligo)}</div>
      <div class="facet"><div class="lbl">Categoria soggetto</div>${chipRow("f-cat", lk.categorie_soggetto, f.categoria_soggetto)}</div>
      <div class="facet"><div class="lbl">Tipo principio</div>${chipRow("f-tprinc", lk.tipi_principio, f.tipo_principio)}</div>
      <div class="facet"><div class="lbl">Oggetto giuridico</div>${chipRow("f-ogg", lk.oggetti_giuridici, f.oggetto_giuridico)}</div>
    </div>
  </div>
  <div class="panel"><h2>Risultati</h2><div id="reslist" class="spin">Caricamento…</div></div>
  <div class="panel">
    <h2>Ricerca per significato <span class="muted" style="font-weight:normal;font-size:12px">(sperimentale, via qmd)</span></h2>
    <div class="controls">
      <input type="text" id="qsem" placeholder="descrivi cosa cerchi, anche senza parole esatte del testo…">
      <button id="btnsem">Cerca</button>
    </div>
    <div id="ressem"></div>
  </div>`;

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

  $("#btnsem").onclick = ricercaSemantica;
  $("#qsem").addEventListener("keydown", e => { if(e.key === "Enter") ricercaSemantica(); });

  await searchNow(true);
}

async function ricercaSemantica(){
  const q = $("#qsem").value.trim();
  const box = document.getElementById("ressem");
  if(!q){ box.innerHTML = ""; return; }
  box.innerHTML = `<div class="spin">Ricerca semantica…</div>`;
  let data;
  try{ data = await api("/api/ricerca-semantica?" + new URLSearchParams({q, n: 10}).toString()); }
  catch(e){ box.innerHTML = `<div class="muted">Ricerca semantica non disponibile: ${esc(e.message)}</div>`; return; }
  if(!data.risultati || !data.risultati.length){ box.innerHTML = `<div class="muted">Nessun risultato.</div>`; return; }
  box.innerHTML = data.risultati.map(o => (o.tipo_nodo === "principio" ? cardPrincipio(o) : cardObbligo(o))
    .replace('<div class="hd">', `<div class="hd"><span class="tag" title="punteggio di rilevanza semantica">score ${o.score.toFixed(2)}</span>`)
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
  // Solo faceted + full-text (nessun ranking semantico ancora, vedi docstring in cima al file):
  // se sono attivi filtri specifici di un solo tipo di nodo, l'altro tipo di ricerca resta comunque
  // eseguita (i suoi filtri semplicemente non si applicano), cosi' un principio puo' emergere anche
  // filtrando per categoria soggetto e viceversa.
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
  return `<div class="panel"><h2>Relazioni tipizzate (grafo)</h2>
    ${vicini.length ? vicini.map(v => `
      <div class="card" onclick="openNodo('${v.tipo_nodo}', ${v.tipo_nodo==='principio'?v.principio_id:v.obbligo_id})">
        <div class="hd"><span class="tag">${esc(v.tipo_relazione)}</span>
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
      ${b.length ? '<button class="act primary" onclick="validaTutte()">Valida tutte</button>' : ""}
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
  const ids = state.bozze.bozze.map(o => o.obbligo_id);
  const errori = [];
  for(const id of ids){
    try{ await valida(id, {silent:true}); }
    catch(e){ errori.push(`#${id}: ${e.message}`); }
  }
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
    print(f"Censimento Obblighi QTSP — http://{args.host}:{args.port}")
    print(f"  SQLite: {DB_PATH}")
    ok, msg = qmd_search.sync_qmd()
    print(f"  qmd sync: {'ok' if ok else 'fallita (' + msg + ')'}")
    uvicorn.run(app, host=args.host, port=args.port, log_level="info")


if __name__ == "__main__":
    main()
