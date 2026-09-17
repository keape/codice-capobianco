// Schema Neo4j del censimento obblighi QTSP (ADR-0006 / docs/plan-migrazione-neo4j.md, Fase 2).
// Equivalente concettuale di schema.sql, non generato da ORM. Idempotente: ogni CREATE usa
// `IF NOT EXISTS`, si puo' rieseguire senza errori su un DB gia' inizializzato.
//
// Mappatura da schema.sql:
// - :Obbligo / :Principio — stesse colonne di obblighi/principi come proprieta'.
// - :Fonte — da tabella fonti; arco (:Obbligo|:Principio)-[:DA_FONTE]->(:Fonte).
// - Archi tipizzati (ADR-0004/0005/0008) — un arco per riga `relazioni`, tipo dell'arco = nome del
//   tipo di relazione (14 tipi, vedi CONTEXT.md); nomi con spazi normalizzati in UPPER_SNAKE
//   (mappatura in migrate_to_neo4j.py::TIPO_RELAZIONE_TO_ARCO). Proprieta' evidence_type/confidence
//   invariate. La relazione inversa (nome_inverso) si ottiene a ritroso via traversal, non
//   duplicata come arco separato.
// - :CategoriaSoggetto — arco (:Obbligo)-[:HA_SOGGETTO {ruolo}]->(:CategoriaSoggetto) al posto
//   di obbligo_soggetti.
// - :OggettoGiuridico — arco (:Principio)-[:HA_OGGETTO]->(:OggettoGiuridico) al posto di
//   principio_oggetti.
// - tipi_obbligo/tipi_principio/stati_norma/stati_fonte: tabelle di lookup puramente enumerative
//   (nessun attributo oltre al nome) NON diventano nodi separati, restano proprieta' stringa
//   dirette (es. Obbligo.tipo_obbligo = "organizzativo") — evita join per valori senza attributi
//   propri.
// - modifiche_rilevate: decisione presa in questa fase (Fase 2) — resta FUORI dal grafo Neo4j.
//   E' monitoraggio automatico delle Fonti, non referenziato da altre entita' del grafo (nessun
//   arco verso obblighi/principi, solo un lookup applicativo per fonte_id+riferimento). Non
//   beneficia di traversal ne' di full-text/vector: e' una coda di lavoro relazionale. Resta in
//   una tabella SQLite separata e minima (`app/monitoraggio.db`, stesso schema della tabella
//   originale) gestita da web_ui.py con sqlite3 in parallelo al driver neo4j.

// ---------------------------------------------------------------- vincoli di unicita'

CREATE CONSTRAINT obbligoIdUnico IF NOT EXISTS FOR (n:Obbligo) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT principioIdUnico IF NOT EXISTS FOR (n:Principio) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT fonteIdUnica IF NOT EXISTS FOR (n:Fonte) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT categoriaSoggettoNomeUnico IF NOT EXISTS FOR (n:CategoriaSoggetto) REQUIRE n.nome IS UNIQUE;
CREATE CONSTRAINT oggettoGiuridicoNomeUnico IF NOT EXISTS FOR (n:OggettoGiuridico) REQUIRE n.nome IS UNIQUE;

// ------------------------------------------------------------------------- indici (ADR-0006)

// 1. Full-text Lucene — sostituisce lo scan Python case-insensitive di /api/obblighi, /api/principi.
CREATE FULLTEXT INDEX idxTestoObbligo IF NOT EXISTS FOR (n:Obbligo) ON EACH [n.testo, n.riferimento, n.testo_integrale];
CREATE FULLTEXT INDEX idxTestoPrincipio IF NOT EXISTS FOR (n:Principio) ON EACH [n.testo, n.riferimento, n.testo_integrale];

// 2. Range index — data_inizio_vigore/data_fine_vigore, mai usate come filtro prima di questa migrazione.
CREATE RANGE INDEX idxVigoreObbligo IF NOT EXISTS FOR (n:Obbligo) ON (n.data_inizio_vigore, n.data_fine_vigore);
CREATE RANGE INDEX idxVigorePrincipio IF NOT EXISTS FOR (n:Principio) ON (n.data_inizio_vigore, n.data_fine_vigore);

// 3. Vector HNSW — embedding di `testo` (sintesi), 768 dimensioni (paraphrase-multilingual-mpnet-base-v2,
//    Fase 0 decisione 1), similarita' coseno. Scritto da app/embed_neo4j.py (Fase 4), non dalla migrazione
//    strutturale (Fase 3).
CREATE VECTOR INDEX idxEmbeddingObbligo IF NOT EXISTS FOR (n:Obbligo) ON (n.embedding)
  OPTIONS { indexConfig: { `vector.dimensions`: 768, `vector.similarity_function`: 'cosine' } };
CREATE VECTOR INDEX idxEmbeddingPrincipio IF NOT EXISTS FOR (n:Principio) ON (n.embedding)
  OPTIONS { indexConfig: { `vector.dimensions`: 768, `vector.similarity_function`: 'cosine' } };
