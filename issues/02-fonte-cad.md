Type: research
Status: resolved

## Question

Individuare la fonte ufficiale, l'URL esatto e il formato disponibile (HTML/PDF) del testo del CAD (D.Lgs. 82/2005 e successive modifiche) su Normattiva. Verificare se Normattiva espone una struttura machine-readable articolo-per-articolo (es. tramite akoma-ntoso XML) o se il testo va segmentato a valle da HTML/PDF grezzo. Riportare come Normattiva espone il "testo vigente" vs le versioni storiche (utile per il meccanismo di confronto automatico tra versioni).

## Answer

Ricerca svolta via web search/fetch l'8/9/2026. Normattiva ha lanciato un portale Open Data (dati.normattiva.it) attivo dal 24/2/2026, con dati aperti dal 1/1/2026 — questo cambia significativamente lo scenario rispetto a una semplice consultazione HTML.

**1. URL esatto pagina CAD**

- URL canonico (URN-based, stabile nel tempo, consigliato come "URL sorgente" della Fonte): `https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82`
- Questo fa redirect alla pagina di dettaglio: `https://www.normattiva.it/atto/caricaDettaglioAtto?atto.dataPubblicazioneGazzetta=2005-05-16&atto.codiceRedazionale=005G0104` (titolo: "DECRETO LEGISLATIVO 7 marzo 2005, n. 82 - Codice dell'amministrazione digitale"). L'URN è preferibile come riferimento stabile perché i parametri `dataPubblicazioneGazzetta`/`codiceRedazionale` sono un dettaglio implementativo della UI classica.

**2. Formati machine-readable / API**

Sì, con due canali distinti:
- **Export per-atto sulla UI classica**: dalla pagina dell'atto è disponibile una funzione "Esporta" che produce HTML, XML (**Akoma Ntoso**), PDF, EPUB.
- **Nuovo portale Open Data (dati.normattiva.it)**, live da fine febbraio 2026: espone atti in formati "AKN, XML NIR, HTML, JSON e URI ELI", con API pensate esplicitamente per "interrogare la banca dati senza ricorrere allo scraping" e supporto a collezioni predefinite o dinamiche. **Non sono riuscito a verificare l'endpoint API esatto** (la home page `https://dati.normattiva.it/` è una SPA e il fetch non ha restituito la documentazione tecnica sottostante — servirebbe un'ispezione via browser reale o la documentazione IPZS collegata). Conferma indiretta dell'esistenza di un'API OpenData: il tool open-source `ondata/normattiva_2_md` (github.com/ondata/normattiva_2_md) ha un flag `--opendata` che "forza il download Akoma Ntoso via API OpenData (ZIP AKN)".
- Non trovata alcuna documentazione di un'API REST "classica" separata dal portale Open Data.

**3. Segmentabilità programmatica**

- **Con Akoma Ntoso XML: sì**, in modo pulito. Lo standard AKN definisce una gerarchia esplicita (capo/sezione, `<article>`, commi come sotto-elementi numerati, liste, definizioni) pensata proprio per l'estrazione programmatica; è lo standard adottato da Normattiva dal 2019 (circolare AGID 2/2019) in sostituzione del precedente markup XML "NIR".
- **Con HTML grezzo: no, servirebbe parsing ad-hoc fragile.** Ispezionando la pagina di dettaglio (`caricaDettaglioAtto`) non risultano classi CSS semantiche dedicate per articoli/commi. La struttura tipica osservata è: un albero di navigazione a sinistra (`<ul>`/`<li>` con link e icone, es. `link_v2.png`) che elenca gli articoli; nel corpo, i titoli articolo appaiono come intestazioni generiche (`<h1>`/`<h2>`, testo tipo "Art. 1", "Definizioni"); i commi sono paragrafi di testo prefissati da numerazione in chiaro ("1.", "1-bis.", "1-ter.") senza wrapper HTML dedicato; le lettere di elenco (a, b, c) sono testo semplice dentro paragrafi generici; le modifiche normative sono segnalate con doppie parentesi `(( ))` attorno al testo modificato/inserito e link alla norma modificante, mentre le disposizioni abrogate compaiono come "LETTERA SOPPRESSA" (spesso con barrato). **Raccomandazione**: usare l'export/API Akoma Ntoso come fonte primaria per il censimento, non l'HTML.

**4. Accesso a versioni storiche (multivigenza)**

Confermati due pattern URL equivalenti, entrambi con parametro data:
- **Formato URN**: si accoda `!vig=YYYY-MM-DD` all'URN-res, es. `https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2008-11-10;180!vig=2009-11-10` restituisce il testo in vigore in quella data.
- **Formato UI classica**: query string sulla pagina `caricaDettaglioAtto` con `tipoDettaglio=singolavigenza` (o `multivigenza` per la vista con storico completo) e `dataVigenza=DD%2FMM%2FYYYY` (data URL-encoded in formato gg/mm/aaaa), es. `...&tipoDettaglio=singolavigenza&dataVigenza=26%2F11%2F2025`.
- Questo pattern è direttamente utilizzabile per il meccanismo di confronto automatico: basta richiedere lo stesso atto con due valori di data diversi (o l'export AKN corrispondente, se il nuovo portale Open Data espone lo stesso parametro sull'API) e diffare il testo strutturato risultante.

**5. Licenza / vincoli di riuso**

- **UI classica normattiva.it (FAQ)**: "la riproduzione dei testi forniti in formato elettronico è consentita a condizione che ne sia citata la fonte e ne sia specificato il carattere non autentico e gratuito." I testi non hanno "carattere di ufficialità": in caso di discordanza prevale il testo della Gazzetta Ufficiale cartacea. Questo è già compatibile con un uso interno aziendale (basta mantenere traccia della fonte/data di estrazione, cosa già prevista dal modello dati come attributo "URL sorgente" della Fonte).
- **Nuovo portale Open Data**: dati rilasciati sotto licenza **Creative Commons CC BY 4.0** dal 1/1/2026, pensati esplicitamente per riuso strutturato da aziende, PA, ricercatori e sviluppatori. CC BY 4.0 richiede solo attribuzione, nessuna clausola ShareAlike o NonCommercial — pienamente compatibile con un uso interno non ridistribuito pubblicamente.
- Nessun vincolo trovato che impedisca l'uso interno aziendale in entrambi i regimi; l'unico obbligo pratico è mantenere la citazione della fonte (già coerente con l'attributo "URL sorgente ufficiale" previsto in CONTEXT.md).

**Fonti verificate**: normattiva.it (pagina atto, FAQ, guida all'uso), dati.normattiva.it, comunicato stampa IPZS (ipzs.it), articoli Ansa.it e sbircialanotizia.it sul lancio dell'Open Data, thread forum.italia.it (Andrea Borruso), repo github.com/ondata/normattiva_2_md.
