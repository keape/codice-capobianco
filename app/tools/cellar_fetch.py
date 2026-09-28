"""Fetch deterministico del testo ufficiale in italiano di un atto UE dal
CELLAR (Ufficio delle pubblicazioni dell'Unione europea) e conversione in
testo piano per `app/.source_cache/<slug>/raw.txt`.

Perche' esiste: il passo 1 di `docs/procedura-import-granulare.md` richiede di
salvare una volta sola il testo ufficiale della fonte da importare, e i
precedenti import di atti UE (Reg. 2025/1566, Reg. 2015/1502) lo avevano
fatto con una fetch manuale la cui provenienza restava in un commento. Un
comando riproducibile rende la provenienza verificabile: stessa richiesta,
stesso atto, stesso hash.

Perche' CELLAR e non l'interfaccia web di EUR-Lex: le pagine
`eur-lex.europa.eu/legal-content/...` rispondono a una fetch non
interattiva con una challenge JavaScript (AWS WAF) e non sono leggibili in
modo automatico. Il servizio di content negotiation del CELLAR
(`publications.europa.eu/resource/celex/<CELEX>`) restituisce invece lo
stesso testo ufficiale della Gazzetta ufficiale in XHTML, selezionando la
lingua con l'header `Accept-Language` (`ita` = italiano).

Uso:

    app/.venv/bin/python app/tools/cellar_fetch.py <CELEX> <slug> [--pdf]

`CELEX`: identificativo dell'atto, nella forma usata dal CELLAR senza
prefisso numerico di settore, es. `32025R1567`, `32025R1569`,
`32015R1502`. `--pdf` accetta invece il PDF ufficiale (utile solo quando
l'XHTML risulti inutilizzabile; il percorso predefinito e' l'XHTML).

Scrive in `app/.source_cache/<slug>/`:
- `raw.txt`        testo piano (una riga per paragrafo/comma, celle della
                   stessa riga di tabella unite da spazio: nei testi OJ la
                   numerazione di commi/considerando sta in una colonna
                   separata, e la sua associazione al testo va preservata);
- `provenance.json` URL CELLAR risolto, lingua richiesta, CELEX, data di
  fetch, dimensione in byte, sha256 di `raw.txt`.

La cartella `.source_cache` e' gitignorata: `provenance.json` serve alla
sessione di import (da riportare nel docstring del modulo capitolo), non al
repository. Il testo ufficiale non va mai incollato inline nei prompt dei
subagent: si passa `local://<testo_path>` (vedi `app/tools/split_source.py`).
"""

import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
CACHE_DIR = APP_DIR / ".source_cache"
CELLAR_URL = "http://publications.europa.eu/resource/celex/{}"
LINGUA = "ita"

_XHTML_ACCEPT = "application/xhtml+xml"
_PDF_ACCEPT = "application/pdf"


def _fetch(celex: str, accept: str, lingua: str) -> tuple[bytes, str]:
    richiesta = urllib.request.Request(
        CELLAR_URL.format(celex),
        headers={
            "Accept-Language": lingua,
            "Accept": accept,
            "User-Agent": "codice-capobianco/1.0 (import granulare fonti normative)",
        },
    )
    try:
        with urllib.request.urlopen(richiesta, timeout=90) as risposta:
            return risposta.read(), risposta.geturl()
    except urllib.error.HTTPError as errore:
        dettaglio = errore.read().decode("utf-8", errors="replace")[:400]
        raise SystemExit(
            f"fetch fallita per CELEX {celex} (HTTP {errore.code}).\n"
            f"Risposta del servizio: {dettaglio}\n"
            "Verificare che il CELEX esista e che la lingua sia disponibile "
            f"(Accept-Language: {lingua})."
        ) from errore


def _xhtml_a_testo(xhtml: str) -> str:
    """Converte l'XHTML OJ del CELLAR in testo piano.

    Regole di conversione (ricavate dalla struttura `oj-*` dei documenti della
    Gazzetta ufficiale, verificata sulle fonti gia' importate):
    - `</td>`/`</th>` -> spazio: nei testi OJ la numerazione di commi e
      considerando occupa una colonna a se' della stessa riga di tabella, e
      l'associazione numero-testo va conservata sulla stessa riga;
    - `</tr>`, `</p>`, `<br/>`, `</div>`, `</h*>` e `<hr/>` -> a capo;
    - il blocco `<head>` (che contiene il nome file della Gazzetta) e' escluso.
    """
    testo = re.sub(r"<head\b.*?</head>", "", xhtml, flags=re.S | re.I)
    testo = re.sub(r"<(script|style)\b.*?</\1>", "", testo, flags=re.S | re.I)
    testo = re.sub(r"</t[dh]>", " ", testo, flags=re.I)
    testo = re.sub(r"<br\s*/?>|</tr>|</p>|</div>|</h[1-6]>|<hr\b[^>]*/>", "\n", testo, flags=re.I)
    testo = re.sub(r"<[^>]+>", "", testo)
    testo = unescape(testo)
    testo = testo.replace("\u00a0", " ").replace("\u2019", "'")
    testo = re.sub(r"[ \t]+", " ", testo)
    testo = re.sub(r" *\n *", "\n", testo)
    testo = re.sub(r"\n{3,}", "\n\n", testo)
    return testo.strip()


def main(argv: list[str]) -> int:
    argomenti = [a for a in argv[1:] if not a.startswith("--")]
    usa_pdf = "--pdf" in argv[1:]
    if len(argomenti) != 2:
        print(__doc__.strip().split("Uso:")[1].split("\n\n")[0].strip())
        return 2
    celex, slug = argomenti

    accettato = _PDF_ACCEPT if usa_pdf else _XHTML_ACCEPT
    contenuto, url_risolto = _fetch(celex, accettato, LINGUA)

    if usa_pdf:
        raise SystemExit(
            "il percorso --pdf scarica il PDF ufficiale in raw.pdf ma non lo "
            "converte: eseguire `pdftotext -layout raw.pdf raw.txt` (stesso "
            "criterio gia' usato per ETSI TS 119 612), poi ripetere senza --pdf "
            "per registrare la provenienza del testo."
        )

    testo = _xhtml_a_testo(contenuto.decode("utf-8", errors="replace"))
    if len(testo) < 1500:
        raise SystemExit(
            f"testo estratto sospetto: {len(testo)} caratteri. Verificare il CELEX "
            f"e l'URL risolto ({url_risolto}) prima di usarlo come fonte."
        )

    destinazione = CACHE_DIR / slug
    destinazione.mkdir(parents=True, exist_ok=True)
    percorso_raw = destinazione / "raw.txt"
    percorso_raw.write_text(testo, encoding="utf-8")

    provenienza = {
        "celex": celex,
        "lingua": LINGUA,
        "url_richiesto": CELLAR_URL.format(celex),
        "url_risolto": url_risolto,
        "formato": "XHTML (Gazzetta ufficiale, content negotiation CELLAR)",
        "data_fetch_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "byte_scaricati": len(contenuto),
        "caratteri_testo": len(testo),
        "sha256_raw_txt": hashlib.sha256(testo.encode("utf-8")).hexdigest(),
        "output": str(percorso_raw.relative_to(APP_DIR.parent)),
    }
    (destinazione / "provenance.json").write_text(
        json.dumps(provenienza, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(f"OK  {celex} -> {provenienza['output']}")
    print(f"    {len(testo)} caratteri, sha256 {provenienza['sha256_raw_txt'][:16]}…")
    print(f"    url risolto: {url_risolto}")
    print("    prima riga: " + testo.splitlines()[0][:120])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
