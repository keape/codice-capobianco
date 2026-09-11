"""Ricerca semantica su compliance-rag via qmd (CLI esterno, modelli locali).

qmd gira interamente in locale (modelli GGUF in cache, nessuna API key verso un servizio LLM
esterno): coerente con ADR-0003 del repo (estrazione LLM solo dentro sessioni Claude Code, mai
batch autonomo con API key propria) — quel vincolo riguarda la generazione delle bozze
Obbligo/Principio, non l'indicizzazione/ricerca locale fatta da qmd.

Wiring:
- `export_qmd.esporta()` scrive un file .md per obbligo/principio in `app/qmd_export/`.
- `sync_qmd()` rilancia l'export e re-indicizza la collection qmd — chiamato ad ogni scrittura
  DB rilevante (valida/rifiuta bozza) e all'avvio di `web_ui.py`: hook automatico, decisione
  esplicita per restare sempre in sync senza comando manuale, a costo di latenza sulla scrittura.
- `ricerca_semantica()` chiama `qmd query` (con reranking, non `vsearch`) in modo sincrono
  dentro la richiesta HTTP: latenza accettata in cambio di risultati migliori, decisione esplicita.
"""

import json
import shutil
import subprocess
from pathlib import Path

import export_qmd

COLLECTION = "compliance-rag"


def _qmd_bin() -> str | None:
    found = shutil.which("qmd")
    if found:
        return found
    fallback = Path.home() / ".nvm/versions/node/v20.20.2/bin/qmd"
    return str(fallback) if fallback.exists() else None


def sync_qmd(timeout: int = 120) -> tuple[bool, str]:
    """Riesporta DB -> markdown e re-indicizza la collection qmd. Non solleva eccezioni."""
    export_qmd.esporta()
    qmd = _qmd_bin()
    if qmd is None:
        return False, "qmd non trovato (né in PATH né nel percorso noto)"
    try:
        aggiunta = subprocess.run(
            [qmd, "collection", "add", str(export_qmd.EXPORT_DIR), "--name", COLLECTION, "--mask", "**/*.md"],
            capture_output=True, text=True, timeout=timeout, check=False,
        )
        if aggiunta.returncode != 0:
            # collection già esistente: re-indicizza invece di ricrearla
            subprocess.run([qmd, "update"], capture_output=True, text=True, timeout=timeout, check=False)
        subprocess.run([qmd, "embed"], capture_output=True, text=True, timeout=timeout, check=False)
    except subprocess.TimeoutExpired:
        return False, "timeout durante la sincronizzazione qmd"
    return True, "ok"


def ricerca_semantica(q: str, n: int = 10, timeout: int = 120) -> tuple[list[dict], str | None]:
    """Esegue `qmd query` sulla collection compliance-rag. Ritorna (risultati, errore)."""
    qmd = _qmd_bin()
    if qmd is None:
        return [], "qmd non installato o non raggiungibile"
    try:
        proc = subprocess.run(
            [qmd, "query", q, "-c", COLLECTION, "--json", "-n", str(n)],
            capture_output=True, text=True, timeout=timeout, check=False,
        )
    except subprocess.TimeoutExpired:
        return [], "timeout durante la ricerca semantica"

    if proc.returncode != 0:
        return [], (proc.stderr or "errore qmd sconosciuto").strip().splitlines()[-1] if proc.stderr else "errore qmd sconosciuto"

    try:
        grezzi = json.loads(proc.stdout or "[]")
    except json.JSONDecodeError:
        return [], "output qmd non interpretabile"

    risultati = []
    for r in grezzi:
        nome_file = Path(r.get("file", "")).name  # es. obbligo-12.md / principio-3.md
        if "-" not in nome_file:
            continue
        tipo, _, resto = nome_file.partition("-")
        if tipo not in ("obbligo", "principio"):
            continue
        try:
            nodo_id = int(resto.removesuffix(".md"))
        except ValueError:
            continue
        risultati.append({"tipo_nodo": tipo, "id": nodo_id, "score": r.get("score"), "snippet": r.get("snippet")})
    return risultati, None
