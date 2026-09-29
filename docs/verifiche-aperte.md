# Verifiche aperte

Registro delle verifiche periodicamente da rifare: cose note, dichiarate e non
ancora chiuse, con l'indicazione di cosa è in sospeso, perché, su quali file
agire e quando riverificare. Serve a non far dipendere la memoria del progetto
dal ricordo di chi ha fatto l'import.

Regola di manutenzione: una voce entra qui quando è un **dubbio o un limite
dichiarato**, non quando è un lavoro da fare (per quello ci sono i piani in
`docs/plan-*.md`). Una voce esce quando la verifica è stata rifatta e il suo
esito è scritto nella scheda della Fonte in `docs/fonti-censite.md` o nel
docstring del modulo interessato.

Ultimo aggiornamento: 2026-09-29 (chiusura di Fonti 28, 29 e 30 - Reg. di
esecuzione (UE) 2024/2979, 2024/482 e 2024/3144 - con § 10 rilanciata ai
tre giri e la nuova voce § 3-bis). Aggiornamento precedente: 2026-09-28
(chiusura del lotto 1: atti di esecuzione eIDAS2 + TS 119 312, TS 119 101, EN
319 102-1; poi decisioni sull'apertura del lotto 2: § 7 chiusa, § 9 integrata
con i rinvii ratificati).

---

## 1. Fonte 10 (ETSI EN 319 401) — scostamento di versione rispetto agli atti che la adeguano

**In sospeso.** Gli atti di esecuzione importati adeguano ETSI EN 319 401
**V3.1.1 (2024-06)**, mentre la Fonte 10 censita è la **V3.2.1 (2026-01)**.

**Perché conta.** Fra le due versioni la numerazione delle clausole è cambiata:
il requisito sui firewall è `REQ-7.8-21X` nell'atto e `REQ-7.8-22` nella norma
censita; l'atto cita come `REQ-7.8-17X` il test di penetrazione che nella
versione censita è `REQ-7.8-18`. Le relazioni sono state agganciate **per
contenuto**, non per numero, ed è annotato caso per caso; ma un lettore del
grafo che confronti i numeri troverà uno scostamento che non è un errore.

**Dove agire.** `app/seed_data/reg_ue_2025_1567/cap01.py` e
`cap02_relazioni_cross.py`; `app/seed_data/reg_ue_2025_2531/cap01.py`;
`app/seed_data/reg_ue_2025_2532/cap01.py`.

**Quando riverificare.** A ogni re-import di Fonte 10 su una versione diversa
dalla V3.2.1, e quando ETSI pubblica una nuova edizione di EN 319 401.

## 2. Fonte 27 (ETSI EN 319 102-1) — nulla da fare, ma da ricordare: prefisso di parte

**In sospeso (condizionato).** I `riferimento` di Fonte 27 **non** portano il
prefisso `"Parte 1: "`, a differenza di ETSI EN 319 412, TS 119 431 ed EN 319
411. Decisione documentata in `docs/plan-import-lotto-eidas2-standard.md`
(sezione "Decisione presa in corso d'import"): con una sola Parte nella Fonte
non esiste ambiguità.

**Dove agire se si importa TS 119 102-2 nella stessa Fonte.** Gli 8 moduli
`app/seed_data/etsi_319_102/cap0[1-8].py`, il capitolo virtuale
`cap09_relazioni_cross.py` e i riferimenti a Fonte 27 presenti nei moduli di
altre Fonti. Solo le stringhe di `riferimento`, `INDICE_ARTICOLI_LOCALE`,
`MAPPATURA_LOCALE` (chiavi e valori) e `RELAZIONI`: **mai** i campi `testo`.

**Quando riverificare.** Prima di importare la Parte 2.

## 3. Fonte 27 — criterio di classificazione delle clausole con tabella "Requirement"

**Chiuso in data 2026-09-28, da riapplicare.** Regola decisa con l'utente: una
clausola la cui tabella ha la colonna `Requirement` (Mandatory/Optional) è
prescrittiva sul processo e va censita come **Obbligo "tecnico/sicurezza"**
anche senza `shall` esplicito; restano Principio le clausole dichiarative o di
interfaccia senza quella colonna.

**Perché era aperto.** cap05 e cap06 avevano classificato Obbligo le clausole
"Inputs" (5.3.2, 5.4.2, 5.5.2), cap04 e cap07 Principio le omologhe (5.2.x,
5.6.x), pur avendo le tabelle la stessa colonna (verificato su 5.2.2.2 e 5.3.2).
La Fonte era quindi internamente incoerente pur passando tutte le guardie —
le guardie verificano la copertura, non l'omogeneità dei criteri.

**Quando riverificare.** A ogni nuovo capitolo di una fonte ETSI che contenga
tabelle di input/output: il criterio va applicato, non reinventato.

## 3-bis. Fonte 29 (Reg. UE 2024/482, EUCC) — tipo_obbligo delle conseguenze della non conformità

**Chiusa il 2026-09-29 su decisione dell'utente: criterio "sanzionatorio" esteso,
da riapplicare.** I capitoli di Fonte 29, scritti in parallelo da 14 subagent
worker, avevano classificato le conseguenze della non conformità / non
compliance in due modi diversi:

- **"sanzionatorio"**: art. 28 §6, art. 29 §2, art. 29 §3 (cap05) e art. 35 §6
  (cap06) — il titolare non propone misure correttive adeguate, la violazione è
  continuata o ricorrente, l'aggiornamento della relazione di valutazione non
  viene fornito.
- **"procedurale"**: art. 14 §1 (cap02) e art. 20 §1 (cap03) — revoca del
  certificato EUCC; art. 21 §5 e art. 22 §6 (cap04) — revoca dell'autorizzazione
  dell'organismo di certificazione e dell'ITSEF; art. 31 §1-§3 e art. 30 §1 e §6
  (cap05) — misure per la non compliance e sospensione.

**Criterio deciso** (vale come precedente per ogni Fonte futura che contenga
revoche, sospensioni o misure di enforcement): "sanzionatorio" comprende
**qualunque conseguenza giuridica del venire meno dei requisiti o di una
violazione o di un accertamento** — revoca, sospensione e misure restrittive
incluse — e non solo sanzioni pecuniarie e responsabilità civile. Sotto-regola
adottata per non estendere l'etichetta ai meri obblighi di comunicazione: chi
**dispone o modula la conseguenza** va a "sanzionatorio"; chi disciplina solo la
**comunicazione della conseguenza** già disposta resta
"informativo/trasparenza". Lettura coerente con i precedenti del corpus (CAD
art. 37 c.4-ter, "intima di ottemperarvi"; SPID art. 12 c.4, previo accertamento
della violazione).

**Applicazione (2026-09-29, `fonte_id=29`).** Portate a "sanzionatorio" nove
righe, tutte quelle che dispongono o modulano la conseguenza: art. 14 §1
(cap02); art. 20 §1 (cap03); art. 21 §5 e art. 22 §6 (cap04); art. 30 §1, art. 30
§6, art. 31 §1, art. 31 §2 e art. 31 §3 (cap05). Restano "informativo/trasparenza"
le quattro righe che notificano o pubblicano una conseguenza già disposta (art.
30 §2, §3, §4 e §5 di cap05) e restano "sanzionatorio" le quattro righe già
classificate così (art. 28 §6, art. 29 §2, art. 29 §3, art. 35 §6). Fonte 29 ha
ora 13 righe "sanzionatorio" su 196 obblighi. Il grafo è stato riallineato con
un nuovo `app/seed.py`; nessun campo `testo`/`testo_integrale` è stato toccato.

**Quando riverificare.** A ogni nuova Fonte con disposizioni di revoca,
sospensione o enforcement: il criterio va **applicato**, non reinventato — è il
senso di questa voce.

## 4. Fonte 25 (ETSI TS 119 312) — relazioni mappate dalla numerazione V1.x

**In sospeso.** Le fonti censite citano TS 119 312 con la numerazione **V1.x**
(`clause A.8`, `clause A.9`, `clause 11`), mentre la versione importata
(V2.1.1, 2026-06) ha rinumerato in clausole 5, 6, 7, 9, 10. Le 21 relazioni
inverse sono agganciate per contenuto; solo le lunghezze di chiave conservano
il numero (clausola 9.3). Le citazioni generiche sono ancorate a
`clausola 1 (Scope)`.

**Dove agire.** `app/seed_data/etsi_119_312/cap05_relazioni_cross.py` (tabella
di mappatura completa nel docstring).

**Quando riverificare.** Se si importa la V1.x di TS 119 312, o gli standard
della famiglia AdES (EN 319 122/132/142), che sono il bersaglio di gran parte
dei rinvii interni di questa fonte.

## 5. Fonte 26 (ETSI TS 119 101) — nessun giro KNN in direzione diretta

**Limite dichiarato.** Per questa Fonte non è stato eseguito il giro di
candidati KNN in direzione diretta (fonte nuova → fonti esistenti): su 275 nodi
lo shortlist è dominato dal lessico comune degli standard ETSI e non da
corrispondenze prescrittive. Le corrispondenze reali sono state colte per
citazione letterale (14 relazioni inverse dalla Fonte 11).

**Dove agire.** `app/seed_data/etsi_119_101/cap05_relazioni_cross.py`
(docstring, sezione "Perché non c'è un giro KNN per questa Fonte").

**Quando riverificare.** Se si vuole il giro completo: va fatto con
classificazione su shortlist **ristretto per nodo**, non con una soglia globale.

## 6. Fonte 12 (Reg. UE 2025/1567) — punto dell'allegato senza controparte in Fonte 10

**In sospeso.** L'allegato punto 6 (clausola 6.8.5 "Controlli crittografici" di
ETSI TS 119 431-1) non ha un nodo corrispondente nella Fonte 11; il requisito da
cui deriva è stato agganciato a `REQ-7.5-01` di Fonte 10. Il punto 6
`OVR-6.8.5-02` resta invece senza archi.

**Dove agire.** `app/seed_data/reg_ue_2025_1567/cap01.py` (docstring),
`cap02_relazioni_cross.py`.

**Quando riverificare.** Se la Fonte 11 o la Fonte 10 vengono rieditate con
clausole nuove.

## 7. eIDAS ed eIDAS2 come due Fonti — chiuso: restano separate

**Chiuso il 2026-09-28, su decisione esplicita dell'utente: eIDAS (Reg.
910/2014, Fonte 1) ed eIDAS2 (Reg. 2024/1183, Fonte 2) restano due Fonti
distinte.** Non è un'incoerenza da sanare ma una scelta di modellazione
confermata, per poter confrontare prima/dopo. La regola di `CONTEXT.md` ("una
Fonte esiste una volta sola nel censimento") va letta con questa eccezione
dichiarata, non come una regola violata; nessuna unificazione, nessun
rimappaggio delle relazioni esistenti.

**Perché la separazione va comunque ricordata.** Gli atti di esecuzione
puntano alla Fonte 2 per le disposizioni vigenti (artt. 24, 29-bis, 45-sexies
eIDAS2): chi cerca una disposizione modificata da eIDAS2 deve sapere che il
nodo vive sulla Fonte 2, non sulla 1.

**Quando riverificare.** Solo se in futuro si decide di unificare: il costo
sarebbe il rimappaggio delle relazioni dei quattro atti di esecuzione del
lotto 1.

## 8. Date di pubblicazione ETSI a precisione mensile

**In sospeso, impatto basso.** Alcune Fonti ETSI hanno `data_entrata_vigore`
con il primo giorno del mese come segnaposto, perché il documento dichiara solo
mese e anno (es. Fonte 25: `2026-06-01`). Il pre-filtro temporale della ricerca
ibrida (ADR-0006) usa quelle date.

**Dove agire.** Blocco `fonti` di `app/seed.py`.

**Quando riverificare.** Se il pre-filtro temporale viene usato per finestre
inferiori al mese.

## 9. Fonte 23 e 24 — rinvii di clausola a norme esterne al censimento

**In sospeso, condizionato.** Gli allegati di Reg. 2025/2531 e 2025/2532
rinviano a **clausole intere** di ETSI EN 319 401 (punti 5, 7.5, 7.8, 7.10) e a
clausole di **CEN/TS 18170** (6.1, 6.2, 7.3, 7.13, 13.3.1), oltre che a ISO
14721/23257/23635, RFC 7515, FIPS PUB 140-3, ISO/IEC 15408 e ai regolamenti
(UE) 2024/482 e 2024/3144. Nessuna di queste ha oggi un nodo controparte, quindi
non è stata creata alcuna relazione: un rinvio di clausola non ha un bersaglio
puntuale e non ne è stato scelto uno arbitrario.

**Decisione del 2026-09-28 (lotto 2): i rinvii restano aperti per scelta, non
per inerzia.** CEN/TS 18170 è **rinviata** (testo non libero *e* revisione CEN
prevista entro fine 2026: importarla ora significherebbe rifare il lavoro sulla
versione corretta); ISO/IEC 15408:2022, ISO 23257:2022 e ISO/TS 23635:2022
sono **rinviate** per indisponibilità del testo ufficiale; ISO 14721:2025 è
**rinviata** in attesa della versione definitiva, senza adottare l'equivalente
gratuito CCSDS 650.0-M-2 come sostituto. Le fonti libere del backlog sono
invece in import: `docs/plan-import-lotto-2-backlog-e-ades.md`.

**Quando riverificare.** Dopo l'import di CEN/TS 18170 (a revisione CEN
conclusa) e a ogni import di una delle norme elencate: quei rinvii diventano
relazioni possibili.

---

## 10. `evidence_type='textual'` — audit eseguito, 337 citazioni da esaminare

**In sospeso, con strumento.** Il 2026-09-28 è stato creato
`app/tools/verifica_relazioni_textual.py`: per ogni relazione dichiarata
`textual` di tipo `richiama` o `attua` verifica che il `testo_integrale` del nodo
citante contenga almeno una traccia del `riferimento` citato (id di requisito,
articolo con ordinale, clausola, annesso, punto).

**Esito del primo giro** (2026-09-28): 1.243 relazioni `textual` esaminate,
**337 senza traccia** del riferimento citato. Distribuzione per fonte citante:
Fonte 18 (ETSI EN 319 421) **155**, Fonte 21 (TS 119 612) 40, Fonte 17 (EN 319
411-1) 28, Fonte 4 (DPCM 22/2/2013) 21, Fonte 20 (TS 119 432) 15, altre sotto
15.

**Esito del secondo giro** (2026-09-29, dopo l'import di Fonte 28): 1.219
relazioni `textual` esaminate, **346 senza traccia** (l'import di Fonte 28 ne
aggiunge 11, tutti classificati: vedi sotto; gli altri due casi in meno
rispetto al primo giro dipendono dalla normalizzazione di Fonte 27 del
2026-09-28 e dalla deduplica dell'audit, non da nuove verifiche).

**Esito del terzo giro** (2026-09-29, dopo l'import di Fonti 29 e 30 - EUCC e
atto modificativo): 1.375 relazioni `textual` esaminate, **356 senza traccia**
(+156 relazioni textual e +10 segnalazioni rispetto al giro precedente: Fonte
30 non ne produce nessuna).

**Esito del quarto giro** (2026-09-29, dopo la rimappatura sulle partizioni,
ADR-0012): 1.429 relazioni `textual` esaminate, **351 senza traccia**. La
rimappatura ha migliorato la verificabilità: le segnalazioni di **Fonte 29
scendono da 14 a 5** (le cinque restanti sono quelle interne al capitolo
documentate dai moduli cap02 e cap07, dove il testo cita l'articolo in blocco e
il bersaglio dichiarato è un comma), **Fonte 30 resta a 0** e Fonte 28 resta a
11 (i suoi casi documentati). Le 130 relazioni di Fonte 29 verso partizioni
passano il gate perché il riferimento del bersaglio è ora l'articolo stesso,
che il testo citante nomina. Le segnalazioni delle Fonti 28 e 29 sono
classificate nei due paragrafi seguenti.

**Fonte 31 (ETSI EN 319 122-1, CAdES), da 41 a 6 casi: causa sistematica confermata e
rimossa nello strumento (2026-09-29).** Gli standard ETSI citano in inglese ("clause
5.4.2", "see Annex D") o con la sola numerazione ("as defined in 5.2.2"), mentre il
`riferimento` del bersaglio nel censimento usa la forma italiana convenzionale ("clausola
5.4.2 (The message-digest attribute)") o la forma di annesso ("Annex D, id-aa-ets-certificateRefs
(...)"). Il gate cercava solo la forma del riferimento e segnalava quindi in blocco i
rinvii fra testi in lingue diverse — la stessa causa dei cluster di Fonte 18 (155), 21
(40), 17 (28) e 20 (15). **Correzione applicata a `app/tools/verifica_relazioni_textual.py`**
(su decisione utente: un rinvio fra testi in lingue diverse e' una relazione legittima):
le tracce sono ora bilingui e comprendono forme singolari e plurali (`clausola`/`clausole`/
`clause`/`clauses`/`subclause`), annessi (`Annex`/`annesso`/`allegato`), sezioni,
paragrafi e punti; la **numerazione nuda multi-segmento** (`5.2.2`, `A.1.1.1`), ammessa
solo se ha almeno due segmenti; gli **id ASN.1** (`id-aa-ets-…`, `id-spq-ets-…`) e i
**nomi di tipo CamelCase** (`CompleteCertificateRefs`), che sono il modo in cui gli
annessi tecnici si citano fra loro. Effetto su Fonte 31: 41 → **6 segnalazioni** su 150.
Effetto globale: **1.609 relazioni `textual` esaminate, 304 senza traccia** (erano 351
prima della correzione, con 180 relazioni in meno esaminate). I **6 casi residui** di
Fonte 31 sono relazioni fra oggetti ASN.1 dell'Annex D dichiarate `textual` dal worker ma
sostenute da una dipendenza *strutturale* (un attributo che usa il tipo definito altrove),
non da una citazione: vanno rilette in revisione, con probabile declassamento a
`inferred`.

**Fonte 28 (Reg. (UE) 2024/2979), 11 casi, tutti esaminati e classificati:** 7
sono **falsi positivi dello strumento** — il `testo_integrale` del nodo citante
cita i commi/lettere al plurale o in forma riassuntiva ("di cui ai paragrafi 1
e 2", "i meccanismi di autenticazione di cui alla lettera b)", "conforme ai
requisiti di cui all'art. 6"), mentre l'estrattore cerca l'ordinale singolare
del `riferimento` bersaglio; 4 hanno invece un **bersaglio scelto per
contenuto**, non citato puntualmente: la base giuridica art. 5 bis §23 eIDAS2
(citata nell'epigrafe dell'atto, fuori dai nodi) e i tre richiami al Reg.
2015/1502 degli artt. 4 §3, 5 §1 e 13, dove il testo nomina il regolamento ma
non l'articolo o il punto di allegato agganciato (scelta documentata nel
docstring di `app/seed_data/reg_ue_2024_2979/cap06_relazioni_cross.py`).
Nessuno dei 11 casi è un'etichetta gonfiata da correggere.

**Fonte 29 (Reg. (UE) 2024/482, EUCC), 14 casi — 10 falsi positivi e 4
etichette corrette.** I 10 falsi positivi sono della stessa classe di Fonte 28:
i moduli cap02 e cap07 citano l'articolo in blocco ("di cui all'articolo 7",
"si applicano le disposizioni dell'articolo 13") mentre il bersaglio dichiarato
e' un comma, e l'estrattore cerca l'ordinale del paragrafo; la scelta di miratura
e' documentata nei docstring dei due moduli. I 4 casi rimanenti erano
un'etichetta `textual` attribuita a un aggancio di contenuto: il punto 16 della
sezione V.1 dell'allegato V rinvia "alla sezione VI.2", ma la sezione che
disciplina l'adattamento del traguardo di sicurezza e' la **V.2** — nel testo
ufficiale della Gazzetta la numerazione romana di questi rinvii interni e'
sbagliata di uno (stessa anomalia al punto 1 della sezione V.2, che cita
"VI.1" per la V.1). Le quattro relazioni verso i punti della sezione V.2 sono
state quindi riclassificate `evidence_type="inferred"` con confidence 0.70
(bersaglio giusto, citazione non letterale) e annotate nel modulo; nessun arco
e' stato creato verso l'allegato VI, sezione VI.2, che riguarda la composizione
del gruppo di valutazione inter pares e non l'adattamento del traguardo di
sicurezza. Fonte 30 (atto modificativo): 0 casi su 21 relazioni `textual`, tutte
citazioni letterali dell'articolo o dell'allegato modificato.

**Perché non è una diagnosi.** Le due cause possibili — (a) etichetta gonfiata
(relazione costruita per costruzione ma dichiarata citazione letterale) e (b)
citazione espressa in una forma che l'estrattore non riconosce — non sono
ancora distinte. L'ispezione di tre relazioni di Fonte 18 ha mostrato almeno un
falso positivo dello strumento (il testo conteneva l'id citato, in maiuscolo,
mentre l'estrattore lavora su testo normalizzato) e un cluster
tematicamente sospetto (`OVR-6.1-01` con sei relazioni verso `REQ-5-01..06` di
Fonte 10). **Nessun campione era però tra i 337 segnalati**: l'indagine va fatta
sui casi segnalati, non su campioni casuali.

**Causa strutturale trovata e rimossa**: il default di `evidence_type` in
`app/seed_data/lib.py` era `"textual"`, quindi ogni relazione inserita senza
dichiarare la provenienza si presentava come citazione letterale. Il default è
ora `"inferred"` (la classe di evidenza più debole): `textual` va dichiarato
esplicitamente da chi ha verificato la citazione sul testo. **Il cambio vale
per le relazioni future**: le centinaia di relazioni già nel grafo (346 al
giro del 2026-09-29) portano in parte l'etichetta attribuita dal default
precedente e vanno riviste con lo strumento.

**Dove agire.** `app/tools/verifica_relazioni_textual.py --fonte-id 18` per il
cluster più grande, poi le altre fonti. Il file non va modificato a mano: le
etichette stanno in `app/seed_data/*/cap*_relazioni_cross.py`.

**Quando riverificare.** Dopo ogni import (lo strumento è nel novero dei
controlli ricorrenti) e in fase di revisione umana, prima di considerare
`textual` un'etichetta affidabile per una query.

## 11. Relazioni interne non verificate prima del primo seed di Fonte 27

**Chiuso, ma da ricordare per gli import futuri.** Il pre-flight usato fino a
Fonte 26 verificava solo i riferimenti verso *altre* Fonti: un tipo di nodo
invertito su un riferimento interno alla fonte in costruzione (relazione
`clausola 4.2.1 (Introduction)` dichiarata verso un Obbligo che il modulo
aveva scritto come Principio) ha fatto fallire il seed a metà strada con un
`KeyError`, dopo aver ricostruito tutto il grafo in memoria. Rimedio:
`app/tools/preflight_relazioni.py`, che risolve anche i riferimenti interni, e
`set -o pipefail` sul seed (una pipe verso `tail` restituisce il codice di
uscita di `tail`, cioè 0, anche quando Python è crollato).

## Verifica ricorrente (non una voce aperta, un controllo da rilanciare)

- `app/.venv/bin/python app/tools/verifica_troncamento.py` — nessun
  `testo_integrale` troncato (ADR-0010), su tutto il grafo o per Fonte.
- `app/.venv/bin/python app/tools/preflight_relazioni.py <fonte_id> <dir>` —
  prima di ogni seed.
- `app/.venv/bin/python app/tools/verifica_relazioni_textual.py` — controllo
  che ogni relazione dichiarata `evidence_type='textual'` trovi riscontro nel
  testo del nodo citante (vedi docstring dello strumento). Da rilanciare dopo
  ogni import e in fase di revisione.
