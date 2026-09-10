Type: grilling
Status: resolved

## Question

Definire lo schema concreto delle tabelle SQLite (`fonti`, `obblighi`, `relazioni`, e le tabelle di supporto necessarie per le categorie di soggetto multi-valore su soggetto obbligato/destinatario) coerente con il modello di dominio in CONTEXT.md, e l'interfaccia di accesso a grafo astratta che le incapsula (ADR-0002) — almeno le operazioni "vicini di un nodo per tipo di relazione" e "cammino tra due nodi fino a N salti". Includere come si rappresenta la natura multi-valore di soggetto obbligato/destinatario (es. tabella di giunzione) e il campo di condizione di applicabilità in testo libero.

## Answer

Deciso tramite grilling l'8/9/2026.

### Decisioni chiave

- **ID**: `INTEGER PRIMARY KEY` (autoincrement nativo SQLite) per tutte le tabelle — pilota locale mono-utente, nessuna sincronizzazione multi-istanza da supportare ora.
- **Enumerazioni**: tutte tramite tabelle di lookup dedicate (non `CHECK` inline), per poter aggiungere/rinominare valori senza migrazioni di schema: `stati_fonte`, `stati_obbligo`, `tipi_obbligo`, `categorie_soggetto`, `tipi_relazione` (quest'ultima porta anche `nome_inverso`, es. "sostituisce" / "è sostituito da").
- **Soggetto obbligato/destinatario**: un'unica tabella di giunzione `obbligo_soggetti` con colonna discriminante `ruolo`, non due tabelle separate — riflette che CONTEXT.md tratta i due ruoli come attributi indipendenti dello stesso concetto (categoria di soggetto), non entità distinte.
- **Relazioni**: direzionali, una riga per fatto (non due righe per ogni coppia sostituisce/è-sostituito-da) — la direzione e il nome inverso si risolvono a livello di interfaccia a grafo, non duplicando dati.
- **Condizione di applicabilità**: colonna `TEXT NULL` in chiaro su `obblighi`, come da modello di dominio (testo libero su un fatto esterno non tracciato, distinta dalla relazione tipizzata "è condizionato da").
- **Stato di validazione bozza**: colonna esplicita `stato_validazione` (`bozza` / `validato` / `rifiutato`), indipendente da `validato_da`/`data_validazione`. Le bozze rifiutate vengono **eliminate** dalla tabella (nessuna traccia storica di scarto).
- **Cascade**: `obbligo_soggetti` → `ON DELETE CASCADE` da `obblighi` (sono puri attributi dell'obbligo). `relazioni` → `ON DELETE RESTRICT` verso `obblighi` (una relazione coinvolge due nodi; l'eliminazione di un obbligo collegato deve essere esplicita, non silenziosamente propagata).
- **Stack**: Python, coerente con `sgsi-rag`. Accesso dati con `sqlite3` stdlib e SQL esplicito (niente ORM: l'interfaccia a grafo è già il livello di astrazione voluto da ADR-0002, un ORM sotto sarebbe un'astrazione ridondante).
- **Interfaccia a grafo**: metodi tipizzati che restituiscono `dataclass` (non `sqlite3.Row`/dict grezzi), per non far trapelare i nomi di colonna oltre il confine dell'interfaccia.
  - `vicini(nodo_id, tipo_relazione=None, direzione='entrambe') -> list[VicinoConRelazione]` — `direzione` ∈ `{'uscenti', 'entranti', 'entrambe'}`.
  - `cammino(nodo_da_id, nodo_a_id, max_salti) -> Cammino | None` — solo il cammino più corto entro N salti, via `WITH RECURSIVE` calcolata al volo (nessuna tabella di chiusura transitiva precalcolata: ottimizzazione prematura alla scala del pilota).

### Schema DDL

```sql
-- Lookup: stato di una Fonte
CREATE TABLE stati_fonte (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE  -- 'vigente', 'abrogata', 'in transizione'
);

-- Lookup: stato/validità temporale di un Obbligo
CREATE TABLE stati_obbligo (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE  -- 'vigente', 'abrogato', 'in transizione eIDAS->eIDAS2'
);

-- Lookup: tipo di Obbligo
CREATE TABLE tipi_obbligo (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE  -- 'organizzativo', 'tecnico/sicurezza', 'informativo/trasparenza',
                                -- 'procedurale', 'di conservazione', 'sanzionatorio', ...
);

-- Lookup: categorie di soggetto (condivisa tra ruolo obbligato e destinatario)
CREATE TABLE categorie_soggetto (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE  -- 'QTSP/gestore', 'Utente/titolare', 'Terza parte', 'Terzi affidanti/pubblico'
);

-- Lookup: tipi di relazione tipizzata tra Obblighi (direzionale, con nome inverso)
CREATE TABLE tipi_relazione (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE,          -- es. 'sostituisce'
    nome_inverso TEXT NOT NULL          -- es. 'è sostituito da'
);

-- Fonte normativa
CREATE TABLE fonti (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    url_sorgente TEXT NOT NULL,
    versione TEXT,
    data_entrata_vigore TEXT,           -- ISO 8601
    stato_id INTEGER NOT NULL REFERENCES stati_fonte(id)
);

-- Obbligo (= Requisito)
CREATE TABLE obblighi (
    id INTEGER PRIMARY KEY,
    fonte_id INTEGER NOT NULL REFERENCES fonti(id),
    riferimento TEXT NOT NULL,          -- articolo/comma/allegato all'interno della Fonte
    testo TEXT NOT NULL,
    tipo_obbligo_id INTEGER NOT NULL REFERENCES tipi_obbligo(id),
    stato_id INTEGER NOT NULL REFERENCES stati_obbligo(id),
    severita TEXT,                      -- scala qualitativa
    sanzioni TEXT,                      -- tipo e riferimento normativo della sanzione, se presente
    condizione_applicabilita TEXT,      -- testo libero, fatto esterno non tracciato nel censimento
    stato_validazione TEXT NOT NULL DEFAULT 'bozza'
        CHECK (stato_validazione IN ('bozza', 'validato', 'rifiutato')),
    validato_da TEXT,
    data_validazione TEXT               -- ISO 8601
);

-- Giunzione multi-valore: soggetto obbligato / destinatario (attributi indipendenti, stesso dominio di valori)
CREATE TABLE obbligo_soggetti (
    obbligo_id INTEGER NOT NULL REFERENCES obblighi(id) ON DELETE CASCADE,
    categoria_soggetto_id INTEGER NOT NULL REFERENCES categorie_soggetto(id),
    ruolo TEXT NOT NULL CHECK (ruolo IN ('obbligato', 'destinatario')),
    PRIMARY KEY (obbligo_id, categoria_soggetto_id, ruolo)
);

-- Relazioni tipizzate tra Obblighi (direzionali, una riga per fatto)
CREATE TABLE relazioni (
    id INTEGER PRIMARY KEY,
    obbligo_da_id INTEGER NOT NULL REFERENCES obblighi(id) ON DELETE RESTRICT,
    obbligo_a_id INTEGER NOT NULL REFERENCES obblighi(id) ON DELETE RESTRICT,
    tipo_relazione_id INTEGER NOT NULL REFERENCES tipi_relazione(id)
);

CREATE INDEX idx_obblighi_fonte ON obblighi(fonte_id);
CREATE INDEX idx_obbligo_soggetti_obbligo ON obbligo_soggetti(obbligo_id);
CREATE INDEX idx_relazioni_da ON relazioni(obbligo_da_id);
CREATE INDEX idx_relazioni_a ON relazioni(obbligo_a_id);
```

### Interfaccia a grafo (Python, `sqlite3` stdlib)

```python
from dataclasses import dataclass
from typing import Literal

Direzione = Literal["uscenti", "entranti", "entrambe"]

@dataclass
class VicinoConRelazione:
    obbligo_id: int
    tipo_relazione: str      # nome nella direzione osservata (nome o nome_inverso)
    relazione_id: int

@dataclass
class PassoCammino:
    obbligo_id: int
    tipo_relazione: str
    relazione_id: int

@dataclass
class Cammino:
    passi: list[PassoCammino]  # sequenza da nodo_da a nodo_a, esclusi il nodo di partenza

class InterfacciaGrafo:
    def __init__(self, connessione: "sqlite3.Connection"): ...

    def vicini(
        self,
        nodo_id: int,
        tipo_relazione: str | None = None,
        direzione: Direzione = "entrambe",
    ) -> list[VicinoConRelazione]: ...

    def cammino(
        self,
        nodo_da_id: int,
        nodo_a_id: int,
        max_salti: int,
    ) -> Cammino | None:
        """Cammino più corto entro max_salti, via WITH RECURSIVE calcolata al volo.
        None se non esiste alcun cammino entro il limite di salti."""
        ...
```

`vicini` con `direzione='uscenti'` filtra su `obbligo_da_id = nodo_id` e restituisce `tipo_relazione` = `tipi_relazione.nome`; con `direzione='entranti'` filtra su `obbligo_a_id = nodo_id` e restituisce `tipi_relazione.nome_inverso`; con `'entrambe'` unisce i due risultati.
