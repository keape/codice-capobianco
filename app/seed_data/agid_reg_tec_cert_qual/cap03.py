"""Regole Tecniche e Raccomandazioni AgID (13 feb 2020, ex art. 71 CAD).
Capitolo 3 di 3: Capitolo 5 del testo ufficiale (Convalida di firme e sigilli
elettronici qualificati) e Capitolo 6 (Norme transitorie e abrogazioni).
Testo ufficiale in app/.source_cache/agid_reg_tec_cert_qual/raw.txt.

Modellazione (ADR-0007):
- Cap. 5, comma 1 (condizioni di conferma della validità in sede di
  convalida, art. 32/27/37 eIDAS) -> Obbligo, tipo "tecnico/sicurezza".
  Soggetto obbligato "Terza parte": la convalida di una firma/sigillo non è
  tipicamente un'attività del QTSP emittente ma di un servizio di
  convalida/relying party (stesso trattamento riservato agli organismi di
  valutazione della conformità in Reg. (UE) 2025/1566 cap01.py e in ETSI TS
  119 461 cap06.py).
- Cap. 5, comma 2 ("si raccomanda che il processo di convalida della
  validazione temporale sia in grado di...") -> Obbligo, tipo
  "tecnico/sicurezza", stesso soggetto "Terza parte" e stessa nota generale
  sulla natura di raccomandazione RFC 2119 già documentata in cap01.py
  "par. 2 §3" (si applica anche a questo comma, non solo al capitolo 4: il
  verbo "si raccomanda" è esplicito nel testo).
- Cap. 6, comma 1 (abrogazione della Deliberazione CNIPA n.45/2009,
  sostituita da questo regolamento) -> Principio, tipo "altro": stabilisce
  un effetto giuridico (abrogazione di un atto non censito nel grafo,
  Deliberazione CNIPA n.45/2009) senza imporre un comportamento a un
  soggetto specifico del censimento. Nessuna relazione "abroga" verso un
  nodo Fonte, poiché la Deliberazione CNIPA n.45/2009 non è una Fonte
  presente nel grafo.
- Cap. 6, comma 2 (termine di 30 giorni per l'adozione delle regole
  tecniche da parte dei prestatori di servizi fiduciari) -> Obbligo, tipo
  "procedurale", soggetto QTSP obbligato.
- Cap. 6, comma 3 (regime transitorio: fino all'adozione, si applicano le
  regole tecniche della Deliberazione n.45/2009) -> Obbligo, tipo
  "procedurale", soggetto QTSP obbligato, con `condizione_applicabilita`
  che ne delimita la vigenza al periodo transitorio del comma 2.
- Cap. 6, comma 4 (le regole tecniche non producono effetto sui certificati
  emessi prima della loro adozione) -> Principio, tipo "altro": disposizione
  di efficacia temporale, non impone un comportamento a un soggetto.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "par. 5, comma 1",
        "testo": "Il processo di convalida di una firma o sigillo elettronico qualificato conferma la validità purché siano verificate le condizioni dell'art. 32 eIDAS e la firma/sigillo sia generata conformemente agli atti di esecuzione emanati dalla Commissione UE ex art. 27/37 §5 eIDAS.",
        "testo_integrale": "1. Il processo di convalida di una firma elettronica qualificata o di un sigillo elettronico qualificato conferma la validità delle stesse purché siano verificate le condizioni di cui all'articolo 32 del regolamento eIDAS e siano generate conformemente a quanto stabilito negli atti di esecuzione emanati dalla Commissione Europea ai sensi del paragrafo 5 degli articoli 27 o 37 del regolamento eIDAS.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 5, comma 2",
        "testo": "Si raccomanda che il processo di convalida della validazione temporale sia in grado di verificare le marche detached e i formati RFC 5544.",
        "testo_integrale": "2. Si raccomanda che il processo di convalida della validazione temporale sia in grado di effettuare la verifica delle marche detached e dei formati RFC 5544.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 6, comma 2",
        "testo": "I prestatori di servizi fiduciari adottano le presenti regole tecniche entro 30 giorni dalla pubblicazione della notizia della loro emanazione sulla Gazzetta Ufficiale.",
        "testo_integrale": "2. Le presenti regole tecniche sono adottate dai prestatori di servizi fiduciari entro 30 giorni dalla data di pubblicazione della notizia della loro emanazione sulla Gazzetta Ufficiale della Repubblica Italiana.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 6, comma 3",
        "testo": "Fino all'adozione delle presenti regole tecniche nel termine del comma 2, i prestatori di servizi fiduciari qualificati continuano ad applicare le regole tecniche della Deliberazione CNIPA n.45/2009.",
        "testo_integrale": "3. Fino all'adozione delle presenti regole tecniche nei termini stabiliti dal precedente comma 2, i prestatori di servizi fiduciari qualificati continuano ad applicare le regole tecniche di cui alla Deliberazione №45/2009.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Regime transitorio: applicabile solo nel periodo antecedente all'adozione delle presenti regole tecniche entro il termine di 30 giorni del comma 2.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "par. 6, comma 1",
        "testo": "Salvo il regime transitorio del comma 2, la Deliberazione CNIPA n.45 del 21 maggio 2009 è abrogata e sostituita dal presente regolamento.",
        "testo_integrale": "1. Salvo quanto disposto al successivo comma 2, la Deliberazione CNIPA №45 del 21 maggio 2009 è abrogata e sostituita dal presente regolamento.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "par. 6, comma 4",
        "testo": "Le presenti regole tecniche non producono alcun effetto sui certificati emessi prima della loro adozione.",
        "testo_integrale": "4. Le presenti regole tecniche non producono alcun effetto sui certificati emessi prima della loro adozione.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "certificato qualificato di firma elettronica",
            "certificato qualificato di sigillo elettronico",
        ],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "par. 5, comma 1",
    "par. 5, comma 2",
    "par. 6, comma 1",
    "par. 6, comma 2",
    "par. 6, comma 3",
    "par. 6, comma 4",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "par. 6, comma 3"),
        "nodo_a": ("obbligo", None, "par. 6, comma 2"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", None, "par. 6, comma 1"),
        "nodo_a": ("obbligo", None, "par. 6, comma 2"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "textual",
        "confidence": 0.6,
    },
]
