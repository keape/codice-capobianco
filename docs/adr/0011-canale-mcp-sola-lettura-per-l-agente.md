# Canale MCP in sola lettura verso il grafo: la scrittura resta monolítica

Contesto: interrogare il censimento durante il lavoro (conteggi per fonte,
verifica di copertura di un capitolo appena importato, audit di troncamento,
shortlist del collegamento cross-fonte di ADR-0009, ricognizione dello
schema) richiedeva ogni volta uno script Python usa-e-getta con il driver
`neo4j` e le credenziali lette da `app/.env`: nessuna superficie di query
stabile, nessuna memoria fra una sessione e l'altra, e ogni ricognizione
andava riscritta da zero. Il grafo ha ormai 3760 nodi su 20 Fonti, e il
fabbisogno reale dell'agente su di esso è quasi sempre di sola lettura. Il
repo è inoltre passato all'harness pi (0.87.1) accanto a Claude Code: pi non
ha supporto MCP nativo in questa versione, quindi serve un client esterno.

Decisione: il grafo è interrogabile dall'agente **in sola lettura** via
Model Context Protocol. Client `pi-mcp-adapter` installato a livello utente
(vale in ogni progetto); server **`neo4j-mcp`, quello ufficiale Neo4j**,
installato con Homebrew e dichiarato in `.mcp.json` **di progetto**, quindi
attivo solo in questa cartella. Le credenziali restano solo in `app/.env` e
non compaiono in nessun file di configurazione: `app/tools/neo4j_mcp_stdio.sh`
le legge a runtime, mappa `NEO4J_*` sulle variabili attese dal binario
(`NEO4J_MCP_*`), forza `NEO4J_MCP_READ_ONLY=true` e disattiva la telemetria.
Prerequisito sull'istanza locale: il plugin **APOC 2026.08.1** (stessa
versione del kernel), perché `neo4j-mcp` non parte senza — il tool
`get-schema` chiama `apoc.meta.schema` e all'avvio il binario verifica la
presenza della procedura e termina con errore se manca. Installato il jar
ufficiale in `plugins/` con `dbms.security.procedures.unrestricted=apoc.meta.*`
(minimo privilegio: solo le procedure che servono, non tutto `apoc.*`).

Perché: il canale di scrittura sul grafo resta **uno solo** — `app/seed.py` e
`app/seed_data/lib.py`, con registro id per riferimento simbolico,
`verifica_copertura` e `verifica_completezza_testo_integrale` (ADR-0010) che
bloccano il seed prima di qualunque INSERT. Il server MCP espone soltanto
`get-schema` e `read-cypher` e **respinge** le query di scrittura, con un
messaggio esplicito che rimanda a un tool `write-cypher` non registrato in
modalità sola lettura: verificato con un tentativo di `CREATE` reale, non
dedotto dalla configurazione. Il confinamento al progetto è doppio: il server
è dichiarato in `.mcp.json` (non nella configurazione globale, che contiene
solo il client) e pi chiede un'approvazione esplicita la prima volta che lo
avvia, saltando i server di progetto non approvati nelle sessioni non
interattive.

Alternativa scartata: server MCP della comunità (`mcp-neo4j-cypher`, Python,
via `uvx`), che non richiede APOC e quindi non tocca l'istanza Neo4j.
Scartata perché manca il requisito di essere il server ufficiale, e il costo
evitato (un plugin in più sull'istanza) era verificabile a priori: la
versione APOC allineata al kernel esiste ed è stata installata con hash
verificato contro il digest della release, quindi il rischio di
disallineamento di versione — l'unico realmente temibile in questo percorso —
era escluso prima di toccare il database.

Alternativa scartata: dare al server MCP accesso in scrittura, per creare
relazioni direttamente in fase di collegamento cross-fonte (ADR-0009) invece
di passare da un modulo "capitolo virtuale" e da `seed.py`. Scartata perché
una scrittura via Cypher arbitrario salta tutte e tre le guardie: nessun id
risolto per riferimento simbolico, nessuna verifica di copertura, nessun
controllo di completezza verbatim. Le guardie funzionano solo se esiste un
unico punto di ingresso scritto.

Alternativa non scartata, per chiarezza: gli script Python con il driver
restano il percorso normale per le scritture e per i controlli bloccanti
(`app/tools/verifica_troncamento.py`, `verifica_copertura`). Il canale MCP è
**additivo** ed è di ispezione, non di certificazione: una query MCP non
sostituisce un controllo che deve bloccare un merge.

Esito (2026-09-28): verificato dal server reale, non dalla configurazione —
`neo4j-mcp v1.6.0` completa l'handshake; tool esposti `get-schema` e
`read-cypher`, nessun tool di scrittura; `get-schema` legge lo schema vero del
censimento (`Obbligo`, `Principio`, `Fonte`, archi con
`relazione_id`/`evidence_type`/`confidence`); `read-cypher` restituisce 2571
Obblighi, 1136 Principi, 29 OggettiGiuridici, 20 Fonti, 4 CategorieSoggetto;
il tentativo di `CREATE` è respinto dal server e nessun nodo estraneo è stato
creato. Lato istanza: 174 procedure APOC caricate e `apoc.meta.schema`
eseguibile. La riga di configurazione in `conf/neo4j.conf` è sopravvissuta al
riavvio dell'istanza, ma Neo4j Desktop riscrive quel file a ogni avvio: se in
futuro sparisse, APOC va reinstallato dalla scheda Plugin della GUI (vedi
`docs/runbook-neo4j-import.md`).

Nota operativa: il wrapper `app/tools/neo4j_mcp_stdio.sh` e `.mcp.json` non
contengono segreti e possono essere versionati. Il puntatore alle skill di
progetto (`.pi/settings.json`) è invece dentro `.pi/`, cartella esclusa per
intero dal `.gitignore`: su un clone va ricreato a mano (vedi `CLAUDE.md`).
