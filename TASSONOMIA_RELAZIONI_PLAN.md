# Integrazione tassonomia estesa delle relazioni (da "Edges e Relazioni")

## Context

Il documento `wiki/3. concepts/Edges e Relazioni.md` descrive un modello di archi tipizzati per Legal KG con 4 categorie (gerarchiche, di rinvio/citazione, di modifica temporale, applicative) più metadati di provenienza per arco (`confidence`, `evidence_type`, ...). Il censimento ha oggi solo 5 `tipi_relazione` (sostituisce, specifica, si sovrappone a, richiede come precondizione, è condizionato da — CONTEXT.md §"Relazioni tipizzate") e nessun metadato di provenienza sull'arco. Decisione utente (vedi risposte ask): estendere il vocabolario con 7 nuovi tipi che coprono le categorie del documento non ancora presenti (rinvio/citazione, modifica parziale distinta da sostituzione integrale, abrogazione, definizione, sanzione, attuazione), e aggiungere `evidence_type`+`confidence` come colonne su `relazioni`. Le relazioni gerarchiche (CONTAINS/HAS_PART/HAS_VERSION) del documento non si applicano: il censimento non ha nodi Articolo/Comma separati, solo Obbligo/Principio con `riferimento` testuale — nessuna azione per quella categoria.

Revisione effettuata in questa pianificazione: l'intero corpus `obblighi`/`principi` di `app/seed.py` (88 obblighi, 25 principi) è stato riletto per trovare istanze reali, testualmente motivate, dei 7 nuovi tipi — non introdotti a vuoto nel vocabolario. Le istanze concrete trovate sono elencate nello step 3bis; dove il corpus non offre un aggancio testuale pulito a un nodo già tracciato (vale per `abroga` e `definisce`), il tipo resta nel vocabolario ma senza istanza seedata, con la motivazione puntuale riportata nello step 3bis — non è un'omissione, è l'esito della revisione.

## Approach

### 1. Schema: metadati di provenienza sull'arco

In `app/schema.sql`, tabella `relazioni` (righe 103-110), aggiungere due colonne dopo `tipo_relazione_id`:

```sql
CREATE TABLE relazioni (
    id INTEGER PRIMARY KEY,
    nodo_da_tipo TEXT NOT NULL CHECK (nodo_da_tipo IN ('obbligo', 'principio')),
    nodo_da_id INTEGER NOT NULL,
    nodo_a_tipo TEXT NOT NULL CHECK (nodo_a_tipo IN ('obbligo', 'principio')),
    nodo_a_id INTEGER NOT NULL,
    tipo_relazione_id INTEGER NOT NULL REFERENCES tipi_relazione(id),
    evidence_type TEXT NOT NULL DEFAULT 'inferred'
        CHECK (evidence_type IN ('textual', 'inferred', 'human-curated')),
    confidence REAL CHECK (confidence IS NULL OR (confidence BETWEEN 0.0 AND 1.0))
);
```

`evidence_type`: `'textual'` = relazione esplicita nel testo normativo (es. un rinvio letterale "ai sensi dell'articolo X"), `'inferred'` = dedotta da un'estrazione LLM non ancora validata da un umano, `'human-curated'` = relazione verificata/costruita da un umano. `confidence` resta `NULL` quando non c'è uno score reale da riportare (evita di inventare un numero); popolato solo quando un'estrazione LLM futura produce davvero uno score. Niente `valid_from`/`valid_to`/`source_span`: la validità temporale è già coperta da `stati_norma` sui nodi Obbligo/Principio, e `source_span` (offset di carattere) non ha un consumatore nel workflow attuale (nessun viewer di `testo_integrale` con evidenziazione per offset).

Aggiornare il commento sopra la tabella (riga 100-102) per menzionare i nuovi campi.

### 2. Vocabolario: 7 nuovi tipi di relazione

In `app/seed.py`, nella chiamata `many("tipi_relazione", ...)` (righe 74-80), aggiungere dopo l'id 5:

```python
(6, "attua", "è attuato da"),
(7, "richiama", "è richiamato da"),
(8, "si applica a", "gli si applica"),
(9, "modifica", "è modificato da"),
(10, "abroga", "è abrogato da"),
(11, "definisce", "è definito da"),
(12, "sanziona", "è sanzionato da"),
```

Mappatura alle categorie del documento: `attua` = IMPLEMENTS/ENFORCES (es. DPCM attua una disposizione CAD); `richiama` = REFERS_TO/CITES (rinvio esplicito); `si applica a` = APPLIES_TO (norma che si applica a un'entità/oggetto giuridico tracciato come altro nodo, non a una categoria di soggetto — quello resta `obbligo_soggetti`); `modifica` = AMENDS, distinto da `sostituisce` (tipo 1) che resta la sostituzione integrale (SUPERSEDES/HAS_VERSION): `modifica` copre il caso in cui il nodo precedente resta rilevante ma con una variazione parziale, `sostituisce` il caso in cui il nodo precedente è del tutto rimpiazzato; `abroga` = REVOKES/REPEALS (abrogazione senza sostituzione diretta); `definisce` = DEFINES; `sanziona` = IMPOSES_SANCTION (da un obbligo di tipo "sanzionatorio" verso l'obbligo la cui violazione sanziona).

### 3. Seed dati esistenti (20 righe già presenti): valorizzare i nuovi campi

Nello stesso file, la lista `relazioni` (righe 787-808) e la chiamata `many(...)` (riga 809): aggiungere le colonne `evidence_type`, `confidence` e valorizzarle per tutte le 20 righe esistenti con `"inferred", None` — sono state estratte dall'LLM nella stessa sessione di estrazione descritta nell'header del file (righe 22-24: "l'estrazione LLM richiede validazione umana esplicita"), quindi coerenti con lo stato `bozza` dei nodi che collegano, non `human-curated`. `confidence` resta `None` per queste 20 righe (nessuno score reale disponibile, non va inventato).

### 3bis. Nuove istanze: applicare i 7 tipi al corpus già estratto (revisione richiesta dall'utente)

Aggiungere alla stessa lista `relazioni` 11 righe nuove (id 21-31), ciascuna un'istanza reale dei nuovi tipi, motivata da un riscontro testuale puntuale nei campi `testo`/`testo_integrale`/`sanzioni` già presenti in `obblighi`/`principi` (nessuna nuova estrazione dal testo normativo originale: solo applicazione della nuova tassonomia a testo già estratto e già in `seed.py`). Tipo id tra parentesi si riferisce ai valori aggiunti allo step 2.

Riferimenti (obbligo/principio `id` → riga in `app/seed.py` già letta in questa sessione):

```python
(21, "obbligo", 74, "obbligo", 66, 6, "textual", None),
  # DPCM art.20-31 (id 74, riga 455) attua CAD art.36§1 sulla revoca dei
  # certificati (id 66, riga 417): testo_integrale di 74 apre con "Fatto
  # salvo quanto previsto all'art. 36 del Codice" e ne elabora la procedura
  # tecnica di dettaglio — rapporto regola tecnica attuativa/norma primaria,
  # coerente con la descrizione della Fonte DPCM ("Regole tecniche per la
  # generazione, apposizione e verifica delle firme...").
(22, "obbligo", 25, "obbligo", 24, 7, "textual", None),
  # art.24§2(fb) (id 25, riga 229) richiama art.24§2(fa) (id 24, riga 225):
  # testo_integrale di 25 cita esplicitamente "l'attuazione delle misure di
  # cui alla lettera f bis)" (= id 24). Citazione letterale, non modifica né
  # sostituzione.
(23, "principio", 25, "obbligo", 86, 8, "textual", None),
(24, "principio", 25, "obbligo", 87, 8, "textual", None),
(25, "principio", 25, "obbligo", 88, 8, "textual", None),
(26, "principio", 25, "obbligo", 84, 8, "textual", None),
(27, "principio", 25, "obbligo", 85, 8, "textual", None),
  # principio 25 (art.55 DPCM, id 25 riga 744) si applica a ciascuno degli
  # obblighi del Titolo V che usano la distinzione soggetto erogante/
  # realizzatore che l'art.55 definisce: obbligo 86 (art.56, riga 505: "Il
  # soggetto erogante (art. 55, comma 2, lettera a)... [c1]"), 87 (art.57
  # c.1, riga 509: stesso incipit), 88 (art.57 c.2, riga 513: stesso
  # incipit), 84 (art.58, riga 517: "soggetti realizzatori (art. 55, comma
  # 2, lettera b)"), 85 (art.59, riga 521: "il soggetto erogante (art. 55,
  # comma 2, lettera a)"). Il campo `condizione_applicabilita` di principio
  # 25 lo dice esplicitamente: "definisce i soggetti... a cui si applicano
  # gli obblighi degli artt. 56-59".
(28, "obbligo", 11, "obbligo", 10, 9, "inferred", None),
(29, "obbligo", 16, "obbligo", 15, 9, "inferred", None),
(30, "obbligo", 17, "obbligo", 15, 9, "inferred", None),
  # modifica (non sostituzione integrale): 11 = art.20§1-bis "nuovo,
  # eIDAS2" (riga 165) è un comma aggiuntivo che affianca 10 = art.20§1
  # vigente (riga 161), senza sostituirlo (non esiste un "20§1-bis
  # abrogato"); analogamente 16 = art.24§1-bis (riga 189) e 17 = art.24§1-
  # ter (riga 193) sono commi aggiuntivi che dettagliano i metodi di
  # verifica del dovere generale posto da 15 = art.24§1 vigente (riga 185),
  # senza sostituirlo. Relazione strutturale dedotta dall'articolazione in
  # commi dello stesso intervento normativo, non da una dicitura testuale
  # esplicita di modifica — per questo `evidence_type="inferred"`, non
  # "textual".
(31, "obbligo", 63, "obbligo", 67, 12, "textual", None),
  # obbligo 63 (CAD art.32-bis, sanzionatorio, riga 405) sanziona obbligo 67
  # (CAD art.37§1-§3, cessazione attività, riga 421): il campo `sanzioni` di
  # 67 dichiara esplicitamente "sanzione ex art. 32-bis (fino al doppio) in
  # caso di mancata ottemperanza entro il termine intimato da AgID" — 32-bis
  # è per l'appunto l'obbligo 63.
```

`abroga` e `definisce` restano senza istanza seedata: nel corpus riletto nessuna abrogazione ha un nodo "da" che la rappresenti (l'unico caso di soppressione senza successore, obbligo 32 — art.24§2(j) — è un punto rimosso dalla riforma eIDAS2 nel suo insieme, non da un altro Obbligo/Principio tracciato, quindi non esiste un'estremità valida per una relazione nodo-a-nodo), e nessun principio del corpus definisce un concetto rappresentato da un nodo Obbligo/Principio a sé (la definizione più vicina, principio 25 sui soggetti erogante/realizzatore, è già coperta da `si applica a` verso gli obblighi che quella distinzione governa, non da un nodo "termine" separato che non esiste in questo schema). Non aggiungere righe fittizie per questi due tipi.


### 4. API: esporre i metadati sui vicini

In `app/web_ui.py`, `_vicini_di` (righe 241-269): la query SQL (righe 244-252) seleziona già `tr.nome`/`tr.nome_inverso`; aggiungere `r.evidence_type`, `r.confidence` a entrambi i `SELECT` (branch diretto e branch inverso dell'`UNION ALL`). Nel dict costruito nel loop (righe 259-268) aggiungere le chiavi:

```python
"evidence_type": v["evidence_type"],
"confidence": v["confidence"],
```

Nessun'altra funzione tocca `relazioni` (nessun endpoint di scrittura esiste oggi per le relazioni — restano popolate solo da `seed.py`), quindi nessun altro punto da aggiornare lato API.

### 5. Frontend: badge di provenienza sui vicini

In `app/web_ui.py`, `renderVicini` (righe 740-751): aggiungere un badge accanto al tag `tipo_relazione` esistente (riga 744) che mostri `evidence_type` e, se presente, `confidence` in percentuale:

```js
<span class="tag ${v.evidence_type==='human-curated'?'ok':v.evidence_type==='textual'?'':'warn'}">${esc(v.evidence_type)}${v.confidence!=null?` ${Math.round(v.confidence*100)}%`:''}</span>
```

Riusa le classi CSS `tag`/`ok`/`warn` già definite e usate altrove nello stesso file (es. riga 725, 747) — nessuna nuova classe CSS da introdurre.

### 6. Documentazione di dominio

In `CONTEXT.md`, sezione "Relazioni tipizzate tra nodi (Obbligo o Principio)" (righe 57-63): aggiungere le 7 nuove voci con la stessa forma delle esistenti (nome / nome inverso — descrizione), e una frase che spiega la distinzione `modifica` (parziale) vs. `sostituisce` (integrale). Aggiungere un paragrafo che documenta `evidence_type`/`confidence` come metadati per-arco, con la stessa semantica di provenienza di `stato_validazione` sui nodi.

Creare `docs/adr/0005-tassonomia-estesa-relazioni-e-provenienza.md` (stile libero come le ADR esistenti, es. `docs/adr/0004-principio-come-secondo-tipo-di-nodo.md`): contesto (il documento wiki esterno "Edges e Relazioni", link alla fonte), le due decisioni prese (7 nuovi tipi, non le relazioni gerarchiche; `evidence_type`+`confidence` sì, `valid_from`/`valid_to`/`source_span` no e perché), e nota esplicita che il popolamento di istanze con i nuovi tipi è demandato a una futura estrazione LLM interattiva (ADR-0003), non fatto in questo cambiamento.

## Critical files & anchors

- `app/schema.sql:100-110` — tabella `relazioni`, punto di aggiunta colonne.
- `app/seed.py:74-80` — seed `tipi_relazione`.
- `app/web_ui.py:241-269` — `_vicini_di`, query + dict da estendere.
- `app/web_ui.py:740-751` — `renderVicini`, badge da aggiungere.
- `app/seed.py:184` (obbligo 25), `:189` (16), `:193` (17), `:288` (38, per contesto), `:405` (63), `:417` (66), `:421` (67), `:455` (74), `:505,509,513,517,521` (86,87,88,84,85), `:744` (principio 25) — righe testuali citate a motivazione delle 11 nuove istanze, rileggere prima di trascrivere gli id nella lista `relazioni`.

## Verification

1. `app/.venv/bin/python app/seed.py` da `app/` — deve ricreare `censimento.db` senza errori (CHECK constraint su `evidence_type`/`confidence` non violati dalle 20+11 righe seedate) e stampare il messaggio finale invariato.
2. `app/.venv/bin/python -c "import sqlite3; c=sqlite3.connect('app/censimento.db'); print(c.execute('SELECT COUNT(*) FROM tipi_relazione').fetchone()); print(c.execute('SELECT COUNT(*) FROM relazioni').fetchone()); print(c.execute(\"SELECT tr.nome, r.evidence_type, r.confidence FROM relazioni r JOIN tipi_relazione tr ON tr.id=r.tipo_relazione_id WHERE r.id >= 21 ORDER BY r.id\").fetchall())"` — atteso: 12 tipi di relazione, 31 relazioni totali; le 11 righe id 21-31 mostrano rispettivamente `attua`/`richiama`/`si applica a` (x5)/`modifica` (x3)/`sanziona`, con `evidence_type` `textual` o `inferred` come specificato allo step 3bis e `confidence=None` su tutte.
3. Avviare `app/.venv/bin/python app/web_ui.py`, poi:
   - `curl http://127.0.0.1:8010/api/obblighi/2` (relazione "sostituisce" preesistente verso l'obbligo 1): `vicini[0]` contiene `"evidence_type": "inferred"` e `"confidence": null` accanto a `"tipo_relazione": "è sostituito da"`.
   - `curl http://127.0.0.1:8010/api/obblighi/74` (nuova relazione "attua"): tra i `vicini` compare l'obbligo 66 con `"tipo_relazione": "attua"`, `"evidence_type": "textual"`.
   - `curl http://127.0.0.1:8010/api/principi/25` (nuove relazioni "si applica a"): `vicini` contiene 5 elementi con `"tipo_relazione": "si applica a"` verso gli obblighi 86, 87, 88, 84, 85.
4. Aprire `http://127.0.0.1:8010/` nel browser, navigare al dettaglio del principio "art. 55" (DPCM, id 25) e verificare visivamente che il pannello "Relazioni tipizzate (grafo)" mostri 5 card con tag `si applica a` e badge `textual`.
