"""Stadio 1 (candidati, zero token LLM) della Fase 6 di ADR-0009, generico.

Generalizza i moduli usa-e-getta `fase6_candidati_431/432/612.py`, che
lavoravano sugli embedding gia' scritti in Neo4j e richiedevano quindi di
seedare la Fonte nuova prima di poter generare i candidati — con la
conseguenza di dover lanciare `app/seed.py` due volte per ogni import (una
per il testo, una per le relazioni cross-fonte trovate dopo).

Qui l'embedding dei nodi nuovi e' calcolato al volo con lo stesso modello e
lo stesso campo (`testo`, normalizzato) usato da `app/embed_neo4j.py` per
tutti gli altri nodi: il confronto con l'indice HNSW gia' popolato e' quindi
omogeneo, e la Fase 6 puo' girare **prima** del seed. Un solo seed per
import.

Non sostituisce la validazione: l'output e' uno shortlist da classificare
(stadio 2, nella sessione principale) e da verificare contro Neo4j (stadio 3,
anti-allucinazione). Le relazioni validate vanno poi scritte in un modulo
"capitolo virtuale" agganciato a `seed.py`, perche' la scrittura sul grafo
passa solo da li' (ADR-0011).

Uso:

    app/.venv/bin/python app/tools/fase6_candidati_knn.py <slug_fonte> <modulo.py> [<modulo.py> ...] \
        [--k 8] [--soglia 0.82] [--max 120]

`slug_fonte` serve solo a nominare il file di output
(`app/.source_cache/<slug_fonte>/fase6_candidati.json`) e a escludere i nodi
della Fonte in esame dai risultati: i nodi nuovi non essendo ancora nel
grafo, la loro esclusione avviene sul `fonte_id` delle controparti, passato
con `--fonte-id` (obbligatorio).

L'output a video e' una riga per coppia candidata, ordinata per score
decrescente: nodo nuovo, controparte esistente (fonte + riferimento), score.
"""

import argparse
import importlib.util
import json
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from neo4j_common import get_database, get_driver  # noqa: E402
from seed_data import lib as seed_lib  # noqa: E402

INDICI = {"obbligo": "idxEmbeddingObbligo", "principio": "idxEmbeddingPrincipio"}


def carica_modulo(percorso: Path):
    spec = importlib.util.spec_from_file_location(percorso.stem, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="slug della fonte (per il file di output)")
    parser.add_argument("moduli", nargs="+", help="moduli capitolo della fonte nuova")
    parser.add_argument("--fonte-id", type=int, required=True, help="fonte_id della fonte nuova")
    parser.add_argument("--k", type=int, default=8, help="vicini da chiedere a ciascun indice (default 8)")
    parser.add_argument("--soglia", type=float, default=0.82, help="score minimo (default 0.82)")
    parser.add_argument("--max", type=int, default=120, help="massimo coppie stampate (default 120)")
    args = parser.parse_args()

    nodi = []
    for percorso in args.moduli:
        modulo = carica_modulo(Path(percorso))
        for riga in modulo.RIGHE_OBBLIGHI:
            nodi.append(("obbligo", riga["riferimento"], riga["testo"]))
        for riga in modulo.RIGHE_PRINCIPI:
            nodi.append(("principio", riga["riferimento"], riga["testo"]))
    if not nodi:
        raise SystemExit("nessuna riga nei moduli indicati")

    from sentence_transformers import SentenceTransformer
    from neo4j_common import EMBEDDING_MODEL_NAME

    modello = SentenceTransformer(EMBEDDING_MODEL_NAME)
    vettori = modello.encode(
        [testo for _, _, testo in nodi], batch_size=32, show_progress_bar=False, normalize_embeddings=True
    )

    driver = get_driver()
    coppie = []
    with driver.session(database=get_database()) as sessione:
        for (tipo, riferimento, _testo), vettore in zip(nodi, vettori):
            righe = sessione.run(
                f"CALL db.index.vector.queryNodes('{INDICI[tipo]}', $k, $vettore) "
                "YIELD node, score "
                "WHERE score >= $soglia AND node.fonte_id <> $fonte_id "
                "RETURN node.fonte_id AS fonte, node.riferimento AS riferimento, node.testo AS testo, score "
                "ORDER BY score DESC",
                k=args.k, vettore=vettore.tolist(), soglia=args.soglia, fonte_id=args.fonte_id,
            ).data()
            for riga in righe:
                coppie.append({
                    "da": riferimento,
                    "da_tipo": tipo,
                    "fonte": riga["fonte"],
                    "a": riga["riferimento"],
                    "a_testo": riga["testo"],
                    "score": round(riga["score"], 4),
                })
    driver.close()

    coppie.sort(key=lambda c: -c["score"])
    out = APP_DIR / ".source_cache" / args.slug / "fase6_candidati.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(coppie, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

    print(f"{len(nodi)} nodi nuovi, {len(coppie)} coppie candidate (soglia {args.soglia}, k={args.k})")
    print(f"shortlist completa: {out.relative_to(APP_DIR.parent)}")
    print()
    for c in coppie[: args.max]:
        print(f"{c['score']:.3f}  {c['da'][:52]:<52} -> f{c['fonte']} {c['a'][:52]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
