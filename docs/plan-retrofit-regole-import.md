# Piano di retrofit — regole di import e adattamenti degli strumenti

Creato il 2026-09-29. Serve a due cose: **tenere traccia delle regole di import** che sono
state precisate strada facendo (così il prossimo import non le reinventa) e **elencare le
correzioni da fare sulle Fonti già censite** quando una regola nuova le riguarda. Ogni voce
ha uno stato: `fatto`, `da fare`, `da valutare per fonte`.

Regola di manutenzione: quando una regola nuova viene applicata a una Fonte già importata,
la voce passa a `fatto` con il commit; quando una regola è applicata solo agli import
futuri, la voce resta `da fare` e dice esattamente cosa toccare.

---

## 1. Regole di import precisate in questo ciclo

### 1.1 Granularità fine per le voci enumerate (decisione dell'utente, 2026-09-29)

**Regola**: ogni voce enumerata che porta una **prescrizione** ha una riga propria — passi
`1)` `2)` `3)`…, lettere `a)` `b)` `c)`…, qualifier, elenchi indicizzati — **anche quando il
documento non la richiama per numero altrove**. Restano nella riga della clausola/comma solo
le intestazioni di puro raggruppamento e le parti non prescrittive (elenchi di documenti,
tabelle informative, rubriche).

**Perché**: l'obiettivo è poter dire *quale singolo aspetto* di un requisito è stato violato
e collegarlo a un obbligo esterno. Una clausola intera non lo permette.

**Dove è scritta**: `docs/procedura-import-granulare.md` § 3 (dispatch dei worker) e
`docs/verifiche-aperte.md` § 3-bis (criterio dei tipi). Vale per tutte le Fonti, non solo
per gli standard tecnici: per la normativa nazionale la stessa regola era già in uso (le
lettere con precetto autonomo sono righe separate), ma va riapplicata con questo metro.

### 1.2 La lingua non blocca la relazione (2026-09-29)

Il censimento tiene i `riferimento` in forma italiana convenzionale; il testo citante cita
nella propria lingua (inglese per gli standard ETSI). Un rinvio fra testi in lingue diverse
è una relazione legittima, e l'audit accetta come traccia la forma italiana e quella
inglese. Dettagli in `docs/procedura-import-granulare.md` § 2-bis.

### 1.3 Riferimenti e tipi delle relazioni cross-fonte: si risolvono, non si scrivono

Un `riferimento` o un `tipo` di nodo scritto a mano in una Fase 6 si sbaglia (è successo due
volte il 2026-09-29, fermato dal preflight). Vanno risolti leggendo i moduli della Fonte
bersaglio (`prefisso → (tipo, riferimento)`), come fa il generatore della parte meccanica.
Strumento dedicato: punto 2.4 sotto.

---

## 2. Adattamenti degli strumenti: registro

| # | adattamento | stato | dove |
|---|---|---|---|
| 2.1 | Tracce bilingui, plurali, numerazione nuda, id ASN.1, nomi di tipo nell'audit | **fatto** (`33182cf`) | `app/tools/verifica_relazioni_textual.py` |
| 2.2 | Partizioni per gli annessi ETSI (`Annex A.1.1.1` → `Annex A, clausola A.1.1` → `Annex A`) | **fatto** (`87f2675`) | `neo4j_common.partizioni_di` |
| 2.3 | Il preflight risolve i bersagli di tipo partizione | **fatto** (`032a85d`) | `app/tools/preflight_relazioni.py` |
| 2.4 | **Risolutore di riferimenti** cross-fonte (prefisso + Fonte → tipo e riferimento esatti) | **da fare** | nuovo `app/tools/risolvi_riferimenti.py` |
| 2.5 | **Split dei PDF ETSI dentro il repo** (filtro testatine/piedini, taglio del front matter, capitoli limitati per dimensione, controllo di copertura con differenza zero) | **da fare — priorità alta** | nuovo `app/tools/split_pdf.py` |
| 2.6 | **Fetch ETSI dentro il repo** (ultima edizione pubblicata `_60` sul deliver, download PDF, `pdftotext -layout`, `provenance.json`) | **da fare** | nuovo `app/tools/etsi_fetch.py`, accanto a `cellar_fetch.py` |
| 2.7 | **Forme di citazione non riconosciute dall'audit**: citazione di una *lettera* o di un *passo* di requisito («references in 1) and 3)», «step d)», «requirement a)»), parole spezzate a fine riga dal PDF | **da fare** | `app/tools/verifica_relazioni_textual.py` |
| 2.8 | **Retrofit delle Fonti del lotto 1** sui rinvii generici ancorati a una clausola di ambito: con ADR-0012 possono puntare all'unità corretta | **da valutare per fonte** | moduli `cap*_relazioni_cross.py` di Fonti 12, 22, 23, 24 |

Oggi gli strumenti 2.5, 2.6 e 2.4 vivono in file temporanei: se sparissero, il prossimo
standard si taglierebbe di nuovo male (è già successo una volta). Sono i primi tre da
portare nel repository.

---

## 3. Retrofit da fare sulle Fonti già censite

### 3.1 Granularità fine: dove la regola non è stata applicata

Misura di partenza (2026-09-29, conteggio dei nodi il cui `testo_integrale` contiene un
elenco enumerato — lettere o numeri — su tutte le 32 Fonti):

| Fonte | nodi con elenchi nel testo | lettura |
|---|---|---|
| 27 ETSI EN 319 102-1 | 23 | candidata: nodi di clausola che contengono passi/lettere prescrittive |
| 32 XAdES | 22 | **certa**: `cap04.py` e `cap05.py` tengono i passi numerati dentro la sottoclausta |
| 3 CAD | 21 | da valutare (normativa: la convenzione "lettere autonome = righe separate" è già in uso) |
| 26 ETSI TS 119 101 | 21 | candidata (granularità a id di controllo già fine; verificare le clausole 9-10) |
| 2 eIDAS2 | 17 | da valutare (le lettere dell'art. 5 bis §4 sono già righe separate) |
| 13 Reg. AgID SPID | 14 | da valutare |
| 1 eIDAS | 12 | da valutare |
| 21 ETSI TS 119 612 | 11 | candidata (118 nodi su 289k caratteri: granularità grossolana) |
| 31 CAdES | 11 | **certa**: stessa verifica di XAdES su `cap03.py`-`cap08.py` |
| 30, 28, 29, 23, 25, 20, 22, 16 | 1-7 ciascuna | da valutare caso per caso |

**Metodo di decisione**, per ogni nodo candidato: (a) gli item enumerati hanno già righe
proprie? se sì, il nodo è a posto; (b) gli item portano una prescrizione? se no (elenco di
documenti, tabella informativa, definizioni) restano nel nodo; (c) se portano prescrizione e
non hanno riga propria, si scompongono. La misura sopra è un tetto massimo, non un elenco di
lavoro: il conteggio vero si ottiene applicando (a)-(c).

Ordine proposto: prima XAdES (32) e CAdES (31), che sono fresche e di cui conosco i moduli;
poi le ETSI grossolane (27, 21, 26); poi la normativa, dove la convenzione è già in uso e la
verifica sarà in gran parte confermativa.

**Avvertenza sui numeri**: applicare la regola aumenta i nodi (indicativamente +10-20% sulle
fonti che enumerano molto) e quindi le righe in coda di validazione. È il prezzo già scelto
per avere il dettaglio di quale singolo aspetto è violato.

### 3.2 Altri retrofit

- **Riferimenti generici ancorati a mano** (voce 2.8): Fonti 12, 22, 23, 24 hanno relazioni
  scritte prima di ADR-0012, con rinvii generici agganciati a una clausola di ambito; vanno
  riportati all'unità corretta (partizione). Meccanico.
- **Forme di citazione di lettera/passo** (voce 2.7): 11 segnalazioni su Fonte 32 e le
  analoghe su Fonte 31 restano in coda all'audit § 10 finché l'audit non riconosce quella
  forma. Non sono etichette gonfiate: sono citazioni letterali in una forma che lo strumento
  non cerca.
- **Relazioni `textual` fra oggetti ASN.1 di Annex D** (Fonte 31, 6 casi): sostenute da
  dipendenza strutturale, non da citazione: da rileggere con probabile declassamento a
  `inferred` (voce già aperta in `docs/verifiche-aperte.md` § 10).

---

## 4. Stato di avanzamento

- **fatto**: 2.1, 2.2, 2.3 (strumenti); regola 1.2 in procedura.
- **da fare subito**: 2.5, 2.6, 2.4 (portare gli strumenti nel repo) — sono la condizione
  perché il resto sia riproducibile.
- **poi**: 3.1 su Fonti 32 e 31; 2.7 (forme di citazione); 2.8 e 3.2 (retrofit lotto 1).
- **poi**: ripresa del blocco B — PAdES, ASiC, JAdES — con la regola 1.1 scritta nei prompt
  dei worker senza discrezionalità.
