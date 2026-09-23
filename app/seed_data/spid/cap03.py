"""DPCM 24 ottobre 2014 (SPID) - artt. 13-17: Adesione ed obblighi dei fornitori di
servizi (13), adesione allo SPID delle pubbliche amministrazioni (14), adesione
allo SPID dei soggetti privati fornitori di servizi (15), accreditamento dei
gestori di attributi qualificati (16), disposizione finale (17).

Testo ufficiale vigente al 21/09/2026 (Normattiva), fonte
app/.source_cache/spid/cap03.txt. Modulo generato secondo il contratto di
app/seed_data/lib.py (ADR-0007): copertura completa comma/lettera per
comma/lettera, nessun discrimine di rilevanza. I fornitori di servizi che
aderiscono allo SPID (artt. 13, 15) sono relying party con un rapporto di
adesione tracciato tramite convenzione con l'Agenzia: categoria 'Terza parte'.
Le pubbliche amministrazioni (art. 14) non sono una categoria di soggetto
censita: le relative righe non valorizzano `soggetti` (stesso pattern usato
per le norme CAD indirizzate ad AgID). I gestori di attributi qualificati
(art. 16) rientrano nella categoria 'QTSP/gestore'.

L'art. 17, comma 1 (domanda di accreditamento) e' l'unica disposizione
sostanziale dell'articolo: la formula di trasmissione agli organi di
controllo, pubblicazione in Gazzetta Ufficiale e le firme di promulgazione
che seguono non sono disposizioni normative autonome e non generano un nodo.

Le relazioni (RELAZIONI) sono limitate a rinvii interni a questo capitolo
(artt. 13-17): i rinvii all'art. 4 (regolamenti attuativi, fuori range), al
CAD (art. 64, art. 2 c.2, art. 6-bis, art. 57-bis) e al d.lgs. 196/2003 e al
d.lgs. 70/2003 sono cross-capitolo/cross-fonte e restano fuori scope di
questo import (verranno collegati a posteriori dalla sessione principale,
ADR-0009).
"""

RIGHE_OBBLIGHI = [
    {
        'riferimento': 'art. 13 c.1',
        'testo': "I fornitori di servizi possono aderire allo SPID stipulando un'apposita "
                 "convenzione con l'Agenzia, secondo lo schema definito nei regolamenti "
                 "attuativi di cui all'art. 4.",
        'testo_integrale': "I fornitori di servizi possono aderire allo SPID stipulando "
                            "apposita convenzione con l'Agenzia il cui schema e' definito "
                            "nell'ambito dei regolamenti attuativi di cui all'art. 4.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 13 c.2',
        'testo': 'I fornitori di servizi conservano per ventiquattro mesi le informazioni '
                 "necessarie a imputare alle singole identità digitali le operazioni "
                 'effettuate sui propri sistemi tramite SPID.',
        'testo_integrale': 'I fornitori di servizi conservano per ventiquattro mesi le '
                            'informazioni necessarie a imputare, alle singole identita\' '
                            'digitali, le operazioni effettuate sui propri sistemi tramite '
                            'SPID.',
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 13 c.3',
        'testo': "Se rilevano un uso anomalo di un'identità digitale, i fornitori di "
                 "servizi ne informano immediatamente l'Agenzia e il gestore "
                 "dell'identità digitale che l'ha rilasciata.",
        'testo_integrale': 'Nel caso in cui i fornitori di servizi rilevino un uso anomalo '
                            "di un'identita' digitale, informano immediatamente l'Agenzia e "
                            "il gestore dell'identita' digitale che l'ha rilasciata.",
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'condizione_applicabilita': "in caso di rilevazione, da parte del fornitore di "
                                     "servizi, di un uso anomalo di un'identità digitale",
        'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 13 c.4',
        'testo': 'I fornitori di servizi trattano i dati personali nel rispetto del d.lgs. '
                 "30 giugno 2003, n. 196 e, nell'ambito della relativa informativa, "
                 "informano l'utente che l'identità digitale e gli eventuali attributi "
                 'qualificati saranno verificati, rispettivamente, presso i gestori '
                 "dell'identità digitale e i gestori degli attributi qualificati.",
        'testo_integrale': 'I fornitori di servizi trattano i dati personali nel rispetto '
                            'del decreto legislativo 30 giugno 2003, n. 196. '
                            "Nell'ambito dell'informativa di cui all'art. 13 del decreto "
                            "legislativo n. 196 del 2003, i fornitori di servizi informano "
                            "l'utente che l'identita' digitale e gli eventuali attributi "
                            'qualificati saranno verificati, rispettivamente, presso i '
                            "gestori dell'identita' digitale e i gestori degli attributi "
                            'qualificati.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 13 c.5',
        'testo': "Salvo quanto previsto dall'art. 14 per le pubbliche amministrazioni, i "
                 'fornitori di servizi possono affidare ai gestori di identità SPID la '
                 'gestione delle interfacce di autenticazione informatica dei propri '
                 'servizi in rete.',
        'testo_integrale': 'I fornitori di servizi, fatto salvo quanto previsto '
                            "dall'art. 14 per le pubbliche amministrazioni, possono "
                            'affidare la gestione delle interfacce di autenticazione '
                            'informatica ai propri servizi in rete ai gestori di '
                            "identita' SPID.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "fatto salvo quanto previsto dall'art. 14 per le "
                                     'pubbliche amministrazioni',
        'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 14 c.1',
        'testo': "Nel rispetto dell'art. 64, comma 2, del CAD, le pubbliche "
                 'amministrazioni che erogano in rete servizi qualificati, direttamente o '
                 'tramite altro fornitore di servizi, consentono agli utenti '
                 "l'identificazione informatica tramite SPID.",
        'testo_integrale': "Nel rispetto dell'art. 64, comma 2, del CAD, le pubbliche "
                            'amministrazioni che erogano in rete servizi qualificati, '
                            'direttamente o tramite altro fornitore di servizi, '
                            "consentono l'identificazione informatica degli utenti "
                            "attraverso l'uso dello SPID.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
    },
    {
        'riferimento': 'art. 14 c.2',
        'testo': 'Ai fini di quanto previsto dal comma 1, le pubbliche amministrazioni di '
                 "cui all'art. 2, comma 2, del CAD aderiscono allo SPID, secondo le "
                 "modalità stabilite dall'Agenzia ai sensi dell'art. 4, entro i "
                 "ventiquattro mesi successivi all'accreditamento del primo gestore "
                 "dell'identità digitale.",
        'testo_integrale': 'Ai fini del comma 1, le pubbliche amministrazioni di cui '
                            "all'art. 2, comma 2, del CAD aderiscono allo SPID, secondo "
                            "le modalita' stabilite dall'Agenzia ai sensi dell'art. 4, "
                            'entro i ventiquattro mesi successivi '
                            "all'accreditamento del primo gestore dell'identita' "
                            'digitale.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
    },
    {
        'riferimento': 'art. 14 c.3',
        'testo': 'Le pubbliche amministrazioni possono affidare ai gestori di identità '
                 'dello SPID le funzioni di autenticazione informatica previste dalla '
                 'normativa vigente in materia.',
        'testo_integrale': 'Le pubbliche amministrazioni possono affidare ai gestori di '
                            "identita' dello SPID le funzioni di autenticazione "
                            'informatica previste dalla normativa vigente in materia.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
    },
    {
        'riferimento': 'art. 14 c.4',
        'testo': 'Le pubbliche amministrazioni possono affidare ai gestori di identità '
                 'SPID le funzioni di autenticazione informatica basate sugli strumenti '
                 "per i quali il diritto dell'Unione europea prevede il mutuo "
                 'riconoscimento.',
        'testo_integrale': 'Le pubbliche amministrazioni possono affidare ai gestori di '
                            "identita' SPID le funzioni di autenticazione informatica "
                            'basate sugli strumenti per i quali il diritto '
                            "dell'Unione europea prevede il mutuo riconoscimento.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
    },
    {
        'riferimento': 'art. 14 c.5',
        'testo': 'Le pubbliche amministrazioni, quali fornitori di servizi, usufruiscono '
                 'gratuitamente delle verifiche rese disponibili dai gestori di identità '
                 "digitali e dai gestori di attributi qualificati; per l'adeguamento "
                 'allo SPID dei propri sistemi informatici, utilizzano le risorse '
                 'finanziarie disponibili a legislazione vigente, senza nuovi o '
                 'maggiori oneri per la finanza pubblica.',
        'testo_integrale': 'Le pubbliche amministrazioni, in qualita\' di fornitori dei '
                            'servizi, usufruiscono gratuitamente delle verifiche rese '
                            "disponibili dai gestori di identita' digitali e dai "
                            "gestori di attributi qualificati. Per l'adeguamento allo "
                            'SPID dei propri sistemi informatici, le amministrazioni '
                            'utilizzano le risorse finanziarie disponibili a '
                            'legislazione vigente, senza nuovi e maggiori oneri a '
                            'carico della finanza pubblica.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
    },
    {
        'riferimento': 'art. 15 c.1',
        'testo': 'Non possono aderire allo SPID i soggetti privati fornitori di servizi '
                 'il cui rappresentante legale, soggetto preposto '
                 "all'amministrazione o componente di organo preposto al controllo sia "
                 'stato condannato con sentenza passata in giudicato per reati '
                 'commessi a mezzo di sistemi informatici.',
        'testo_integrale': 'Non possono aderire allo SPID i soggetti privati fornitori '
                            'di servizi il cui rappresentante legale, soggetto '
                            "preposto all'amministrazione o componente di organo "
                            'preposto al controllo risulta condannato con sentenza '
                            'passata in giudicato per reati commessi a mezzo di '
                            'sistemi informatici.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 15 c.2',
        'testo': "Ai sensi dell'art. 64, comma 2-quinquies, del CAD, i soggetti privati "
                 'che aderiscono allo SPID per la verifica dell\'accesso ai servizi '
                 'erogati in rete, nel rispetto del presente decreto e dei regolamenti '
                 "attuativi adottati dall'Agenzia ai sensi dell'art. 4, soddisfano gli "
                 "obblighi dell'art. 17, comma 2, del d.lgs. 9 aprile 2003, n. 70 "
                 'comunicando il codice identificativo dell\'identità digitale '
                 "utilizzata dall'utente.",
        'testo_integrale': "Ai sensi dell'art. 64, comma 2-quinquies, del CAD, i "
                            'soggetti privati che aderiscono allo SPID per la '
                            "verifica dell'accesso ai servizi erogati in rete, nel "
                            'rispetto del presente decreto e dei regolamenti '
                            "attuativi adottati dall'Agenzia ai sensi dell'art. 4, "
                            "soddisfano gli obblighi di cui all'art. 17, comma 2, "
                            'del decreto legislativo 9 aprile 2003, n. 70 con la '
                            'comunicazione del codice identificativo '
                            "dell'identita' digitale utilizzata dall'utente.",
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'Terza parte', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 16 c.1',
        'testo': 'I soggetti che hanno il potere, in base alle norme vigenti, di '
                 'attestare gli attributi qualificati si accreditano indicando i dati '
                 'che intendono rendere disponibili nello SPID, nel rispetto del '
                 'presente decreto e secondo le modalità indicate nei regolamenti '
                 "attuativi adottati ai sensi dell'art. 4.",
        'testo_integrale': 'I soggetti che hanno il potere, in base alle norme '
                            'vigenti, di attestare gli attributi qualificati si '
                            'accreditano indicando i dati che intendono rendere '
                            'disponibili nello SPID, nel rispetto del presente '
                            "decreto e secondo le modalita' indicate nei "
                            "regolamenti attuativi adottati ai sensi dell'art. 4.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 16 c.2',
        'testo': "L'Agenzia inserisce in un apposito registro, accessibile ai "
                 'fornitori di servizi, le tipologie di dati resi disponibili da '
                 'ciascun gestore di attributi qualificati.',
        'testo_integrale': "L'Agenzia inserisce in un apposito registro, accessibile "
                            'da parte dei fornitori di servizi, le tipologie di '
                            'dati resi disponibili da ciascun gestore di attributi '
                            'qualificati.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
    },
    {
        'riferimento': 'art. 17 c.1',
        'testo': "I soggetti interessati a ottenere l'accreditamento allo SPID possono "
                 "presentare domanda all'Agenzia successivamente all'emanazione dei "
                 "regolamenti attuativi di cui all'art. 4.",
        'testo_integrale': 'I soggetti interessati a ottenere l\'accreditamento allo '
                            "SPID possono presentare domanda all'Agenzia "
                            "successivamente all'emanazione dei regolamenti "
                            "attuativi di cui all'art. 4.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "successivamente all'emanazione dei regolamenti "
                                     "attuativi di cui all'art. 4",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
]

RIGHE_PRINCIPI = [
    {
        'riferimento': 'art. 15 c.3',
        'testo': 'Nella convenzione tra i fornitori di servizi privati e l\'Agenzia, '
                 "nell'ambito dei regolamenti attuativi di cui all'art. 4, possono "
                 'essere regolati i corrispettivi dovuti dai fornitori di servizi ai '
                 "gestori dell'identità digitale e ai gestori degli attributi "
                 'qualificati per i servizi di verifica.',
        'testo_integrale': 'Nella convenzione che i fornitori di servizi privati '
                            "stipulano con l'Agenzia, nell'ambito dei regolamenti "
                            "attuativi di cui all'art. 4, possono essere regolati i "
                            'corrispettivi dovuti dai fornitori di servizi ai '
                            "gestori dell'identita' digitale e ai gestori degli "
                            'attributi qualificati per i servizi di verifica.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'oggetti_giuridici': ['identificazione elettronica'],
    },
    {
        'riferimento': 'art. 16 c.3 lett.a)',
        'testo': 'Su richiesta degli interessati, è accreditato di diritto come gestore '
                 'di attributi qualificati il Ministero dello sviluppo economico, in '
                 "relazione ai dati contenuti nell'indice nazionale degli indirizzi PEC "
                 "delle imprese e dei professionisti di cui all'art. 6-bis del CAD.",
        'testo_integrale': 'Su richiesta degli interessati, sono accreditati di '
                            'diritto i seguenti gestori di attributi qualificati: '
                            'a) il Ministero dello sviluppo economico in relazione '
                            "ai dati contenuti nell'indice nazionale degli "
                            'indirizzi PEC delle imprese e dei professionisti di '
                            "cui all'art. 6-bis del CAD;",
        'tipo_principio': 'presunzione legale',
        'stato': 'vigente',
        'oggetti_giuridici': ['attestato elettronico di attributi'],
    },
    {
        'riferimento': 'art. 16 c.3 lett.b)',
        'testo': 'Su richiesta degli interessati, sono accreditati di diritto come '
                 'gestori di attributi qualificati i consigli, gli ordini e i collegi '
                 "delle professioni regolamentate, per l'attestazione dell'iscrizione "
                 'agli albi professionali.',
        'testo_integrale': 'b) i consigli, gli ordini e i collegi delle professioni '
                            "regolamentate relativamente all'attestazione "
                            "dell'iscrizione agli albi professionali;",
        'tipo_principio': 'presunzione legale',
        'stato': 'vigente',
        'oggetti_giuridici': ['attestato elettronico di attributi'],
    },
    {
        'riferimento': 'art. 16 c.3 lett.c)',
        'testo': 'Su richiesta degli interessati, sono accreditate di diritto come '
                 'gestori di attributi qualificati le camere di commercio, industria, '
                 "artigianato e agricoltura, per l'attestazione delle cariche e degli "
                 'incarichi societari iscritti nel registro delle imprese.',
        'testo_integrale': 'c) le camere di commercio, industria, artigianato e '
                            "agricoltura per l'attestazione delle cariche e degli "
                            'incarichi societari iscritti nel registro delle '
                            'imprese;',
        'tipo_principio': 'presunzione legale',
        'stato': 'vigente',
        'oggetti_giuridici': ['attestato elettronico di attributi'],
    },
    {
        'riferimento': 'art. 16 c.3 lett.d)',
        'testo': 'Su richiesta degli interessati, è accreditata di diritto come gestore '
                 "di attributi qualificati l'Agenzia, in relazione ai dati contenuti "
                 "nell'indice dei domicili digitali della pubblica amministrazione e dei "
                 "gestori di pubblici servizi di cui all'art. 6-ter del CAD (riferimento "
                 "aggiornato dal DPCM 19 ottobre 2021, art. 5).",
        'testo_integrale': "d) l'Agenzia in relazione ai dati contenuti nell'indice dei "
                            "domicili digitali delle pubbliche amministrazioni e dei "
                            "gestori di pubblici servizi di cui all'art. 6-ter.",
        'tipo_principio': 'presunzione legale',
        'stato': 'vigente',
        'oggetti_giuridici': ['attestato elettronico di attributi'],
    },
]

INDICE_ARTICOLI_LOCALE = [
    'art. 13 c.1',
    'art. 13 c.2',
    'art. 13 c.3',
    'art. 13 c.4',
    'art. 13 c.5',
    'art. 14 c.1',
    'art. 14 c.2',
    'art. 14 c.3',
    'art. 14 c.4',
    'art. 14 c.5',
    'art. 15 c.1',
    'art. 15 c.2',
    'art. 15 c.3',
    'art. 16 c.1',
    'art. 16 c.2',
    'art. 16 c.3 lett.a)',
    'art. 16 c.3 lett.b)',
    'art. 16 c.3 lett.c)',
    'art. 16 c.3 lett.d)',
    'art. 17 c.1',
]

MAPPATURA_LOCALE = {
    'art. 13 c.1': ['art. 13 c.1'],
    'art. 13 c.2': ['art. 13 c.2'],
    'art. 13 c.3': ['art. 13 c.3'],
    'art. 13 c.4': ['art. 13 c.4'],
    'art. 13 c.5': ['art. 13 c.5'],
    'art. 14 c.1': ['art. 14 c.1'],
    'art. 14 c.2': ['art. 14 c.2'],
    'art. 14 c.3': ['art. 14 c.3'],
    'art. 14 c.4': ['art. 14 c.4'],
    'art. 14 c.5': ['art. 14 c.5'],
    'art. 15 c.1': ['art. 15 c.1'],
    'art. 15 c.2': ['art. 15 c.2'],
    'art. 15 c.3': ['art. 15 c.3'],
    'art. 16 c.1': ['art. 16 c.1'],
    'art. 16 c.2': ['art. 16 c.2'],
    'art. 16 c.3 lett.a)': ['art. 16 c.3 lett.a)'],
    'art. 16 c.3 lett.b)': ['art. 16 c.3 lett.b)'],
    'art. 16 c.3 lett.c)': ['art. 16 c.3 lett.c)'],
    'art. 16 c.3 lett.d)': ['art. 16 c.3 lett.d)'],
    'art. 17 c.1': ['art. 17 c.1'],
}

RELAZIONI = [
    {
        'nodo_da': ('obbligo', None, 'art. 14 c.1'),
        'nodo_a': ('obbligo', None, 'art. 13 c.1'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', None, 'art. 15 c.1'),
        'nodo_a': ('obbligo', None, 'art. 13 c.1'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('obbligo', None, 'art. 14 c.1'),
        'nodo_a': ('obbligo', None, 'art. 13 c.5'),
        'tipo_relazione': 'deroga a',
        'evidence_type': 'textual',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('obbligo', None, 'art. 14 c.2'),
        'nodo_a': ('obbligo', None, 'art. 14 c.1'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, 'art. 16 c.2'),
        'nodo_a': ('obbligo', None, 'art. 16 c.1'),
        'tipo_relazione': 'attua',
        'evidence_type': 'inferred',
        'confidence': 0.6,
    },
    {
        'nodo_da': ('principio', None, 'art. 16 c.3 lett.a)'),
        'nodo_a': ('obbligo', None, 'art. 16 c.1'),
        'tipo_relazione': 'deroga a',
        'evidence_type': 'textual',
        'confidence': 0.65,
    },
    {
        'nodo_da': ('principio', None, 'art. 16 c.3 lett.b)'),
        'nodo_a': ('obbligo', None, 'art. 16 c.1'),
        'tipo_relazione': 'deroga a',
        'evidence_type': 'textual',
        'confidence': 0.65,
    },
    {
        'nodo_da': ('principio', None, 'art. 16 c.3 lett.c)'),
        'nodo_a': ('obbligo', None, 'art. 16 c.1'),
        'tipo_relazione': 'deroga a',
        'evidence_type': 'textual',
        'confidence': 0.65,
    },
    {
        'nodo_da': ('principio', None, 'art. 16 c.3 lett.d)'),
        'nodo_a': ('obbligo', None, 'art. 16 c.1'),
        'tipo_relazione': 'deroga a',
        'evidence_type': 'textual',
        'confidence': 0.65,
    },
]
