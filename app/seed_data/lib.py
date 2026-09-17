"""Libreria condivisa per l'import granulare per fonte/capitolo (ADR-0007).

Sostituisce la numerazione manuale degli id usata finora in `app/seed.py`
(ogni riga porta un id intero assegnato a mano, con range espliciti tipo
"eIDAS/eIDAS2: id 1-100, CAD/DPCM: id 101-135" — vedi commenti in `seed.py`)
con una risoluzione simbolica per `riferimento`: ogni riga di un capitolo
dichiara solo il proprio riferimento testuale (es. "art. 24 §2(e)"); l'id
numerico è assegnato da sqlite al momento dell'inserimento (`cursor.lastrowid`)
e tracciato in un registro `(tipo, fonte_id, riferimento) -> id`, usato per
risolvere `obbligo_soggetti`/`principio_oggetti`/`relazioni` sia interne al
capitolo sia cross-capitolo/cross-fonte (es. CAD che rinvia a un articolo
eIDAS già inserito).

Motivo del cambio: la numerazione manuale richiede che ogni modulo capitolo
conosca il range id globale delle altre fonti/capitoli — impossibile da
garantire quando l'autoria è distribuita su subagent paralleli senza farli
comunicare tra loro, ed è la causa strutturale della classe di bug
"collisione tra output di subagent diversi" osservata nell'import eIDAS.
Con id assegnati da sqlite e riferimenti simbolici, due capitoli non possono
mai collidere per costruzione: ciascuno scrive nel proprio file, con nomi di
riferimento propri (unici perché derivano dal testo normativo).

Un modulo capitolo (`app/seed_data/<fonte>/cap0N.py`) espone:

    RIGHE_OBBLIGHI: list[dict]
        Chiavi: riferimento, testo, testo_integrale, tipo_obbligo (nome),
        stato (nome), severita?, sanzioni?, condizione_applicabilita?,
        soggetti?: list[{"categoria": nome, "ruolo": "obbligato"|"destinatario"}]
    RIGHE_PRINCIPI: list[dict]
        Chiavi: riferimento, testo, testo_integrale, tipo_principio (nome),
        stato (nome), condizione_applicabilita?,
        oggetti_giuridici?: list[nome]
    INDICE_ARTICOLI_LOCALE: list[str]
        Item di indice normativo coperti da questo capitolo (sottoinsieme
        del manifest prodotto da `split_source.py`).
    MAPPATURA_LOCALE: dict[str, list[str]]
        riferimento di riga -> lista di item di INDICE_ARTICOLI_LOCALE coperti
        da quella riga (di norma un solo item; più di uno se la riga accorpa
        più commi/lettere in un'unica prescrizione continua).
    RELAZIONI: list[dict]
        {"nodo_da": (tipo, fonte_id_o_None, riferimento),
         "nodo_a": (tipo, fonte_id_o_None, riferimento),
         "tipo_relazione": nome,
         "evidence_type": "textual"|"inferred"|"human-curated" (default "textual"),
         "confidence": float|None (default None)}
        `fonte_id_o_None`: None risolve alla fonte corrente (quella passata a
        `inserisci_capitoli`); un intero esplicito referenzia un'altra fonte
        già inserita in precedenza nello stesso `registro`.
"""

import json
from pathlib import Path

APP_DIR = Path(__file__).parent.parent
SOURCE_CACHE_DIR = APP_DIR / ".source_cache"


def verifica_copertura(indice: list[str], mappatura: dict[str, list[str]]) -> None:
    """Solleva ValueError se `indice` non è coperto da esattamente una riga
    per item (nessun item mancante, nessun item coperto da più righe)."""
    coperti: dict[str, list[str]] = {}
    for riferimento, items in mappatura.items():
        for item in items:
            coperti.setdefault(item, []).append(riferimento)

    mancanti = [item for item in indice if item not in coperti]
    doppi = {item: righe for item, righe in coperti.items() if len(righe) > 1}

    if mancanti or doppi:
        messaggio = []
        if mancanti:
            messaggio.append(f"item non coperti: {mancanti}")
        if doppi:
            messaggio.append(f"item coperti da più righe: {doppi}")
        raise ValueError("verifica_copertura fallita — " + "; ".join(messaggio))


def nome_a_id(conn, tabella: str, id_col: str = "id", nome_col: str = "nome") -> dict[str, int]:
    """Costruisce un lookup nome->id leggendo dal DB in-memory già popolato da
    `seed.py` (fonte di verità unica, evita di duplicare le liste nome/id in
    più moduli Python che possono divergere)."""
    righe = conn.execute(f"SELECT {id_col}, {nome_col} FROM {tabella}").fetchall()
    return {nome: id_ for id_, nome in righe}


def costruisci_lookup(conn) -> dict[str, dict[str, int]]:
    return {
        "tipi_obbligo": nome_a_id(conn, "tipi_obbligo"),
        "tipi_principio": nome_a_id(conn, "tipi_principio"),
        "stati_norma": nome_a_id(conn, "stati_norma"),
        "oggetti_giuridici": nome_a_id(conn, "oggetti_giuridici"),
        "categorie_soggetto": nome_a_id(conn, "categorie_soggetto"),
        "tipi_relazione": nome_a_id(conn, "tipi_relazione"),
    }


def carica_manifest(fonte: str) -> dict:
    """Legge il manifest prodotto da `app/tools/split_source.py` per `fonte`
    (`app/.source_cache/<fonte>/manifest.json`)."""
    path = SOURCE_CACHE_DIR / fonte / "manifest.json"
    if not path.exists():
        raise FileNotFoundError(
            f"manifest non trovato per fonte '{fonte}': {path}. "
            "Eseguire prima app/tools/split_source.py."
        )
    return json.loads(path.read_text(encoding="utf-8"))


def inserisci_capitoli(cursor, fonte_id: int, capitoli: list, lookup: dict, registro: dict) -> dict:
    """Inserisce in ordine deterministico (l'ordine di `capitoli`, tipicamente
    l'ordine del manifest) le righe di una lista di moduli capitolo per una
    fonte, verificando prima la copertura aggregata, poi risolvendo le
    relazioni (incluse cross-fonte) tramite `registro`, aggiornato in-place.

    `capitoli`: lista ordinata di moduli capN già importati dal chiamante
    (l'ordine deve essere deterministico e deciso dal chiamante, non dai
    moduli stessi — evita che l'ordine di merge dipenda da come i subagent
    hanno finito il proprio lavoro).
    """
    indice_totale: list[str] = []
    mappatura_totale: dict[str, list[str]] = {}
    for modulo in capitoli:
        indice_totale += modulo.INDICE_ARTICOLI_LOCALE
        mappatura_totale.update(modulo.MAPPATURA_LOCALE)
    verifica_copertura(indice_totale, mappatura_totale)

    for modulo in capitoli:
        for riga in modulo.RIGHE_OBBLIGHI:
            cursor.execute(
                """INSERT INTO obblighi
                   (fonte_id, riferimento, testo, testo_integrale, tipo_obbligo_id,
                    stato_id, severita, sanzioni, condizione_applicabilita, stato_validazione)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'bozza')""",
                (
                    fonte_id, riga["riferimento"], riga["testo"], riga.get("testo_integrale"),
                    lookup["tipi_obbligo"][riga["tipo_obbligo"]],
                    lookup["stati_norma"][riga["stato"]],
                    riga.get("severita"), riga.get("sanzioni"), riga.get("condizione_applicabilita"),
                ),
            )
            obbligo_id = cursor.lastrowid
            registro[("obbligo", fonte_id, riga["riferimento"])] = obbligo_id
            for soggetto in riga.get("soggetti", []):
                cursor.execute(
                    "INSERT INTO obbligo_soggetti (obbligo_id, categoria_soggetto_id, ruolo) VALUES (?, ?, ?)",
                    (obbligo_id, lookup["categorie_soggetto"][soggetto["categoria"]], soggetto["ruolo"]),
                )

        for riga in modulo.RIGHE_PRINCIPI:
            cursor.execute(
                """INSERT INTO principi
                   (fonte_id, riferimento, testo, testo_integrale, tipo_principio_id,
                    stato_id, condizione_applicabilita, stato_validazione)
                   VALUES (?, ?, ?, ?, ?, ?, ?, 'bozza')""",
                (
                    fonte_id, riga["riferimento"], riga["testo"], riga.get("testo_integrale"),
                    lookup["tipi_principio"][riga["tipo_principio"]],
                    lookup["stati_norma"][riga["stato"]],
                    riga.get("condizione_applicabilita"),
                ),
            )
            principio_id = cursor.lastrowid
            registro[("principio", fonte_id, riga["riferimento"])] = principio_id
            for oggetto in riga.get("oggetti_giuridici", []):
                cursor.execute(
                    "INSERT INTO principio_oggetti (principio_id, oggetto_giuridico_id) VALUES (?, ?)",
                    (principio_id, lookup["oggetti_giuridici"][oggetto]),
                )

    for modulo in capitoli:
        for rel in modulo.RELAZIONI:
            tipo_da, fonte_da, rif_da = rel["nodo_da"]
            tipo_a, fonte_a, rif_a = rel["nodo_a"]
            fonte_da = fonte_id if fonte_da is None else fonte_da
            fonte_a = fonte_id if fonte_a is None else fonte_a
            try:
                nodo_da_id = registro[(tipo_da, fonte_da, rif_da)]
                nodo_a_id = registro[(tipo_a, fonte_a, rif_a)]
            except KeyError as e:
                raise KeyError(
                    f"relazione non risolvibile (fonte_id={fonte_id}): nodo mancante nel registro: {e}"
                ) from e
            cursor.execute(
                """INSERT INTO relazioni
                   (nodo_da_tipo, nodo_da_id, nodo_a_tipo, nodo_a_id, tipo_relazione_id,
                    evidence_type, confidence)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (
                    tipo_da, nodo_da_id, tipo_a, nodo_a_id,
                    lookup["tipi_relazione"][rel["tipo_relazione"]],
                    rel.get("evidence_type", "textual"), rel.get("confidence"),
                ),
            )

    return registro
