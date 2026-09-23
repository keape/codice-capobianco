"""Estrazione granulare DPCM 22 febbraio 2013 - Titolo VI, Disposizioni finali
(artt. 62-63: valore delle firme elettroniche qualificate e digitali nel tempo,
disposizioni finali e transitorie inclusa la sostituzione del DPCM 30 marzo 2009).

Testo ufficiale vigente al 17/09/2026, fonte app/.source_cache/dpcm/cap08.txt (ADR-0007).
Modulo generato secondo il contratto di app/seed_data/lib.py: nessun discrimine di rilevanza,
copertura completa comma/lettera per comma/lettera.
"""

RIGHE_OBBLIGHI = [
    {
        'riferimento': 'art. 63 c.2',
        'testo': "I certificatori accreditati ai sensi dell'art. 29 del Codice devono "
                 'aggiornare la documentazione prevista per lo svolgimento di tale attività '
                 'entro centoventi giorni dalla data di entrata in vigore del presente '
                 'decreto.',
        'testo_integrale': "I certificatori accreditati ai sensi dell'art. 29 del Codice "
                            'aggiornano la documentazione prevista per lo svolgimento di tale '
                            "attività entro centoventi giorni dall'entrata in vigore del "
                            'presente decreto.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'art. 63 c.3',
        'testo': 'Le eventuali difformità nella generazione delle firme digitali, delle '
                 'firme elettroniche qualificate, dei certificati qualificati e delle marche '
                 'temporali rispetto alle regole tecnologiche di cui al Titolo II non ne '
                 'compromettono la validità, purché non ne mettano a rischio la sicurezza; '
                 "l'Agenzia valuta tali difformità e rende note le proprie decisioni sul "
                 'proprio sito internet.',
        'testo_integrale': 'Eventuali difformità nella generazione delle firme digitali, '
                            'delle firme elettroniche qualificate, dei certificati '
                            'qualificati e delle marche temporali, alle regole tecnologiche '
                            'di cui al Titolo II, che non ne mettano a rischio la sicurezza, '
                            "non ne inficiano la validità. L'Agenzia valuta tali difformità "
                            'e rende note le proprie decisioni sul proprio sito internet.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'condizione_applicabilita': 'la difformità non deve mettere a rischio la sicurezza '
                                     'della firma/certificato/marca temporale',
        'soggetti': [{'categoria': 'Terzi affidanti/pubblico', 'ruolo': 'obbligato'}],
    },
]

RIGHE_PRINCIPI = [
    {
        'riferimento': 'art. 62 c.1',
        'testo': 'Le firme elettroniche qualificate e digitali restano valide, anche se il '
                 'relativo certificato qualificato del sottoscrittore è nel frattempo '
                 'scaduto, revocato o sospeso, purché ad esse sia associabile un riferimento '
                 'temporale opponibile ai terzi che ne collochi la generazione in un momento '
                 'precedente alla scadenza, revoca o sospensione del certificato.',
        'testo_integrale': 'Le firme elettroniche qualificate e digitali, ancorché sia '
                            'scaduto, revocato o sospeso il relativo certificato qualificato '
                            'del sottoscrittore, sono valide se alle stesse è associabile un '
                            'riferimento temporale opponibile ai terzi che collochi la '
                            'generazione di dette firme rispettivamente in un momento '
                            'precedente alla scadenza, revoca o sospensione del suddetto '
                            'certificato.',
        'tipo_principio': 'valore probatorio',
        'stato': 'vigente',
        'oggetti_giuridici': ['firma elettronica qualificata',
                               'certificato qualificato di firma elettronica'],
    },
    {
        'riferimento': 'art. 63 c.1',
        'testo': 'Il presente decreto sostituisce il DPCM 30 marzo 2009, recante le regole '
                 'tecniche in materia di generazione, apposizione e verifica delle firme '
                 'digitali e di validazione temporale dei documenti informatici, pubblicato '
                 'nella Gazzetta Ufficiale del 6 giugno 2009, n. 129.',
        'testo_integrale': 'Il presente decreto sostituisce il decreto del Presidente del '
                            'Consiglio dei Ministri 30 marzo 2009, recante «Regole tecniche '
                            'in materia di generazione, apposizione e verifica delle firme '
                            'digitali e validazione temporale dei documenti informatici.», '
                            'pubblicato nella Gazzetta Ufficiale 6 giugno 2009, n. 129.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'oggetti_giuridici': [],
    },
]

INDICE_ARTICOLI_LOCALE = [
    'art. 62 c.1',
    'art. 63 c.1',
    'art. 63 c.2',
    'art. 63 c.3',
]

MAPPATURA_LOCALE = {
    'art. 62 c.1': ['art. 62 c.1'],
    'art. 63 c.1': ['art. 63 c.1'],
    'art. 63 c.2': ['art. 63 c.2'],
    'art. 63 c.3': ['art. 63 c.3'],
}

RELAZIONI = [
    {
        'nodo_da': ('obbligo', None, 'art. 63 c.3'),
        'nodo_a': ('principio', None, 'art. 62 c.1'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.4,
    },
]
