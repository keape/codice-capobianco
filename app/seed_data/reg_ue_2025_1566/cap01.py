"""Regolamento di esecuzione (UE) 2025/1566 della Commissione, del 29 luglio
2025 - modalita' di applicazione dell'art. 24 §1-quater del regolamento (UE)
n.910/2014 (eIDAS/eIDAS2) sulle norme di riferimento per la verifica
dell'identita' e degli attributi del richiedente un certificato qualificato o
un attestato elettronico di attributi qualificato (QEAA). Fonte 8, un unico
capitolo (atto di 2 soli articoli + un allegato di 6 punti di adeguamento,
sta comodamente nel contesto di una sessione principale - nessuna
suddivisione per subagent necessaria, stesso criterio gia' usato per Fonte 6
"DPCM 19/10/2021" e Fonte 7 "ETSI EN 319 412-5"). Testo ufficiale in
app/.source_cache/reg-ue-2025-1566/raw.txt (fetch diretto da EUR-Lex,
CELEX:32025R1566, 2026-09-21).

Modellazione (ADR-0007):
- Art. 1 (designa l'allegato come sede delle norme di riferimento ex art. 24
  §1-quater eIDAS2) -> Principio, tipo "altro" (nessun tipo dedicato in
  tassonomia a una disposizione di mero rinvio/designazione; non e'
  "definitorio" in senso proprio ne' di "scopo/ambito"). Relazione "attua"
  verso il Principio eIDAS2 "art. 24 §1-quater (nuovo, eIDAS2)" (fonte_id=2),
  che e' l'esatta base giuridica abilitante citata sia nel preambolo sia nel
  testo dell'articolo - stesso trattamento gia' riservato alle designazioni
  di norme di riferimento negli artt. 42 §2/44 §2 eIDAS2 (visti nel corpo
  principale di seed.py).
- Art. 2 (clausola finale) -> due nodi distinti, stesso criterio gia' usato
  per l'art. 52 §1/§2 eIDAS (id 310/311 in seed.py): "entrata in vigore" e
  "applicazione" sono fatti giuridici autonomi con effetti pratici diversi
  (qui il differimento di 24 mesi dell'applicazione e' esplicitamente
  motivato nel considerando 3 - non e' una formula equivalente). Entrambi
  Principio tipo "altro", stesso tipo usato per l'art. 52 eIDAS. La terza
  frase dell'art. 2 ("obbligatorio in tutti i suoi elementi e direttamente
  applicabile...") e' la formula di chiusura standard di ogni regolamento UE
  self-executing, priva di contenuto normativo autonomo distinto dalla forma
  giuridica "regolamento" gia' presupposta dall'intero censimento - esclusa
  per lo stesso motivo del preambolo/"considerando" (mai un nodo a se'
  stante), non e' un "comma" nel senso di ADR-0007 ma un elemento di
  formattazione dell'atto.
- Allegato, 6 punti di adeguamento allo standard ETSI TS 119 461 V2.1.1 (atto
  non censito come Fonte separata in questo grafo - a differenza di ETSI EN
  319 412-5/Fonte 7, che e' un documento diverso): ogni punto e' un item di
  indice distinto (nessun discrimine di rilevanza, incluso il punto 1 che si
  limita ad aggiungere un riferimento bibliografico allo standard ETSI EN 319
  401, perche' e' comunque un adeguamento sostanziale del testo dell'allegato
  di QUESTO regolamento, non paratesto amministrativo del regolamento stesso
  come lo erano invece Contents/Foreword/History nel caso ETSI EN 319 412-5).
  - Punto 1 (riferimento normativo aggiunto) -> Principio, tipo "altro"
    (aggiunta bibliografica, nessun comportamento imposto).
  - Punti 2, 4, 6 (obbligo "deve"/"stabilisce" con soggetto individuabile nel
    prestatore di servizi fiduciari qualificato/IPSP) -> Obbligo, categoria
    "QTSP/gestore", ruolo "obbligato", tipo_obbligo "tecnico/sicurezza"
    (punti 2 e 4, requisiti tecnici del processo di verifica) o
    "organizzativo" (punto 6, piano di cessazione - stesso tipo gia' usato
    per l'obbligo eIDAS2 "art. 24 §2(i)" a cui questo punto rinvia).
  - Punti 3 e 5 (obbligo il cui soggetto obbligato e' l'organismo di
    valutazione della conformita'/laboratorio accreditato/autorita'
    nazionale competente, non il QTSP) -> Obbligo, categoria "Terza parte",
    ruolo "obbligato", tipo_obbligo "tecnico/sicurezza".
  - Punto 2 e' esplicitamente condizionale ("Se la verifica dell'identita' ...
    e' effettuata in concomitanza con ...") -> condizione_applicabilita
    valorizzata, stessa convenzione di QCS-4.3.5-02 in ETSI EN 319 412-5.
  - Punto 6 cita testualmente l'art. 24 §5 eIDAS2 (base abilitante degli atti
    di esecuzione sul piano di cessazione) e specifica l'obbligo eIDAS2
    "art. 24 §2(i)" (che impone gia' il piano di cessazione in se') ->
    relazioni "richiama" e "specifica" verso quei due nodi (fonte_id=2),
    evidence_type "textual" (citazione esplicita nel testo).

Fase 6 (ADR-0009, 2026-09-21): pipeline completa eseguita nella sessione
principale. Grep sul testo ufficiale grezzo per citazioni esplicite ad altre
fonti censite: nessuna occorrenza di "82/2005" (CAD), "22 febbraio 2013"/
"DPCM" (Fonte 4), "24 ottobre 2014"/SPID (Fonte 5), "19 ottobre 2021"
(Fonte 6), "319 412-5" (Fonte 7) - solo citazioni a eIDAS (910/2014) e,
tramite considerando, a eIDAS2 (2024/1183), entrambe gia' modellate sopra
come relazioni native (non differite). KNN sull'indice vettoriale HNSW
(soglia 0.80) dei 9 nodi di questo capitolo contro tutti i nodi delle altre 6
fonti (CAD, DPCM 22/2/2013, SPID, DPCM 19/10/2021, ETSI EN 319 412-5):
nessuna coppia sopra soglia (il documento e' un dettaglio tecnico molto
specifico dell'art. 24 eIDAS/eIDAS2 - verifica dell'identita' per il
rilascio di certificati/QEAA - senza sovrapposizione concettuale sufficiente
con gli obblighi di firma elettronica/SPID/QCStatement gia' censiti nelle
altre fonti). Esito riportato come verificato, non come fase saltata: zero
relazioni aggiuntive oltre alle due relazioni native verso eIDAS2 gia' sopra.
"""

RIGHE_OBBLIGHI = [
    {
        'riferimento': 'allegato, punto 2 (QTS-C3-01)',
        'testo': "Se la verifica dell'identità per un certificato qualificato o un attestato elettronico qualificato di attributi è effettuata in concomitanza con la verifica dell'identità per il rilascio di prove autorevoli, tale processo di verifica dell'identità deve essere stato sottoposto a valutazione tra pari o certificato da un organismo di valutazione della conformità accreditato ai fini della conformità a un livello di garanzia elevato, oppure deve soddisfare i requisiti delle clausole da C3.1 a C3.6 di ETSI TS 119 461.",
        'testo_integrale': "C.3 Casi d'uso per il rilascio di certificati qualificati o attestati elettronici di attributi qualificati in conformità all'articolo 24, paragrafi 1, 1 bis e 1 ter, del regolamento (UE) n.910/2014 — [CONDIZIONALE] QTS-C3-01: Se la verifica dell'identità per un certificato qualificato o un attestato elettronico qualificato è effettuata in concomitanza con la verifica dell'identità per il rilascio di prove autorevoli, tale processo di verifica dell'identità: — deve essere stato sottoposto a valutazione tra pari o certificato da un organismo di valutazione della conformità accreditato ai fini della conformità a un livello di garanzia elevato a norma del regolamento (UE) n.910/2014, oppure — ai requisiti di cui alle clausole da C3.1 a C3.6",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica solo se la verifica dell'identità per il certificato qualificato/QEAA è effettuata in concomitanza con la verifica dell'identità per il rilascio di prove autorevoli (electronic attestation of attributes basata su prove autorevoli).",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 3 (QTS-C.3.4-06A)',
        'testo': "L'organismo indipendente di valutazione della conformità che verifica il controllo dell'identità mediante altri mezzi di identificazione deve essere accreditato ai sensi dell'art. 3, punto 18, del regolamento (UE) n.910/2014; la valutazione deve dar luogo a un certificato di conformità basato su un processo di certificazione formale che fa riferimento ai livelli di garanzia degli attestati/portafogli notificati e comprende prove rigorose di resistenza a minacce alla sicurezza.",
        'testo_integrale': "C.3.4 Caso d'uso per il controllo dell'identità mediante altri mezzi di identificazione — QTS-C.3.4-06A: L'organismo indipendente di valutazione della conformità di cui al [CONDIZIONALE] QTS-C.3.4-06, lettera c), deve essere accreditato a norma dell'articolo 3, punto 18, del regolamento (UE) n.910/2014 e, se sono soddisfatti tutti i requisiti applicabili, la valutazione dovrebbe dar luogo a un certificato di conformità basato su una verifica della certificazione. Tale processo di certificazione formale deve essere basato su un processo di valutazione della sicurezza che fa riferimento ai livelli di garanzia definiti per i mezzi di identificazione elettronica notificati o i portafogli europei di identità digitale certificati a norma del regolamento (UE) n.910/2014 e deve comprendere prove rigorose per valutare la resistenza a potenziali minacce alla sicurezza. Ai fini di tali valutazioni occorre avvalersi di norme tecniche pertinenti per dimostrare la solidità contro tali attacchi.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica quando il controllo dell'identità è effettuato mediante altri mezzi di identificazione (caso d'uso QTS-C.3.4-06, lettera c) - valutazione da parte di un organismo indipendente).",
        'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 4 (USE-9.2.3.4-04)',
        'testo': "Nei processi di verifica dell'identità completamente automatizzati, l'IPSP stabilisce valori target per FAR e FRR sulla base di un'analisi dei rischi e della relativa procedura di intelligence sulle minacce, seguendo la metodologia ENISA \"Methodology for sector cybersecurity assessment\" o una metodologia equivalente; tali valori devono essere pari o inferiori a quelli fissati per i casi d'uso ibridi, e devono essere mantenuti coerentemente nel tempo.",
        'testo_integrale': "9.2.3.4 Caso d'uso per il funzionamento automatizzato — USE-9.2.3.4-04: L'IPSP stabilisce valori target per FAR e FRR, sulla base di un'analisi dei rischi e della relativa procedura di intelligence sulle minacce, seguendo la metodologia stabilita nella relazione dell'ENISA \"Methodology for sector cybersecurity assessment\" [i.28] o una metodologia equivalente, nei processi di verifica dell'identità completamente automatizzati. Tali valori target devono essere pari o inferiori a quelli fissati per i casi d'uso ibridi, se esistenti. L'IPSP mantiene coerentemente tali valori target per FAR e FRR, supportato da un'analisi dei rischi e dalla relativa procedura di intelligence sulle minacce.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "Si applica ai soli processi di verifica dell'identità completamente automatizzati (non ai casi d'uso ibridi o manuali).",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 5 (VAL-8.3.3-21)',
        'testo': "L'efficacia delle misure adottate per conformarsi ai requisiti di convalida del documento di identità fisica (VAL-8.3.3-05X/05A/05B/05C/07A/07X) deve essere verificata da un laboratorio accreditato o da un'autorità nazionale competente, ogniqualvolta siano designati, al più tardi entro il 19 agosto 2027 e successivamente ogni due anni.",
        'testo_integrale': "8.3.3 Convalida del documento di identità fisica — VAL-8.3.3-21 L'efficacia delle misure per conformarsi ai requisiti VAL-8.3.3-05X, VAL-8.3.3-05A, VAL-8.3.3-05B, VAL-8.3.3-05C, VAL-8.3.3-07A e VAL-8.3.3-07X deve essere verificata da un laboratorio accreditato o da un'autorità nazionale competente, ogniqualvolta siano designati, al più tardi entro il 19 agosto 2027 e successivamente ogni due anni.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "La verifica è dovuta 'ogniqualvolta siano designati' un laboratorio accreditato o un'autorità nazionale competente; termine iniziale 19 agosto 2027, poi periodicità biennale.",
        'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'allegato, punto 6 (OVR-7.12-02)',
        'testo': "Il piano di cessazione del prestatore di servizi fiduciari qualificato deve essere conforme ai requisiti stabiliti negli atti di esecuzione adottati a norma dell'art. 24 §5 del regolamento (UE) n.910/2014.",
        'testo_integrale': "7.12. Cessazione e piani di cessazione — OVR-7.12-02: Il piano di cessazione deve essere conforme ai requisiti stabiliti negli atti di esecuzione adottati a norma dall'articolo 24, paragrafo 5, del regolamento (UE) n.910/2014",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
]

RIGHE_PRINCIPI = [
    {
        'riferimento': 'art. 1',
        'testo': "Le norme di riferimento e le specifiche di cui all'art. 24 §1-quater del regolamento (UE) n.910/2014 (verifica dell'identità e degli attributi ai fini del rilascio di certificati qualificati/QEAA) figurano nell'allegato del presente regolamento.",
        'testo_integrale': "Articolo 1\n\nLe norme di riferimento e le specifiche di cui all'articolo 24, paragrafo 1 quater, del regolamento (UE) n.910/2014 figurano nell'allegato del presente regolamento.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'art. 2, entrata in vigore',
        'testo': "Il regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea.",
        'testo_integrale': "Il presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'art. 2, applicazione',
        'testo': "Il regolamento si applica a decorrere dal 19 agosto 2027 (24 mesi dopo l'entrata in vigore, per dare ai prestatori di servizi fiduciari qualificati un periodo transitorio per adeguarsi ai requisiti dell'allegato).",
        'testo_integrale': "Il presente regolamento si applica a decorrere dal 19 agosto 2027.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'condizione_applicabilita': "Data di applicazione differita rispetto all'entrata in vigore: gli obblighi tecnici dell'allegato non sono vincolanti prima del 19 agosto 2027.",
    },
    {
        'riferimento': 'allegato, punto 1 (riferimenti normativi)',
        'testo': "Alla clausola 2.1 di ETSI TS 119 461 (riferimenti normativi) è aggiunto il riferimento a ETSI EN 319 401 V3.1.1 (2024-06), \"Requisiti di politica generale per i prestatori di servizi fiduciari\".",
        'testo_integrale': "2.1 Riferimenti normativi — [1] ETSI EN 319 401 V3.1.1 (2024-06): \"Firme elettroniche e infrastrutture fiduciarie (ESI); Requisiti di politica generale per i prestatori di servizi fiduciari\"",
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
]

INDICE_ARTICOLI_LOCALE = [
    'art. 1',
    'art. 2, entrata in vigore',
    'art. 2, applicazione',
    'allegato, punto 1 (riferimenti normativi)',
    'allegato, punto 2 (QTS-C3-01)',
    'allegato, punto 3 (QTS-C.3.4-06A)',
    'allegato, punto 4 (USE-9.2.3.4-04)',
    'allegato, punto 5 (VAL-8.3.3-21)',
    'allegato, punto 6 (OVR-7.12-02)',
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI = [
    {
        'nodo_da': ('principio', None, 'art. 1'),
        'nodo_a': ('principio', 2, 'art. 24 §1-quater (nuovo, eIDAS2)'),
        'tipo_relazione': 'attua',
        'evidence_type': 'textual',
        'confidence': 0.95,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 6 (OVR-7.12-02)'),
        'nodo_a': ('obbligo', 2, 'art. 24 §2(i) (vigente, eIDAS2)'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 6 (OVR-7.12-02)'),
        'nodo_a': ('principio', 2, 'art. 24 §5 (vigente, eIDAS2)'),
        'tipo_relazione': 'richiama',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
]
