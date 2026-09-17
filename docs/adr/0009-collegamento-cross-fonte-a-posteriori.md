# Collegamento cross-fonte a posteriori: prefiltro economico + classificazione LLM solo sullo shortlist

## Contesto

L'import granulare del CAD (2026-09-16, ADR-0007) ha prodotto 594 nodi nuovi, collegati tra loro (113 relazioni interne) e con 1 sola relazione preesistente verso DPCM, ma **zero** relazioni verso eIDAS/eIDAS2 — per scelta deliberata: i subagent per capitolo erano stati istruiti a non tentare relazioni cross-fonte, per evitare `KeyError` su `riferimento` eIDAS non verificati durante un merge parallelo (vedi `docs/procedura-import-granulare.md`). Risultato: il CAD (58% dei nodi del grafo) era di fatto un'isola, contraddicendo l'obiettivo di lungo termine dell'utente — un censimento in cui ogni obbligo/principio comunica con le altre fonti, non un insieme di sottografi separati per fonte.

Il rischio concreto nel colmare questo gap è lo stesso che ha causato il costo eccessivo (due finestre di 5 ore) dell'import eIDAS originale: un confronto "a prodotto cartesiano" tra tutti i nodi CAD e tutti i nodi eIDAS/eIDAS2 (594 × 413 ≈ 245.000 coppie) affidato a un LLM senza prefiltro, con testo ripetuto in ogni chiamata.

## Decisione

Pipeline a 3 stadi, eseguita nella sessione principale (nessun subagent), pensata per essere riusabile per qualunque coppia di fonti già presenti nel grafo (non solo CAD↔eIDAS):

1. **Generazione candidati — zero token LLM.** Due prefiltri indipendenti, poi unione:
   - grep testuale sul testo ufficiale grezzo (`app/.source_cache/<fonte>/raw.txt`) per pattern di citazione esplicita (es. `articolo N ... del regolamento ... 910/2014|eIDAS`), risolto poi contro `testo_integrale` in Neo4j per ottenere il `riferimento` esatto del nodo che contiene la citazione;
   - KNN sull'indice vettoriale HNSW già popolato da `embed_neo4j.py` (`idxEmbeddingObbligo`/`idxEmbeddingPrincipio`, già presente per ogni nodo esistente — nessun embedding aggiuntivo da calcolare), con soglia di score configurabile (usata 0.80) per limitare i falsi positivi tematici.
   - Costo: query Cypher dirette, millisecondi per nodo, nessuna chiamata a un LLM.
2. **Classificazione — solo sullo shortlist.** Per lo shortlist risultante (nell'import CAD: 293 coppie su 128 nodi, non 245.000), chiamate `completion()` dirette in batch (10 nodi per batch, eseguite in parallelo con `wait()`), non subagent — evita la duplicazione di contesto che ha causato il costo eccessivo dell'import eIDAS. Ogni batch riceve solo `riferimento`+`testo` sintetico dei nodi coinvolti (mai `testo_integrale` completo o il testo ufficiale grezzo), un system prompt con la tassonomia di `CONTEXT.md` ristretta ai tipi di relazione rilevanti per il giro in corso, output vincolato a uno schema JSON strutturato. Il prompt istruisce esplicitamente a essere conservativi (omettere una coppia dubbia piuttosto che inventare una relazione).
3. **Validazione e inserimento.** Filtro per `confidence` minima (usata 0.5; le relazioni con evidenza testuale esplicita hanno tutte confidence ≥0.7), validazione di ogni `riferimento` proposto contro i nodi realmente esistenti in Neo4j (anti-allucinazione — un paio di stringhe leggermente imprecise dell'LLM sono state corrette per prefisso, non scartate), poi scrittura come modulo "capitolo virtuale" (`RIGHE_OBBLIGHI`/`RIGHE_PRINCIPI`/`INDICE_ARTICOLI_LOCALE`/`MAPPATURA_LOCALE` vuoti, solo `RELAZIONI` con `nodo_a`/`nodo_da` a fonte esplicita) nello stesso formato dei capitoli di `app/seed_data/lib.py`, agganciato in coda alla lista `capitoli` passata a `inserisci_capitoli` — riusa lo stesso meccanismo di risoluzione simbolica per riferimento già esistente, nessun codice nuovo nel merge.

Esito sul CAD: 53 relazioni cross-fonte inserite (specifica 23, richiama 11, si sovrappone a 10, attua 7, recepisce 2), tutte con `evidence_type`/`confidence` per-arco (ADR-0005).

## Alternative scartate

- **LLM su tutte le coppie senza prefiltro**: scartata, è la causa diretta del costo eccessivo già osservato sull'import eIDAS.
- **Subagent dedicati per la classificazione**: scartata per questo stadio. A differenza dell'estrazione per capitolo (dove il parallelismo su testo disgiunto è la fonte di risparmio), la classificazione cross-fonte lavora su uno shortlist già piccolo — l'overhead di dispatch/contesto di un subagent (system prompt, tool discovery) supera il beneficio del parallelismo per batch da 10-15 coppie. Le chiamate `completion()` dirette in parallelo ottengono lo stesso parallelismo senza quell'overhead.
- **Solo grep o solo KNN**: scartate singolarmente su richiesta esplicita dell'utente — combinate danno copertura sia delle citazioni letterali (alta precisione, `evidence_type=textual`) sia delle sovrapposizioni concettuali senza citazione esplicita (es. "si sovrappone a"), che il solo grep non troverebbe.

## Conseguenze

- Riusabile senza modifiche concettuali per DPCM↔eIDAS/eIDAS2 (fuori scope di questo giro, scope limitato a CAD su richiesta esplicita dell'utente) e per le fonti future del perimetro (AgID, ETSI, ISO, GDPR, CONTEXT.md §"Perimetro del pilota").
- Tutte le 53 relazioni nascono con `evidence_type`/`confidence` tracciati — nessuna diventa "human-curated" automaticamente; restano soggette alla stessa logica di revisione delle righe in bozza (coda di validazione UI), anche se lo schema attuale non ha un concetto di "stato_validazione" sulle relazioni (solo sui nodi Obbligo/Principio) — gap noto, non risolto da questa ADR.
- Il file `app/seed_data/cad/cap08_relazioni_eidas.py` documenta nel proprio docstring la pipeline di generazione, per evitare che una futura rigenerazione manuale la riproduca in modo incoerente.
</content>
