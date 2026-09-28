"""Regolamento di esecuzione (UE) 2025/1569 della Commissione, del 29 luglio
2025 — modalità di applicazione del regolamento (UE) n. 910/2014 (eIDAS2) per
quanto riguarda gli attestati elettronici qualificati di attributi (QEAA) e
gli attestati elettronici di attributi rilasciati da un organismo del settore
pubblico responsabile di una fonte autentica o per suo conto (artt. 45
quater-45 septies eIDAS2). Fonte 22 (id assegnato dal wiring della sessione
principale, questo modulo NON tocca seed.py).

Porzione di questo modulo (cap03 di 3, come da manifest di split): allegati
I-III. Testo ufficiale in app/.source_cache/reg_ue_2025_1569/cap03.txt
(fetch CELLAR, CELEX 32025R1569, italiano — vedi provenance.json).

Copertura ADR-0007 (nessun discrimine di rilevanza): 14 item di indice, uno
per ogni unità normativa della porzione — "allegato I"; "allegato II, punto
1"; il chapeau "allegato II, punto 2" e le sue tre lettere; il chapeau
"allegato II, punto 3" e le sue due lettere; "allegato III" con i suoi 4
punti. Un item, un nodo (l'unica riga che ne copre più di uno è quella
dell'allegato III, elenco puramente enumerativo: vedi sotto).

Modellazione, secondo i criteri specifici degli atti di esecuzione
(docs/plan-import-lotto-eidas2-standard.md §5) e le convenzioni del
censimento già in essere:

- Allegato I (norme di riferimento ex art. 3): una sola frase che NON è un
  elenco a punti ma una prescrizione unitaria ("rilasciano i rispettivi
  attestati ... conformemente alle specifiche ... stabilite nella norma ETSI
  EN 319 401 v3.1.1 (2024-06)") -> Obbligo (c'è un soggetto che agisce: i
  fornitori di attestati) e non Principio di mero rinvio come l'art. 1 del
  Reg. 2025/1566, che si limitava a designare l'allegato come sede delle
  norme. tipo_obbligo "organizzativo": ETSI EN 319 401 è la norma dei
  requisiti di politica generale del prestatore di servizi fiduciari
  (governance/policy), non un controllo tecnico puntuale.
- Allegato II punto 1 (formato): Obbligo "tecnico/sicurezza" (conformità di
  formato a una delle norme dell'allegato II del Reg. di esecuzione (UE)
  2024/2979). La nota a piè di pagina (1) — identificazione bibliografica
  completa dello stesso regolamento richiamato, agganciata al segnaposto
  "(1)" presente nel testo del punto — è riportata verbatim in coda al
  `testo_integrale` di questa riga (non è paratesto di pubblicazione come le
  righe finali "ELI:"/"ISSN", che restano escluse).
- Allegato II punti 2 e 3: chapeau e lettere hanno trattamento diverso perché
  hanno statuto diverso. I due chapeau ("Per il rilascio di attestati a
  persone fisiche o giuridiche, i fornitori ...:" / "Inoltre, se l'attestato è
  rilasciato a un portafoglio europeo di identità digitale, il fornitore
  dell'attestato:") non impongono un comportamento proprio e non hanno un
  soggetto obbligato distinto da quello delle lettere, ma dichiarano il caso
  di applicazione delle prescrizioni che seguono -> Principio, tipo
  "scopo/ambito di applicazione" (stessa logica con cui ADR-0007 censisce le
  disposizioni di cornice con un tipo dedicato invece di escluderle). Le
  lettere invece contengono ciascuna una prescrizione autonoma distinta
  (2(a) diritto di agire per conto, 2(b) identità della fonte autentica,
  2(c) insieme minimo di attributi; 3(a) autenticazione nell'unità di
  portafoglio, 3(b) verifica di revoca/sospensione) -> una riga per lettera,
  come da convenzione del batch. Il chapeau NON è ripetuto in ogni
  `testo_integrale` di lettera (niente duplicazione verbatim): il suo
  contenuto resta nel nodo Principio del punto e, dove è una condizione
  esplicita, in `condizione_applicabilita` della lettera.
- tipo_obbligo delle lettere: "procedurale" per 2(a)/2(b) (verifiche interne
  alla procedura di rilascio); "organizzativo" per 2(c) (limitazione del
  trattamento all'insieme minimo di attributi: regola di gestione del dato,
  non controllo di sicurezza); "tecnico/sicurezza" per 3(a)/3(b)
  (autenticazione verso l'unità di portafoglio e controllo dello stato di
  revoca/sospensione dell'unità, entrambi controlli tecnici).
- condizione_applicabilita: valorizzata su 2(a) e 2(b) con la formula
  condizionale testuale ("se del caso") e su 3(a)/3(b) con la condizione del
  chapeau del punto 3 (attestato rilasciato a un portafoglio europeo di
  identità digitale).
- Allegato III (notifiche ex art. 5): elenco puramente enumerativo — il
  chapeau contiene l'unica prescrizione ("Gli Stati membri notificano alla
  Commissione almeno:"), i punti 1)-4) ne sono il contenuto minimo, senza
  prescrizione autonoma per voce -> UNA sola riga Obbligo, con tutti e cinque
  gli item ("allegato III" e "allegato III, punto 1" ... "punto 4")
  indicizzati separatamente e mappati a quella riga, stesso trattamento
  riservato alle liste definitorie (art. 3 eIDAS). Soggetto obbligato:
  "Terza parte" — gli Stati membri sono il soggetto istituzionale con un
  ruolo identificabile (notificante), non "Terzi affidanti/pubblico"
  (riservato al pubblico indistinto). tipo_obbligo "informativo/trasparenza"
  (flusso informativo verso la Commissione). Il punto 4 cita l'art. 45
  septies §3 eIDAS2: nessuna relazione è costruita qui (vedi RELAZIONI).
- Titoli degli allegati ("Elenco delle norme di riferimento ...", "Specifiche
  tecniche per il rilascio ...", "Notifiche di cui all'articolo 5"): non sono
  unità normative ma intestazioni, quindi non producono nodi e non sono
  duplicate nel `testo_integrale` delle righe (stesso trattamento dei titoli
  di articolo negli altri moduli del censimento).
- Fedeltà al testo ufficiale: l'italiano della GU contiene un refuso nel
  punto 1 dell'allegato III ("lo Stato membro in cui il l'organismo del
  settore pubblico è stabilito"), riportato verbatim senza correzione
  (ADR-0010: mai ricostruire a memoria né "sistemare" la fonte).

RELAZIONI = [] per istruzione del batch: i collegamenti verso eIDAS/eIDAS2
(art. 45 quater-45 septies, art. 45 septies §3 citato dall'allegato III
punto 4), verso il Reg. di esecuzione (UE) 2024/2979 (allegato II punto 1) e
verso ETSI EN 319 401 (allegato I) li costruisce la sessione principale dopo
il dispatch dei capitoli, non questo modulo.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "allegato I",
        "testo": "Il rilascio di attestati elettronici qualificati di attributi (QEAA) e di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto avviene, da parte dei rispettivi fornitori, nei confronti di persone fisiche o giuridiche e conformemente alle specifiche per i prestatori di servizi fiduciari stabilite nella norma ETSI EN 319 401 v3.1.1 (2024-06).",
        "testo_integrale": "I fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto rilasciano i rispettivi attestati a persone fisiche o giuridiche conformemente alle specifiche per i prestatori di servizi fiduciari stabilite nella norma ETSI EN 319 401 v3.1.1 (2024-06) (\"ETSI EN 319 401\").",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato II, punto 1",
        "testo": "I fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto rilasciano i rispettivi attestati in un formato conforme a una delle norme elencate nell'allegato II del regolamento di esecuzione (UE) 2024/2979 della Commissione.",
        "testo_integrale": "I fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto rilasciano i rispettivi attestati in un formato conforme a una delle norme di cui all'allegato II del regolamento di esecuzione (UE) 2024/2979 della Commissione (1).\n\n(1) Regolamento di esecuzione (UE) 2024/2979 della Commissione, del 28 novembre 2024, recante modalità di applicazione del regolamento (UE) n. 910/2014 del Parlamento europeo e del Consiglio per quanto riguarda l'integrità e le funzionalità di base dei portafogli europei di identità digitale (GU L, 2024/2979, 4.12.2024, ELI: http://data.europa.eu/eli/reg_impl/2024/2979/oj).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato II, punto 2(a)",
        "testo": "Per il rilascio di attestati a persone fisiche o giuridiche, il fornitore verifica, se del caso, che il richiedente l'attestato abbia il diritto di agire per conto della persona cui si riferisce l'attestato.",
        "testo_integrale": "se del caso, verificano che il richiedente l'attestato abbia il diritto di agire per conto della persona cui si riferisce l'attestato;",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica \"se del caso\" (formula condizionale del testo): la verifica è dovuta solo ove il richiedente l'attestato abbia un diritto di agire per conto della persona cui l'attestato si riferisce.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato II, punto 2(b)",
        "testo": "Per il rilascio di attestati a persone fisiche o giuridiche, il fornitore verifica, se del caso, l'identità della fonte autentica utilizzata come fonte per gli attributi inclusi nell'attestato.",
        "testo_integrale": "se del caso, verificano l'identità della fonte autentica utilizzata come fonte per gli attributi inclusi nell'attestato;",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica \"se del caso\" (formula condizionale del testo): la verifica è dovuta solo ove gli attributi inclusi nell'attestato provengano da una fonte autentica.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato II, punto 2(c)",
        "testo": "Per il rilascio di attestati a persone fisiche o giuridiche, il fornitore tratta solo l'insieme minimo di attributi necessario per il rilascio e la gestione dell'attestato.",
        "testo_integrale": "trattano solo l'insieme minimo di attributi necessario per il rilascio e la gestione dell'attestato.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato II, punto 3(a)",
        "testo": "Se l'attestato è rilasciato a un portafoglio europeo di identità digitale, il fornitore dell'attestato si autentica nell'unità di portafoglio.",
        "testo_integrale": "si autentica nell'unità di portafoglio;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo se l'attestato è rilasciato a un portafoglio europeo di identità digitale (condizione del chapeau del punto 3).",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato II, punto 3(b)",
        "testo": "Se l'attestato è rilasciato a un portafoglio europeo di identità digitale, il fornitore dell'attestato verifica che l'unità di portafoglio non sia revocata o sospesa.",
        "testo_integrale": "verifica che l'unità di portafoglio non sia revocata o sospesa.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica solo se l'attestato è rilasciato a un portafoglio europeo di identità digitale (condizione del chapeau del punto 3).",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "allegato III",
        "testo": "Gli Stati membri notificano alla Commissione almeno: il nome dell'organismo del settore pubblico e, se del caso, il numero di registrazione quali utilizzati nei documenti ufficiali; lo Stato membro in cui l'organismo è stabilito; la normativa dell'Unione o nazionale in virtù della quale l'organismo è stabilito come responsabile della fonte autentica in base alla quale è rilasciato l'attestato elettronico di attributi oppure è designato ad agire per conto dell'organismo del settore pubblico responsabile della fonte autentica; l'e-mail e il numero di telefono di contatto dell'organismo; l'URL della pagina web dove sono reperibili ulteriori informazioni sull'organismo; la relazione di valutazione della conformità di cui all'articolo 45 septies, paragrafo 3, del regolamento (UE) n. 910/2014.",
        "testo_integrale": "Gli Stati membri notificano alla Commissione almeno:\n1) il nome dell'organismo del settore pubblico e, se del caso, il numero di registrazione quali utilizzati nei documenti ufficiali; lo Stato membro in cui il l'organismo del settore pubblico è stabilito; la normativa dell'Unione o nazionale in virtù della quale l'organismo del settore pubblico è stabilito come il responsabile della fonte autentica in base alla quale è rilasciato l'attestato elettronico di attributi oppure è designato ad agire per conto dell'organismo del settore pubblico responsabile della fonte autentica;\n2) l'e-mail e il numero di telefono di contatto dell'organismo del settore pubblico;\n3) l'URL della pagina web dove sono reperibili ulteriori informazioni sull'organismo del settore pubblico;\n4) la relazione di valutazione della conformità di cui all'articolo 45 septies, paragrafo 3, del regolamento (UE) n. 910/2014.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "allegato II, punto 2",
        "testo": "Le prescrizioni del punto 2 valgono per il rilascio di attestati a persone fisiche o giuridiche da parte dei fornitori di attestati elettronici qualificati di attributi e dei fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto.",
        "testo_integrale": "Per il rilascio di attestati a persone fisiche o giuridiche, i fornitori di attestati elettronici qualificati di attributi e i fornitori di attestati elettronici di attributi rilasciati da un organismo del settore pubblico responsabile di una fonte autentica o per suo conto:",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "allegato II, punto 3",
        "testo": "Quando l'attestato è rilasciato a un portafoglio europeo di identità digitale, al fornitore dell'attestato si applicano, in aggiunta a quelli del punto 2, gli adempimenti delle lettere a) e b).",
        "testo_integrale": "Inoltre, se l'attestato è rilasciato a un portafoglio europeo di identità digitale, il fornitore dell'attestato:",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "allegato I",
    "allegato II, punto 1",
    "allegato II, punto 2",
    "allegato II, punto 2(a)",
    "allegato II, punto 2(b)",
    "allegato II, punto 2(c)",
    "allegato II, punto 3",
    "allegato II, punto 3(a)",
    "allegato II, punto 3(b)",
    "allegato III",
    "allegato III, punto 1",
    "allegato III, punto 2",
    "allegato III, punto 3",
    "allegato III, punto 4",
]

MAPPATURA_LOCALE = {
    "allegato I": ["allegato I"],
    "allegato II, punto 1": ["allegato II, punto 1"],
    "allegato II, punto 2": ["allegato II, punto 2"],
    "allegato II, punto 2(a)": ["allegato II, punto 2(a)"],
    "allegato II, punto 2(b)": ["allegato II, punto 2(b)"],
    "allegato II, punto 2(c)": ["allegato II, punto 2(c)"],
    "allegato II, punto 3": ["allegato II, punto 3"],
    "allegato II, punto 3(a)": ["allegato II, punto 3(a)"],
    "allegato II, punto 3(b)": ["allegato II, punto 3(b)"],
    "allegato III": [
        "allegato III",
        "allegato III, punto 1",
        "allegato III, punto 2",
        "allegato III, punto 3",
        "allegato III, punto 4",
    ],
}

# Relazioni native. Allegato I rende vincolanti per il rilascio degli
# attestati le specifiche per i prestatori di servizi fiduciari di ETSI EN
# 319 401 v3.1.1: relazione verso la clausola di ambito della Fonte 10 (non
# verso un requisito puntuale, perche' il rinvio e' alla norma nel suo
# insieme). Allegato III punto 4 richiama testualmente la relazione di
# valutazione della conformita' di cui all'art. 45 septies §3 eIDAS2.
RELAZIONI = [
    {
        'nodo_da': ('obbligo', None, 'allegato I'),
        'nodo_a': ('principio', 10, 'clausola 1 (Scope)'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato III'),
        'nodo_a': ('principio', 2, 'art. 45 septies §3'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
]
