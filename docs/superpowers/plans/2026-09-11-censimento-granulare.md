# Censimento granulare per articolo/comma Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Sostituire l'import accorpato di `app/seed.py` con un'estrazione granulare (una riga = una unità di prescrizione distinta) per tutte e 4 le fonti (eIDAS, eIDAS2, CAD, DPCM 22/2/2013), con verifica di copertura automatica e relazioni evidenti create nella stessa passata.

**Architecture:** `app/seed.py` diventa un orchestratore che importa 4 moduli dati (`app/seed_data/eidas.py`, `eidas2.py`, `cad.py`, `dpcm.py`), esegue `verifica_copertura` per ciascuno (blocca se un item dell'indice normativo non è coperto da esattamente una riga), poi `inserisci_fonte` (insert righe, poi risoluzione+insert relazioni via un registro riferimento→id costruito durante l'inserimento).

**Tech Stack:** Python 3.14, sqlite3 (stdlib), nessuna libreria esterna, nessun framework di test (repo non ne ha).

**Spec:** [docs/superpowers/specs/2026-09-11-censimento-granulare-design.md](../specs/2026-09-11-censimento-granulare-design.md)

## Global Constraints

- Nessun accorpamento di default: una riga copre una unità di prescrizione distinta (può stare sotto o sopra il livello di comma, spec sezione "Decisioni di design", punto 1).
- Nessuna nuova categoria di nodo pre-decisa: resta Obbligo/Principio salvo necessità emersa caso per caso durante l'autoria di una fonte.
- Tutte e 4 le fonti vanno riscritte in questo lavoro (non solo DPCM).
- Le relazioni evidenti vanno create nella stessa passata di autoria di ciascuna fonte, non rimandate.
- Si riparte da zero: nessuna migrazione delle validazioni umane pregresse sulle righe accorpate.
- Nessuna modifica a `app/schema.sql`.
- Niente pytest/framework di test nuovo (fuori scope, spec sezione "Fuori scope").
- Gli id di `obblighi`/`principi` sono autoincrement DB: nessun id esplicito nei moduli dati.
- Ordine di inserimento fonti fissato: eIDAS → eIDAS2 → CAD → DPCM.

---

## Nota sui task di autoria contenuto (Task 3-6)

I Task 3-6 producono un modulo dati per fonte il cui contenuto (indice articoli, testo di sintesi, `testo_integrale`, relazioni) va scritto leggendo il testo normativo ufficiale in una sessione Claude Code interattiva (ADR-0003) — non può essere pre-scritto qui, sia perché il testo va verificato/parafrasato dal documento ufficiale al momento (non da un pre-scritto potenzialmente disallineato), sia perché è un lavoro di trascrizione/sintesi normativa lungo migliaia di righe, non logica applicativa. Questi task specificano quindi la procedura esatta (dove leggere il testo, come costruire l'indice, come verificarlo, come iterare fino al pass) e i vincoli strutturali esatti (forma del dict Python), non il contenuto legale finale.

---

## Task 1: Scaffold di `verifica_copertura` e `inserisci_fonte`

**Files:**
- Modify: `app/seed.py` (aggiungere funzioni, non toccare ancora le sezioni fonti/obblighi/principi esistenti)

**Interfaces:**
- Produce: `verifica_copertura(indice: list[str], mappatura: dict[str, list[str]]) -> None` — solleva `ValueError` se copertura non torna.
- Produce: `Registro = dict[tuple[str, int, str], int]` — chiave `(tipo, fonte_id, riferimento)` → id riga inserita.
- Produce: `inserisci_fonte(conn, cursor, fonte_id: int, modulo, lookup: dict, registro: Registro) -> None` — inserisce `RIGHE_OBBLIGHI`, `RIGHE_PRINCIPI`, poi risolve e inserisce `RELAZIONI` del modulo, aggiornando `registro` in-place.
- Consuma: `lookup` = dict con chiavi `"tipi_obbligo"`, `"stati_norma"`, `"tipi_principio"`, `"oggetti_giuridici"`, `"categorie_soggetto"`, `"tipi_relazione"`, ciascuna un dict nome→id (già presenti come liste in `seed.py`, oggi inserite come tuple con id espliciti — qui serve anche il dict nome→id per la risoluzione).

- [ ] **Step 1: Aggiungere `verifica_copertura` a `app/seed.py`**

Aggiungere in cima al file, dopo gli import esistenti:

```python
def verifica_copertura(indice: list[str], mappatura: dict[str, list[str]]) -> None:
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
```

- [ ] **Step 2: Verificare a mano il caso di fallimento**

Eseguire da terminale, dalla cartella `app/`:

```bash
app/.venv/bin/python -c "
from seed import verifica_copertura
try:
    verifica_copertura(['a', 'b', 'c'], {'r1': ['a', 'b']})
    print('ERRORE: doveva sollevare ValueError')
except ValueError as e:
    print('OK:', e)
"
```

Expected: stampa `OK: verifica_copertura fallita — item non coperti: ['c']`.

- [ ] **Step 3: Verificare a mano il caso doppio**

```bash
app/.venv/bin/python -c "
from seed import verifica_copertura
try:
    verifica_copertura(['a', 'b'], {'r1': ['a', 'b'], 'r2': ['a']})
    print('ERRORE: doveva sollevare ValueError')
except ValueError as e:
    print('OK:', e)
"
```

Expected: stampa `OK: verifica_copertura fallita — item coperti da più righe: {'a': ['r1', 'r2']}`.

- [ ] **Step 4: Verificare a mano il caso di successo**

```bash
app/.venv/bin/python -c "
from seed import verifica_copertura
verifica_copertura(['a', 'b'], {'r1': ['a'], 'r2': ['b']})
print('OK: nessuna eccezione')
"
```

Expected: stampa `OK: nessuna eccezione`.

- [ ] **Step 5: Aggiungere `inserisci_fonte` a `app/seed.py`**

Aggiungere subito dopo `verifica_copertura`:

```python
def inserisci_fonte(conn, cursor, fonte_id, modulo, lookup, registro):
    verifica_copertura(modulo.INDICE_ARTICOLI, modulo.MAPPATURA)

    for riga in modulo.RIGHE_OBBLIGHI:
        cursor.execute(
            """INSERT INTO obblighi
               (fonte_id, riferimento, testo, testo_integrale, tipo_obbligo_id,
                stato_id, severita, sanzioni, condizione_applicabilita)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
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
                stato_id, condizione_applicabilita)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
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

    for rel in modulo.RELAZIONI:
        tipo_da, fonte_da, rif_da = rel["nodo_da"]
        tipo_a, fonte_a, rif_a = rel["nodo_a"]
        try:
            nodo_da_id = registro[(tipo_da, fonte_da, rif_da)]
            nodo_a_id = registro[(tipo_a, fonte_a, rif_a)]
        except KeyError as e:
            raise KeyError(f"relazione non risolvibile, nodo mancante nel registro: {e}") from e
        cursor.execute(
            """INSERT INTO relazioni (nodo_da_tipo, nodo_da_id, nodo_a_tipo, nodo_a_id, tipo_relazione_id)
               VALUES (?, ?, ?, ?, ?)""",
            (tipo_da, nodo_da_id, tipo_a, nodo_a_id, lookup["tipi_relazione"][rel["tipo_relazione"]]),
        )

    conn.commit()
```

- [ ] **Step 6: Verificare `inserisci_fonte` con un modulo fittizio**

Creare un file temporaneo nello scratchpad di sessione (non nel repo), es. `/tmp` o lo scratchpad indicato dall'ambiente, per un modulo fittizio e testarlo:

```bash
cat > /tmp/_fonte_fittizia.py <<'EOF'
RIGHE_OBBLIGHI = [
    {"riferimento": "art.1 c.1", "testo": "test", "testo_integrale": "test integrale",
     "tipo_obbligo": "organizzativo", "stato": "vigente",
     "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}]},
]
RIGHE_PRINCIPI = [
    {"riferimento": "art.2 c.1", "testo": "principio test", "testo_integrale": None,
     "tipo_principio": "altro", "stato": "vigente", "oggetti_giuridici": ["altro"]},
]
INDICE_ARTICOLI = ["art.1 c.1", "art.2 c.1"]
MAPPATURA = {"art.1 c.1": ["art.1 c.1"], "art.2 c.1": ["art.2 c.1"]}
RELAZIONI = [
    {"nodo_da": ("obbligo", 99, "art.1 c.1"), "nodo_a": ("principio", 99, "art.2 c.1"),
     "tipo_relazione": "specifica"},
]
EOF
app/.venv/bin/python -c "
import sys, sqlite3
sys.path.insert(0, '/tmp')
sys.path.insert(0, 'app')
import _fonte_fittizia as modulo
from seed import inserisci_fonte

conn = sqlite3.connect(':memory:')
conn.executescript(open('app/schema.sql', encoding='utf-8').read())
cur = conn.cursor()
cur.execute('INSERT INTO tipi_obbligo (id, nome) VALUES (1, \"organizzativo\")')
cur.execute('INSERT INTO tipi_principio (id, nome) VALUES (1, \"altro\")')
cur.execute('INSERT INTO stati_norma (id, nome) VALUES (1, \"vigente\")')
cur.execute('INSERT INTO oggetti_giuridici (id, nome) VALUES (1, \"altro\")')
cur.execute('INSERT INTO categorie_soggetto (id, nome) VALUES (1, \"QTSP/gestore\")')
cur.execute('INSERT INTO tipi_relazione (id, nome, nome_inverso) VALUES (1, \"specifica\", \"è specificato da\")')
cur.execute('INSERT INTO fonti (id, nome, url_sorgente, versione, data_entrata_vigore, stato_id) VALUES (99, \"fittizia\", \"x\", \"x\", \"2026-01-01\", 1)')
conn.commit()

lookup = {
    'tipi_obbligo': {'organizzativo': 1}, 'tipi_principio': {'altro': 1},
    'stati_norma': {'vigente': 1}, 'oggetti_giuridici': {'altro': 1},
    'categorie_soggetto': {'QTSP/gestore': 1},
    'tipi_relazione': {'specifica': 1},
}
registro = {}
inserisci_fonte(conn, cur, 99, modulo, lookup, registro)
assert cur.execute('SELECT COUNT(*) FROM obblighi').fetchone()[0] == 1
assert cur.execute('SELECT COUNT(*) FROM principi').fetchone()[0] == 1
assert cur.execute('SELECT COUNT(*) FROM relazioni').fetchone()[0] == 1
print('OK: inserisci_fonte funziona')
"
rm /tmp/_fonte_fittizia.py
```

Expected: stampa `OK: inserisci_fonte funziona` senza eccezioni.

- [ ] **Step 7: Commit**

```bash
cd "app/.." && git add app/seed.py
git commit -m "$(cat <<'EOF'
Aggiungi verifica_copertura e inserisci_fonte a seed.py

Scaffold per l'import granulare per fonte: verifica_copertura blocca
l'inserimento se l'indice articoli non e' coperto da esattamente una
riga, inserisci_fonte inserisce righe e risolve le relazioni tramite
un registro riferimento->id costruito durante l'inserimento.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

## Task 2: Wiring dell'orchestratore con moduli fonte stub

**Files:**
- Modify: `app/seed.py` (rimuovere i blocchi inline `obblighi`/`principi`/`obbligo_soggetti`/`principio_oggetti`/`relazioni` esistenti, aggiungere il loop orchestratore; mantenere invariate le sezioni lookup e `fonti`)
- Create: `app/seed_data/__init__.py` (vuoto)
- Create: `app/seed_data/eidas.py` (stub)
- Create: `app/seed_data/eidas2.py` (stub)
- Create: `app/seed_data/cad.py` (stub)
- Create: `app/seed_data/dpcm.py` (stub)

**Interfaces:**
- Consuma: `verifica_copertura`, `inserisci_fonte` (Task 1).
- Consuma: id fonte già presenti in `app/seed.py` (blocco `fonti`, invariato): 1=eIDAS, 2=eIDAS2, 3=CAD, 4=DPCM.
- Produce: ogni modulo `app/seed_data/<fonte>.py` espone `RIGHE_OBBLIGHI: list[dict]`, `RIGHE_PRINCIPI: list[dict]`, `INDICE_ARTICOLI: list[str]`, `MAPPATURA: dict[str, list[str]]`, `RELAZIONI: list[dict]` (forma esatta come in Task 1, Step 6).

- [ ] **Step 1: Creare gli stub dei 4 moduli fonte**

```bash
mkdir -p app/seed_data
touch app/seed_data/__init__.py
```

Per ciascuno dei 4 file (`app/seed_data/eidas.py`, `eidas2.py`, `cad.py`, `dpcm.py`), stesso contenuto stub (verrà sostituito nei Task 3-6):

```python
"""Stub in attesa di autoria granulare (vedi Task 3-6 del piano di
implementazione censimento granulare, docs/superpowers/plans/2026-09-11-censimento-granulare.md).
"""

RIGHE_OBBLIGHI: list[dict] = []
RIGHE_PRINCIPI: list[dict] = []
INDICE_ARTICOLI: list[str] = []
MAPPATURA: dict[str, list[str]] = {}
RELAZIONI: list[dict] = []
```

- [ ] **Step 2: Rimuovere i blocchi inline esistenti da `app/seed.py`**

Cancellare da `app/seed.py`: l'intero blocco `obblighi = [...]` con la relativa `many("obblighi", ...)`, il blocco `principi = [...]` con `many("principi", ...)`, i blocchi `many("obbligo_soggetti", ...)` e `many("principio_oggetti", ...)`, il blocco `relazioni = [...]` con `many("relazioni", ...)`. Mantenere intatti: gli import, `DB_PATH`/`SCHEMA_PATH`, la funzione `many` (resta utile per le tabelle lookup e per `fonti`), tutti i blocchi lookup (`stati_fonte`, `stati_norma`, `tipi_obbligo`, `tipi_principio`, `oggetti_giuridici`, `categorie_soggetto`, `tipi_relazione`), il blocco `fonti`.

- [ ] **Step 3: Costruire il dict `lookup` e il loop orchestratore**

Aggiungere in `app/seed.py`, subito dopo il blocco `fonti` esistente e prima della chiamata di chiusura della funzione `seed()`:

```python
    from seed_data import eidas, eidas2, cad, dpcm

    def nome_a_id(tabella, id_col="id", nome_col="nome"):
        righe = conn.execute(f"SELECT {id_col}, {nome_col} FROM {tabella}").fetchall()
        return {nome: id_ for id_, nome in righe}

    lookup = {
        "tipi_obbligo": nome_a_id("tipi_obbligo"),
        "stati_norma": nome_a_id("stati_norma"),
        "tipi_principio": nome_a_id("tipi_principio"),
        "oggetti_giuridici": nome_a_id("oggetti_giuridici"),
        "categorie_soggetto": nome_a_id("categorie_soggetto"),
        "tipi_relazione": nome_a_id("tipi_relazione"),
    }

    cursor = conn.cursor()
    registro = {}
    for fonte_id, modulo in [(1, eidas), (2, eidas2), (3, cad), (4, dpcm)]:
        inserisci_fonte(conn, cursor, fonte_id, modulo, lookup, registro)
```

Nota sull'import relativo: `app/seed.py` viene eseguito come script dalla cartella `app/` (vedi docstring in cima al file), quindi `from seed_data import ...` risolve correttamente `app/seed_data/`.

- [ ] **Step 4: Eseguire il seed e verificare che non fallisca**

```bash
app/.venv/bin/python app/seed.py
app/.venv/bin/python -c "
import sqlite3
conn = sqlite3.connect('app/censimento.db')
print('obblighi:', conn.execute('SELECT COUNT(*) FROM obblighi').fetchone()[0])
print('principi:', conn.execute('SELECT COUNT(*) FROM principi').fetchone()[0])
print('relazioni:', conn.execute('SELECT COUNT(*) FROM relazioni').fetchone()[0])
print('fonti:', conn.execute('SELECT COUNT(*) FROM fonti').fetchone()[0])
"
```

Expected: nessuna eccezione, `obblighi: 0`, `principi: 0`, `relazioni: 0`, `fonti: 4`.

- [ ] **Step 5: Commit**

```bash
git add app/seed.py app/seed_data/
git commit -m "$(cat <<'EOF'
Sposta i dati del censimento in moduli seed_data per fonte

app/seed.py diventa un orchestratore: rimuove i blocchi obblighi/
principi/relazioni accorpati inline e li sostituisce con un loop che
chiama inserisci_fonte per ciascuno dei 4 moduli in app/seed_data/
(al momento stub vuoti, autoria granulare nei task successivi).

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

## Task 3: Autoria granulare `app/seed_data/eidas.py`

**Files:**
- Modify: `app/seed_data/eidas.py` (da stub a contenuto reale)

**Interfaces:**
- Consuma: forma dict esatta definita in Task 1 Step 6 e Task 2 Step 1.
- Consuma: id lookup per nome, non per numero — usare esattamente i nomi già presenti nei blocchi lookup di `app/seed.py` (es. `"tipo_obbligo": "tecnico/sicurezza"`, non l'id `2`).
- Produce: `RIGHE_OBBLIGHI`, `RIGHE_PRINCIPI`, `INDICE_ARTICOLI`, `MAPPATURA`, `RELAZIONI` per la fonte eIDAS 910/2014 (fonte_id=1 nel loop orchestratore).

- [ ] **Step 1: Recuperare il perimetro e le fonti già consultate**

Leggere la docstring corrente di `app/seed.py` (righe 1-25 prima delle modifiche del Task 2 — recuperabile con `git log -p -- app/seed.py` o `git show <commit-precedente-Task-2>:app/seed.py`) per il perimetro già stabilito (Capitolo III, Trust Services, escluse le disposizioni il cui unico soggetto è uno Stato membro/Commissione/organismo di vigilanza, escluse le disposizioni puramente definitorie senza soggetto individuabile — queste ultime diventano candidate Principio, non escluse, sotto ADR-0004) e gli URL EUR-Lex già usati:
- Testo originario 2014: CELEX 32014R0910
- Versione consolidata vigente: CELEX 02014R0910-20241018

- [ ] **Step 2: Costruire `INDICE_ARTICOLI`**

Aprire il testo ufficiale (URL sopra) e elencare in `INDICE_ARTICOLI` ogni comma (e ogni lettera dove il comma contiene più punti indipendenti) del Capitolo III che rientra nel perimetro, nella forma `"art. N c.M"` o `"art. N c.M lett.X"`. Includere anche le disposizioni puramente dichiarative escluse finora (es. art. 25) come candidate Principio, non ometterle dall'indice.

- [ ] **Step 3: Scrivere `RIGHE_OBBLIGHI` e `RIGHE_PRINCIPI`**

Per ogni unità di prescrizione distinta identificata: una riga con `riferimento` (deve coincidere con uno o più item di `INDICE_ARTICOLI`, vedi Step 4), `testo` (sintesi in italiano, parafrasata come nel resto del repo — non riproduzione letterale, coerente con la nota "Testo parafrasato" già in `seed.py`), `testo_integrale` (testo ufficiale completo del comma/lettera, copiato dalla fonte), `tipo_obbligo`/`tipo_principio` (nome, non id), `stato` (nome, non id), `soggetti`/`oggetti_giuridici` come da forma Task 1 Step 6. Decidere qui, riga per riga, se un caso richiede una categoria diversa da Obbligo/Principio (Global Constraints) — se succede, fermarsi e segnalarlo all'utente prima di proseguire, non introdurre la categoria unilateralmente.

- [ ] **Step 4: Scrivere `MAPPATURA`**

Per ogni riga di `RIGHE_OBBLIGHI`/`RIGHE_PRINCIPI`, `MAPPATURA[riferimento] = [lista di item di INDICE_ARTICOLI coperti]`. Nella maggior parte dei casi sarà `[riferimento]` stesso (un item coperto); per una riga che fonde più commi in un'unica prescrizione continua, sarà la lista di tutti gli item coperti.

- [ ] **Step 5: Scrivere `RELAZIONI` evidenti interne a eIDAS**

Se durante la scrittura emerge una relazione evidente tra due righe appena scritte (es. un comma che specifica un obbligo generale di un altro articolo), aggiungerla con la forma `{"nodo_da": (tipo, 1, riferimento), "nodo_a": (tipo, 1, riferimento), "tipo_relazione": nome}` (fonte_id=1 per eIDAS, entrambi i lati in questa fonte).

- [ ] **Step 6: Eseguire la verifica di copertura**

```bash
app/.venv/bin/python -c "
import sys; sys.path.insert(0, 'app')
from seed_data import eidas
from seed import verifica_copertura
verifica_copertura(eidas.INDICE_ARTICOLI, eidas.MAPPATURA)
print('OK: copertura eIDAS completa')
"
```

Se fallisce, correggere `RIGHE_OBBLIGHI`/`RIGHE_PRINCIPI`/`MAPPATURA` finché non passa (Step 3-4 in loop).

- [ ] **Step 7: Eseguire il seed completo e verificare i conteggi**

```bash
app/.venv/bin/python app/seed.py
app/.venv/bin/python -c "
import sqlite3
conn = sqlite3.connect('app/censimento.db')
print('obblighi fonte 1:', conn.execute('SELECT COUNT(*) FROM obblighi WHERE fonte_id=1').fetchone()[0])
print('principi fonte 1:', conn.execute('SELECT COUNT(*) FROM principi WHERE fonte_id=1').fetchone()[0])
"
```

Expected: nessuna eccezione (le altre 3 fonti restano stub vuoti, non causano errore); conteggi coerenti con il numero di righe scritte.

- [ ] **Step 8: Commit**

```bash
git add app/seed_data/eidas.py
git commit -m "$(cat <<'EOF'
Autoria granulare eIDAS 910/2014 in seed_data/eidas.py

Sostituisce lo stub con l'estrazione granulare per unita' di
prescrizione (una riga per comma o lettera indipendente, niente
accorpamento di default), con indice di copertura verificato e
relazioni evidenti interne alla fonte.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

## Task 4: Autoria granulare `app/seed_data/eidas2.py`

**Files:**
- Modify: `app/seed_data/eidas2.py` (da stub a contenuto reale)

**Interfaces:**
- Consuma: stessa forma dict di Task 3.
- Consuma: registro cross-fonte — a questo punto eIDAS (fonte_id=1) è già inserita nell'ordine dell'orchestratore, quindi `RELAZIONI` di questo modulo può referenziare righe eIDAS con `("obbligo"|"principio", 1, riferimento_eidas)` (es. un articolo eIDAS2 che sostituisce un articolo eIDAS originario).
- Produce: `RIGHE_OBBLIGHI`, `RIGHE_PRINCIPI`, `INDICE_ARTICOLI`, `MAPPATURA`, `RELAZIONI` per fonte_id=2.

- [ ] **Step 1: Costruire `INDICE_ARTICOLI` dal testo emendante**

Fonte: CELEX 32024R1183 (Regolamento (UE) 2024/1183). Elencare in `INDICE_ARTICOLI` solo le disposizioni nuove o sostituite dall'atto emendante che rientrano nel perimetro Capitolo III/Trust Services (stesso perimetro di Task 3 Step 1), stessa forma `"art. N c.M"`/`"art. N c.M lett.X"`.

- [ ] **Step 2-5: Ripetere Task 3 Step 3-6 per eIDAS2**

Stessa procedura di Task 3 (righe, mappatura, relazioni — qui includendo esplicitamente relazioni cross-fonte verso eIDAS quando un articolo eIDAS2 sostituisce/specifica un articolo eIDAS originario, tipo_relazione `"sostituisce"` o `"specifica"` da CONTEXT.md/schema `tipi_relazione`), verifica di copertura con `eidas2.INDICE_ARTICOLI`/`eidas2.MAPPATURA`.

- [ ] **Step 6: Eseguire il seed completo e verificare i conteggi**

```bash
app/.venv/bin/python app/seed.py
app/.venv/bin/python -c "
import sqlite3
conn = sqlite3.connect('app/censimento.db')
print('obblighi fonte 2:', conn.execute('SELECT COUNT(*) FROM obblighi WHERE fonte_id=2').fetchone()[0])
print('principi fonte 2:', conn.execute('SELECT COUNT(*) FROM principi WHERE fonte_id=2').fetchone()[0])
print('relazioni cross eIDAS->eIDAS2:', conn.execute(\"SELECT COUNT(*) FROM relazioni r JOIN obblighi o ON r.nodo_da_tipo='obbligo' AND r.nodo_da_id=o.id WHERE o.fonte_id=1\").fetchone()[0])
"
```

Expected: nessuna eccezione, conteggi coerenti, eventuali relazioni cross-fonte visibili se scritte.

- [ ] **Step 7: Commit**

```bash
git add app/seed_data/eidas2.py
git commit -m "$(cat <<'EOF'
Autoria granulare eIDAS2 2024/1183 in seed_data/eidas2.py

Estrazione granulare delle disposizioni nuove/sostituite dall'atto
emendante, con relazioni esplicite verso gli articoli eIDAS
originari sostituiti o specificati.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

## Task 5: Autoria granulare `app/seed_data/cad.py`

**Files:**
- Modify: `app/seed_data/cad.py` (da stub a contenuto reale)

**Interfaces:**
- Consuma: stessa forma dict di Task 3.
- Consuma: registro cross-fonte con eIDAS (fonte_id=1) ed eIDAS2 (fonte_id=2), già inserite.
- Produce: `RIGHE_OBBLIGHI`, `RIGHE_PRINCIPI`, `INDICE_ARTICOLI`, `MAPPATURA`, `RELAZIONI` per fonte_id=3.

- [ ] **Step 1: Costruire `INDICE_ARTICOLI` dal testo CAD**

Fonte: Normattiva, D.Lgs. 82/2005, testo vigente multivigente (URL già presente nel blocco `fonti` di `app/seed.py`). Definire il perimetro (quali Titoli/Capi del CAD riguardano servizi fiduciari qualificati QTSP — verificare che coincida con quanto già implicito nelle righe CAD esistenti prima della riscrittura, recuperabili con `git log -p -- app/seed.py` sul commit precedente al Task 2) prima di costruire l'indice.

- [ ] **Step 2-5: Ripetere Task 3 Step 3-6 per CAD**

Stessa procedura, includendo relazioni cross-fonte verso eIDAS/eIDAS2 dove il CAD rinvia esplicitamente alla disciplina eIDAS (es. firma digitale vs firma elettronica qualificata eIDAS), verifica con `cad.INDICE_ARTICOLI`/`cad.MAPPATURA`.

- [ ] **Step 6: Eseguire il seed completo e verificare i conteggi**

```bash
app/.venv/bin/python app/seed.py
app/.venv/bin/python -c "
import sqlite3
conn = sqlite3.connect('app/censimento.db')
print('obblighi fonte 3:', conn.execute('SELECT COUNT(*) FROM obblighi WHERE fonte_id=3').fetchone()[0])
print('principi fonte 3:', conn.execute('SELECT COUNT(*) FROM principi WHERE fonte_id=3').fetchone()[0])
"
```

Expected: nessuna eccezione, conteggi coerenti.

- [ ] **Step 7: Commit**

```bash
git add app/seed_data/cad.py
git commit -m "$(cat <<'EOF'
Autoria granulare CAD in seed_data/cad.py

Estrazione granulare per unita' di prescrizione del D.Lgs. 82/2005,
con relazioni esplicite verso eIDAS/eIDAS2 dove il CAD rinvia alla
disciplina europea.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

## Task 6: Autoria granulare `app/seed_data/dpcm.py`

**Files:**
- Modify: `app/seed_data/dpcm.py` (da stub a contenuto reale)

**Interfaces:**
- Consuma: stessa forma dict di Task 3.
- Consuma: registro cross-fonte con eIDAS, eIDAS2, CAD (fonte_id 1,2,3), già inserite.
- Produce: `RIGHE_OBBLIGHI`, `RIGHE_PRINCIPI`, `INDICE_ARTICOLI`, `MAPPATURA`, `RELAZIONI` per fonte_id=4.

- [ ] **Step 1: Recuperare i pattern di accorpamento già identificati**

Il DPCM è la fonte con il pattern di accorpamento più marcato già documentato: `git log -p -- app/seed.py` (sul commit precedente al Task 2) mostra le righe id 67-81 (`"art. 3 §4-5"` fino a `"art. 44-46"`, ciascuna con più articoli/commi compressi in una sintesi) e le righe id 82-88 (Titolo V, già split correttamente il 2026-09-10 — usare quella parte come riferimento di stile per il livello di granularità corretto, non da riscrivere da zero se già granulare).

- [ ] **Step 2: Costruire `INDICE_ARTICOLI` dal testo DPCM**

Fonte: Normattiva, DPCM 22/2/2013 (URL già presente nel blocco `fonti`). Coprire almeno tutti gli articoli già rappresentati nelle vecchie righe 67-88, comma per comma/lettera per lettera dove indipendenti (in particolare art. 35 comma 1, 22 lettere a-v, e art. 40 comma 3, 19 lettere a-s — verificare durante l'autoria se sono elenchi di documentazione checklist che condividono un'unica prescrizione o obblighi indipendenti, caso per caso).

- [ ] **Step 3-6: Ripetere Task 3 Step 3-6 per DPCM**

Stessa procedura, includendo relazioni cross-fonte se il DPCM specifica/è specificato da CAD o eIDAS (es. regole tecniche DPCM che specificano un obbligo generale CAD), verifica con `dpcm.INDICE_ARTICOLI`/`dpcm.MAPPATURA`.

- [ ] **Step 7: Eseguire il seed completo end-to-end**

```bash
app/.venv/bin/python app/seed.py
app/.venv/bin/python -c "
import sqlite3
conn = sqlite3.connect('app/censimento.db')
for fonte_id in (1, 2, 3, 4):
    o = conn.execute('SELECT COUNT(*) FROM obblighi WHERE fonte_id=?', (fonte_id,)).fetchone()[0]
    p = conn.execute('SELECT COUNT(*) FROM principi WHERE fonte_id=?', (fonte_id,)).fetchone()[0]
    print(f'fonte {fonte_id}: obblighi={o} principi={p}')
print('relazioni totali:', conn.execute('SELECT COUNT(*) FROM relazioni').fetchone()[0])
"
```

Expected: nessuna eccezione, tutte e 4 le fonti con conteggi > 0.

- [ ] **Step 8: Commit**

```bash
git add app/seed_data/dpcm.py
git commit -m "$(cat <<'EOF'
Autoria granulare DPCM 22/2/2013 in seed_data/dpcm.py

Sostituisce le righe accorpate (es. art.6-13, art.20-31) con
un'estrazione granulare per unita' di prescrizione, stesso livello
di dettaglio gia' applicato al Titolo V nella correzione del
2026-09-10.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

## Task 7: Verifica finale end-to-end e pulizia

**Files:**
- Modify: `app/seed.py` (solo se la verifica trova problemi di wiring)
- Nessun nuovo file

**Interfaces:**
- Nessuna nuova interfaccia; verifica quelle prodotte da Task 1-6.

- [ ] **Step 1: Eseguire il seed da zero e controllare che non ci siano eccezioni**

```bash
app/.venv/bin/python app/seed.py
```

Expected: nessuna eccezione, `app/censimento.db` ricreato.

- [ ] **Step 2: Query di integrità delle relazioni**

```bash
app/.venv/bin/python -c "
import sqlite3
conn = sqlite3.connect('app/censimento.db')
rotte = conn.execute('''
    SELECT r.id, r.nodo_da_tipo, r.nodo_da_id, r.nodo_a_tipo, r.nodo_a_id FROM relazioni r
    WHERE NOT EXISTS (
        SELECT 1 FROM obblighi o WHERE r.nodo_da_tipo='obbligo' AND o.id=r.nodo_da_id
    ) AND NOT EXISTS (
        SELECT 1 FROM principi p WHERE r.nodo_da_tipo='principio' AND p.id=r.nodo_da_id
    )
''').fetchall()
print('relazioni con nodo_da inesistente:', rotte)
"
```

Expected: lista vuota (`[]`). Se non vuota, correggere il modulo fonte responsabile (Task 3-6) e ripetere.

- [ ] **Step 3: Spot-check `testo_integrale` a campione**

Per ciascuna delle 4 fonti, scegliere manualmente 2-3 righe (`SELECT riferimento, testo_integrale FROM obblighi WHERE fonte_id=? LIMIT 3`) e confrontare `testo_integrale` con il testo ufficiale alla fonte URL corrispondente (blocco `fonti` in `app/seed.py`). Annotare eventuali discrepanze e correggerle nel modulo fonte pertinente.

- [ ] **Step 4: Avviare la web UI e verificare la coda di revisione**

```bash
app/.venv/bin/python app/web_ui.py
```

Aprire `http://127.0.0.1:8010`, verificare che la coda di revisione mostri le nuove righe granulari con `stato_validazione='bozza'` e che il dettaglio di un obbligo/principio mostri correttamente `testo_integrale` nel blocco collassabile.

- [ ] **Step 5: Commit finale (se Step 2-3 hanno richiesto correzioni)**

```bash
git add app/seed_data/ app/seed.py
git commit -m "$(cat <<'EOF'
Correzioni da verifica end-to-end del censimento granulare

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

Se Step 2-3 non hanno richiesto correzioni, nessun commit aggiuntivo: il lavoro è già tutto committato nei Task 1-6.
