"""Pre-flight delle relazioni di una fonte in costruzione, PRIMA del seed.

Perche' esiste: le relazioni di un capitolo si risolvono in `inserisci_capitoli`
attraverso il registro `(tipo, fonte_id, riferimento) -> id`, popolato mentre il
seed procede. Un riferimento sbagliato — tipo di nodo invertito (Obbligo dove il
modulo ha scritto Principio), riferimento non esistente, fonte citata dopo nel
wiring — non produce un errore di sintassi: fa fallire il seed a meta' strada con
un `KeyError`, dopo aver ricostruito tutto il grafo in memoria.

Questo controllo anticipa l'errore e lo localizza, distinguendo i due casi:
- riferimenti INTERNI alla fonte in costruzione (`fonte_id_o_None = None` nel
  modulo): risolti contro i nodi dichiarati dai moduli della fonte stessa;
- riferimenti ESTERNI: risolti contro il grafo Neo4j corrente.

Il secondo caso da' un falso negativo se la fonte citata non e' ancora stata
seedata (il nodo esiste nel registro futuro, non nel grafo di ora): in quel caso
usare `--atteso-dopo` per elencare le fonti che il seed inserira' prima di questa.

Uso:

    app/.venv/bin/python app/tools/preflight_relazioni.py <fonte_id> <dir_moduli>

Nella stessa sessione, il seed va lanciato con `set -o pipefail`: una pipe verso
`tail` restituisce il codice di uscita di `tail` (0) anche quando Python e'
crollato, e il fallimento passerebbe per successo.
"""

import importlib.util
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from neo4j_common import get_database, get_driver  # noqa: E402


def carica(percorso: Path):
    spec = importlib.util.spec_from_file_location(percorso.stem, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__.strip().split("Uso:")[1].split("\n\n")[0].strip())
        return 2
    fonte_id = int(sys.argv[1])
    dir_moduli = Path(sys.argv[2])

    moduli = [carica(p) for p in sorted(dir_moduli.glob("cap*.py"))]
    if not moduli:
        raise SystemExit(f"nessun modulo cap*.py in {dir_moduli}")

    interni = set()
    for modulo in moduli:
        for riga in modulo.RIGHE_OBBLIGHI:
            interni.add(("obbligo", fonte_id, riga["riferimento"]))
        for riga in modulo.RIGHE_PRINCIPI:
            interni.add(("principio", fonte_id, riga["riferimento"]))

    driver = get_driver()
    mancanti = []
    totale = 0
    with driver.session(database=get_database()) as sessione:
        for modulo in moduli:
            for rel in modulo.RELAZIONI:
                totale += 1
                for lato in ("nodo_da", "nodo_a"):
                    tipo, fonte, riferimento = rel[lato]
                    if fonte is None:
                        if (tipo, fonte_id, riferimento) not in interni:
                            mancanti.append((lato, tipo, "INTERNO", riferimento))
                        continue
                    etichetta = "Obbligo" if tipo == "obbligo" else "Principio"
                    trovato = sessione.run(
                        f"MATCH (n:{etichetta}) WHERE n.fonte_id=$f AND n.riferimento=$r RETURN count(n) AS c",
                        f=fonte, r=riferimento,
                    ).single()["c"]
                    if trovato == 0:
                        mancanti.append((lato, tipo, fonte, riferimento))
    driver.close()

    print(f"Fonte {fonte_id}: {len(moduli)} moduli, {len(interni)} nodi, {totale} relazioni")
    if mancanti:
        print("RIFERIMENTI MANCANTI (il seed fallirebbe con KeyError):")
        for mancante in mancanti:
            print("   ", mancante)
        return 1
    print("riferimenti mancanti: nessuno")
    return 0


if __name__ == "__main__":
    sys.exit(main())
