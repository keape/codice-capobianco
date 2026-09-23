"""Regolamento di esecuzione (UE) 2015/1502 della Commissione, dell'8
settembre 2015 - specifiche e procedure tecniche minime relative ai livelli
di garanzia dei mezzi di identificazione elettronica ex art. 8 §3 eIDAS.
Fonte 14 (non ancora inserita in Neo4j al momento della scrittura di questo
modulo). Questo capitolo copre l'allegato, punto 2.2 "Gestione dei mezzi di
identificazione elettronica" (sottosezioni 2.2.1-2.2.4) e punto 2.3
"Autenticazione" (paragrafo introduttivo + sottosezione 2.3.1). Testo
ufficiale in app/.source_cache/reg_ue_2015_1502/cap02.txt.

Modellazione (ADR-0007):
- Ognuna delle 4 sottosezioni 2.2.1-2.2.4 e la sottosezione 2.3.1 e' un
  singolo nodo Obbligo. Ogni sottosezione presenta nel testo ufficiale una
  tabella a tre righe (Basso/Significativo/Elevato) con colonne "Livello di
  garanzia" e "Elementi necessari" rese nel testo grezzo con il separatore
  letterale " | "; qui riformattata in prosa ("Livello Basso: ... Livello
  Significativo: ... Livello Elevato: ...") in `testo_integrale`, senza
  parafrasi/sintesi/omissione di alcuna prescrizione elementare - solo
  conversione da tabella a prosa (nessun contenuto normativo aggiunto o
  tolto). La sintesi in `testo` riflette le differenze sostanziali tra i tre
  livelli quando esistono (2.2.1, 2.2.2, 2.3.1: requisiti crescenti a ogni
  livello) e segnala esplicitamente quando due livelli coincidono testualmente
  (2.2.3: identico ai tre livelli; 2.2.4: Significativo identico a Basso,
  Elevato aggiunge un requisito).
- Soggetto obbligato: categoria "QTSP/gestore", ruolo "obbligato" - per
  coerenza con la convenzione gia' adottata per Fonte 5 (DPCM SPID) e Fonte
  13 (Regolamento modalita' attuative SPID) nello stesso grafo, dove il
  gestore/fornitore del mezzo di identificazione elettronica notificato e'
  mappato a questa categoria pur non essendo tecnicamente un prestatore di
  servizi fiduciari in senso stretto. Nessuna delle 5 righe individua un
  destinatario/beneficiario esplicito distinto (sono specifiche tecniche sul
  mezzo/processo, non garanzie procedurali verso un richiedente identificato)
  - nessuna riga "destinatario" aggiunta.
- tipo_obbligo: la sezione 2.2 "Gestione dei mezzi di identificazione
  elettronica" descrive per lo piu' processi del ciclo di vita del mezzo
  (rilascio/consegna/attivazione, sospensione/revoca/riattivazione,
  rinnovo/sostituzione) -> "organizzativo" per 2.2.2/2.2.3/2.2.4. Il punto
  2.2.1 ("Caratteristiche e concezione") descrive invece proprieta'
  tecniche intrinseche del mezzo stesso (numero/tipologia di fattori di
  autenticazione, resistenza a duplicazione/manomissione) -> "tecnico/
  sicurezza", stesso tipo del punto 2.3.1 (meccanismo di autenticazione:
  controlli di sicurezza contro guessing/intercettazione/replay/
  manipolazione, calibrati sul potenziale di attacco dell'aggressore
  Enhanced-Basic/Moderate/High) che e' inequivocabilmente un requisito
  tecnico/di sicurezza.
- Paragrafo introduttivo di 2.3 (prima della tabella 2.3.1): descrive
  l'oggetto della sezione ("minacce associate all'uso del meccanismo di
  autenticazione") e un criterio di proporzionalita' dei controlli ai
  rischi, senza imporre di per se' un comportamento distinto e verificabile
  ne' introdurre una definizione autonoma - e' testo di cornice/contesto
  per la tabella 2.3.1 che segue immediatamente (il paragrafo introduttivo
  di 2.3.1 stesso, "nella tabella riportata di seguito...", e' della stessa
  natura). Incorporato nella sintesi/testo_integrale del nodo 2.3.1 invece
  di diventare un nodo a se' stante, per due motivi: (1) a differenza dei
  paragrafi introduttivi di scopo/ambito trattati altrove come Principio
  autonomo (es. art. 1 di regolamenti-allegato precedenti), qui il paragrafo
  non e' associabile a un articolo/comma numerato proprio ma e' parte
  integrante dell'esposizione della sottosezione 2.3.1 (l'unica sottosezione
  di 2.3); (2) non contiene alcun elemento normativo autonomo separabile dal
  requisito tecnico che segue - e' criterio interpretativo ("i controlli si
  intendono proporzionati ai rischi") che si applica solo in combinazione
  con la tabella, non un principio isolabile con effetto giuridico proprio.
  Nessun nodo perso: il contenuto e' interamente presente, verbatim, in
  testo_integrale del nodo 2.3.1.
- RELAZIONI locali: nessuna. Le 5 righe sono materia tecnica autonoma senza
  sovrapposizione interna che giustifichi un arco "specifica"/"si applica
  a" tra loro (sono sottosezioni sorelle dello stesso punto 2.2/2.3, non
  l'una specificazione dell'altra). Nessuna relazione cross-fonte in questo
  modulo (demandata alla fase di collegamento a posteriori, ADR-0009).
"""

RIGHE_OBBLIGHI = [
    {
        'riferimento': 'allegato, punto 2.2.1',
        'testo': (
            "L'entita' che rilascia il mezzo di identificazione elettronica deve "
            "concepirlo secondo requisiti crescenti nei tre livelli di garanzia: al "
            "livello Basso e' richiesto almeno un fattore di autenticazione e misure "
            "ragionevoli per accertare l'uso esclusivo da parte del titolare; al "
            "livello Significativo sono richiesti almeno due fattori di "
            "autenticazione di categorie differenti e una concezione che presupponga "
            "l'uso esclusivo da parte del titolare; al livello Elevato, oltre ai "
            "requisiti del livello Significativo, il mezzo deve essere protetto "
            "contro duplicazione e manomissione (anche da aggressori con potenziale "
            "di attacco elevato) e deve poter essere protetto in modo affidabile dal "
            "titolare per evitarne l'uso da parte di terzi."
        ),
        'testo_integrale': (
            "2.2.1. Caratteristiche e concezione dei mezzi di identificazione "
            "elettronica.\n"
            "Livello Basso: 1. Il mezzo di identificazione elettronica utilizza "
            "almeno un fattore di autenticazione. 2. Il mezzo di identificazione "
            "elettronica e' concepito in modo tale che l'entita' che lo rilascia "
            "adotti ragionevoli misure per accertare che sia utilizzato "
            "esclusivamente dalla persona a cui appartiene o sotto il suo controllo.\n"
            "Livello Significativo: 1. Il mezzo di identificazione elettronica "
            "utilizza almeno due fattori di autenticazione appartenenti a categorie "
            "differenti. 2. Il mezzo di identificazione elettronica e' concepito in "
            "modo che si possa presupporre che sia utilizzato esclusivamente dalla "
            "persona a cui appartiene o sotto il suo controllo.\n"
            "Livello Elevato: Livello significativo, piu': 1. Il mezzo di "
            "identificazione elettronica e' protetto contro la duplicazione e la "
            "manomissione, nonche' contro gli aggressori con un potenziale di "
            "attacco elevato (High). 2. Il mezzo di identificazione elettronica e' "
            "concepito in modo da poter essere protetto in modo affidabile dalla "
            "persona a cui appartiene per evitare che venga utilizzato da altri "
            "utenti."
        ),
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 2.2.2',
        'testo': (
            "L'entita' che rilascia il mezzo di identificazione elettronica deve "
            "consegnarlo con garanzie crescenti nei tre livelli: al livello Basso il "
            "meccanismo di consegna deve solo consentire di presumere che il mezzo "
            "sia ricevuto unicamente dal destinatario previsto; al livello "
            "Significativo il meccanismo deve consentire di presumere che sia "
            "consegnato unicamente alla persona a cui il mezzo appartiene (legame "
            "piu' stretto con l'identita' del titolare, non solo col destinatario "
            "generico); al livello Elevato non basta la presunzione, il processo di "
            "attivazione deve verificare attivamente che il mezzo sia stato "
            "consegnato unicamente alla persona a cui appartiene."
        ),
        'testo_integrale': (
            "2.2.2. Rilascio, consegna e attivazione.\n"
            "Livello Basso: In seguito al rilascio, il mezzo di identificazione "
            "elettronica e' consegnato tramite un meccanismo che consente di "
            "presumere che sia ricevuto unicamente dal destinatario previsto.\n"
            "Livello Significativo: In seguito al rilascio, il mezzo di "
            "identificazione elettronica e' consegnato tramite un meccanismo che "
            "consente di presumere che sia consegnato unicamente alla persona a cui "
            "appartiene.\n"
            "Livello Elevato: Il processo di attivazione verifica che il mezzo di "
            "identificazione elettronica sia stato consegnato unicamente alla "
            "persona a cui appartiene."
        ),
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 2.2.3',
        'testo': (
            "L'entita' che rilascia il mezzo di identificazione elettronica deve "
            "garantire, con lo stesso identico requisito ai tre livelli di garanzia "
            "(basso, significativo, elevato - nessuna differenziazione tra i "
            "livelli per questo punto): la possibilita' di sospendere e/o revocare "
            "il mezzo in modo tempestivo ed efficace; l'esistenza di misure che "
            "impediscono sospensione, revoca e/o riattivazione non autorizzate; e "
            "che la riattivazione avvenga solo se continuano a essere soddisfatti "
            "gli stessi requisiti di garanzia stabiliti prima della sospensione o "
            "della revoca."
        ),
        'testo_integrale': (
            "2.2.3. Sospensione, revoca e riattivazione.\n"
            "Livello Basso: 1. E' possibile sospendere e/o revocare un mezzo di "
            "identificazione elettronica in modo tempestivo ed efficace. 2. Esistono "
            "misure che impediscono la sospensione, la revoca e/o la riattivazione "
            "non autorizzate. 3. La riattivazione e' eseguita solo se continuano ad "
            "essere soddisfatti gli stessi requisiti di garanzia stabiliti prima "
            "della sospensione o della revoca.\n"
            "Livello Significativo: Come per il livello Basso.\n"
            "Livello Elevato: Come per il livello Basso."
        ),
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 2.2.4',
        'testo': (
            "Per il rinnovo o la sostituzione del mezzo di identificazione "
            "elettronica, ai livelli Basso e Significativo (identici tra loro) "
            "l'entita' che lo rilascia deve, tenendo conto dei rischi di variazione "
            "dei dati di identificazione personale, applicare gli stessi requisiti "
            "di garanzia del controllo e della verifica dell'identita' iniziali, "
            "oppure basarsi su un mezzo di identificazione elettronica valido con "
            "lo stesso livello di garanzia o superiore; al livello Elevato, in "
            "aggiunta, se il rinnovo o la sostituzione si basa su un mezzo valido "
            "esistente, i dati identificativi devono essere in ogni caso verificati "
            "con una fonte autorevole."
        ),
        'testo_integrale': (
            "2.2.4. Rinnovo e sostituzione.\n"
            "Livello Basso: Tenendo conto dei rischi di variazione dei dati di "
            "identificazione personale, il rinnovo o la sostituzione deve "
            "soddisfare gli stessi requisiti di garanzia del controllo e della "
            "verifica dell'identita' iniziali oppure si basa su un mezzo di "
            "identificazione elettronica valido che presenti lo stesso livello di "
            "garanzia o un livello superiore.\n"
            "Livello Significativo: Come per il livello Basso.\n"
            "Livello Elevato: Livello basso, piu': Se il rinnovo o la sostituzione "
            "si basa su un mezzo di identificazione elettronica valido, i dati "
            "identificativi sono verificati con una fonte autorevole."
        ),
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 2.3.1',
        'testo': (
            "La presente sezione (2.3, incorporata in questo nodo insieme alla "
            "sottosezione 2.3.1 - vedi docstring del modulo) verte sulle minacce "
            "associate all'uso del meccanismo di autenticazione mediante il quale la "
            "persona fisica o giuridica utilizza il mezzo di identificazione "
            "elettronica per confermare la propria identita' alla parte facente "
            "affidamento, con controlli proporzionati ai rischi del livello. Ai tre "
            "livelli di garanzia, il meccanismo di autenticazione deve resistere a "
            "un potenziale di attacco crescente (Enhanced-Basic al livello Basso, "
            "Moderate al livello Significativo, High al livello Elevato) contro "
            "attacchi quali guessing, intercettazione, replay o manipolazione della "
            "comunicazione; al livello Basso e' inoltre richiesta la verifica "
            "affidabile del mezzo e della sua validita' prima della divulgazione dei "
            "dati di identificazione personale, con protezione di tali dati se "
            "memorizzati nel meccanismo (anche contro l'analisi offline); dal "
            "livello Significativo in su la verifica del mezzo prima della "
            "divulgazione dei dati deve avvenire tramite autenticazione dinamica."
        ),
        'testo_integrale': (
            "2.3. Autenticazione.\n"
            "La presente sezione verte sulle minacce associate all'uso del "
            "meccanismo di autenticazione ed elenca i requisiti per ciascun livello "
            "di garanzia. Ai fini della presente sezione i controlli si intendono "
            "proporzionati ai rischi che sussistono a un dato livello.\n"
            "2.3.1. Meccanismo di autenticazione.\n"
            "Nella tabella riportata di seguito sono elencati i requisiti fissati "
            "per ciascun livello di garanzia in relazione al meccanismo di "
            "autenticazione, mediante il quale la persona fisica o giuridica "
            "utilizza il mezzo di identificazione elettronica per confermare la "
            "propria identita' alla parte facente affidamento sulla certificazione.\n"
            "Livello Basso: 1. La divulgazione dei dati di identificazione "
            "personale e' preceduta dalla verifica affidabile del mezzo di "
            "identificazione elettronica e della sua validita'. 2. Qualora i dati di "
            "identificazione personale siano memorizzati nell'ambito del "
            "meccanismo di autenticazione, tali informazioni sono protette per "
            "evitarne la perdita o la compromissione, compresa l'analisi offline. "
            "3. Il meccanismo di autenticazione verifica il mezzo di "
            "identificazione elettronica attuando controlli di sicurezza che "
            "rendono altamente improbabile che tale meccanismo venga corrotto da "
            "attivita' quali gli attacchi di tipo guessing, le intercettazioni, gli "
            "attacchi di replicazione dati (replay) o la manipolazione di una "
            "comunicazione da parte di un aggressore con un potenziale di attacco "
            "di base avanzato (Enhanced-Basic).\n"
            "Livello Significativo: Livello basso, piu': 1. La divulgazione dei "
            "dati di identificazione personale e' preceduta dalla verifica "
            "affidabile del mezzo di identificazione elettronica e della sua "
            "validita' tramite un'autenticazione dinamica. 2. Il meccanismo di "
            "autenticazione verifica il mezzo di identificazione elettronica "
            "attuando controlli di sicurezza che rendono altamente improbabile che "
            "tale meccanismo venga corrotto da attivita' quali gli attacchi di tipo "
            "guessing, le intercettazioni, gli attacchi di replicazione dati "
            "(replay) o la manipolazione di una comunicazione da parte di un "
            "aggressore con un potenziale di attacco moderato (Moderate).\n"
            "Livello Elevato: Livello significativo, piu': Il meccanismo di "
            "autenticazione verifica il mezzo di identificazione elettronica "
            "attuando controlli di sicurezza che rendono altamente improbabile che "
            "tale meccanismo venga corrotto da attivita' quali gli attacchi di tipo "
            "guessing, le intercettazioni, gli attacchi di replicazione dati "
            "(replay) o la manipolazione di una comunicazione da parte di un "
            "aggressore con un potenziale di attacco elevato (High)."
        ),
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
]

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = [
    'allegato, punto 2.2.1',
    'allegato, punto 2.2.2',
    'allegato, punto 2.2.3',
    'allegato, punto 2.2.4',
    'allegato, punto 2.3.1',
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI = []
