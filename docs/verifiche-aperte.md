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

Ultimo aggiornamento: 2026-09-28 (chiusura del lotto 1: atti di esecuzione
eIDAS2 + TS 119 312, TS 119 101, EN 319 102-1).

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

## 7. Inconsistenza dichiarata e non risolta: eIDAS ed eIDAS2 come due Fonti

**In sospeso da prima di questo lotto.** `CONTEXT.md` dichiara che una Fonte
esiste una volta sola nel censimento; `app/seed.py` modella il Reg. 910/2014 e
il Reg. 2024/1183 come **due Fonti separate** (1 e 2), scelta deliberata per
poter confrontare prima/dopo, con una nota in `CLAUDE.md` che la segnala come
divergenza "da riconciliare esplicitamente con l'utente".

**Perché conta.** Determina dove vivono i nodi degli articoli modificati da
eIDAS2: tutti gli atti di esecuzione importati puntano alla Fonte 2 per le
disposizioni vigenti (artt. 24, 29-bis, 45-sexies eIDAS2). Se le due Fonti
venissero unificate, tutte le relazioni di quei 4 atti dovrebbero essere
rimappate.

**Quando riverificare.** Alla prima occasione di revisione con l'utente: è una
decisione di modellazione, non un errore da correggere in autonomia.

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

**Quando riverificare.** Dopo l'import di CEN/TS 18170 (backlog) e a ogni
import di una delle norme elencate: quei rinvii diventano relazioni possibili.

---

## 10. `evidence_type='textual'` — audit eseguito, 337 citazioni da esaminare

**In sospeso, con strumento.** Il 2026-09-28 è stato creato
`app/tools/verifica_relazioni_textual.py`: per ogni relazione dichiarata
`textual` di tipo `richiama` o `attua` verifica che il `testo_integrale` del nodo
citante contenga almeno una traccia del `riferimento` citato (id di requisito,
articolo con ordinale, clausola, annesso, punto).

**Esito del primo giro**: 1.243 relazioni `textual` esaminate, **337 senza
traccia** del riferimento citato. Distribuzione per fonte citante: Fonte 18
(ETSI EN 319 421) **155**, Fonte 21 (TS 119 612) 40, Fonte 17 (EN 319 411-1) 28,
Fonte 4 (DPCM 22/2/2013) 21, Fonte 20 (TS 119 432) 15, altre sotto 15.

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
per le relazioni future**: le 337 già nel grafo portano l'etichetta attribuita
dal default precedente e vanno riviste con lo strumento.

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
