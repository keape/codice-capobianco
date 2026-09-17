# Tassonomia estesa delle relazioni tipizzate e metadati di provenienza per arco

Contesto: il documento esterno `wiki/3. concepts/Edges e Relazioni.md` descrive un modello di archi tipizzati per Legal Knowledge Graph con 4 categorie (gerarchiche, di rinvio/citazione, di modifica temporale, applicative) più metadati di provenienza per arco (`confidence`, `evidence_type`, ...). Il censimento aveva solo 5 `tipi_relazione` (sostituisce, specifica, si sovrappone a, richiede come precondizione, è condizionato da — CONTEXT.md, ADR-0004) e nessun metadato di provenienza sull'arco, a differenza dei nodi Obbligo/Principio che già hanno `stato_validazione`.

## Decisione 1: 7 nuovi tipi di relazione, non le relazioni gerarchiche

Aggiunti al vocabolario: `attua`/`è attuato da` (IMPLEMENTS/ENFORCES), `richiama`/`è richiamato da` (REFERS_TO/CITES), `si applica a`/`gli si applica` (APPLIES_TO, verso un nodo tracciato — non verso una categoria di soggetto, che resta `obbligo_soggetti`), `modifica`/`è modificato da` (AMENDS, modifica parziale), `abroga`/`è abrogato da` (REVOKES/REPEALS), `definisce`/`è definito da` (DEFINES), `sanziona`/`è sanzionato da` (IMPOSES_SANCTION).

`modifica` è distinta da `sostituisce` (tipo 1, già esistente): `sostituisce` rappresenta la sostituzione integrale (il nodo precedente non è più applicabile), `modifica` una variazione parziale in cui il nodo precedente resta rilevante e il nuovo nodo lo affianca/integra.

Non adottate le relazioni gerarchiche pure del documento wiki (es. PART_OF, la struttura ad albero articolo→comma→lettera): il censimento tratta già ogni comma/lettera come nodo Obbligo/Principio a sé con un `riferimento` testuale (es. "art. 24 §2(fb)"), senza una tabella di containment esplicita — introdurla sarebbe una ristrutturazione dello schema dei nodi, non un'estensione del vocabolario di relazione, e va oltre lo scopo di questo cambiamento.

## Decisione 2: `evidence_type` + `confidence` sull'arco, non `valid_from`/`valid_to`/`source_span`

Aggiunte a `relazioni` due colonne: `evidence_type TEXT NOT NULL DEFAULT 'inferred' CHECK IN ('textual', 'inferred', 'human-curated')` e `confidence REAL CHECK (confidence IS NULL OR BETWEEN 0.0 AND 1.0)`.

`evidence_type`: `textual` = relazione esplicita nel testo normativo (es. un rinvio letterale "ai sensi dell'articolo X"), `inferred` = dedotta da un'estrazione LLM non ancora validata da un umano, `human-curated` = relazione verificata/costruita da un umano. Stessa semantica di provenienza di `stato_validazione` sui nodi, ma per-arco.

`confidence` resta `NULL` quando non c'è uno score reale da riportare — evita di inventare un numero; popolato solo quando una futura estrazione LLM produce davvero uno score.

Non adottati dal documento wiki: `valid_from`/`valid_to` (la validità temporale è già coperta da `stati_norma` sui nodi Obbligo/Principio, non serve duplicarla sull'arco) e `source_span` (offset di carattere nel testo normativo: non ha un consumatore nel workflow attuale, nessun viewer di `testo_integrale` con evidenziazione per offset).

## Popolamento

Le 20 relazioni esistenti in `seed.py` sono state marcate `evidence_type='inferred'`, `confidence=NULL` (estratte da LLM nella stessa sessione descritta in ADR-0003, coerenti con lo stato `bozza` dei nodi che collegano). 11 nuove istanze dei 7 nuovi tipi sono state aggiunte al seed, motivate da riscontro testuale puntuale in `testo`/`testo_integrale`/`sanzioni` già presenti nel corpus (nessuna nuova estrazione dal testo normativo originale). `abroga` e `definisce` restano nel vocabolario senza istanza seedata: nel corpus non esiste un'estremità nodo-a-nodo valida per questi due casi (vedi commento in `seed.py` accanto alla lista `relazioni`).

Il popolamento di ulteriori istanze con i nuovi tipi è demandato a una futura estrazione LLM interattiva dentro sessioni Claude Code (ADR-0003), non fatto in questo cambiamento.
