Type: research
Status: resolved

## Question

Individuare la fonte ufficiale, l'URL esatto e il formato disponibile (HTML/PDF/XML) del testo di eIDAS (Regolamento (UE) 910/2014) e di eIDAS2 (Regolamento (UE) 2024/1183) su EUR-Lex. Verificare se EUR-Lex espone già una struttura machine-readable articolo-per-articolo (es. tramite l'API EUR-Lex o un formato XML strutturato) o se il testo va segmentato in articoli a valle da testo HTML/PDF grezzo. Riportare anche se e come EUR-Lex espone lo storico delle versioni (utile per il meccanismo di confronto automatico tra versioni).

## Answer

Verificato navigando direttamente le pagine EUR-Lex (non solo tramite ricerca web) l'8/9/2026.

### 1. URL esatti

- **eIDAS (Reg. (UE) 910/2014)**, atto originale, tutte le lingue/formati:
  `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R0910`
  (CELEX `32014R0910`). Pagina che elenca anche le versioni consolidate disponibili (18/10/2024, 20/05/2024, 17/09/2014).
- **eIDAS2 (Reg. (UE) 2024/1183)**, atto che modifica il 910/2014:
  `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1183`
  (CELEX `32024R1183`; pubblicato in OJ L, 2024/1183, 30.4.2024; ELI `http://data.europa.eu/eli/reg/2024/1183/oj`).
- **Versione consolidata corrente di eIDAS** (già integra le modifiche di eIDAS2 e successive, aggiornata al 18/10/2024), utile come "testo vigente" di riferimento per l'estrazione:
  `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02014R0910-20241018`
  (nota il CELEX consolidato con prefisso `0` e suffisso data `-YYYYMMDD`; esiste anche in forma ELI: `https://eur-lex.europa.eu/eli/reg/2014/910/2024-10-18/eng`).

### 2. Formati machine-readable disponibili

- Ogni documento è scaricabile in **HTML** e **PDF** dalla pagina "Text" (link diretti tipo `.../TXT/HTML/?uri=...` e `.../TXT/PDF/?uri=...`).
- Il formato XML strutturato ufficiale della Publications Office è **Formex** (usato per i testi pubblicati in Gazzetta Ufficiale); è convertibile in **Akoma Ntoso** (profilo AKN4EU) — ma questa conversione non è esposta come output diretto scaricabile per singolo atto dalla pagina EUR-Lex standard, è più un formato di scambio/interno.
- Esiste un repository dati comune, **Cellar**, con due interfacce ufficiali:
  - **SPARQL endpoint** per interrogare i metadati (relazioni tra atti, versioni, date, ecc.) — query su tutta la base di conoscenza RDF/CDM.
  - **REST API di Cellar** per recuperare il contenuto dei documenti (HTML, PDF, Formex) a partire dagli identificativi.
  Non è un'unica "API EUR-Lex" con un solo endpoint semplice: serve capire l'identificativo CELEX/ELI e poi interrogare Cellar. Esiste anche un "Webservice" EUR-Lex in XML per utenti registrati, e bulk download (data dump) per scaricare in blocco tutti gli atti in vigore.
- **Non trovato**: un endpoint che restituisca direttamente "l'Articolo N di 32014R0910 in JSON/XML segmentato" pronto all'uso senza passare da Cellar/Formex o dal parsing dell'HTML.

### 3. Segmentabilità in articoli/commi

**La pagina HTML della versione consolidata è già segmentata semanticamente per articolo**, verificato ispezionando il DOM di `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02014R0910-20241018`:

- Ogni articolo è un `<div class="eli-subdivision" id="art_N">` (es. `id="art_1"`, `id="art_5a"` per articoli aggiunti da eIDAS2, `id="art_11a"`, ecc. — la lettera suffissa indica un articolo inserito da un emendamento successivo all'originale).
- Il titolo dell'articolo è in `<p class="title-article-norm">Article&nbsp;1</p>` seguito da `<div class="eli-title" id="art_1.tit_1"><p class="stitle-article-norm">Subject matter</p></div>`.
- Il testo normativo di un paragrafo è in `<p class="norm">...</p>`.
- Liste puntate (es. lettere a), b), c)) sono marcate con `<div class="grid-container grid-list"><div class="grid-list-column-1"><span>(a)&nbsp;</span></div><div class="grid-list-column-2"><p class="norm">testo...</p></div></div>`.
- Non è stato verificato in questa sessione il markup esatto per i commi numerati (1., 2., 3. dentro un articolo — probabile pattern analogo con id tipo `art_N.pnum_M`), ma la struttura ad albero con classi `eli-subdivision`/`eli-title`/`norm` rende la segmentazione programmatica per articolo **affidabile via parsing HTML/CSS-selector mirato** (niente Formex/Akoma Ntoso necessario per il pilota) — non serve un parsing ad-hoc su PDF grezzo.
- Le modifiche storiche sono visibili inline con marcatori tipo `▼M2` (rimando alla nota di modifica), utile per capire quale versione ha introdotto/modificato un articolo.

**Conclusione pratica per il progetto**: usare la versione HTML consolidata (`TXT/HTML/?uri=CELEX:02014R0910-YYYYMMDD`) e segmentare via selettore su `div.eli-subdivision[id^="art_"]`, escludendo i div con id contenente `.tit_` per isolare solo il contenitore di primo livello di ciascun articolo.

### 4. Storico versioni consolidate

Sì. La pagina del documento (es. `.../TXT/?uri=CELEX:32014R0910`) mostra un pannello "Hide/Show consolidated versions" con l'elenco delle date di consolidamento disponibili (per eIDAS, verificate: 17/09/2014 - atto originale, 20/05/2024, 18/10/2024 - versione corrente dopo eIDAS2). Ogni versione consolidata ha un proprio CELEX (`0` + CELEX originale + `-YYYYMMDD`) e una propria pagina, quindi è possibile:
- accedere a una versione storica specifica via `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02014R0910-YYYYMMDD` (sostituendo la data),
- oppure via ELI: `https://eur-lex.europa.eu/eli/reg/2014/910/YYYY-MM-DD/eng`.
Questo pattern URL prevedibile è utilizzabile per un job di monitoraggio periodico (poll sulla pagina CELEX principale per rilevare nuove date di consolidamento, poi fetch della nuova versione datata per il diff).

**Nota importante**: EUR-Lex stessa segnala che le versioni consolidate "hanno valore puramente documentale" (documentary value only) — solo il testo pubblicato in Gazzetta Ufficiale (OJ) è autentico e fa fede legalmente. Per il censimento va bene usare la consolidata come fonte di lavoro, ma il riferimento legale ultimo resta l'OJ.

### 5. Licenza/riuso

Verificato su `https://eur-lex.europa.eu/content/legal-notice/legal-notice.html`:

- **Copyright**: "© European Union, 1998-2026". La politica di riuso della Commissione si basa sulla **Decisione 2011/833/UE**: "Unless otherwise specified, you can re-use the legal documents published in EUR-Lex for commercial or non-commercial purposes."
- Il contenuto editoriale, i riassunti di legislazione UE e **i testi consolidati** sono specificamente sotto licenza **Creative Commons Attribution 4.0 International (CC BY 4.0)**: riuso consentito citando la fonte e indicando eventuali modifiche.
- I **metadati** EUR-Lex sono dedicati al pubblico dominio con **CC0 1.0**.
- Eccezioni: contenuti che coinvolgono persone fisiche identificabili o opere di terzi possono richiedere permessi aggiuntivi; software/marchi/loghi coperti da proprietà industriale sono esclusi dalla policy di riuso; il logo EUR-Lex richiede consenso preventivo per l'uso.
- **Per un uso interno aziendale (non redistribuzione pubblica)** come quello previsto dal progetto (estrazione di obblighi in un knowledge graph interno, nessuna ripubblicazione del testo integrale al pubblico): nessun vincolo di licenza risulta bloccante. È comunque buona prassi mantenere nel censimento l'attribuzione alla fonte (URL EUR-Lex + CELEX) già prevista come metadato della Fonte nel modello di dominio (CONTEXT.md), il che soddisfa comunque il requisito di attribuzione della CC BY 4.0 anche se non fosse strettamente necessario per uso puramente interno.
