"""Fase 6 (ADR-0009) stadio 1 - generazione candidati a zero token LLM per
ETSI TS 119 431-1 (fonte_id=11) e ETSI TS 119 431-2 (fonte_id=12).

Uso: app/.venv/bin/python app/tools/fase6_candidati_431.py

Scrive app/.source_cache/fase6_431_candidati.json con:
  {"grep": [...], "knn": [...]}
per ciascuna fonte, pronto per lo stadio 2 (classificazione LLM sullo shortlist).
"""
import json
import re
import sys
from pathlib import Path

APP_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(APP_DIR))

from neo4j_common import get_driver, get_database

FONTI_TARGET = {11: "etsi_119_431_1", 12: "etsi_119_431_2"}

# fonte_id -> pattern di citazione testuale plausibile nel testo ufficiale
FONTI_CITAZIONE = {
    1: [r"910/2014", r"\beIDAS\b(?!2)", r"\beIDASv2\b"],
    2: [r"2024/1183", r"eIDAS2", r"eIDASv2"],
    3: [r"82/2005", r"\bCAD\b"],
    4: [r"22 february 2013", r"22 febbraio 2013"],
    5: [r"24 october 2014", r"24 ottobre 2014", r"\bSPID\b"],
    6: [r"19 october 2021", r"19 ottobre 2021"],
    7: [r"319 412-5", r"319412-5", r"QCStatement"],
    8: [r"2025/1566"],
    9: [r"TS 119 461", r"119461", r"119 461"],
    10: [r"EN 319 401", r"319401", r"319 401"],
    11: [r"TS 119 431-1", r"119431-1", r"119 431-1"],
    12: [r"TS 119 431-2", r"119431-2", r"119 431-2"],
}

driver = get_driver()
db = get_database()


def testo_nodi(fonte_id: int) -> list[dict]:
    with driver.session(database=db) as s:
        res = s.run(
            """
            MATCH (n) WHERE (n:Obbligo OR n:Principio)
            MATCH (n)-[:DA_FONTE]->(f:Fonte {id: $fonte_id})
            RETURN labels(n)[0] AS tipo, n.riferimento AS riferimento, n.testo AS testo, n.id AS id
            """,
            fonte_id=fonte_id,
        )
        return [dict(r) for r in res]


def knn_per_nodo(tipo: str, node_id: int, escludi_fonte_id: int, soglia: float = 0.80, top_k: int = 8) -> list[dict]:
    idx = "idxEmbeddingObbligo" if tipo == "Obbligo" else "idxEmbeddingPrincipio"
    label = tipo
    with driver.session(database=db) as s:
        res = s.run(
            f"""
            MATCH (src) WHERE (src:Obbligo OR src:Principio) AND src.id = $node_id
            MATCH (src)-[:DA_FONTE]->(:Fonte {{id: $fonte_id}})
            CALL db.index.vector.queryNodes($idx, $top_k, src.embedding) YIELD node, score
            WHERE score >= $soglia
            MATCH (node)-[:DA_FONTE]->(tf:Fonte)
            WHERE tf.id <> $escludi_fonte_id
            RETURN labels(node)[0] AS tipo_target, node.riferimento AS riferimento_target,
                   tf.id AS fonte_target, score
            ORDER BY score DESC
            """,
            node_id=node_id, fonte_id=escludi_fonte_id, idx=idx, top_k=top_k, soglia=soglia,
            escludi_fonte_id=escludi_fonte_id,
        )
        return [dict(r) for r in res]


def main():
    output = {}
    for fonte_id, slug in FONTI_TARGET.items():
        raw_path = APP_DIR / ".source_cache" / slug / "raw.txt"
        raw_text = raw_path.read_text(encoding="utf-8")

        # --- grep: quali altre fonti sono citate nel testo grezzo ---
        citazioni_trovate = {}
        for altro_fonte_id, patterns in FONTI_CITAZIONE.items():
            if altro_fonte_id == fonte_id:
                continue
            hits = []
            for pat in patterns:
                for m in re.finditer(pat, raw_text, re.IGNORECASE):
                    start = max(0, m.start() - 150)
                    end = min(len(raw_text), m.end() + 150)
                    hits.append(raw_text[start:end].replace("\n", " "))
            if hits:
                citazioni_trovate[altro_fonte_id] = hits[:15]  # cap per fonte

        # --- KNN: per ogni nodo della fonte, top-k verso tutte le altre fonti ---
        nodi = testo_nodi(fonte_id)
        knn_coppie = []
        for n in nodi:
            tipo_neo = "Obbligo" if n["tipo"] == "Obbligo" else "Principio"
            vicini = knn_per_nodo(tipo_neo, n["id"], fonte_id)
            for v in vicini:
                knn_coppie.append({
                    "nodo_da_tipo": n["tipo"], "nodo_da_riferimento": n["riferimento"],
                    "nodo_da_testo": n["testo"],
                    "nodo_a_tipo": v["tipo_target"], "nodo_a_riferimento": v["riferimento_target"],
                    "nodo_a_fonte": v["fonte_target"], "score": round(v["score"], 4),
                })

        output[str(fonte_id)] = {
            "n_nodi": len(nodi),
            "grep_citazioni": citazioni_trovate,
            "knn_coppie": knn_coppie,
        }
        print(f"fonte_id={fonte_id}: {len(nodi)} nodi, grep su {len(citazioni_trovate)} fonti, {len(knn_coppie)} coppie KNN sopra soglia 0.80")

    out_path = APP_DIR / ".source_cache" / "fase6_431_candidati.json"
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Scritto {out_path}")


if __name__ == "__main__":
    main()
