"""Divide un testo normativo grezzo in file per capitolo/sezione, con path
deterministici assegnati centralmente (non dal subagent che poi li userà),
e produce un manifest.json letto da `app/seed_data/lib.py`.

Motivo: nell'import eIDAS ogni subagent-per-capitolo riceveva il testo
ufficiale incollato inline nel prompt, duplicando in ogni subagent l'intero
regolamento e non solo la propria porzione — e due subagent hanno scritto sul
medesimo file di output per assenza di un'assegnazione di path esplicita e
precedente al dispatch. Questo script fa entrambe le cose una volta sola,
prima di aprire qualunque subagent:
  1) split del testo grezzo in una porzione per capitolo (letta una sola
     volta dalla sessione principale, non da ciascun subagent);
  2) assegnazione dei path di output (sia del testo sorgente sia, per
     convenzione, del modulo Python che lo autora) prima del dispatch.

Uso:

    app/.venv/bin/python app/tools/split_source.py <fonte> <raw.txt> <boundaries.json>

`raw.txt`: testo ufficiale completo, salvato una volta dalla sessione
principale (es. con lo strumento `read` su un URL EUR-Lex/Normattiva, poi
`write` su questo path — nessuna fetch di rete fatta da questo script).

`boundaries.json`: lista ordinata di oggetti, uno per capitolo/sezione in cui
si vuole dividere il lavoro di autoria, nella forma:

    [
      {"capitolo": "cap01", "titolo": "Capo I - Disposizioni generali", "marker": "Art. 1."},
      {"capitolo": "cap02", "titolo": "Capo II - Identificazione elettronica", "marker": "Art. 6."}
    ]

`marker`: stringa cercata letteralmente (prima occorrenza, non regex) nel
testo grezzo da cui inizia quel capitolo; l'ultimo capitolo elencato si
estende fino a fine testo. I marker devono comparire nell'ordine dato.

Scrive:
    app/.source_cache/<fonte>/cap01.txt, cap02.txt, ...
    app/.source_cache/<fonte>/manifest.json

`manifest.json`:
    {
      "fonte": "<fonte>",
      "capitoli": [
        {"capitolo": "cap01", "titolo": ..., "testo_path": "app/.source_cache/<fonte>/cap01.txt",
         "modulo_path": "app/seed_data/<fonte>/cap01.py"},
        ...
      ]
    }

`modulo_path` è il path di output assegnato per l'autoria di quel capitolo
(dict RIGHE_OBBLIGHI/RIGHE_PRINCIPI/INDICE_ARTICOLI_LOCALE/MAPPATURA_LOCALE/
RELAZIONI, vedi `app/seed_data/lib.py`) — da passare al subagent come unico
riferimento di output, invece di lasciarglielo scegliere.
"""

import json
import sys
from pathlib import Path

APP_DIR = Path(__file__).parent.parent
SOURCE_CACHE_DIR = APP_DIR / ".source_cache"


def split_source(fonte: str, raw_path: Path, boundaries_path: Path) -> dict:
    testo = raw_path.read_text(encoding="utf-8")
    boundaries = json.loads(boundaries_path.read_text(encoding="utf-8"))
    if not boundaries:
        raise ValueError("boundaries.json vuoto: serve almeno un capitolo")

    posizioni = []
    ricerca_da = 0
    for b in boundaries:
        idx = testo.find(b["marker"], ricerca_da)
        if idx == -1:
            raise ValueError(
                f"marker non trovato (o fuori ordine) per capitolo '{b['capitolo']}': {b['marker']!r}"
            )
        posizioni.append(idx)
        ricerca_da = idx + len(b["marker"])

    out_dir = SOURCE_CACHE_DIR / fonte
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest_capitoli = []
    for i, b in enumerate(boundaries):
        inizio = posizioni[i]
        fine = posizioni[i + 1] if i + 1 < len(boundaries) else len(testo)
        porzione = testo[inizio:fine]

        testo_path = out_dir / f"{b['capitolo']}.txt"
        testo_path.write_text(porzione, encoding="utf-8")

        modulo_path = APP_DIR / "seed_data" / fonte / f"{b['capitolo']}.py"

        manifest_capitoli.append({
            "capitolo": b["capitolo"],
            "titolo": b.get("titolo", ""),
            "testo_path": str(testo_path.relative_to(APP_DIR.parent)),
            "modulo_path": str(modulo_path.relative_to(APP_DIR.parent)),
        })

    manifest = {"fonte": fonte, "capitoli": manifest_capitoli}
    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest


def main() -> None:
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    fonte, raw, boundaries = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    manifest = split_source(fonte, raw, boundaries)
    print(f"OK: {len(manifest['capitoli'])} capitoli scritti in {SOURCE_CACHE_DIR / fonte}")
    for c in manifest["capitoli"]:
        print(f"  {c['capitolo']}: {c['testo_path']} -> {c['modulo_path']}")


if __name__ == "__main__":
    main()
