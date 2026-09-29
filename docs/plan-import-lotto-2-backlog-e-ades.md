# Piano di import — lotto 2: backlog normativo + famiglia AdES

Creato 2026-09-28, subito dopo la chiusura del lotto 1 (7 import: atti di
esecuzione eIDAS2, ETSI TS 119 312, TS 119 101, EN 319 102-1). Ordine richiesto
dall'utente: prima il backlog, poi la famiglia AdES.

## 1. Un problema di accesso da risolvere prima di iniziare

La procedura del progetto (`docs/procedura-import-granulare.md`) richiede il
**testo ufficiale** della fonte in `app/.source_cache/<fonte>/`, e la copertura
granulare di ADR-0007 richiede di leggerlo per intero. Per alcune fonti del
backlog quel testo **non è scaricabile** dall'agente. Verificato il 2026-09-28:

| fonte | accessibilità | nota |
|---|---|---|
| Reg. di esecuzione (UE) 2024/2979 | **libera** (CELLAR, come gli atti del lotto 1) | — |
| Regg. di esecuzione (UE) 2024/482 e 2024/3144 | **libera** (CELLAR) | schema EUCC |
| FIPS PUB 140-3 (2019) | **libera** (NIST) | — |
| IETF RFC 7515 | **libera** (IETF) | documento breve |
| ENISA ECCG «Agreed Cryptographic Mechanisms» | **libera** (ENISA) | da verificare il formato |
| ETSI EN 319 122-1, 132-1, 142-1, 162-1, TS 119 182-1 | **libera** (ETSI deliver, con User-Agent browser) | famiglia AdES |
| **CEN/TS 18170:2025** | **non libera** (portale CEN, per membri) | *e* in revisione: la Commissione ha rilevato gap e CEN prevede una nuova versione **entro fine 2026** |
| ISO/IEC 15408:2022 | **non libera** (ISO) | — |
| ISO 14721:2025 (OAIS) | **non libera** (ISO), ma il modello OAIS è pubblicato gratuitamente dal CCSDS come CCSDS 650.0-M-2 | da valutare se il testo CCSDS è equivalente ai fini del censimento |
| ISO 23257:2022, ISO/TS 23635:2022 | **non libera** (ISO) | — |

**Conseguenza pratica**: il backlog si divide in due. Le fonti libere possono
essere importate subito, con la procedura del lotto 1. Le fonti a pagamento
(CEN/TS 18170 e le ISO) richiedono che il testo ufficiale sia fornito
dall'utente, oppure che l'import sia rinviato.

**Su CEN/TS 18170, in particolare, la raccomandazione è di rimandare**, non solo
per l'accesso: è la norma portante dell'intero allegato di Reg. (UE) 2025/2532,
e importarla ora significherebbe rifare il lavoro quando CEN pubblicherà la
versione corretta entro il 2026. Il rinvio lascia in sospeso i rinvii di
clausola registrati in `docs/verifiche-aperte.md` § 9: sono un limite noto, non
un errore.

## 2. Perimetro, ordine e `fonte_id`

`fonte_id` da 28 in avanti, nell'ordine di esecuzione. L'ordine privilegia
accessibilità e stabilità, non l'ordine in cui le fonti sono state elencate nel
backlog.

**Blocco A — fonti libere del backlog**

| # | fonte | accesso | perché in questo punto |
|---|---|---|---|
| 1 | Reg. di esecuzione (UE) 2024/2979 — integrità e funzionalità di base dei portafogli EUDI | CELLAR | richiamato testualmente dall'allegato II punto 1 di 1569; formati degli attestati |
| 2 | Reg. di esecuzione (UE) 2024/482 + 2024/3144 — EUCC | CELLAR | richiamati da 2531 e 2532 come standard di certificazione dei dispositivi sicuri |
| 3 | FIPS PUB 140-3 (2019) | NIST | richiamato da 2531 e 2532 (`REQ-7.5-06`, adeguamento e) |
| 4 | IETF RFC 7515 (JWS) | IETF | richiamato dall'allegato di 2531 (parametro di intestazione `x5c`) |
| 5 | ENISA ECCG «Agreed Cryptographic Mechanisms» | ENISA | richiamato da 1567, 2531 e 2532: è la fonte ultima degli algoritmi ammessi |

**Blocco B — famiglia AdES** (richiesta esplicita dell'utente, subito dopo il backlog)

| # | fonte | note |
|---|---|---|
| 6 | ETSI EN 319 122-1 V1.3.1 (2023-06) CAdES — baseline signatures | citata da TS 119 312 e 119 461 |
| 7 | ETSI EN 319 132-1 V1.3.1 (2024-07) XAdES — baseline signatures | idem |
| 8 | ETSI EN 319 142-1 PAdES — baseline signatures | idem |
| 9 | ETSI EN 319 162-1 ASiC — baseline signatures | idem |
| 10 | ETSI TS 119 182-1 V1.2.1 (2024-07) JAdES — baseline signatures | citata testualmente dall'allegato di 2531 |

Le cinque fonti del blocco B sono un **deliverable per famiglia**: ciascuna ha
un profilo *baseline* (Parte 1) e, in alcuni casi, profili avanzati (Parte 2+).
Verificare al momento dell'import quali Parti esistono e pinnare la versione
corrente con la ricetta già in uso (listing ETSI + User-Agent browser, vedi
lotto 1 § 4).

**Blocco C — bloccate o volatili** (da non iniziare senza decisione dell'utente)

| fonte | stato |
|---|---|
| CEN/TS 18170:2025 | testo non libero **e** revisione CEN prevista entro fine 2026: rimandare |
| ISO/IEC 15408:2022 (p. 1-5) | testo non libero: serve il testo dall'utente, o rinvio |
| ISO 14721:2025 (OAIS) | testo non libero; valutare l'equivalente CCSDS 650.0-M-2 (gratuito) |
| ISO 23257:2022, ISO/TS 23635:2022 | testo non libero: serve il testo dall'utente, o rinvio |

## 3. Procedura (invariata dal lotto 1, con le due correzioni apprese)

Per ogni fonte, i sette passi di `docs/procedura-import-granulare.md` e del
piano del lotto 1, con in più:

- `app/tools/cellar_fetch.py` per gli atti UE; listing ETSI + User-Agent browser
  per gli standard ETSI; per NIST/IETF/ENISA, fetch diretto e conversione;
- `app/tools/split_source.py` con il front matter tagliato prima dello split
  quando l'indice del documento ripete i titoli dei capitoli;
- Fase 6 **in entrambe le direzioni**: candidati KNN con
  `app/tools/fase6_candidati_knn.py` (prima del seed) **e** ricognizione delle
  citazioni inverse, cioè dei nodi già nel grafo che citano la fonte nuova
  (query su `testo_integrale`), che nel lotto 1 hanno prodotto 44 relazioni
  altrimenti impossibili. Il backlog del lotto 2 è in gran parte fatto di fonti
  citate proprio dagli atti appena importati: la direzione inversa sarà
  probabilmente quella principale, come per Fonti 25-27;
- `app/tools/preflight_relazioni.py` prima di ogni seed, `set -o pipefail` sul
  seed, `verifica_troncamento.py` e `verifica_relazioni_textual.py` dopo;
- per le fonti con id propri di requisito, granularità all'id (lezione di
  Fonte 26); per le fonti senza id, granularità di clausola;
- `evidence_type` dichiarato esplicitamente per ogni relazione (il default di
  `lib.py` è ora `inferred`, vedi `docs/verifiche-aperte.md` § 10).

## 4. Fuori perimetro di questo lotto

- Le fonti del blocco C finché non c'è il testo ufficiale o una decisione di
  rinvio esplicita.
- Ogni fonte che il lotto 1 ha lasciato in sospeso e che non è nel backlog
  (es. TS 119 102-2, i profili AdES *avanzati*, ETSI EN 319 403, TS 119 615,
  TS 119 172, TS 119 511, EN 319 521/522/532, EN 419 241): restano candidate
  per un lotto 3, da valutare dopo il blocco B, perché le fonti AdES appena
  importate le citeranno e il censimento le richiederà a catena.

## 5. Stato

**Aggiornamento 2026-09-29.** Blocco A: **Fonte 28 chiusa** — Reg. di
esecuzione (UE) 2024/2979, 48 nodi (35 obblighi, 13 principi), 95 item di
indice, 24 relazioni (14 native interne + 10 cross-fonte, compresa una in
direzione inversa da Fonte 22), Fase 6 in
`app/seed_data/reg_ue_2024_2979/cap06_relazioni_cross.py`, scheda in
`docs/fonti-censite.md`. Subito dopo, su richiesta dell'utente, **Fonte 29
(Reg. di esecuzione (UE) 2024/482, EUCC) e Fonte 30 (Reg. di esecuzione (UE)
2024/3144, che modifica e rettifica la 482)**: testi ufficiali acquisiti via
CELLAR (`app/.source_cache/reg_ue_2024_482/`, 135k caratteri;
`app/.source_cache/reg_ue_2024_3144/`, 22k), split in 14 + 5 capitoli
(`app/tools/split_source.py`), autoria affidata a 19 subagent worker. La 3144
è un atto modificativo: le sue righe sono i punti dell'art. 1 e dell'art. 2,
gli artt. 2-3 e i suoi due allegati, con le relazioni `modifica`/`abroga`
verso la Fonte 29 costruite nella Fase 6 della Fonte 30.

Nota di perimetro sulla questione aperta all'inizio del lotto: la 2024/3144
rettifica la 2024/482 anche sull'allegato IV, quindi la voce § 9 di
`docs/verifiche-aperte.md` (rinvii a norme esterne) va riletta dopo il seed
delle due Fonti.

**Aggiornamento 2026-09-28 (sera).** Blocco A **in corso**: primo import =
Fonte 28, Reg. di esecuzione (UE) 2024/2979 (testo ufficiale in
`app/.source_cache/reg_ue_2024_2979/`, provenienza CELLAR, split in 5 capitoli:
Capo I-IV + allegati I-V).

Decisioni dell'utente sul blocco C, tutte di **rinvio**, quindi il blocco resta
fuori dal perimetro eseguito: CEN/TS 18170 rimandata (accesso non libero *e*
revisione CEN prevista entro fine 2026); ISO/IEC 15408, ISO 23257 e ISO/TS
23635 rimandate per indisponibilità del testo ufficiale; ISO 14721 rimandata in
attesa della versione definitiva, senza adottare come sostituto l'equivalente
gratuito CCSDS 650.0-M-2. Di conseguenza i rinvii di clausola registrati in
`docs/verifiche-aperte.md` § 9 restano aperti, come limite dichiarato e non
come errore.

Precedente (§ 5 al momento della scrittura del piano): nessun import di questo
lotto era iniziato; era in corso solo la normalizzazione di Fonte 27 (criterio
Input/Inputs di EN 319 102-1, deciso dall'utente il 2026-09-28), conclusa con i
commit `23fa4ee` e `44ae598`.
