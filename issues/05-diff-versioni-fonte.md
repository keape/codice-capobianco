Type: grilling
Status: resolved
Blocked by: 01, 02

## Question

Definire il meccanismo di confronto automatico del testo di una Fonte tra versioni successive: granularità del confronto (intero testo vs per-articolo), strategia di diffing, soglia oltre la quale una modifica genera la notifica attiva (badge UI) e come si individuano gli Obblighi (via riferimento puntuale) impattati da una modifica rilevata. Dipende da cosa risulta disponibile su EUR-Lex/Normattiva in termini di formato e storico versioni (ticket 01, 02).

## Answer

Deciso senza grilling il 9/9/2026 — scelte derivate direttamente dai vincoli già accertati in 01/02 e dallo schema in 03, senza spazio di design ampio da esplorare con l'utente.

### Decisioni chiave

- **Granularità: per articolo, non intero testo.** Sia eIDAS (HTML consolidato, `div.eli-subdivision[id^="art_"]`, ticket 01) sia CAD (Akoma Ntoso, `<article>`, ticket 02) sono già segmentabili programmaticamente per articolo — usare questa segmentazione nativa invece di un diff su blob di testo, perché il riferimento puntuale (`obblighi.riferimento`) è già espresso ad articolo/comma (schema 03) ed è l'unità naturale per collegare una modifica agli Obblighi impattati.
- **Strategia di diffing: confronto testuale diretto tra due fetch datati, non diff semantico.** Entrambe le fonti espongono lo stesso atto a date diverse tramite pattern URL parametrico già verificato (EUR-Lex: CELEX consolidato `-YYYYMMDD`; Normattiva: `!vig=YYYY-MM-DD` / `dataVigenza=`). Il job di monitoraggio: (1) individua l'ultima versione datata disponibile per una Fonte, (2) se più recente dell'ultima già processata, effettua il fetch e segmenta per articolo, (3) confronta testo-per-articolo (normalizzato: whitespace collassato, case preservato) contro lo snapshot precedente salvato. Nessun diff semantico (embedding/LLM): il pilota non deve dipendere da un LLM per il solo rilevamento del cambiamento (coerente con ADR-0003 — l'LLM entra in gioco solo nella sessione Claude Code che poi esamina la modifica).
- **Soglia: nessuna soglia fuzzy — qualunque differenza testuale rilevata sull'articolo genera notifica.** Pilota mono-utente (vedi map.md): il costo di un falso positivo (badge su una modifica solo tipografica) è basso — un rapido scarto manuale — mentre una soglia mal calibrata rischierebbe di nascondere in silenzio una modifica sostanziale. Non ottimizzare prematuramente per il rumore prima di aver osservato il pilota in uso.
- **Obblighi impattati: match esatto su `fonte_id` + `riferimento`.** Tutti gli Obblighi il cui `riferimento` coincide con l'articolo modificato sono marcati come "da rivedere" — non vengono modificati automaticamente (nessuna riscrittura silenziosa di un Obbligo validato): l'utente li esamina dal badge e decide se il testo/attributi restano validi o vanno corretti a mano nella prossima sessione di estrazione.
- **Persistenza**: nuova tabella `modifiche_rilevate` (non prevista nello schema originale del ticket 03, la aggiunge in append):

  ```sql
  CREATE TABLE modifiche_rilevate (
      id INTEGER PRIMARY KEY,
      fonte_id INTEGER NOT NULL REFERENCES fonti(id),
      riferimento TEXT NOT NULL,       -- articolo/comma modificato
      data_rilevamento TEXT NOT NULL,  -- ISO 8601
      testo_precedente TEXT NOT NULL,
      testo_nuovo TEXT NOT NULL,
      esaminata INTEGER NOT NULL DEFAULT 0 CHECK (esaminata IN (0,1))
  );
  CREATE INDEX idx_modifiche_fonte ON modifiche_rilevate(fonte_id, esaminata);
  ```

- **Contratto `monitoraggio_stato` (ticket 04) completato**: aggiunge per ogni fonte con modifiche non esaminate la lista di `riferimento` modificati e, per ciascuno, gli `obbligo_id` impattati (join su `obblighi.riferimento`):

  ```
  monitoraggio_stato() -> {
      status: "ok",
      fonti_con_modifiche: [{
          fonte_id, nome, data_rilevamento,
          modifiche: [{ riferimento, obblighi_impattati: [int] }]
      }]
  }
  ```

- **Trigger del job**: fuori scope del pilota fissare *quando* schedularlo (cron esterno vs comando manuale) — resta una decisione operativa, non architetturale; il meccanismo di rilevamento sopra è indipendente da come viene invocato.
