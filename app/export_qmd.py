"""Export obblighi/principi da censimento.db a markdown per l'indicizzazione qmd (ricerca semantica).

Rigenera `app/qmd_export/*.md` da zero, in modo idempotente: sovrascrive i file esistenti e
rimuove quelli orfani (record cancellati o rifiutati). Include anche le bozze
(`stato_validazione='bozza'`), non solo i record validati — decisione esplicita per dare
copertura di ricerca più ampia (vedi `docs/qmd-semantic-search-spec.md`).

    app/.venv/bin/python app/export_qmd.py
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "censimento.db"
EXPORT_DIR = Path(__file__).parent / "qmd_export"


def _conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _scrivi(path: Path, riferimento, fonte, testo, testo_integrale, stato_validazione):
    path.write_text(
        f"# {riferimento}\n\n"
        f"fonte: {fonte}\n"
        f"stato_validazione: {stato_validazione}\n\n"
        f"## Sintesi\n\n{testo}\n\n"
        f"## Testo integrale\n\n{testo_integrale or 'non disponibile'}\n",
        encoding="utf-8",
    )


def esporta() -> int:
    """Rigenera l'export. Ritorna il numero di file scritti."""
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    attesi = set()
    with _conn() as conn:
        fonti = {r["id"]: r["nome"] for r in conn.execute("SELECT id, nome FROM fonti")}
        for r in conn.execute("SELECT * FROM obblighi"):
            nome = f"obbligo-{r['id']}.md"
            _scrivi(EXPORT_DIR / nome, r["riferimento"], fonti.get(r["fonte_id"], "?"),
                    r["testo"], r["testo_integrale"], r["stato_validazione"])
            attesi.add(nome)
        for r in conn.execute("SELECT * FROM principi"):
            nome = f"principio-{r['id']}.md"
            _scrivi(EXPORT_DIR / nome, r["riferimento"], fonti.get(r["fonte_id"], "?"),
                    r["testo"], r["testo_integrale"], r["stato_validazione"])
            attesi.add(nome)

    for f in EXPORT_DIR.glob("*.md"):
        if f.name not in attesi:
            f.unlink()

    return len(attesi)


if __name__ == "__main__":
    n = esporta()
    print(f"Esportati {n} record in {EXPORT_DIR}")
