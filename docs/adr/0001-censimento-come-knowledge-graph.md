# Il censimento è un knowledge graph di Obblighi, non una tabella piatta

Contesto: il censimento deve rappresentare relazioni tra obblighi provenienti da fonti e momenti diversi (una fonte che ne sostituisce un'altra, un obbligo generale specificato da uno più tecnico, obblighi sovrapposti tra fonti senza gerarchia, precondizioni, condizionalità). Una tabella con un campo "riferimenti incrociati" come lista di link avrebbe potuto bastare per un primo censimento semplice.

Deciso: gli Obblighi sono nodi di un grafo, collegati da relazioni tipizzate ed esplicitamente navigabili (sostituisce/è sostituito da, specifica/è specificato da, si sovrappone a/duplica, richiede come precondizione, è condizionato da/condiziona), non un campo testuale libero.

Perché: l'utente ha indicato la visualizzazione e navigazione di queste relazioni come un asset di lavoro importante fin dal pilota, non un'estensione futura — in particolare per orientarsi tra fonti diverse (eIDAS/CAD) e nel tempo (transizione eIDAS→eIDAS2). Passare da tabella a grafo dopo che il censimento è popolato richiederebbe ri-modellare le relazioni già inserite come testo libero, quindi la scelta va fissata prima del popolamento dei dati, non dopo.
