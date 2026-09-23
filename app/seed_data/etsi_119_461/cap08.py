"""ETSI TS 119 461 V2.1.1 (2025-02) - Policy and security requirements for
trust service components providing identity proofing of trust service
subjects. Capitolo 8/8 (Fonte 9, sarà cablata dalla sessione principale):
Annex A (informative, Void), Annex B (informative, Threats to identity
proofing), Annex C (normative, Use cases for identity proofing for EU
qualified trust services), Annex D (informative, Mapping to applicable
requirements of the amended eIDAS regulation), History. Testo ufficiale in
app/.source_cache/etsi_119_461/cap08.txt.

Modellazione (ADR-0007), coerente con le convenzioni già adottate per
ETSI EN 319 412-5 (app/seed_data/etsi_319_412_5/cap01.py) per questo
genere di fonte (standard tecnico ETSI a clausole numerate):

- Annex A "Void" -> nessun nodo (rimando strutturale privo di contenuto
  proprio, stesso trattamento delle clausole "void" già viste in
  ETSI EN 319 412-5).
- Annex B (informativa) è una tabella minaccia/copertura compilata da
  ENISA: il testo stesso dichiara che ogni minaccia è già coperta dai
  requisiti posti nella clausola 8 (e, per le minacce di processo, nella
  clausola 9) del presente documento, cioè da nodi Obbligo/Principio già
  censiti negli altri capitoli di questa fonte. Un nodo per riga di
  minaccia duplicherebbe contenuto normato altrove senza introdurre una
  disposizione propria dell'allegato: modellata quindi come UN solo
  Principio complessivo, tipo "altro", riferimento "Annex B", che
  riassume struttura, fonte (ENISA) e funzione della tabella senza
  ripetere le singole minacce.
- Annex C (normativa) profila i requisiti di clausola 9 specificamente
  per il rilascio di certificati qualificati/attestati elettronici
  qualificati di attributi (art. 24 §1 eIDAS originale; art. 24 §1/§1-bis/
  §1-ter eIDAS modificato) e per l'identificazione di mittenti/destinatari
  di QERDS (art. 44, invariato tra le due versioni del regolamento):
  - Ogni requisito con id proprio "QTS-C.x[.y]-NN" enunciato con "shall"/
    "shall not" -> Obbligo, categoria_soggetto "QTSP/gestore", ruolo
    "obbligato", tipo_obbligo "procedurale" (direttiva esplicita
    dell'assegnazione, applicata in modo uniforme anche a QTS-C.2.4-07 e
    QTS-C.3.4-08 il cui soggetto grammaticale è l'organismo di
    valutazione della conformità: l'Annex C nel suo complesso vincola il
    QTSP come responsabile ultimo del caso d'uso, la conferma del CAB è
    parte integrante dell'adempimento che il QTSP deve assicurare).
  - I 4 requisiti enunciati con "should" (raccomandazione, non
    prescrizione vincolante: QTS-C.2.3-06, QTS-C.3.3-07, QTS-C.4-02,
    QTS-C.4-03) -> Principio, tipo "altro" (nessun soggetto obbligato in
    senso proprio, stesso criterio "shall/shall not -> Obbligo,
    descrittivo/facoltativo -> Principio" di ETSI EN 319 412-5, esteso a
    "should").
  - Le premesse di C.1 Introduction (nessun id di requisito proprio,
    spiegano il perimetro dell'Annex C rispetto alle due versioni di
    eIDAS e la misura transitoria dell'art. 51 §2-ter modificato) ->
    1 Principio "altro", riferimento "clausola C.1".
  - Ogni sottoclausola C.2.x/C.3.x si apre con una condizione
    "[CONDITIONAL] If identity proofing is done for the purpose of...",
    che governa TUTTI i requisiti della sottoclausola: riportata in
    condizione_applicabilita di ciascun nodo della sottoclausola (non
    solo dei requisiti marcati "[CONDITIONAL]" a livello di singolo id,
    la cui condizione aggiuntiva è annessa in coda). QTS-C.4-01 non ha
    condizione_applicabilita propria (si applica in via generale ai sensi
    dell'art. 44, con QTS-C.4-02/03 come innalzamento facoltativo
    condizionato).
  - NOTE annesse a un requisito: assorbite nel testo_integrale/
    condizione_applicabilita SOLO quando aggiungono un'eccezione/
    condizione sostanziale (es. l'esenzione dalla registrazione in
    registri ufficiali per alcune persone giuridiche, annessa a
    QTS-C.2.5-02/QTS-C.2.6-03/QTS-C.3.5-03/QTS-C.3.6-04); le NOTE
    puramente esplicative/di contesto o che si limitano a richiamare la
    base giuridica eIDAS senza mutare la portata del requisito (es. le
    NOTE ripetute "This requirement answers Article 24.1b..." annesse a
    QTS-C.3.1-04/QTS-C.3.2-04/QTS-C.3.3-05/QTS-C.3.4-07, o le NOTE su
    lavori ETSI TC ESI in corso) sono scartate come mera esemplificazione,
    tranne la NOTE di QTS-C.4-01 che spiega perché il livello minimo di
    identity proofing per QERDS è impostato a Baseline LoIP (contenuto
    sostanziale, assorbito nel testo_integrale).
- Annex D (informativa) è una tabella di mapping articolo eIDAS
  modificato -> clausola del presente documento, priva di contenuto
  normativo autonomo (non impone alcun comportamento, si limita a
  indicare dove il documento soddisfa ciascun articolo): modellata come
  UN solo Principio complessivo, tipo "altro", riferimento "Annex D", con
  testo_integrale che riporta l'elenco degli articoli eIDAS citati nella
  tabella (art. 5, 15, 24 §1/§1-bis/§1-ter, 44) come base testuale per le
  relazioni cross-fonte verso eIDAS/eIDAS2 in una fase 6 successiva (NON
  costruite in questo import).
- History (mero changelog di versione) -> nessun nodo, stesso
  trattamento riservato al front matter amministrativo in
  ETSI EN 319 412-5.

RELAZIONI: costruita una sola relazione interna, l'unica citazione
testuale di un id esatto all'interno di questo capitolo (QTS-C.2.4-07:
"The fulfilment of requirement QTS-C.2.4-06 shall be confirmed by a
conformity assessment body."). Altri rinvii dell'Annex C sono a intere
sottoclausole (es. QTS-C.2.6-02 -> "clause C.2.1, or C.2.2, or C.2.3, or
C.2.4") e non a un id di requisito preciso: nessun nodo di questo
capitolo corrisponde 1:1 a una sottoclausola intera (ogni sottoclausola è
frazionata in più nodi per singolo requisito), quindi il rinvio non ha un
target univoco e viene omesso per evitare un riferimento inventato,
coerentemente con l'istruzione di preferire l'omissione al rischio.
Nessuna relazione cross-fonte in questo import (demandate a fase 6).
"""

_COND_C21 = (
    "Si applica quando l'identity proofing è svolto ai fini del rilascio di un "
    "certificato qualificato ai sensi dell'art. 24 §1 del regolamento eIDAS "
    "originale, mediante presenza fisica del richiedente (lettera a dell'articolo)."
)
_COND_C22 = (
    "Si applica quando l'identity proofing è svolto ai fini del rilascio di un "
    "certificato qualificato ai sensi dell'art. 24 §1 del regolamento eIDAS "
    "originale, mediante autenticazione con mezzo di identificazione elettronica "
    "(eID) (lettera b dell'articolo)."
)
_COND_C23 = (
    "Si applica quando l'identity proofing è svolto ai fini del rilascio di un "
    "certificato qualificato ai sensi dell'art. 24 §1 del regolamento eIDAS "
    "originale, mediante il certificato di una firma elettronica qualificata o di "
    "un sigillo elettronico qualificato (lettera c dell'articolo)."
)
_COND_C24 = (
    "Si applica quando l'identity proofing è svolto ai fini del rilascio di un "
    "certificato qualificato ai sensi dell'art. 24 §1 del regolamento eIDAS "
    "originale, mediante altri mezzi di identificazione (lettera d dell'articolo)."
)
_COND_C25 = (
    "Si applica quando l'identity proofing è svolto ai fini del rilascio di un "
    "certificato qualificato ai sensi dell'art. 24 §1 del regolamento eIDAS "
    "originale e riguarda una persona giuridica."
)
_COND_C26 = (
    "Si applica quando l'identity proofing è svolto ai fini del rilascio di un "
    "certificato qualificato ai sensi dell'art. 24 §1 del regolamento eIDAS "
    "originale e riguarda una persona fisica che rappresenta una persona giuridica."
)
_COND_C31 = (
    "Si applica quando l'identity proofing è svolto ai fini del rilascio di un "
    "certificato qualificato o di un attestato elettronico qualificato di "
    "attributi ai sensi dell'art. 24 §1, §1-bis o §1-ter del regolamento eIDAS "
    "modificato, mediante presenza fisica del richiedente (lettera d dell'art. 24 "
    "§1-bis e/o lettera e dell'art. 24 §1-ter)."
)
_COND_C32 = (
    "Si applica quando l'identity proofing è svolto ai fini del rilascio di un "
    "certificato qualificato o di un attestato elettronico qualificato di "
    "attributi ai sensi dell'art. 24 §1, §1-bis o §1-ter del regolamento eIDAS "
    "modificato, mediante autenticazione con mezzo di identificazione elettronica "
    "(eID) (lettera a dell'art. 24 §1-bis e/o lettera a dell'art. 24 §1-ter)."
)
_COND_C33 = (
    "Si applica quando l'identity proofing è svolto ai fini del rilascio di un "
    "certificato qualificato o di un attestato elettronico qualificato di "
    "attributi ai sensi dell'art. 24 §1, §1-bis o §1-ter del regolamento eIDAS "
    "modificato, mediante il certificato di una firma elettronica qualificata o "
    "di un sigillo elettronico qualificato (lettera b dell'art. 24 §1-bis e/o "
    "lettera b dell'art. 24 §1-ter)."
)
_COND_C34 = (
    "Si applica quando l'identity proofing è svolto ai fini del rilascio di un "
    "certificato qualificato o di un attestato elettronico qualificato di "
    "attributi ai sensi dell'art. 24 §1, §1-bis o §1-ter del regolamento eIDAS "
    "modificato, mediante altri mezzi di identificazione (lettera c dell'art. 24 "
    "§1-bis e/o lettera d dell'art. 24 §1-ter)."
)
_COND_C35 = (
    "Si applica quando l'identity proofing è svolto ai fini del rilascio di un "
    "certificato qualificato o di un attestato elettronico qualificato di "
    "attributi ai sensi dell'art. 24 §1, §1-bis o §1-ter del regolamento eIDAS "
    "modificato e riguarda una persona giuridica."
)
_COND_C36 = (
    "Si applica quando l'identity proofing è svolto ai fini del rilascio di un "
    "certificato qualificato o di un attestato elettronico qualificato di "
    "attributi ai sensi dell'art. 24 §1, §1-bis o §1-ter del regolamento eIDAS "
    "modificato e riguarda una persona fisica che rappresenta una persona giuridica."
)
_EXEMPTION_ORIG = (
    " Alcune persone giuridiche (es. enti del settore pubblico in alcuni Stati "
    "membri UE) possono essere esentate dalla registrazione in registri ufficiali "
    "(Allegato III del regolamento eIDAS originale)."
)
_EXEMPTION_MOD = (
    " Alcune persone giuridiche (es. enti del settore pubblico in alcuni Stati "
    "membri UE) possono essere esentate dalla registrazione in registri ufficiali "
    "(Allegato III del regolamento eIDAS modificato)."
)
_ATTENDED_DOC = (
    " Si applica inoltre solo se si utilizza l'identity proofing remoto assistito "
    "(attended) con documento di identità fisico o digitale come prova autorevole."
)
_UNATTENDED_DOC = (
    " Si applica inoltre solo se si utilizza l'identity proofing remoto non "
    "assistito (unattended) con documento di identità fisico o digitale come "
    "prova autorevole."
)
_ENHANCING = (
    " Si applica inoltre solo se l'identity proofing è svolto potenziando un "
    "identity proofing per Baseline LoIP che utilizza un eID come prova autorevole."
)

_FURTHER_ATTR_TESTO = (
    "L'identity proofing per ogni ulteriore attributo aggiuntivo rispetto "
    "all'identità unica della persona deve avvenire secondo i requisiti di una "
    "delle clausole C.3.1, C.3.2, C.3.3 o C.3.4, oppure mediante attestato "
    "elettronico qualificato di attributi, oppure mediante prova supplementare "
    "che, secondo il contesto di identity proofing, sia considerata prova "
    "autorevole ai sensi dei requisiti delle clausole 8.2.6 e 8.3.6 (registro "
    "fidato), e/o 8.2.7 e 8.3.7 (prova di accesso), e/o 8.2.8 e 8.3.8 (documenti "
    "e attestazioni) del presente documento."
)


def _further_attr_integrale(rif: str) -> str:
    return (
        f"{rif}: Identity proofing for any further attributes additional to the "
        "unique identity of the person shall be either according to the "
        "requirements of one of the clauses C.3.1, C.3.2, C.3.3, or C.3.4 of the "
        "present document, or by means of qualified electronic attestation of "
        "attributes, or by means of supplementary evidence that according to the "
        "identity proofing context is regarded as authoritative evidence "
        "according to the requirements of clauses 8.2.6 and 8.3.6 (trusted "
        "register), and/or clauses 8.2.7 and 8.3.7 (proof of access), and/or "
        "clauses 8.2.8 and 8.3.8 (documents and attestations) of the present "
        "document."
    )


RIGHE_OBBLIGHI = [
    # --- C.2.1 ---
    {
        "riferimento": "QTS-C.2.1-01",
        "testo": "Si applicano i requisiti della clausola 9.2.1.1 del presente documento.",
        "testo_integrale": "QTS-C.2.1-01: The requirements of clause 9.2.1.1 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C21,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.1-02",
        "testo": "Si applicano i requisiti della clausola 9.2.1.2, oppure della clausola 9.2.1.3, oppure della clausola 9.2.1.4 del presente documento.",
        "testo_integrale": "QTS-C.2.1-02: The requirements of either clause 9.2.1.2 or clause 9.2.1.3 or clause 9.2.1.4 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C21,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- C.2.2 ---
    {
        "riferimento": "QTS-C.2.2-01",
        "testo": "Si applicano i requisiti per il Baseline LoIP della clausola 9.2.4 del presente documento.",
        "testo_integrale": "QTS-C.2.2-01: The requirements for Baseline LoIP of clause 9.2.4 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C22,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.2-02",
        "testo": "Il mezzo di identificazione elettronica (eID) deve essere un eID eIDAS 'significativo' (substantial) o 'elevato' (high).",
        "testo_integrale": "QTS-C.2.2-02: The eID means shall be eIDAS substantial eID or eIDAS high eID.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C22,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.2-03",
        "testo": "Il mezzo di identificazione elettronica (eID) deve essere stato rilasciato sulla base della presenza fisica della persona fisica o di un rappresentante autorizzato della persona giuridica.",
        "testo_integrale": "QTS-C.2.2-03: The eID means shall have been issued based on physical presence of the natural person or an authorized representative of the legal person.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C22,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- C.2.3 ---
    {
        "riferimento": "QTS-C.2.3-01",
        "testo": "Si applicano i requisiti della clausola 9.2.5 del presente documento.",
        "testo_integrale": "QTS-C.2.3-01: The requirements of clause 9.2.5 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C23,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.3-02",
        "testo": "Se il richiedente è una persona fisica, o una persona fisica che rappresenta una persona giuridica, la firma digitale deve essere una firma elettronica qualificata.",
        "testo_integrale": "QTS-C.2.3-02: If the applicant is a natural person or a natural person representing a legal person, the digital signature shall be a qualified electronic signature.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C23 + " Si applica inoltre solo se il richiedente è una persona fisica o una persona fisica che rappresenta una persona giuridica.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.3-03",
        "testo": "Se il richiedente è una persona giuridica, la firma digitale deve essere un sigillo elettronico qualificato o una firma elettronica qualificata.",
        "testo_integrale": "QTS-C.2.3-03: If the applicant is a legal person, the digital signature shall be a qualified electronic seal or a qualified electronic signature.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C23 + " Si applica inoltre solo se il richiedente è una persona giuridica.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.3-04",
        "testo": "Il certificato qualificato deve essere stato rilasciato sulla base di un identity proofing effettuato o mediante previa presenza fisica della persona fisica o di un rappresentante autorizzato della persona giuridica, oppure mediante un eID eIDAS 'significativo' o 'elevato' a sua volta basato su un identity proofing per presenza fisica della persona fisica o di un rappresentante autorizzato.",
        "testo_integrale": "QTS-C.2.3-04: The qualified certificate shall have been issued based on identity proofing either by a prior physical presence of the natural person or of an authorized representative of the legal person, or by an eIDAS substantial eID or an eIDAS high eID that is in turn based on identity proofing by the physical presence of the natural person or an authorized representative of the legal person.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C23,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.3-05",
        "testo": "La firma deve essere convalidata mediante la convalida della firma eIDAS.",
        "testo_integrale": "QTS-C.2.3-05: The signature shall be validated by eIDAS signature validation.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C23,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- C.2.4 ---
    {
        "riferimento": "QTS-C.2.4-01",
        "testo": "Se si utilizza l'identity proofing remoto assistito (attended) con documento di identità fisico o digitale come prova autorevole, si applicano i requisiti della clausola 9.2.2.1 del presente documento.",
        "testo_integrale": "QTS-C.2.4-01: If attended remote identity proofing using physical or digital identity document as authoritative evidence is used, the requirements of clause 9.2.2.1 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C24 + _ATTENDED_DOC,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.4-02",
        "testo": "Se si utilizza l'identity proofing remoto assistito (attended) con documento di identità fisico o digitale come prova autorevole, si applicano i requisiti della clausola 9.2.2.2 oppure della clausola 9.2.2.3 del presente documento.",
        "testo_integrale": "QTS-C.2.4-02: If attended remote identity proofing using physical or digital identity document as authoritative evidence is used, the requirements of either clause 9.2.2.2 or 9.2.2.3 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C24 + _ATTENDED_DOC,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.4-03",
        "testo": "Se si utilizza l'identity proofing remoto non assistito (unattended) con documento di identità fisico o digitale come prova autorevole, si applicano i requisiti della clausola 9.2.3.1 del presente documento.",
        "testo_integrale": "QTS-C.2.4-03: If unattended remote identity proofing using physical or digital identity document as authoritative evidence is used, the requirements of clause 9.2.3.1 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C24 + _UNATTENDED_DOC,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.4-04",
        "testo": "Se si utilizza l'identity proofing remoto non assistito (unattended) con documento di identità fisico o digitale come prova autorevole, si applicano i requisiti della clausola 9.2.3.2, oppure 9.2.3.3, oppure 9.2.3.4 del presente documento.",
        "testo_integrale": "QTS-C.2.4-04: If unattended remote identity proofing using physical or digital identity document as authoritative evidence is used, the requirements of either clause 9.2.3.2 or 9.2.3.3 or 9.2.3.4 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C24 + _UNATTENDED_DOC,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.4-05",
        "testo": "Il metodo di identity proofing deve essere riconosciuto a livello nazionale dallo Stato membro UE in cui il prestatore di servizi fiduciari qualificato è registrato.",
        "testo_integrale": "QTS-C.2.4-05: The identity proofing method shall be recognized at national level by the EU Member State in which the qualified trust service provider is registered.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C24,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.4-06",
        "testo": "Il metodo di identity proofing deve fornire, in termini di affidabilità, un livello di garanzia equivalente alla presenza fisica, come determinato a livello nazionale dallo Stato membro UE in cui il prestatore di servizi fiduciari qualificato è registrato.",
        "testo_integrale": "QTS-C.2.4-06: The identity proofing method shall in terms of reliability provide equivalent assurance of the identity proofing to physical presence as determined at national level by the EU Member State in which the qualified trust service provider is registered.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C24,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.4-07",
        "testo": "L'adempimento del requisito QTS-C.2.4-06 deve essere confermato da un organismo di valutazione della conformità.",
        "testo_integrale": "QTS-C.2.4-07: The fulfilment of requirement QTS-C.2.4-06 shall be confirmed by a conformity assessment body.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C24,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- C.2.5 ---
    {
        "riferimento": "QTS-C.2.5-01",
        "testo": "Si applicano i requisiti della clausola 9.3 del presente documento.",
        "testo_integrale": "QTS-C.2.5-01: The requirements of clause 9.3 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C25,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.5-02",
        "testo": "Ove pertinente, il numero di registrazione della persona giuridica, come indicato nel pertinente registro ufficiale fidato, deve essere raccolto e convalidato.",
        "testo_integrale": "QTS-C.2.5-02: Where applicable, the legal person registration number as stated in the appropriate official, trusted register shall be collected and validated.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C25 + _EXEMPTION_ORIG,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- C.2.6 ---
    {
        "riferimento": "QTS-C.2.6-01",
        "testo": "Si applicano i requisiti della clausola 9.4 del presente documento per il Baseline LoIP o l'Extended LoIP.",
        "testo_integrale": "QTS-C.2.6-01: The requirements of clause 9.4 of the present document for Baseline LoIP or Extended LoIP shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C26,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.6-02",
        "testo": "L'identità della persona fisica deve essere comprovata secondo i requisiti della clausola C.2.1, oppure C.2.2, oppure C.2.3, oppure C.2.4 del presente documento.",
        "testo_integrale": "QTS-C.2.6-02: The identity of the natural person shall be proven according to the requirements of clause C.2.1, or C.2.2, or C.2.3, or C.2.4 of the present document.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C26,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.2.6-03",
        "testo": "Ove pertinente, il numero di registrazione della persona giuridica, come indicato nel pertinente registro ufficiale fidato, deve essere raccolto e convalidato.",
        "testo_integrale": "QTS-C.2.6-03: Where applicable, the legal person registration number as stated in the appropriate official, trusted register shall be collected and validated.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C26 + _EXEMPTION_ORIG,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- C.3.1 ---
    {
        "riferimento": "QTS-C.3.1-01",
        "testo": "Si applicano i requisiti per l'Extended LoIP della clausola 9.2.1.1 del presente documento.",
        "testo_integrale": "QTS-C.3.1-01: The requirements for Extended LoIP of clause 9.2.1.1 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C31,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.1-02",
        "testo": "Si applicano i requisiti per l'Extended LoIP della clausola 9.2.1.2, oppure 9.2.1.3, oppure 9.2.1.4 del presente documento.",
        "testo_integrale": "QTS-C.3.1-02: The requirements for Extended LoIP of either clause 9.2.1.2 or 9.2.1.3 or 9.2.1.4 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C31,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.1-03",
        "testo": "La procedura per la presenza fisica deve essere conforme al diritto nazionale dello Stato membro UE in cui il prestatore di servizi fiduciari qualificato è registrato.",
        "testo_integrale": "QTS-C.3.1-03: The procedure for physical presence shall be in accordance with national law in the EU Member State where the qualified trust service provider is registered.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C31,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.1-04",
        "testo": _FURTHER_ATTR_TESTO,
        "testo_integrale": _further_attr_integrale("QTS-C.3.1-04"),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C31,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- C.3.2 ---
    {
        "riferimento": "QTS-C.3.2-01",
        "testo": "Si applicano i requisiti per l'Extended LoIP della clausola 9.2.4 del presente documento.",
        "testo_integrale": "QTS-C.3.2-01: The requirements for Extended LoIP of clause 9.2.4 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C32,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.2-02",
        "testo": "Il mezzo di identificazione elettronica (eID) deve essere conforme a eIDAS high eID.",
        "testo_integrale": "QTS-C.3.2-02: The eID means shall conform to eIDAS high eID.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C32,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.2-03",
        "testo": "Il mezzo di identificazione elettronica (eID) deve essere un eID notificato eIDAS.",
        "testo_integrale": "QTS-C.3.2-03: The eID means shall be eIDAS notified eID.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C32,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.2-04",
        "testo": _FURTHER_ATTR_TESTO,
        "testo_integrale": _further_attr_integrale("QTS-C.3.2-04"),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C32,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- C.3.3 ---
    {
        "riferimento": "QTS-C.3.3-01",
        "testo": "Si applicano i requisiti per l'Extended LoIP della clausola 9.2.5 del presente documento.",
        "testo_integrale": "QTS-C.3.3-01: The requirements for Extended LoIP of clause 9.2.5 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C33,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.3-02",
        "testo": "Se il richiedente è una persona fisica, o una persona fisica che rappresenta una persona giuridica, la firma digitale deve essere una firma elettronica qualificata.",
        "testo_integrale": "QTS-C.3.3-02: If the applicant is a natural person or a natural person representing a legal person, the digital signature shall be a qualified electronic signature.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C33 + " Si applica inoltre solo se il richiedente è una persona fisica o una persona fisica che rappresenta una persona giuridica.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.3-03",
        "testo": "Se il richiedente è una persona giuridica, la firma digitale deve essere un sigillo elettronico qualificato o una firma elettronica qualificata.",
        "testo_integrale": "QTS-C.3.3-03: If the applicant is a legal person, the digital signature shall be a qualified electronic seal or a qualified electronic signature.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C33 + " Si applica inoltre solo se il richiedente è una persona giuridica.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.3-04",
        "testo": "Il certificato qualificato utilizzato per l'identity proofing deve essere stato rilasciato sulla base di un identity proofing effettuato secondo una delle seguenti alternative: a) presenza fisica ai sensi della clausola C.3.1 o C.2.1; b) mezzo di identificazione elettronica (eID) ai sensi della clausola C.3.2; c) eID ai sensi della clausola C.2.2, quando l'eID è al contempo eIDAS high eID ed eID notificato eIDAS; d) altri mezzi di identificazione ai sensi della clausola C.3.4.",
        "testo_integrale": "QTS-C.3.3-04: The qualified certificate used for the identity proofing shall have been issued based on identity proofing by one of the following alternatives: a) physical presence according to clause C.3.1 or C.2.1 of the present document; b) eID means according to clause C.3.2 of the present document; c) eID means according to clause C.2.2 of the present document when the eID is both an eIDAS high eID and an eIDAS notified eID; d) Other identification means according to clause C.3.4 of the present document.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C33,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.3-05",
        "testo": _FURTHER_ATTR_TESTO,
        "testo_integrale": _further_attr_integrale("QTS-C.3.3-05"),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C33,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.3-06",
        "testo": "La firma deve essere convalidata secondo la convalida della firma eIDAS.",
        "testo_integrale": "QTS-C.3.3-06: The signature shall be validated according to eIDAS signature validation.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C33,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- C.3.4 ---
    {
        "riferimento": "QTS-C.3.4-01",
        "testo": "Se si utilizza l'identity proofing remoto assistito (attended) con documento di identità fisico o digitale come prova autorevole, si applicano i requisiti per l'Extended LoIP della clausola 9.2.2.1 del presente documento.",
        "testo_integrale": "QTS-C.3.4-01: If attended remote identity proofing using physical or digital identity document as authoritative evidence is used, the requirements for Extended LoIP of clause 9.2.2.1 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C34 + _ATTENDED_DOC,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.4-02",
        "testo": "Se si utilizza l'identity proofing remoto assistito (attended) con documento di identità fisico o digitale come prova autorevole, si applicano i requisiti per l'Extended LoIP della clausola 9.2.2.3 del presente documento.",
        "testo_integrale": "QTS-C.3.4-02: If attended remote identity proofing using physical or digital identity document as authoritative evidence is used, the requirements for Extended LoIP of clause 9.2.2.3 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C34 + _ATTENDED_DOC,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.4-03",
        "testo": "Se si utilizza l'identity proofing remoto non assistito (unattended) con documento di identità fisico o digitale come prova autorevole, si applicano i requisiti per l'Extended LoIP della clausola 9.2.3.1 del presente documento.",
        "testo_integrale": "QTS-C.3.4-03: If unattended remote identity proofing using physical or digital identity document as authoritative evidence is used, the requirements for Extended LoIP of clause 9.2.3.1 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C34 + _UNATTENDED_DOC,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.4-04",
        "testo": "Se si utilizza l'identity proofing remoto non assistito (unattended) con documento di identità fisico o digitale come prova autorevole, si applicano i requisiti per l'Extended LoIP della clausola 9.2.3.3 oppure 9.2.3.4 del presente documento.",
        "testo_integrale": "QTS-C.3.4-04: If unattended remote identity proofing using physical or digital identity document as authoritative evidence is used, the requirements for Extended LoIP of either clause 9.2.3.3 or clause 9.2.3.4 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C34 + _UNATTENDED_DOC,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.4-05",
        "testo": "Se l'identity proofing è svolto potenziando un identity proofing per Baseline LoIP che utilizza un eID come prova autorevole, si applicano i requisiti della clausola 9.5 del presente documento.",
        "testo_integrale": "QTS-C.3.4-05: If identity proofing is done by enhancing an identity proofing for Baseline LoIP using eID as authoritative evidence, the requirements of clause 9.5 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C34 + _ENHANCING,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.4-06",
        "testo": "Se l'identity proofing è svolto potenziando un identity proofing per Baseline LoIP che utilizza un eID come prova autorevole, l'eID utilizzato come prova autorevole deve essere un eID eIDAS 'significativo' o 'elevato' e inoltre: a) essere un eID notificato eIDAS; oppure b) essere un eID certificato eIDAS; oppure c) essere stato valutato da un organismo indipendente di valutazione della conformità come conforme ai requisiti per un eID eIDAS 'significativo' o 'elevato'.",
        "testo_integrale": "QTS-C.3.4-06: If identity proofing is done by enhancing an identity proofing for Baseline LoIP using eID as authoritative evidence, the eID used as authoritative evidence shall be an eIDAS substantial eID or eIDAS high eID and either: a) be an eIDAS notified eID; or b) be an eIDAS certified eID; or c) have been assessed by an independent conformity assessment body to fulfil the requirements for an eIDAS substantial eID or eIDAS high eID.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C34 + _ENHANCING,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.4-07",
        "testo": _FURTHER_ATTR_TESTO,
        "testo_integrale": _further_attr_integrale("QTS-C.3.4-07"),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C34,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.4-08",
        "testo": "La conformità del metodo di identity proofing ai requisiti della presente clausola C.3.4 deve essere confermata da un organismo di valutazione della conformità.",
        "testo_integrale": "QTS-C.3.4-08: The conformity of the identity proofing method with the requirements of this clause C.3.4 of the present document shall be confirmed by a conformity assessment body.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C34,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- C.3.5 ---
    {
        "riferimento": "QTS-C.3.5-01",
        "testo": "L'identity proofing per l'identità unica della persona giuridica deve avvenire secondo i requisiti per l'Extended LoIP della clausola 9.3 del presente documento.",
        "testo_integrale": "QTS-C.3.5-01: Identity proofing for the unique identity of the legal person shall be according to the requirements for Extended LoIP of clause 9.3 of the present document.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C35,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.5-02",
        "testo": "L'identity proofing per ogni ulteriore attributo aggiuntivo rispetto all'identità unica della persona giuridica deve avvenire secondo i requisiti per l'Extended LoIP della clausola 9.3 del presente documento, oppure mediante attestato elettronico qualificato di attributi.",
        "testo_integrale": "QTS-C.3.5-02: Identity proofing for any further attributes additional to the unique identity of the legal person shall be either according to the requirements for Extended LoIP of clause 9.3 of the present document or by means of qualified electronic attestation of attributes.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C35,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.5-03",
        "testo": "Ove pertinente, il numero di registrazione della persona giuridica, come indicato nel pertinente registro ufficiale fidato, deve essere raccolto e convalidato.",
        "testo_integrale": "QTS-C.3.5-03: Where applicable, the legal person registration number as stated in the appropriate official, trusted register shall be collected and validated.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C35 + _EXEMPTION_MOD,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- C.3.6 ---
    {
        "riferimento": "QTS-C.3.6-01",
        "testo": "Si applicano i requisiti per l'Extended LoIP della clausola 9.4 del presente documento.",
        "testo_integrale": "QTS-C.3.6-01: The requirements for Extended LoIP of clause 9.4 of the present document shall apply.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C36,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.6-02",
        "testo": "L'identità della persona fisica deve essere comprovata secondo i requisiti della clausola C.3.1, oppure C.3.2, oppure C.3.3, oppure C.3.4 del presente documento.",
        "testo_integrale": "QTS-C.3.6-02: The identity of the natural person shall be proven according to the requirements of clause C.3.1, or C.3.2, or C.3.3, or C.3.4 of the present document.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C36,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.6-03",
        "testo": "L'identity proofing per ogni ulteriore attributo aggiuntivo rispetto all'identità unica della persona giuridica e/o della persona fisica deve avvenire secondo i requisiti per l'Extended LoIP della clausola 9.4 del presente documento, oppure mediante attestato elettronico qualificato di attributi.",
        "testo_integrale": "QTS-C.3.6-03: Identity proofing for any further attributes additional to the unique identity of the legal person and/or the natural person shall be either according to the requirements for Extended LoIP of clause 9.4 of the present document or by means of qualified electronic attestation of attributes.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C36,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "QTS-C.3.6-04",
        "testo": "Ove pertinente, il numero di registrazione della persona giuridica, come indicato nel pertinente registro ufficiale fidato, deve essere raccolto e convalidato.",
        "testo_integrale": "QTS-C.3.6-04: Where applicable, the legal person registration number as stated in the appropriate official, trusted register shall be collected and validated.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C36 + _EXEMPTION_MOD,
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- C.4 ---
    {
        "riferimento": "QTS-C.4-01",
        "testo": "L'identity proofing per mittenti e destinatari di un QERDS (servizio elettronico di recapito certificato qualificato) deve, come minimo, avvenire mediante applicazione del pertinente caso d'uso della clausola C.2 del presente documento.",
        "testo_integrale": (
            "QTS-C.4-01: Identity proofing for senders and addressees of a QERDS "
            "shall at a minimum be done by application of the relevant use case "
            "from clause C.2 of the present document. NOTE: Requirements for "
            "identification of senders and addressees of Qualified Electronic "
            "Registered Delivery Services (QERDS) are not changed from the "
            "original to the amended eIDAS regulation [i.25]. In line with "
            "current practice for deployed QERDSs, the requirement for identity "
            "proofing is set to Baseline LoIP according to clause C.2 of the "
            "present document. Preamble (52) to the amended eIDAS regulation "
            "[i.25] can be read as requiring a higher level of identity proofing. "
            "This is reflected in conditional requirements for Extended LoIP "
            "where authenticity and/or confidentiality of the information "
            "delivered is critical."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "Annex B",
        "testo": (
            "L'Annex B (informativo) raccoglie un elenco non esaustivo di minacce "
            "all'identity proofing remoto, compilato dall'ENISA nel rapporto "
            "\"Remote ID proofing - Analysis of methods to carry out identity "
            "proofing remotely\", organizzato per fase del processo: minacce di "
            "avvio, minacce alla raccolta e validazione di attributi e prove, "
            "minacce al binding con il richiedente, minacce generali non "
            "specifiche di una singola fase. Per ciascuna minaccia il testo "
            "indica la relativa copertura da parte dei requisiti già posti nella "
            "clausola 8 (e, per le minacce di processo, nella clausola 9) del "
            "presente documento: l'allegato non introduce prescrizioni "
            "normative autonome ulteriori rispetto a quelle già censite nei "
            "capitoli relativi alla clausola 8/9 di questa fonte."
        ),
        "testo_integrale": (
            "Annex B (informative): Threats to identity proofing. The list of "
            "threats below is compiled by ENISA in the report \"Remote ID "
            "proofing-Analysis of methods to carry out identity proofing "
            "remotely\" [i.15]. The list is compiled from the replies received "
            "by ENISA from their stakeholders' questionnaire and considering "
            "various other literature on identity proofing as referenced by the "
            "ENISA report. It is a non-exhaustive list of threats, as all such "
            "lists will be not least due to the rapidly changing threat "
            "landscape in the identity proofing area. The threats are at a "
            "relatively coarse level that can be detailed in further versions "
            "of the present document. Threats are described relatively to the "
            "process tasks defined in the present document: initiation threats, "
            "attribute and evidence collection and validation threats (Table "
            "B.2), binding to applicant threats (Table B.3), and general "
            "threats that are not specific to any task of the identity proofing "
            "process (Table B.4). For each threat, the table states its "
            "coverage by the requirements of clause 8 (and, where relevant, "
            "clause 9) of the present document."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola C.1",
        "testo": (
            "La clausola C.1 introduce l'Annex C precisando che l'allegato "
            "specifica i requisiti per l'identity proofing finalizzato "
            "specificamente all'adempimento dell'art. 24 §1 del regolamento "
            "eIDAS originale (rilascio di certificati qualificati), dell'art. "
            "24 §1/§1-bis/§1-ter del regolamento eIDAS modificato (rilascio di "
            "certificati qualificati e attestati elettronici qualificati di "
            "attributi) e dell'art. 44 (identificazione di mittenti e "
            "destinatari dei QERDS, requisito invariato tra le due versioni del "
            "regolamento); per gli altri servizi fiduciari qualificati, né il "
            "regolamento originale né quello modificato pongono requisiti "
            "specifici di identity proofing. L'art. 24 §1 originale è sostituito "
            "dall'art. 24 §1/§1-bis/§1-ter modificato, ma l'art. 51 §2-ter del "
            "regolamento modificato prevede una misura transitoria che consente "
            "a un prestatore già qualificato prima dell'entrata in vigore del "
            "regolamento modificato di continuare ad avvalersi dei metodi "
            "dell'art. 24 §1 originale per 24 mesi da tale entrata in vigore: "
            "per questo l'Annex C include sia i casi d'uso per il regolamento "
            "originale (clausola C.2) sia quelli per il regolamento modificato "
            "(clausola C.3). Riguardo agli attestati elettronici qualificati di "
            "attributi, l'Allegato VI del regolamento modificato specifica un "
            "elenco minimo di attributi per i quali gli Stati membri devono "
            "fornire mezzi di verifica rispetto a fonti autentiche; poiché molti "
            "di questi attributi non possono provenire da prove autorevoli come "
            "definite dal presente documento, è necessario ricorrere a prove "
            "supplementari - il regolamento modificato non richiede che "
            "l'attestato si basi (solo) su fonti autentiche, potendo includere "
            "anche altri attributi ulteriori rispetto a quelli dell'Allegato VI."
        ),
        "testo_integrale": (
            "C.1 Introduction. This annex specifies requirements for identity "
            "proofing targeted explicitly to fulfil requirements of the "
            "original eIDAS regulation [i.1] and the amended eIDAS regulation "
            "[i.25]. Requirements for identity proofing are posed in Article "
            "24.1 of the original eIDAS regulation [i.1] for issuing of "
            "qualified certificates, in Article 24.1, 24.1a, and 24.1b of the "
            "amended eIDAS regulation [i.25] for issuing of qualified "
            "certificates and qualified electronic attestation of attributes, "
            "and in Article 44 (same requirements for both the original [i.1] "
            "and the amended [i.25] eIDAS regulation) for identification of "
            "senders and addressees of Qualified Electronic Registered Delivery "
            "Services (QERDS). For other qualified trust services, neither the "
            "original nor the amended eIDAS regulation pose specific "
            "requirements for identity proofing. Article 24.1 of the original "
            "eIDAS regulation [i.1] is superseded by Article 24.1, 24.1a, and "
            "24.1b of the amended eIDAS regulation [i.25] but the amended "
            "eIDAS regulation [i.25] Article 51.2b specifies a transitional "
            "measure where a qualified trust service provider that is granted "
            "the qualified status before entry into force of the amended "
            "eIDAS regulation [i.25] is allowed to continue to rely on the "
            "methods set out in Article 24.1 of the original eIDAS regulation "
            "[i.1] until 24 months after the entry into force of the amended "
            "eIDAS regulation [i.25]. Hence, the present document includes use "
            "cases to fulfil the requirements of Article 24.1 of the original "
            "eIDAS regulation [i.1] in clause C.2. Regarding qualified "
            "electronic attestation of attributes, Annex VI of the amended "
            "eIDAS regulation [i.25] specifies a minimum list of attributes for "
            "which EU Member States are required to provide means for "
            "verification against authentic sources. Many of these attributes "
            "cannot be expected to be provided by authoritative evidence as "
            "defined by the present document, meaning supplementary evidence is "
            "required for these attributes. The amended eIDAS regulation "
            "[i.25] however has no requirement for a qualified electronic "
            "attestation of attributes to be based (solely) on authentic "
            "sources; other supplementary evidence can be used. Qualified "
            "electronic attestations of attributes can include other "
            "attributes than those defined by Annex VI of the amended eIDAS "
            "regulation [i.25]."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "QTS-C.2.3-06",
        "testo": "La firma dovrebbe essere convalidata secondo ETSI TS 119 172-4.",
        "testo_integrale": "QTS-C.2.3-06: The signature should be validated according to ETSI TS 119 172-4 [7].",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C23,
    },
    {
        "riferimento": "QTS-C.3.3-07",
        "testo": "La firma dovrebbe essere convalidata secondo ETSI TS 119 172-4.",
        "testo_integrale": "QTS-C.3.3-07: The signature should be validated according to ETSI TS 119 172-4 [7].",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": _COND_C33,
    },
    {
        "riferimento": "QTS-C.4-02",
        "testo": "Se il QERDS supporta consegne per le quali l'autenticità dell'informazione è critica, l'identity proofing per i mittenti pertinenti del QERDS dovrebbe avvenire mediante applicazione del pertinente caso d'uso della clausola C.3 del presente documento.",
        "testo_integrale": "QTS-C.4-02: If the QERDS supports deliveries where the authenticity of the information is critical, identity proofing for the relevant senders of the QERDS should be done by application of the relevant use case from clause C.3 of the present document.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se il QERDS supporta consegne per le quali l'autenticità dell'informazione è critica.",
    },
    {
        "riferimento": "QTS-C.4-03",
        "testo": "Se il QERDS supporta consegne per le quali la riservatezza dell'informazione è critica, l'identity proofing per i destinatari pertinenti del QERDS dovrebbe avvenire mediante applicazione del pertinente caso d'uso della clausola C.3 del presente documento.",
        "testo_integrale": "QTS-C.4-03: If the QERDS supports deliveries where the confidentiality of the information is critical, identity proofing for the relevant addressees of the QERDS should be done by application of the relevant use case from clause C.3 of the present document.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica se il QERDS supporta consegne per le quali la riservatezza dell'informazione è critica.",
    },
    {
        "riferimento": "Annex D",
        "testo": (
            "L'Annex D (informativo) mappa i requisiti del regolamento eIDAS "
            "modificato applicabili specificamente all'identity proofing (che "
            "non è di per sé un servizio fiduciario ma una componente di "
            "servizio fiduciario) verso le clausole del presente documento che "
            "ne assicurano l'adempimento: art. 5 (pseudonimi nelle transazioni "
            "elettroniche), art. 15 (accessibilità per persone con disabilità e "
            "bisogni speciali), art. 24 (requisiti per i prestatori di servizi "
            "fiduciari qualificati - verifica dell'identità §1-bis e verifica "
            "degli attributi §1-ter, oltre al §1 del regolamento originale), "
            "art. 44 (requisiti per i servizi elettronici di recapito "
            "certificato qualificato - QERDS). La tabella precisa che, quando "
            "un QTSP subappalta un IPSP per l'identity proofing, l'IPSP dovrà "
            "comunque soddisfare determinati requisiti eIDAS (in particolare su "
            "gestione del rischio e sicurezza) tramite il contratto tra QTSP e "
            "IPSP, aspetto non coperto dalla tabella stessa. La mappatura è una "
            "base testuale utile per le relazioni cross-fonte verso "
            "eIDAS/eIDAS2 da costruire in una fase 6 successiva, non ancora "
            "effettuata in questo import."
        ),
        "testo_integrale": (
            "Annex D (informative): Mapping to applicable requirements of the "
            "amended eIDAS regulation. Identity proofing is not in itself a "
            "trust service, but a trust service component. Table D.1 covers "
            "the requirements from the amended eIDAS regulation [i.25] that "
            "explicitly apply to identity proofing. When a QTSP subcontracts "
            "an IPSP for identity proofing, the IPSP will need to fulfil "
            "certain eIDAS requirements especially regarding risk management "
            "and security; these aspects are not covered in the table because "
            "fulfilment of eIDAS requirements will be part of the contract "
            "between the QTSP and the IPSP. Articles mapped: Article 5 "
            "(Pseudonyms in electronic transactions) - COL-8.2.2.1-02A and "
            "note; Article 15 (Accessibility for persons with disabilities and "
            "special needs) - INI-8.1-04 and note; Article 24 (Requirements "
            "for qualified trust service providers), paragraph (1a) "
            "verification of identity by methods (a)-(d) - Clause C.3.2 (and "
            "C.3.5 for legal person, C.3.6 for natural person representing "
            "legal person) for the European Digital Identity Wallet/notified "
            "eID at assurance level high; Clause C.3.3 (and C.3.5/C.3.6) for "
            "qualified certificate of electronic signature/seal; Clause C.3.4 "
            "(and C.3.5/C.3.6) for other identification methods confirmed by a "
            "conformity assessment body; Clause C.3.1 (and C.3.5/C.3.6) for "
            "physical presence; paragraph (1b) verification of attributes by "
            "methods (a)-(e) - QTS-C3.1-04, QTS-C.3.2-04, QTS-C-3-3-05, "
            "QTS-C.3.4-07 (and QTS-C.3.5-02 for legal person, QTS-C.3.6-03 for "
            "natural person representing legal person); paragraph (1) of the "
            "original eIDAS regulation (verification of identity and "
            "attributes for qualified certificate/QEAA) - Clause C.3; Article "
            "44 (Requirements for qualified electronic registered delivery "
            "services), paragraph (1) letters (c)-(d) (identification of "
            "sender/addressee with a high level of confidence before delivery) "
            "- Clause C.4."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [riga["riferimento"] for riga in RIGHE_OBBLIGHI] + [
    riga["riferimento"] for riga in RIGHE_PRINCIPI
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "QTS-C.2.4-07"),
        "nodo_a": ("obbligo", None, "QTS-C.2.4-06"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
