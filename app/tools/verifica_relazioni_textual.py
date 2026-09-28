"""Audit delle relazioni dichiarate `evidence_type='textual'`.

Perche' esiste. Nel grafo ogni arco porta `evidence_type` (ADR-0005): `textual`
significa "la relazione e' esplicita nel testo normativo, es. un rinvio
letterale". E' la classe di evidenza piu' forte che il censimento sappia
produrre, ed e' anche quella che puo' sbagliare nel modo peggiore: un
`riferimento` mappato male produce un arco che *sembra* una citazione letterale
senza esserlo, e nessuna guardia se ne accorge (le guardie verificano la
copertura e la completezza del testo, non la veridicita' degli archi). L'errore
si scopre solo rileggendo il testo, ed e' esattamente quello che questo script
meccanizza.

Cosa verifica.

  A. GATE — relazioni di tipo `richiama` e `attua` dichiarate `textual`: nel
     `testo_integrale` del nodo citante deve comparire almeno una *traccia* del
     `riferimento` del nodo citato (un id di requisito, un articolo con
     l'ordinale, una clausola o un annesso). Se non compare nulla, l'arco va
     riletto a mano: puo' essere un rinvio citato in una forma diversa (es. nel
     preambolo, che non e' nel `testo_integrale`) o un aggancio sbagliato.
     Sono esclusi dal gate i nodi citanti privi di `testo_integrale` (nessuna
     prova testuale disponibile) e le relazioni `richiama` verso la clausola di
     ambito di uno standard, che per costruzione sono rinvii generici.

  B. INFORMATIVO — le altre relazioni `textual` (`modifica`, `si sovrappone a`,
     `specifica`, `definisce`, ...): la loro evidenza e' il *contenuto*, non un
     id, quindi non sono verificabili meccanicamente. Vengono elencate con il
     bersaglio e con l'indicazione se il testo del nodo citante nomina almeno
     la *fonte* controparte: quelle che non la nominano sono le piu' esposte a
     revisione (tipico: gli adeguamenti di un atto che integra una clausola di
     uno standard citandone solo il numero di clausola).

Uso:

    app/.venv/bin/python app/tools/verifica_relazioni_textual.py [--fonte-id N] [--tutto]

Senza `--tutto` stampa solo i casi da esaminare. Esce con 1 se la sezione A non
e' vuota (utilizzabile come gate prima di un commit di import).
"""

import argparse
import re
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from neo4j_common import get_database, get_driver  # noqa: E402

TIPI_CON_CITAZIONE = ("richiama", "attua")
SINONIMI = {
    "clausola": ("clausola", "clause"),
    "clausole": ("clausola", "clausole", "clause", "clauses"),
    "articolo": ("articolo", "art.", "art", "article"),
    "allegato": ("allegato", "annex"),
    "annex": ("annex", "allegato"),
    "punto": ("punto", "point", "clause", "clausola"),
}


def normalizza(testo: str) -> str:
    testo = (testo or "").lower()
    testo = testo.replace("’", "'").replace("§", " § ")
    testo = re.sub(r"[\u00ad\u00a0]", " ", testo)
    testo = re.sub(r"\s+", " ", testo)
    return testo


def tracce(riferimento: str) -> list[str]:
    """Sottostringhe distintive del riferimento citato, cercabili nel testo del
    nodo citante. Ritorna la lista delle tracce possibili (basta che una ci
    sia)."""
    rif = normalizza(riferimento)
    trovate = []

    # id di requisito/controllo: REQ-7.8-13, OVR-6.4.4-02, SCP 13, GSM 1.4, UI 1, TIS-7.6.2-05
    for id_req in re.findall(r"\b[a-z]{2,4}[ \-]\d+(?:\.\d+)*[a-z]?\b", rif):
        trovate.append(id_req.replace("-", " ").replace("  ", " ").strip())
        trovate.append(id_req)

    # articoli con eventuale ordinale latino: art. 45 sexies, art. 3-bis
    for art in re.findall(
        r"\bart\.?\s*(\d+(?:\s?-\s?(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies|undecies|duodecies|terdecies))?)",
        rif,
    ):
        trovate.append(art.strip())
    # paragrafi in forma romana ("§ 2") o italiana ("c.2", "comma 2", "c. 2-bis")
    for par in re.findall(r"§\s*(\d+(?:[ \-]?(?:bis|ter|quater|quinquies|sexies|septies|octies))?)", rif):
        trovate.append(f"paragrafo {par}")
        trovate.append(f"§ {par}")
    for comma in re.findall(r"\bc\.\s*(\d+(?:[ \-]?(?:bis|ter|quater|quinquies|sexies|septies|octies))?)", rif):
        trovate.append(f"comma {comma}")
        trovate.append(f"c.{comma}")
        trovate.append(f"c. {comma}")
    for comma in re.findall(r"\bcomma\s*(\d+)", rif):
        trovate.append(f"comma {comma}")

    # clausole e annessi: clausola 5.4.2, annex a.7.3
    for cl in re.findall(r"\bclausol[ae]\s+(\d+(?:\.\d+)*)", rif):
        trovate.append(f"clausola {cl}")
        trovate.append(f"clause {cl}")
    for ann in re.findall(r"\bannex\s+([a-z](?:\.\d+(?:\.\d+)*)?)", rif):
        trovate.append(f"annex {ann}")
    for allg in re.findall(r"\ballegato\s+([a-z0-9](?:\.\d+)*)", rif):
        trovate.append(f"allegato {allg}")
        trovate.append(f"allegato {allg.upper()}")

    # "punto N" e "punto 3(a)": negli atti di esecuzione il punto e' chiave
    for punto in re.findall(r"\bpunto\s+(\d+)", rif):
        trovate.append(f"punto {punto}")
    for lettera in re.findall(r"punto\s+\d+\(([a-z])\)", rif):
        trovate.append(f"{lettera})")

    # riferimenti a numeri di atto (2015/1502) e a sigle di standard (319 401)
    for num in re.findall(r"\b(\d{4})/(\d{2,4})\b", rif):
        trovate.append(f"{num[0]}/{num[1]}")
    for etsi in re.findall(r"\b(\d{3}\s?\d{3}(?:-\d)?)\b", rif):
        trovate.append(etsi)

    return sorted({t for t in trovate if len(t) >= 2})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fonte-id", type=int, default=None, help="limita ai nodi citanti di questa Fonte")
    parser.add_argument("--tutto", action="store_true", help="stampa anche l'elenco informativo completo")
    args = parser.parse_args()

    driver = get_driver()
    with driver.session(database=get_database()) as sessione:
        query = (
            "MATCH (a)-[r]->(b) "
            "WHERE r.tipo_relazione IS NOT NULL AND r.evidence_type = 'textual' "
            "AND a.riferimento IS NOT NULL AND b.riferimento IS NOT NULL "
        )
        if args.fonte_id is not None:
            query += f"AND a.fonte_id = {args.fonte_id} "
        query += (
            "RETURN labels(a)[0] AS tipo_da, a.fonte_id AS fonte_da, a.riferimento AS rif_da, "
            "a.testo_integrale AS testo_da, labels(b)[0] AS tipo_a, b.fonte_id AS fonte_a, "
            "b.riferimento AS rif_a, b.testo_integrale AS testo_a, r.tipo_relazione AS tipo "
            "ORDER BY fonte_da, rif_da"
        )
        righe = sessione.run(query).data()
    driver.close()

    da_esaminare = []
    informative = []
    for riga in righe:
        testo = normalizza(riga["testo_da"])
        if not testo:
            continue
        rif_a = riga["rif_a"]
        trovate = tracce(rif_a)
        presente = next((t for t in trovate if t in testo), None) if trovate else None
        if riga["tipo"] in TIPI_CON_CITAZIONE:
            generico = rif_a.lower().endswith("(scope)") or rif_a.lower().startswith("clausola 1 (")
            if presente is None and not generico and trovate:
                da_esaminare.append((riga, trovate))
        else:
            # la fonte controparte e' nominata nel testo citante?
            fonte_citata = None
            for sigla in re.findall(r"et[ ]?si[ ]?(?:en|ts|tr)?[ ]?\d{3}[ ]?\d{3}", normalizza(riga["testo_da"])):
                fonte_citata = sigla
            informative.append((riga, bool(fonte_citata)))

    print(f"relazioni textual esaminate: {len(righe)}")
    print()
    print(f"A. GATE — citazioni dichiarate senza traccia del riferimento citato: {len(da_esaminare)}")
    for riga, trovate in da_esaminare:
        print(f"   f{riga['fonte_da']} {riga['rif_da'][:55]:<55} --{riga['tipo']}--> f{riga['fonte_a']} {riga['rif_a'][:45]}")
        print(f"        tracce cercate: {trovate[:6]}")
    print()
    if args.tutto:
        senza_nome = [r for r, nominata in informative if not nominata]
        print(f"B. INFORMATIVO — altre relazioni textual, di cui {len(senza_nome)} senza menzione della fonte controparte:")
        for riga, nominata in informative:
            if nominata and not args.tutto:
                continue
            flag = "fonte controparte NON nominata" if not nominata else "fonte nominata"
            print(f"   f{riga['fonte_da']} {riga['rif_da'][:45]:<45} --{riga['tipo']}--> f{riga['fonte_a']} {riga['rif_a'][:40]}  [{flag}]")
    else:
        nominate = sum(1 for _, nominata in informative if nominata)
        print(f"B. INFORMATIVO — altre relazioni textual: {len(informative)} "
              f"({nominate} nominano la fonte controparte, {len(informative) - nominate} no; usa --tutto per l'elenco)")
    return 1 if da_esaminare else 0


if __name__ == "__main__":
    sys.exit(main())
