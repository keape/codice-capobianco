# L'estrazione LLM degli obblighi avviene solo dentro sessioni Claude Code, mai come chiamata autonoma

Contesto: lo strumento deve generare bozze di Obbligo dal testo delle Fonti tramite LLM, poi farle validare da un umano in una coda di revisione nella UI web. Un'implementazione naturale farebbe girare l'estrazione come processo batch indipendente, con una propria API key verso un servizio LLM in cloud.

Deciso: l'estrazione è sempre avviata e guidata da una sessione Claude Code interattiva usata dall'utente (con il suo account già autenticato), tramite un tool MCP dedicato che scrive le bozze nella coda; la UI web non chiama mai un LLM per conto proprio, e nessun componente del sistema detiene una propria API key verso un servizio LLM esterno.

Perché: vincolo esplicito dell'utente — niente credenziali/API separate verso LLM in cloud per questa attività. La UI web resta quindi puramente di lettura/scrittura sul database (consultazione, revisione bozze, badge di monitoraggio), mai un chiamante autonomo di un modello.
