-- Schema del censimento obblighi QTSP (ticket 03, con l'aggiunta di
-- modifiche_rilevate decisa nel ticket 05 e del nodo Principio deciso
-- nel ticket 08 / ADR-0004). Vedi map.md e CONTEXT.md.

CREATE TABLE stati_fonte (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

-- Stato/validità temporale, condiviso tra Obbligo e Principio (ticket 08).
CREATE TABLE stati_norma (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE tipi_obbligo (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE tipi_principio (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE oggetti_giuridici (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE categorie_soggetto (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE tipi_relazione (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE,
    nome_inverso TEXT NOT NULL
);

CREATE TABLE fonti (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    url_sorgente TEXT NOT NULL,
    urn TEXT UNIQUE,
    versione TEXT,
    data_entrata_vigore TEXT,
    stato_id INTEGER NOT NULL REFERENCES stati_fonte(id)
);

CREATE TABLE obblighi (
    id INTEGER PRIMARY KEY,
    fonte_id INTEGER NOT NULL REFERENCES fonti(id),
    riferimento TEXT NOT NULL,
    testo TEXT NOT NULL,
    testo_integrale TEXT,
    tipo_obbligo_id INTEGER NOT NULL REFERENCES tipi_obbligo(id),
    stato_id INTEGER NOT NULL REFERENCES stati_norma(id),
    data_inizio_vigore TEXT,
    data_fine_vigore TEXT,
    severita TEXT,
    sanzioni TEXT,
    condizione_applicabilita TEXT,
    stato_validazione TEXT NOT NULL DEFAULT 'bozza'
        CHECK (stato_validazione IN ('bozza', 'validato', 'rifiutato')),
    validato_da TEXT,
    data_validazione TEXT,
    CHECK (data_fine_vigore IS NULL OR data_inizio_vigore IS NULL OR data_fine_vigore >= data_inizio_vigore)
);

CREATE TABLE obbligo_soggetti (
    obbligo_id INTEGER NOT NULL REFERENCES obblighi(id) ON DELETE CASCADE,
    categoria_soggetto_id INTEGER NOT NULL REFERENCES categorie_soggetto(id),
    ruolo TEXT NOT NULL CHECK (ruolo IN ('obbligato', 'destinatario')),
    PRIMARY KEY (obbligo_id, categoria_soggetto_id, ruolo)
);

-- Principio (ticket 08 / ADR-0004): norma dichiarativa che non impone un
-- comportamento a un soggetto (effetto giuridico, presunzione, non
-- discriminazione) — niente obbligo_soggetti, ma un oggetto giuridico
-- multi-valore a cui il principio si applica.
CREATE TABLE principi (
    id INTEGER PRIMARY KEY,
    fonte_id INTEGER NOT NULL REFERENCES fonti(id),
    riferimento TEXT NOT NULL,
    testo TEXT NOT NULL,
    testo_integrale TEXT,
    tipo_principio_id INTEGER NOT NULL REFERENCES tipi_principio(id),
    stato_id INTEGER NOT NULL REFERENCES stati_norma(id),
    data_inizio_vigore TEXT,
    data_fine_vigore TEXT,
    condizione_applicabilita TEXT,
    stato_validazione TEXT NOT NULL DEFAULT 'bozza'
        CHECK (stato_validazione IN ('bozza', 'validato', 'rifiutato')),
    validato_da TEXT,
    data_validazione TEXT,
    CHECK (data_fine_vigore IS NULL OR data_inizio_vigore IS NULL OR data_fine_vigore >= data_inizio_vigore)
);

CREATE TABLE principio_oggetti (
    principio_id INTEGER NOT NULL REFERENCES principi(id) ON DELETE CASCADE,
    oggetto_giuridico_id INTEGER NOT NULL REFERENCES oggetti_giuridici(id),
    PRIMARY KEY (principio_id, oggetto_giuridico_id)
);

-- Relazioni tipizzate tra nodi del grafo (Obbligo o Principio, ADR-0004):
-- polimorfica tramite discriminante di tipo, senza FK sulle estremità
-- (integrità verificata a livello applicativo, coerente con ticket 04).
-- evidence_type/confidence (ADR-0005): metadati di provenienza per arco,
-- stessa semantica di stato_validazione sui nodi.
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

-- Aggiunta ticket 05: cambiamenti rilevati dal monitoraggio automatico delle Fonti.
CREATE TABLE modifiche_rilevate (
    id INTEGER PRIMARY KEY,
    fonte_id INTEGER NOT NULL REFERENCES fonti(id),
    riferimento TEXT NOT NULL,
    data_rilevamento TEXT NOT NULL,
    testo_precedente TEXT NOT NULL,
    testo_nuovo TEXT NOT NULL,
    esaminata INTEGER NOT NULL DEFAULT 0 CHECK (esaminata IN (0,1))
);

CREATE INDEX idx_obblighi_fonte ON obblighi(fonte_id);
CREATE INDEX idx_obbligo_soggetti_obbligo ON obbligo_soggetti(obbligo_id);
CREATE INDEX idx_principi_fonte ON principi(fonte_id);
CREATE INDEX idx_principio_oggetti_principio ON principio_oggetti(principio_id);
CREATE INDEX idx_relazioni_da ON relazioni(nodo_da_tipo, nodo_da_id);
CREATE INDEX idx_relazioni_a ON relazioni(nodo_a_tipo, nodo_a_id);
CREATE INDEX idx_modifiche_fonte ON modifiche_rilevate(fonte_id, esaminata);
