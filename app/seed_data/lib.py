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
         "evidence_type": "textual"|"inferred"|"human-curated" (default "inferred":
             va dichiarato "textual" solo se la relazione e' una citazione letterale
             verificata sul testo, mai per inerzia — vedi ADR-0005),
         "confidence": float|None (default None)}
        `fonte_id_o_None`: None risolve alla fonte corrente (quella passata a
        `inserisci_capitoli`); un intero esplicito referenzia un'altra fonte
        già inserita in precedenza nello stesso `registro`.
"""

import json
import re
import sys
from pathlib import Path

if str(Path(__file__).parent.parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).parent.parent))

from neo4j_common import partizioni_di  # noqa: E402

APP_DIR = Path(__file__).parent.parent
SOURCE_CACHE_DIR = APP_DIR / ".source_cache"


def _registra_partizioni(cursor, fonte_id: int, riferimento: str, registro: dict) -> None:
    """Crea, per la fonte in lavorazione, i nodi di partizione a cui appartiene la riga appena
    inserita, e li registra come ('partizione', fonte_id, riferimento) -> id (ADR-0012).

    Idempotente: la partizione gia' creata per un'altra riga della stessa fonte non viene
    duplicata (chiave presente nel registro). Senza catena di partizioni (la riga e' essa
    stessa l'unita' indivisa, o il riferimento non e' strutturato) non fa nulla: e' il caso
    normale delle clausole di primo livello.
    """
    for rif_partizione, tipo in partizioni_di(riferimento):
        chiave = ("partizione", fonte_id, rif_partizione)
        if chiave in registro:
            continue
        cursor.execute(
            "INSERT INTO partizioni (fonte_id, riferimento, tipo_partizione) VALUES (?, ?, ?)",
            (fonte_id, rif_partizione, tipo),
        )
        registro[chiave] = cursor.lastrowid


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


_MARKER_TRONCAMENTO = ("…", "...", "[...]", "[…]")
_OMISSIS_NORMATTIVA = re.compile(r"\(\(\s*\.{3}\s*\)\)")
_ASN1_EXTENSIBILITY = re.compile(r"\|\s*\.\.\.\s*[\)\}]")
# Terza convenzione nota (ETSI TS 119 432 V1.3.1, import 2026-09-24): nei
# blocchi EXAMPLE di quello standard il testo ufficiale abbrevia esso stesso i
# payload (token JWT/Base64, parametri di richiesta HTTP, URL con segnaposto)
# con `...`. L'ellissi e' quindi contenuto autentico, non un'elisione del
# modello. Riconoscerla senza aprire un varco alle troncature di prosa
# richiede tre condizioni strette — dentro una stringa quotata, oppure dopo
# `=`/`{`, oppure incollata a un token che porta cifre o un run maiuscolo: un
# `...` incollato a una parola di prosa (il caso reale di troncamento, es.
# "il prestatore qualificato...") non ricade in nessuna delle tre e resta
# bloccato.
_ELLISSI_IN_STRINGA = re.compile(r'"[^"\n]*\.\.\.[^"\n]*"')
_ELLISSI_SEGNAPOSTO = re.compile(r"[={]\s?\.\.\.")
_ELLISSI_SU_TOKEN = re.compile(
    r"(?=[A-Za-z0-9+/_.\-]{8,}\.\.\.)"
    r"(?:[A-Za-z0-9+/_.\-]*[0-9][A-Za-z0-9+/_.\-]*|[A-Z/+_.\-]{6,})\.\.\."
)
# Quarta convenzione nota (ETSI TS 119 612 V2.4.1, import 2026-09-24): in
# Annex D (registro normativo degli URI) il testo ufficiale abbrevia con
# un'ellissi il radix degli URI registrati, dentro una stringa quotata che
# contiene un URI: "http://uri.etsi.org/19612/……" e
# "http://uri.etsi.org/TrstSvc/……". Condizione ristretta alla stringa quotata
# contenente un radix http/https: un'ellissi di prosa non ha mai questa forma,
# quindi resta bloccata.
_ELLISSI_SU_RADIX_URI = re.compile(r'"[^"\n]*https?://[^"\n]*(?:…+|\.\.\.)[^"\n]*"')
# Quinta convenzione nota (ETSI TS 119 612 V2.4.1, clausola 5.5.3): l'ellissi
# e' usata come segnaposto di segmento dentro un pattern di URI NON quotato
# ("http://uri.etsi.org/TrstSvc/Svctype/.../nothavingPKIid"). Condizione
# ristretta: l'ellissi e' dentro un token contiguo che inizia con http(s)://,
# senza spazi — una prosa con ellissi non ha mai questa forma.
_ELLISSI_IN_URI = re.compile(r'https?://[^\s"\']*(?:…+|\.\.\.)[^\s"\',;)]*')


# Sesta convenzione nota (ETSI EN 319 102-1 V1.4.1, clausola 5.1.3, tabella
# "Reported Validation Information", import 2026-09-28): lo standard abbrevia
# esso stesso un elenco esemplificativo dentro parentesi - "the algorithms that
# have been used in material (e.g. the signature value, a certificate...)".
# Condizione ristretta: l'ellissi sta dentro una parentesi che si apre con
# "e.g." - una troncatura di prosa introdotta in estrazione non ha questa
# forma, e un'ellissi su prosa resta bloccata.
_ELLISSI_IN_PARENTESI_ESEMPLIFICATIVA = re.compile(r"\(e\.g\.[^)\n]*(?:…+|\.\.\.)[^)\n]*\)")


def _senza_omissis_legittimi(testo: str) -> str:
    """Rimuove le convenzioni note in cui `...`/`((...))` sono contenuto
    normativo/tecnico autentico e non un'elisione introdotta in estrazione:
    - Normattiva `((...))`: testo soppresso da una modifica legislativa,
      riportato letteralmente così nel testo ufficiale italiano consolidato;
    - marcatore di estensibilità ASN.1 (`| ...)` / `| ...}`, ITU-T X.680):
      sintassi normativa reale nelle dichiarazioni QC-STATEMENT/SEQUENCE,
      non un'abbreviazione del modello;
    - abbreviazione di payload negli EXAMPLE di ETSI TS 119 432 (vedi
      `_ELLISSI_IN_STRINGA`/`_ELLISSI_SEGNAPOSTO`/`_ELLISSI_SU_TOKEN`);
    - ellissi sul radix degli URI registrati in Annex D di ETSI TS 119 612
      (vedi `_ELLISSI_SU_RADIX_URI`) e segnaposto di segmento dentro un
      pattern di URI non quotato nella clausola 5.5.3 dello stesso documento
      (vedi `_ELLISSI_IN_URI`);
    - elenco esemplificativo abbreviato dallo standard dentro parentesi
      (vedi `_ELLISSI_IN_PARENTESI_ESEMPLIFICATIVA`, ETSI EN 319 102-1)."""
    testo = _OMISSIS_NORMATTIVA.sub("", testo)
    testo = _ASN1_EXTENSIBILITY.sub("", testo)
    testo = _ELLISSI_IN_STRINGA.sub("", testo)
    testo = _ELLISSI_SEGNAPOSTO.sub("", testo)
    testo = _ELLISSI_SU_TOKEN.sub("", testo)
    testo = _ELLISSI_SU_RADIX_URI.sub("", testo)
    testo = _ELLISSI_IN_URI.sub("", testo)
    testo = _ELLISSI_IN_PARENTESI_ESEMPLIFICATIVA.sub("", testo)
    return testo


def verifica_completezza_testo_integrale(capitoli: list) -> None:
    """Solleva ValueError se una riga (Obbligo o Principio) di `capitoli` porta
    in `testo_integrale` un marcatore di elisione (`…`, `...`, `[...]`) —
    segno che l'estrazione ha troncato il testo normativo invece di
    riportarlo per intero, in violazione di ADR-0007/ADR-0010 (copertura
    completa vale anche all'interno di una singola riga, non solo tra
    articoli). Un testo ufficiale verbatim non contiene mai questi
    marcatori salvo le convenzioni note elencate in
    `_senza_omissis_legittimi` (Normattiva `((...))`, estensibilità ASN.1,
    abbreviazione di payload negli EXAMPLE di ETSI TS 119 432, ellissi sul
    radix degli URI registrati in Annex D di ETSI TS 119 612 e segnaposto di
    segmento negli URI della clausola 5.5.3, elenco esemplificativo
    abbreviato dentro parentesi in ETSI EN 319 102-1), escluse a monte: se
    compaiono, sono stati introdotti dal modello in fase di estrazione al
    posto di una porzione di testo reale.

    Chiamata da `inserisci_capitoli` prima di qualunque INSERT, sullo stesso
    modello di `verifica_copertura` — blocca l'intero seed, non solo la riga
    incriminata, perché un troncamento non segnalato non deve mai finire nel
    grafo nemmeno per una singola riga."""
    trovati: list[str] = []
    for modulo in capitoli:
        for riga in list(modulo.RIGHE_OBBLIGHI) + list(modulo.RIGHE_PRINCIPI):
            testo_integrale = _senza_omissis_legittimi(riga.get("testo_integrale") or "")
            if any(marker in testo_integrale for marker in _MARKER_TRONCAMENTO):
                trovati.append(riga["riferimento"])
    if trovati:
        raise ValueError(
            "verifica_completezza_testo_integrale fallita — testo_integrale "
            f"troncato (marcatore di elisione) per: {trovati}. Recuperare il "
            "testo verbatim completo dalla fonte ufficiale, mai abbreviare."
        )

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
    verifica_completezza_testo_integrale(capitoli)

    # Partizioni (ADR-0012): prima di risolvere le relazioni di questa fonte, assicura che
    # esistano nel registro le partizioni di TUTTE le righe già inserite (comprese le Fonti i
    # cui dati stanno inline in seed.py, che non passano da qui): una relazione può avere come
    # estremo la partizione di un articolo di un'altra Fonte. Idempotente.
    registra_partizioni_mancanti(cursor, registro)

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
            _registra_partizioni(cursor, fonte_id, riga["riferimento"], registro)
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
            _registra_partizioni(cursor, fonte_id, riga["riferimento"], registro)
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
                    # Default 'inferred', non 'textual' (cambiato il 2026-09-28): una
                    # relazione la cui provenienza non e' dichiarata dal modulo
                    # capitolo non deve dichiararsi da sola "citazione letterale nel
                    # testo": `textual` e' la classe di evidenza piu' forte del
                    # censimento (ADR-0005) e va attribuita solo quando chi scrive la
                    # relazione l'ha verificata sul testo. Con il default opposto ogni
                    # relazione costruita per costruzione si presentava come citazione
                    # letterale senza esserlo (rilevato da
                    # app/tools/verifica_relazioni_textual.py).
                    rel.get("evidence_type", "inferred"), rel.get("confidence"),
                ),
            )

    return registro


def registra_partizioni_mancanti(cursor, registro: dict) -> int:
    """Crea i nodi di partizione per le righe inserite fuori da `inserisci_capitoli`
    (import storici scritti inline in `seed.py`: eIDAS/eIDAS2, Codice Civile), che non
    passano per `_registra_partizioni`. Idempotente: le partizioni già registrate non
    vengono ricreate. Restituisce il numero di partizioni nuove.

    Serve a garantire che il livello delle partizioni (ADR-0012) copra *tutte* le Fonti,
    indipendentemente da come sono state inserite le loro righe.
    """
    creati = 0
    for tabella in ("obblighi", "principi"):
        righe = cursor.execute(f"SELECT fonte_id, riferimento FROM {tabella}").fetchall()
        for riga in righe:
            prima = len(registro)
            _registra_partizioni(cursor, riga["fonte_id"], riga["riferimento"], registro)
            creati += len(registro) - prima
    return creati
