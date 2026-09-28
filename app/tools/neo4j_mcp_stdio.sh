#!/bin/sh
# Wrapper stdio per il server MCP ufficiale Neo4j (neo4j-mcp), usato da Pi
# tramite pi-mcp-adapter (config di progetto: .mcp.json).
#
# Perche' esiste:
#  - le credenziali vivono solo in app/.env (gitignorato), cosi' .mcp.json
#    resta senza segreti;
#  - il binario legge solo variabili NEO4J_MCP_* mentre il progetto usa
#    NEO4J_* (i nomi NEO4J_* sono accettati come deprecati, con warning a
#    ogni avvio: qui non vengono nemmeno esportati);
#  - forza sola lettura: le scritture sul grafo restano possibili solo via
#    app/seed.py + app/seed_data/lib.py (registro id, verifica_copertura,
#    guardia ADR-0010), mai dal canale MCP;
#  - telemetria disattivata: nessun dato inviato a servizi esterni (stesso
#    principio di ADR-0003).
set -eu

DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ENV_FILE="$DIR/../.env"

if [ ! -f "$ENV_FILE" ]; then
  echo "neo4j_mcp_stdio.sh: manca $ENV_FILE (copiare da app/.env.example)" >&2
  exit 1
fi

# Legge il valore di una chiave da .env senza fare `source` (nessuna variabile
# del progetto finisce nell'ambiente del server) e senza interpretare il valore.
valore() {
  grep -m1 "^$1=" "$ENV_FILE" | cut -d= -f2-
}

NEO4J_MCP_URI=$(valore NEO4J_URI)
NEO4J_MCP_USERNAME=$(valore NEO4J_USER)
NEO4J_MCP_PASSWORD=$(valore NEO4J_PASSWORD)
NEO4J_MCP_DATABASE=$(valore NEO4J_DATABASE)
[ -n "$NEO4J_MCP_DATABASE" ] || NEO4J_MCP_DATABASE=neo4j

if [ -z "$NEO4J_MCP_URI" ] || [ -z "$NEO4J_MCP_PASSWORD" ]; then
  echo "neo4j_mcp_stdio.sh: NEO4J_URI o NEO4J_PASSWORD mancanti in $ENV_FILE" >&2
  exit 1
fi

export NEO4J_MCP_URI NEO4J_MCP_USERNAME NEO4J_MCP_PASSWORD NEO4J_MCP_DATABASE
export NEO4J_MCP_READ_ONLY=true
export NEO4J_MCP_TELEMETRY=false

exec neo4j-mcp "$@"
