"""Audit di troncamento su `testo_integrale` per tutti i nodi già in Neo4j.

Complementare a `seed_data.lib.verifica_completezza_testo_integrale`: quella
funzione blocca un seed che sta per inserire righe troncate; questo script
audita ciò che è già nel grafo (incluse correzioni fatte a mano via Cypher,
fonti seedate prima dell'introduzione della guardia, o import futuri che
bypassano `inserisci_capitoli`). Stesso criterio (ADR-0010): marcatore di
elisione (`…`, `...`, `[...]`) in `testo_integrale` = estrazione troncata,
mai un dato accettabile nel censimento — esclusa la convenzione Normattiva
`((...))` (testo soppresso da una modifica legislativa, riportato
letteralmente così nel testo ufficiale consolidato) e il marcatore di
estensibilità ASN.1 `| ...)` (ITU-T X.680): entrambi contenuto normativo/
tecnico autentico, non un'elisione di estrazione.

Uso:
    app/.venv/bin/python app/tools/verifica_troncamento.py [--fonte-id N]

Senza `--fonte-id`, audita tutte le Fonti. Uscita non-zero se trova
troncature (utilizzabile come guardia anche fuori da un import, es. dopo
una correzione manuale o come controllo periodico).
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from neo4j_common import get_driver, get_database  # noqa: E402

MARKER_TRONCAMENTO = ("…", "...", "[...]", "[…]")
OMISSIS_NORMATTIVA = re.compile(r"\(\(\s*\.{3}\s*\)\)")
ASN1_EXTENSIBILITY = re.compile(r"\|\s*\.\.\.\s*[\)\}]")


def _senza_omissis_legittimi(testo: str) -> str:
    testo = OMISSIS_NORMATTIVA.sub("", testo)
    testo = ASN1_EXTENSIBILITY.sub("", testo)
    return testo


def audita(fonte_id: int | None = None) -> list[dict]:
    """Ritorna la lista dei nodi (Obbligo o Principio) il cui `testo_integrale`
    contiene un marcatore di elisione. Lista vuota = nessuna troncatura nota."""
    condizioni = ["n.testo_integrale IS NOT NULL"]
    if fonte_id is not None:
        condizioni.append("f.id = $fonte_id")
    where_clause = "WHERE " + " AND ".join(condizioni)
    query = f"""
        MATCH (n)-[:DA_FONTE]->(f:Fonte)
        {where_clause}
        RETURN elementId(n) as eid, labels(n)[0] as tipo, f.id as fonte_id,
               f.nome as fonte_nome, n.riferimento as riferimento,
               n.testo_integrale as testo_integrale
    """
    d = get_driver()
    try:
        with d.session(database=get_database()) as s:
            righe = list(s.run(query, fonte_id=fonte_id))
    finally:
        d.close()

    trovati = []
    for riga in righe:
        testo = _senza_omissis_legittimi(riga["testo_integrale"] or "")
        marker_trovati = [m for m in MARKER_TRONCAMENTO if m in testo]
        if marker_trovati:
            trovati.append({
                "eid": riga["eid"],
                "tipo": riga["tipo"],
                "fonte_id": riga["fonte_id"],
                "fonte_nome": riga["fonte_nome"],
                "riferimento": riga["riferimento"],
                "marker": marker_trovati,
                "coda": testo[-60:],
            })
    return trovati


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fonte-id", type=int, default=None,
                         help="limita l'audit a una singola Fonte (default: tutte)")
    args = parser.parse_args()

    trovati = audita(fonte_id=args.fonte_id)
    if not trovati:
        print("Nessuna troncatura rilevata.")
        return 0

    print(f"{len(trovati)} nodo/i con testo_integrale troncato:")
    for t in trovati:
        print(f"  [{t['tipo']}] fonte_id={t['fonte_id']} ({t['fonte_nome']}) "
              f"riferimento={t['riferimento']!r} marker={t['marker']} coda={t['coda']!r}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
