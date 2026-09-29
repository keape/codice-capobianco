# ADR-0012 — Nodi di partizione per i rinvii a unità indivise

Stato: accettata (2026-09-29). Decisione dell'utente su proposta dell'agente,
con tre scelte esplicite: nodo di partizione dedicato (non un nodo
Obbligo/Principio di articolo), ambito generico (articoli, allegati, sezioni,
clausole e paragrafi), backfill su tutte le Fonti censite.

## Contesto

I nodi del censimento sono **unità di prescrizione**: un comma, una lettera, un
punto di allegato, un requisito numerato di uno standard. I testi normativi
però rinviano spesso a **unità indivise**, più grandi di un comma e prive di un
nodo che le rappresenti: "il riesame è effettuato in conformità degli articoli
13 e 19", "si applica l'allegato IV", "clausola 6.8.5 di ETSI TS 119 431-1",
"l'articolo 5 bis, paragrafo 4" (paragrafo modellato per lettere, senza nodo di
chapeau).

Conseguenza misurata negli import di settembre 2026: o il rinvio restava
**senza arco**, o veniva agganciato a un'unità più fine scelta a mano. Casi
reali: Fonte 29 (Reg. UE 2024/482, EUCC) — su 132 rinvii interni a un articolo
citato in blocco, 81 sono stati ancorati con una soglia arbitraria ("articolo
con al più 3 commi") e **51 lasciati senza arco**; Fonte 28 — 1 rinvio senza
arco (art. 3 §1 → art. 5 bis §4 eIDAS2); Fonte 30 — l'abrogazione degli
articoli 23 e 24 ha richiesto cinque archi per articolo, uno per comma
soppresso, perché il bersaglio "articolo" non esiste. Le fonti ETSI del blocco
AdES hanno la stessa struttura (clausole e sottoclavole) e avrebbero
riprodotto il problema in ogni import successivo.

Non è un difetto di estrazione: è un **livello mancante nel modello**.

## Decisione

Introdurre un tipo di nodo **ausiliario** `:Partizione` — come già sono
`:Fonte`, `:CategoriaSoggetto` e `:OggettoGiuridico` — con proprietà
`fonte_id`, `riferimento`, `tipo_partizione` (`articolo`, `allegato`,
`sezione`, `clausola`, `paragrafo`). Un nodo per ciascuna unità indivisa
citabile in blocco.

1. **Generazione deterministica, mai a mano.** `neo4j_common.partizioni_di(riferimento)`
   deriva la catena di partizioni di una riga dai riferimenti già normalizzati:
   `art. 13 §1` → `art. 13`; `allegato IV, sezione IV.3, punto 5` → `allegato
   IV, sezione IV.3` → `allegato IV`; `clausola 5.2.2 (…)` → `clausola 5.2` →
   `clausola 5`; id di requisito con la clausola nel nome (`REQ-7.8-13`,
   `ISS-8.5.1-01`, `QTS-C.2.3-03`) → `clausola 7.8` (o `8.5.1`, `C.2.3`) e le
   sue radici; `par. 3.1 §1` (fonti AgID) → `par. 3.1` → `par. 3`; prefisso di
   parte conservato (`Parte 2: clausola 6.5.1`). Un riferimento la cui unità
   indivisa **è** la riga stessa (una clausola di primo livello, un articolo
   senza commi) non produce partizione: il nodo esiste già e le citazioni a
   quella unità puntano a quello. Un riferimento non strutturato (id di
   controllo tipo `SCP 13`) non produce partizione: meglio nessun nodo che un
   nodo inventato.
2. **Appartenenza derivata, non memorizzata.** `migrate_to_neo4j` crea
   `(nodo)-[:PARTE_DI]->(partizione)` per ogni riga e
   `(partizione)-[:PARTE_DI]->(partizione padre)` per la gerarchia. Le partizioni
   vivono nella tabella `partizioni` (schema.sql) solo per poter essere
   referenziate dagli id delle relazioni; l'appartenenza non è una tabella,
   così le regole di derivazione restano in un solo posto.
3. **Le partizioni non hanno testo normativo** (nessuna duplicazione, nessun
   conteggio gonfiato) e **non entrano nella coda di validazione**: non sono
   bozze di estrazione, sono struttura. La coda resta sui nodi di prescrizione.
4. **Backfill su tutte le Fonti censite**: `seed.py` chiama
   `seed_data.lib.registra_partizioni_mancanti` dopo il cablaggio, così anche le
   Fonti i cui dati sono ancora inline in `seed.py` (eIDAS, eIDAS2, Codice
   Civile) ricevono le partizioni. Esito del primo seed: **1.070 partizioni**
   (448 articoli, 581 clausole, 24 allegati, 8 sezioni, 9 paragrafi) e 4.702
   archi `PARTE_DI`.
5. I rinvii a unità indivise possono ora essere dichiarati nei moduli come
   relazioni con estremo `("partizione", fonte_id, "art. 13")`: il registro di
   `seed_data/lib.py` li risolve come per gli altri nodi, e i 14 tipi di
   relazione restano invariati (il CHECK di `relazioni.nodo_da_tipo`/`nodo_a_tipo`
   è stato esteso a `partizione`).

## Alternative scartate

- **Nodo Obbligo/Principio di articolo**, con il testo dell'articolo accanto ai
  commi. Scartata: duplica il testo normativo già presente comma per comma,
  rompe la regola ADR-0007 ("un nodo per unità di prescrizione"), gonfia la coda
  di validazione con centinaia di nodi fittizi e rende ambiguo quale nodo è "la"
  disposizione.
- **Convenzione di ancoraggio documentata** (primo comma, o "comma che regge la
  materia"). Scartata su rilievo esplicito dell'utente: resta arbitraria, non
  verificabile e non navigabile, e non chiude il problema all'indietro.
- **Ancorare al nodo più ampio esistente** (es. la clausola di scope, come fa
  Fonte 25 per i rinvii generici). È la prassi che il censimento seguiva *in
  mancanza di meglio*: con le partizioni diventa inutile, perché il bersaglio
  corretto esiste.

## Conseguenze

- Un rinvio a unità indivisa ha finalmente un bersaglio legittimo: sparano gli
  archi arbitrari e si possono recuperare i rinvii rimasti senza arco.
- La navigazione acquista un livello: da una partizione si risale ai nodi di
  prescrizione che la compongono (`PARTE_DI` a ritroso) e da lì alle altre
  partizioni citate.
- `web_ui.py` mostra le partizioni fra i vicini di un nodo (etichetta
  distinta, nessun link, nessuno stato di validazione). Non esiste ancora una
  vista dedicata per partizione: è un miglioramento di interfaccia, non un
  requisito della decisione.
- Costo: schema (tabella `partizioni`, vincolo e indice `partizioneUnica`),
  `neo4j_common.partizioni_di`, `seed_data/lib.py`, `migrate_to_neo4j.py`, un
  adeguamento di `web_ui.py`, un wire in `seed.py`. Nessuna modifica ai moduli
  dei capitoli già scritti (restano validi).
- **Lavoro aperto dichiarato**: i rinvii già censiti che oggi sono ancorati a un
  comma "per forza" (Fonte 29: 81 archi) vanno rimappati sulle partizioni, e i
  52 rinvii lasciati senza arco (Fonte 29: 51, Fonte 28: 1) vanno creati. La
  decisione è presa; l'esecuzione è un passo separato, perché tocca i moduli
  `cap15_relazioni_cross.py` di Fonte 29, `cap06_relazioni_cross.py` di Fonte 28
  e i `modifica`/`abroga` di Fonte 30.
- Il comando di applicazione dello schema documentato in `CLAUDE.md` va usato
  dopo aver rimosso le righe di commento `//`: lo split ingenuo per `;`
  spezzava i commenti di intestazione in "statement" invalidi.
