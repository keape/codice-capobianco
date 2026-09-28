"""Regolamento di esecuzione (UE) 2025/1567 della Commissione, del 29 luglio
2025 - modalita' di applicazione del regolamento (UE) n.910/2014 per quanto
riguarda la gestione di dispositivi qualificati per la creazione di una firma
elettronica a distanza e di dispositivi qualificati per la creazione di un
sigillo elettronico a distanza come servizi fiduciari qualificati.

Fonte 12 (unico id libero della tabella `fonti`: il 12 era la ex-Fonte
"ETSI TS 119 431-2", consolidata nella Fonte 11 il 2026-09-23). Atto breve
(2 articoli + allegato di 7 punti di adeguamento: ~9.700 caratteri), quindi
un solo capitolo, estratto direttamente in sessione principale senza
subagent/split_source.py - stesso criterio gia' applicato a Fonte 6 (DPCM
19/10/2021), Fonte 7 (ETSI EN 319 412-5) e Fonte 8 (Reg. 2025/1566).

Testo ufficiale (italiano) in app/.source_cache/reg_ue_2025_1567/raw.txt,
acquisito con app/tools/cellar_fetch.py il 2026-09-28:

    app/.venv/bin/python app/tools/cellar_fetch.py 32025R1567 reg_ue_2025_1567

Provenienza registrata in provenance.json: content negotiation CELLAR
(publications.europa.eu/resource/celex/32025R1567, Accept-Language: ita),
url risolto .../cellar/8a505cff-6cdd-11f0-bf4e-01aa75ed71a1.0014.03/DOC_1,
9.702 caratteri, sha256 cf96443c8d206865… (integrale nel file di
provenienza). Non e' stata usata l'interfaccia web di EUR-Lex: risponde a
una fetch non interattiva con una challenge JavaScript e non e' leggibile in
modo automatico.

Modellazione (ADR-0007, nessun discrimine di rilevanza):
- Preambolo (considerando 1-8) -> nessun nodo, come in tutte le Fonti gia'
  censite; la formula di chiusura dell'art. 2 comma 3 ("obbligatorio in tutti
  i suoi elementi e direttamente applicabile in ciascuno degli Stati
  membri") -> nessun nodo, stesso criterio del Reg. 2025/1566 (elemento di
  formattazione dell'atto, non un comma con contenuto normativo proprio).
- Art. 1 (designa l'allegato come sede delle norme di riferimento ex art. 29
  bis §2 e art. 39 bis eIDAS2) -> Principio, tipo "altro": e' una
  disposizione di mero rinvio/designazione, non definitoria ne' di
  scopo/ambito (stesso trattamento dell'art. 1 del Reg. 2025/1566).
- Art. 2 commi 1 e 2 -> due nodi Principio distinti ("entrata in vigore" e
  "applicazione differita al 19 agosto 2027"): fatti giuridici autonomi, con
  spazio temporale di vigenza diverso (lo stesso atto entra in vigore il
  20esimo giorno dopo la pubblicazione ma si applica 24 mesi dopo) - stesso
  criterio dell'art. 2 del Reg. 2025/1566 e dell'art. 52 §1/§2 eIDAS.
- Allegato, chapeau (designa ETSI TS 119 431-1 V1.3.1 come norma rispetto a
  cui valutare la conformita' del servizio applicativo EU Server Signing
  Application Service v2 Policy, conformemente all'allegato A, "con i
  seguenti adeguamenti") -> Principio tipo "altro".
- Allegato, punto 1 (aggiunge alla clausola 2.1 "Riferimenti normativi" della
  norma il riferimento a ETSI EN 319 401 V3.1.1 e ai meccanismi
  crittografici concordati ENISA) -> Principio tipo "altro": aggiunta
  bibliografica senza comportamento imposto (stesso trattamento del punto 1
  dell'allegato del Reg. 2025/1566).
- Allegato, punti 2-7 -> Obbligo, un nodo **per ogni requirement id**
  effettivamente introdotto dall'atto (OVR-6.1-04; OVR-6.4.4-02 e -03;
  OVR-6.4.9-02; OVR-6.5.5-02 e -03; OVR-6.8.5-01 e -02; OVR-A.3-02): la
  granuralita' e' quella dei requisiti numerati della norma che l'atto
  adegua, la stessa con cui e' gia' censita la Fonte 11 (un nodo per id
  REQ-/PRO-/OVR-). I 7 punti dell'atto non sono quindi 7 nodi ma 9: i punti
  3, 5 e 6 introducono due requisiti autonomi ciascuno (contenuto
  indipendente, non due frasi dello stesso precetto - es. OVR-6.4.4-02
  richiede personale qualificato, OVR-6.4.4-03 impone aggiornamenti almeno
  annuali sulle minacce: due obblighi distinti). Soggetto obbligato sempre
  "QTSP/gestore" (il prestatore che offre il servizio SSASP), tranne
  nessuno: nessun punto di questo atto impone obblighi a terze parti
  (organismo di valutazione/laboratorio), a differenza dei punti 3 e 5
  dell'allegato del Reg. 2025/1566.
- `condizione_applicabilita` valorizzata su tutti e 9 gli obblighi: gli
  adeguamenti valgono nell'ambito della valutazione di conformita' del
  servizio applicativo SSASP alla EU SSASP v2 Policy, conformemente
  all'allegato A di ETSI TS 119 431-1 (chapeau dell'allegato).
- `tipo_obbligo` allineato al nodo corrispondente della Fonte 11 dove
  esiste (OVR-6.1-04 "informativo/trasparenza"; OVR-6.4.4-01 e OVR-6.4.9-01
  "organizzativo"; OVR-6.5.5-01 "tecnico/sicurezza"; OVR-A.3-02
  "informativo/trasparenza"), per non introdurre un'incoerenza di
  classificazione tra l'originale e il suo adeguamento.

Copertura: 14 item di indice, 14 righe (5 Principi + 9 Obblighi) - un nodo
per articolo/comma e per requirement id introdotto, con l'unica esclusione
documentata della formula di chiusura.

Relazioni native (12), tutte di citazione letterale nel testo dell'atto, non
differite a Fase 6:
- art. 1 -> "attua" verso eIDAS2 "art. 29 bis §2" e "art. 39 bis" (base
  giuridica abilitante, citata nei "visti" e ripresa testualmente dall'art.
  1);
- allegato, chapeau -> "specifica" verso ETSI TS 119 431-1 "Parte 1:
  clausola 1 (Scope)": l'atto non ripete il contenuto della norma ma ne
  rende operativo l'ambito per la valutazione di conformita' (policy
  EUSPv2/SSASP, allegato A);
- ai punti 2, 3, 4, 5 e 7 l'atto *integra* una clausola gia' presente nella
  norma censita -> "modifica" verso il requisito esistente della stessa
  clausola (OVR-6.1-04; OVR-6.4.4-01 per entrambi i requisiti aggiunti
  nella clausola 6.4.4; OVR-6.4.9-01; OVR-6.5.5-01 per entrambi quelli
  della clausola 6.5.5; OVR-A.3-02, di cui l'atto da' la versione italiana
  ufficiale della stessa prescrizione). "Modifica" e non "sostituisce"
  perche' il requisito della norma resta applicabile e viene affiancato,
  non interamente superato (definizione di CONTEXT.md);
- punto 4 -> "richiama" verso eIDAS2 "art. 24 §5" (citazione testuale degli
  atti di esecuzione sul piano di cessazione);
- punto 5 (OVR-6.5.5-02) -> "richiama" verso (Fonte 10) "REQ-7.8-13"
  (citazione letterale dell'id di ETSI EN 319 401 nella clausola 6.5.5).

Nessuna relazione nativa per il punto 6 (clausola 6.8.5 "Controlli
crittografici"): la Fonte 11 non ha un nodo per quella clausola (i nodi
contigui sono 6.8.1-01, 6.8.3-01, 6.8.4-01 e "clausola 6.8.2 (Additional
testing)" - nessuno dei quali e' semanticamente il requisito integrato), e
la regola anti-allucinazione vieta di agganciare il nodo al piu' vicino solo
perche' tale. Il rinvio del punto 1 e del punto 6 al documento ENISA "Agreed
Cryptographic Mechanisms" non produce relazione per assenza di nodo
controparte nel grafo (documento ENISA, non fonte censita).

Fase 6 (ADR-0009): vedi il docstring di cap02_relazioni_cross.py (8
relazioni cross-fonte validate, pipeline ed esito completo, incluse le
proposte scartate).
"""

RIGHE_OBBLIGHI = [
    {
        'riferimento': 'allegato, punto 2 (OVR-6.1-04)',
        'testo': "Le informazioni individuate da OVR-6.1-01 (clausola 6.1 della norma, responsabilità delle pubblicazioni e dell'archivio) sono disponibili al pubblico e a livello internazionale.",
        'testo_integrale': "2) 6.1 Responsabilità delle pubblicazioni e dell'archivio — OVR-6.1-04: Le informazioni individuate in OVR-6.1-01 sono disponibili al pubblico e a livello internazionale.",
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'condizione_applicabilita': "Adeguamento della clausola 6.1 di ETSI TS 119 431-1: si applica nell'ambito della valutazione di conformità del servizio applicativo SSASP alla EU SSASP v2 Policy, conformemente all'allegato A di tale norma (il regolamento si applica dal 19 agosto 2027).",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 3 (OVR-6.4.4-02)',
        'testo': "Il servizio SSASP impiega personale in ruoli di fiducia, e se del caso subappaltatori in ruoli di fiducia, che possiede le conoscenze specialistiche, l'esperienza e le qualifiche necessarie, sulla base di formazione e credenziali formali, di esperienza, o di una loro combinazione.",
        'testo_integrale': "3) 6.4.4 Controlli del personale — OVR-6.4.4-02: Il servizio SSASP impiega personale in ruoli di fiducia e, se del caso, subappaltatori in ruoli di fiducia, che possiedono le conoscenze specialistiche, l'esperienza e le qualifiche necessarie sulla base di formazione e credenziali formali o dell'esperienza, o di una loro combinazione.",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'condizione_applicabilita': "Adeguamento della clausola 6.4.4 di ETSI TS 119 431-1: si applica nell'ambito della valutazione di conformità del servizio applicativo SSASP alla EU SSASP v2 Policy, conformemente all'allegato A di tale norma (il regolamento si applica dal 19 agosto 2027).",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 3 (OVR-6.4.4-03)',
        'testo': "La conformità a OVR-6.4.4-02 comprende aggiornamenti periodici delle conoscenze del personale, almeno ogni 12 mesi, sulle nuove minacce e sulle pratiche di sicurezza vigenti.",
        'testo_integrale': "— OVR-6.4.4-03: La conformità a OVR-6.4.4-02 comprende aggiornamenti periodici (almeno ogni 12 mesi) sulle nuove minacce e sulle pratiche di sicurezza vigenti.",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'condizione_applicabilita': "Adeguamento della clausola 6.4.4 di ETSI TS 119 431-1: si applica nell'ambito della valutazione di conformità del servizio applicativo SSASP alla EU SSASP v2 Policy, conformemente all'allegato A di tale norma (il regolamento si applica dal 19 agosto 2027).",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 4 (OVR-6.4.9-02)',
        'testo': "Il piano di cessazione del servizio SSASP è conforme agli atti di esecuzione adottati a norma dell'art. 24 §5 del regolamento (UE) n.910/2014.",
        'testo_integrale': "4) 6.4.9 Cessazione del servizio SSASP — OVR-6.4.9-02: Il piano di cessazione del servizio SSASP è conforme agli atti di esecuzione adottati a norma dell'articolo 24, paragrafo 5, del regolamento (UE) n. 910/2014 [i.1].",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'condizione_applicabilita': "Adeguamento della clausola 6.4.9 di ETSI TS 119 431-1: si applica nell'ambito della valutazione di conformità del servizio applicativo SSASP alla EU SSASP v2 Policy, conformemente all'allegato A di tale norma (il regolamento si applica dal 19 agosto 2027).",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 5 (OVR-6.5.5-02)',
        'testo': "La scansione delle vulnerabilità richiesta da REQ-7.8-13 di ETSI EN 319 401 deve essere eseguita almeno una volta al trimestre.",
        'testo_integrale': "5) 6.5.5 Controlli di sicurezza della rete — OVR-6.5.5-02: La scansione delle vulnerabilità richiesta da REQ-7.8-13 di ETSI EN 319 401 [1] deve essere eseguita almeno una volta al trimestre.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Adeguamento della clausola 6.5.5 di ETSI TS 119 431-1: si applica nell'ambito della valutazione di conformità del servizio applicativo SSASP alla EU SSASP v2 Policy, conformemente all'allegato A di tale norma (il regolamento si applica dal 19 agosto 2027). La cadenza trimestrale è un requisito aggiuntivo rispetto alla scansione delle vulnerabilità già imposta da REQ-7.8-13 di ETSI EN 319 401, che non fissa la periodicità.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 5 (OVR-6.5.5-03)',
        'testo': "I firewall devono essere configurati in modo da impedire tutti i protocolli e gli accessi non necessari per il funzionamento del TSP.",
        'testo_integrale': "— OVR-6.5.5-03: I firewall devono essere configurati in modo da impedire tutti i protocolli e gli accessi non necessari per il funzionamento del TSP.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Adeguamento della clausola 6.5.5 di ETSI TS 119 431-1: si applica nell'ambito della valutazione di conformità del servizio applicativo SSASP alla EU SSASP v2 Policy, conformemente all'allegato A di tale norma (il regolamento si applica dal 19 agosto 2027).",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 6 (OVR-6.8.5-01)',
        'testo': "Devono essere posti in essere adeguati controlli di sicurezza per la gestione di tutte le tecniche crittografiche del servizio SSASP durante tutto il loro ciclo di vita.",
        'testo_integrale': "6) 6.8.5 Controlli crittografici — OVR-6.8.5-01: Devono essere posti in essere adeguati controlli di sicurezza per la gestione di tutte le tecniche crittografiche del servizio SSASP durante tutto il loro ciclo di vita.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Adeguamento della clausola 6.8.5 di ETSI TS 119 431-1 (clausola per cui la norma censita non ha un requisito corrispondente): si applica nell'ambito della valutazione di conformità del servizio applicativo SSASP alla EU SSASP v2 Policy, conformemente all'allegato A di tale norma (il regolamento si applica dal 19 agosto 2027).",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 6 (OVR-6.8.5-02)',
        'testo': "In relazione a OVR-6.8.5-01, il servizio SSASP seleziona e utilizza tecniche crittografiche adeguate, conformi ai meccanismi crittografici concordati approvati dal gruppo europeo per la certificazione della cibersicurezza dell'ENISA.",
        'testo_integrale': "— OVR-6.8.5-02: Per quanto riguarda OVR-6.8.5-01, il servizio SSASP seleziona e utilizza tecniche crittografiche adeguate conformi ai meccanismi crittografici concordati approvati dal gruppo europeo per la certificazione della cibersicurezza dell'ENISA [7].",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Adeguamento della clausola 6.8.5 di ETSI TS 119 431-1: si applica nell'ambito della valutazione di conformità del servizio applicativo SSASP alla EU SSASP v2 Policy, conformemente all'allegato A di tale norma (il regolamento si applica dal 19 agosto 2027). Il documento ENISA richiamato non è censito nel grafo: la conformità si misura su un atto esterno al censimento.",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 7 (OVR-A.3-02)',
        'testo': "La dichiarazione sulla prassi del TSP include il riferimento alla certificazione del QSCD impiegato conformemente ai requisiti di cui all'allegato II del regolamento (UE) n.910/2014.",
        'testo_integrale': "7) Allegato A, sezione A.3 Requisiti generali — OVR-A.3-02 [EUSPv2]: La dichiarazione sulla prassi del TSP include il riferimento alla certificazione del QSCD impiegato conformemente ai requisiti del regolamento (UE) n. 910/2014 [i.1], allegato II.",
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'condizione_applicabilita': "Adeguamento dell'allegato A, sezione A.3 di ETSI TS 119 431-1 (policy EUSPv2): si applica nell'ambito della valutazione di conformità del servizio applicativo SSASP alla EU SSASP v2 Policy, conformemente all'allegato A di tale norma (il regolamento si applica dal 19 agosto 2027).",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
]

RIGHE_PRINCIPI = [
    {
        'riferimento': 'art. 1',
        'testo': "Le norme di riferimento e le specifiche per la gestione di dispositivi qualificati per la creazione a distanza di firma e sigillo elettronici come servizi fiduciari qualificati, di cui all'art. 29 bis §2 e all'art. 39 bis del regolamento (UE) n.910/2014, figurano nell'allegato del presente regolamento.",
        'testo_integrale': "Articolo 1\n\nNorme di riferimento e specifiche\n\nLe norme di riferimento e le specifiche per la gestione di dispositivi qualificati per la creazione di una firma elettronica a distanza e di dispositivi qualificati per la creazione di un sigillo elettronico a distanza come servizi fiduciari qualificati di cui all'articolo 29 bis, paragrafo 2, e all'articolo 39 bis del regolamento (UE) n. 910/2014 figurano nell'allegato del presente regolamento.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'art. 2, entrata in vigore',
        'testo': "Il regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea.",
        'testo_integrale': "Articolo 2\n\nEntrata in vigore e applicabilità\n\nIl presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'art. 2, applicazione',
        'testo': "Il regolamento si applica a decorrere dal 19 agosto 2027 (24 mesi dopo l'entrata in vigore, per dare ai prestatori di servizi fiduciari un periodo di adeguamento ai nuovi requisiti).",
        'testo_integrale': "Il presente regolamento si applica a decorrere dal 19 agosto 2027.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'condizione_applicabilita': "Data di applicazione differita rispetto all'entrata in vigore: gli obblighi di adeguamento dell'allegato non sono vincolanti prima del 19 agosto 2027, pur essendo il regolamento già in vigore.",
    },
    {
        'riferimento': 'allegato, chapeau (norma di riferimento e ambito di applicazione)',
        'testo': "La norma ETSI TS 119 431-1 V1.3.1 (2024-12) si applica allo scopo di valutare la conformità del servizio applicativo \"EU Server Signing Application Service v2 Policy\" (SSASP), conformemente all'allegato A di tale norma, con gli adeguamenti di cui ai punti da 1 a 7 dell'allegato.",
        'testo_integrale': "ALLEGATO\n\nElenco delle norme di riferimento e delle specifiche per la gestione di dispositivi qualificati per la creazione di una firma elettronica a distanza e dispositivi qualificati per la creazione di un sigillo elettronico a distanza\n\nLa norma ETSI TS 119 431-1 V1.3.1 (2024-12) (\"ETSI TS 119 431-1\") si applica allo scopo di valutare la conformità al servizio applicativo EU Server Signing Application Service v2 Policy (SSASP) conformemente all'allegato A di tale norma, con i seguenti adeguamenti:",
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'allegato, punto 1 (riferimenti normativi)',
        'testo': "Alla clausola 2.1 (riferimenti normativi) di ETSI TS 119 431-1 sono aggiunti il riferimento a ETSI EN 319 401 V3.1.1 (2024-06), \"Firme elettroniche e infrastrutture fiduciarie (ESI); Requisiti di politica generale per i prestatori di servizi fiduciari\", e il riferimento ai meccanismi crittografici concordati (\"Agreed Cryptographic Mechanisms\") pubblicati dall'Agenzia dell'Unione europea per la cibersicurezza (ENISA).",
        'testo_integrale': "1) 2.1 Riferimenti normativi — [1] ETSI EN 319 401 V3.1.1 (2024-06): \"Firme elettroniche e infrastrutture fiduciarie (ESI); Requisiti di politica generale per i prestatori di servizi fiduciari\"; — [7] Gruppo europeo per la certificazione della cibersicurezza, sottogruppo sulla crittografia: \"Agreed Cryptographic Mechanisms\" (meccanismi crittografici concordati) pubblicati dall'Agenzia dell'Unione europea per la cibersicurezza (ENISA) (1).",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'condizione_applicabilita': "Aggiunta di riferimenti bibliografici alla clausola 2.1 della norma, operata dall'allegato del regolamento (che si applica dal 19 agosto 2027); non impone un comportamento autonomo, ma rende vincolanti per la norma i documenti ivi richiamati.",
    },
]

INDICE_ARTICOLI_LOCALE = [
    'art. 1',
    'art. 2, entrata in vigore',
    'art. 2, applicazione',
    'allegato, chapeau (norma di riferimento e ambito di applicazione)',
    'allegato, punto 1 (riferimenti normativi)',
    'allegato, punto 2 (OVR-6.1-04)',
    'allegato, punto 3 (OVR-6.4.4-02)',
    'allegato, punto 3 (OVR-6.4.4-03)',
    'allegato, punto 4 (OVR-6.4.9-02)',
    'allegato, punto 5 (OVR-6.5.5-02)',
    'allegato, punto 5 (OVR-6.5.5-03)',
    'allegato, punto 6 (OVR-6.8.5-01)',
    'allegato, punto 6 (OVR-6.8.5-02)',
    'allegato, punto 7 (OVR-A.3-02)',
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI = [
    # Base giuridica abilitante (citata nei "visti" e ripresa dall'art. 1).
    {
        'nodo_da': ('principio', None, 'art. 1'),
        'nodo_a': ('principio', 2, 'art. 29-bis §2'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.95,
    },
    {
        'nodo_da': ('principio', None, 'art. 1'),
        'nodo_a': ('principio', 2, 'art. 39-bis'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.95,
    },
    # Chapeau: rende operativo l'ambito della norma per la valutazione di
    # conformita' del servizio SSASP (policy EUSPv2, allegato A).
    {
        'nodo_da': ('principio', None, 'allegato, chapeau (norma di riferimento e ambito di applicazione)'),
        'nodo_a': ('principio', 11, 'Parte 1: clausola 1 (Scope)'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'textual',
        'confidence': 0.8,
    },
    # Adeguamenti che integrano una clausola della norma -> "modifica" verso
    # il requisito esistente della stessa clausola.
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 2 (OVR-6.1-04)'),
        'nodo_a': ('obbligo', 11, 'Parte 1: OVR-6.1-04'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3 (OVR-6.4.4-02)'),
        'nodo_a': ('obbligo', 11, 'Parte 1: OVR-6.4.4-01'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3 (OVR-6.4.4-03)'),
        'nodo_a': ('obbligo', 11, 'Parte 1: OVR-6.4.4-01'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 4 (OVR-6.4.9-02)'),
        'nodo_a': ('obbligo', 11, 'Parte 1: OVR-6.4.9-01'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 4 (OVR-6.4.9-02)'),
        'nodo_a': ('principio', 2, 'art. 24 §5 (vigente, eIDAS2)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 5 (OVR-6.5.5-02)'),
        'nodo_a': ('obbligo', 11, 'Parte 1: OVR-6.5.5-01'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 5 (OVR-6.5.5-02)'),
        'nodo_a': ('obbligo', 10, 'REQ-7.8-13'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 5 (OVR-6.5.5-03)'),
        'nodo_a': ('obbligo', 11, 'Parte 1: OVR-6.5.5-01'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 7 (OVR-A.3-02)'),
        'nodo_a': ('obbligo', 11, 'Parte 1: OVR-A.3-02'),
        'tipo_relazione': 'modifica',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
]
