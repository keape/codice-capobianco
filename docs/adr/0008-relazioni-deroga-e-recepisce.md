# Aggiunta dei tipi di relazione "deroga a" e "recepisce"

## Contesto

La tassonomia delle relazioni tipizzate contava 12 tipi (5 originari da ADR-0004, 7 aggiunti da ADR-0005). In sede di revisione della copertura semantica sono emersi due gap non coperti da nessuno dei 12 tipi esistenti:

1. **Deroga**: il pattern normativo molto comune, soprattutto in fonti italiane, "in deroga a quanto previsto dall'articolo X" non è rappresentabile né con `modifica` (presuppone una variazione del contenuto che resta comunque rilevante) né con `abroga` (soppressione integrale) né con `è condizionato da` (applicabilità legata a un fatto/nodo tracciato in generale, non a un'eccezione esplicita posta da un altro nodo normativo per casi specifici). Serve un tipo dedicato che rappresenti l'esclusione puntuale dell'applicazione di un nodo generale, che resta pienamente vigente al di fuori dei casi derogati.
2. **Recepimento**: il rapporto per cui un nodo incorpora formalmente il contenuto di un altro in un contesto normativo diverso non era rappresentabile con `attua` (che aggiunge dettaglio operativo/tecnico a una norma di rango superiore che resta l'unica fonte del precetto) né con `specifica` (rende operativo un nodo generale senza sostituirne la fonte del precetto). Su richiesta esplicita dell'utente, il tipo non è limitato al caso classico direttiva UE → norma nazionale di recepimento: copre anche, ad esempio, una norma nazionale generale il cui contenuto viene ripreso/recepito all'interno di una normativa di settore o tecnica (schema concettualmente identico, cambia solo il livello degli strumenti normativi coinvolti).

## Decisione

Aggiunti 2 nuovi tipi al vocabolario (14 tipi totali), stesso schema di provenienza per-arco (`evidence_type`/`confidence`, ADR-0005) dei 12 esistenti:

- `deroga a` / `è derogato da` (arco Cypher `DEROGA_A`) — peso di direttezza (`DIRETTEZZA_PESO`) 4, stesso livello di `modifica`/`specifica`: è un'alterazione mirata e testualmente esplicita dell'applicabilità, più diretta di un rinvio ma meno di una sostituzione/abrogazione integrale.
- `recepisce` / `è recepito da` (arco Cypher `RECEPISCE`) — peso di direttezza 3, stesso livello di `attua`/`si applica a`/`sanziona`: è un rapporto applicativo tra norme, non un rapporto strutturale (sostituzione/modifica) né puramente referenziale (richiama).

Modificati: `app/neo4j_common.py` (`TIPI_RELAZIONE_INVERSO`, `TIPO_RELAZIONE_TO_ARCO`, `DIRETTEZZA_PESO`), `app/seed.py` (righe 13/14 di `tipi_relazione`), `app/neo4j_schema.cypher` (commento aggiornato a 14 tipi), `CONTEXT.md` (glossario).

## Popolamento

Nessuna istanza seedata in questo cambiamento: coerentemente con il precedente di `abroga`/`definisce` in ADR-0005, non si inventano relazioni senza un riscontro testuale puntuale nel corpus attuale (eIDAS/eIDAS2/CAD/DPCM). Il popolamento di istanze `deroga a`/`recepisce` è demandato a una futura estrazione LLM interattiva dentro sessioni Claude Code (ADR-0003), quando emerga un riscontro testuale reale in `testo`/`testo_integrale`.

## Impatto sullo schema

`app/schema.sql` (tabella `tipi_relazione`, colonne `nome`/`nome_inverso` senza vincolo `CHECK` sui valori) non richiede modifiche strutturali: i nuovi tipi sono righe aggiuntive, non nuove colonne. `app/censimento.db` (SQLite storico, non più letto da `web_ui.py` — vedi CLAUDE.md) non viene rigenerato da questo cambiamento; chi rilancia `migrate_to_neo4j.py` da quel backup vedrà solo i 12 tipi storici finché non viene rieseguito `seed.py`.
