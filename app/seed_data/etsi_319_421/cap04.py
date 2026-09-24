"""ETSI EN 319 421 V1.3.1 (2025-07) - Electronic Signatures and Trust
Infrastructures (ESI); Policy and Security Requirements for Trust Service
Providers issuing Time-Stamps. Fonte 18 (unica, non multi-parte; la
numerazione definitiva e' cablata dalla sessione principale in app/seed.py -
questo modulo NON tocca seed.py). Capitolo 4: clausola 7.7 (Time-stamping:
7.7.1 Time-stamp issuance, 7.7.2 Clock synchronization with UTC), 7.8
(Physical and environmental security), 7.9 (Operation security), 7.10
(Network security), 7.11 (Incident management), 7.12 (Collection of
evidence), 7.13 (Business continuity management), 7.14 (TSA termination and
termination plans), 7.15 (Compliance), 7.16 (Supply chain). Testo ufficiale
in app/.source_cache/etsi_319_421/cap04.txt. Manifest di split:
app/.source_cache/etsi_319_421/manifest.json.

Modellazione (ADR-0007/ADR-0010), stesso criterio gia' applicato agli altri
standard tecnici ETSI censiti (ETSI TS 119 461/Fonte 9, ETSI EN 319 401/
Fonte 10, ETSI EN 319 411, ETSI TS 119 431): un nodo Obbligo per ogni
requisito numerato del testo, `riferimento` = requirement id esatto come
appare nel testo ufficiale (prefisso "TIS-" per le clausole 7.7.1/7.7.2,
prefisso "OVR-" per le clausole da 7.8 a 7.16), senza testo aggiuntivo.

Perimetro e conteggio (verificato scorrendo l'intero file cap04.txt):

- 7.7.1 Time-stamp issuance -> 9 Obblighi TIS-7.7.1-01..09.
- 7.7.2 Clock synchronization with UTC -> 9 Obblighi TIS-7.7.2-01..09.
- 7.8 Physical and environmental security -> 12 Obblighi OVR-7.8-01..12.
- 7.9 Operation security -> 2 Obblighi OVR-7.9-01..02.
- 7.10 Network security -> 4 Obblighi OVR-7.10-01..04.
- 7.11 Incident management -> 1 Obbligo OVR-7.11-01.
- 7.12 Collection of evidence -> 6 Obblighi OVR-7.12-01..06.
- 7.13 Business continuity management -> 5 Obblighi OVR-7.13-01..05.
- 7.14 TSA termination and termination plans -> 4 Obblighi
  OVR-7.14-01..04.
- 7.15 Compliance -> 1 Obbligo OVR-7.15-01.
- 7.16 Supply chain -> 1 Obbligo OVR-7.16-01.
Totale: 54 Obblighi, 0 Principi, 54 item di indice. Nessun requisito porta
un suffisso letterale (non compaiono forme tipo "OVR-7.8-01A" in questo
perimetro: verificato sull'intero testo del capitolo).

Clausole/titoli senza requisito proprio -> NESSUN nodo e nessun item di
indice aggiuntivo, per le ragioni seguenti:

- I titoli di clausola ("7.8 Physical and environmental security", "7.10
  Network security", ...) non hanno testo discorsivo autonomo: la clausola
  apre immediatamente con il proprio primo requisito numerato.
- I tre titoli intermedi in grassetto non numerati di clausola 7.9 e 7.12
  ("System Planning" dentro 7.9; "TSU key management" e "Clock
  Synchronization" dentro 7.12) NON sono requisiti: sono etichette
  organizzatrici di sotto-blocchi tematici. Non generano nodi ne' item di
  indice (la loro funzione organizzatrice e' gia' coperta dai requisiti che
  seguono, e il criterio di ADR-0007 modella i requisiti numerati, non i
  raggruppamenti tipografici), coerentemente con il trattamento gia'
  riservato ai titoli non numerati negli altri capitoli ETSI di questo
  censimento. Il testo discorsivo immediatamente adiacente a ciascuno di
  essi NON e' perso: e' la frase "In addition, the following particular
  requirements apply:" (che chiude il requisito di applicabilita' che precede
  il titolo) oppure, quando il titolo e' in coda alla clausola, il requisito
  stesso che lo precede (OVR-7.12-04 chiude il blocco "TSU key management" e
  apre "Clock Synchronization" con il proprio enunciato). In particolare:
  "System Planning" e' assorbito in coda a OVR-7.9-01; "TSU key management"
  e' assorbito in coda a OVR-7.12-01; "Clock Synchronization" e' assorbito in
  coda a OVR-7.12-04 (i cui record riguardano proprio la sincronizzazione
  dell'orologio, per cui il titolo che segue e' il suo naturale
  raggruppamento). Questa e' l'unica scelta di attribuzione non
  autoevidente del capitolo ed e' esplicitata qui.
- Nessuna clausola di cornice priva di requisito (Scope, definizioni,
  abbreviazioni, notazione, clausole discorsive) cade in questo perimetro:
  le clausole 1-4 sono coperte da cap01, le clausole 5-6 da cap02, le
  clausole 7.1-7.6.7 da cap03. Per questo RIGHE_PRINCIPI = [].

Requisiti [CONDITIONAL] e requisiti con "may":

- 9 requisiti portano la marcatura "[CONDITIONAL]" nel testo ufficiale e
  valorizzano `condizione_applicabilita` con la condizione testuale
  (TIS-7.7.1-06, TIS-7.7.1-07, TIS-7.7.2-06, OVR-7.13-03, OVR-7.13-04,
  OVR-7.13-05, OVR-7.14-02, OVR-7.14-03, OVR-7.14-04). Le condizioni sono
  riportate in italiano nel campo e restano integralmente in inglese nel
  `testo_integrale`.
- Ambiguita' di resa tipografica: nel testo ufficiale OVR-7.13-04 e' marcato
  "[ CONDITIONAL]" (con uno spazio dopo la parentesi quadra aperta, unica
  occorrenza del capitolo), mentre gli altri otto sono marcati
  "[CONDITIONAL]". La marcatura e' la stessa: lo spazio e' un artefatto di
  conversione PDF->markdown e non cambia la semantica del requisito. Nel
  `testo_integrale` la marcatura e' normalizzata a "[CONDITIONAL]" (stessa
  forma usata da tutti gli altri capitoli ETSI di questo censimento), perche'
  il testo ufficiale non contiene alcun marcatore di elisione e la
  normalizzazione e' puramente di spaziatura.
- OVR-7.8-12 ("Other functions may be supported ... provided that ...") e'
  formulato con "may": come da criterio, i requisiti formulati con
  "should"/"may" (raccomandazione o facolta' vincolata) sono comunque
  modellati come Obbligo (lo schema ha un solo tipo prescrittivo; precedente:
  tutti i REQ/PRO di ETSI EN 319 401 e ETSI EN 319 411-1). Il "may" di
  OVR-7.8-12 e' una facolta' condizionata da un vincolo ("provided that the
  access is limited to authorized personnel"), non un requisito facoltativo.
  Analogamente TIS-7.7.1-06 e' formulato in minuscolo ("if the accuracy is
  defined ...") dopo la marcatura, e non per questo perde la natura
  prescrittiva dello "shall" che contiene.

`tipo_obbligo`: criterio applicato voce per voce.

- "tecnico/sicurezza" per i controlli tecnici in senso proprio: conformita'
  al profilo di marca temporale e firma (TIS-7.7.1-01, -02, -08), orologio e
  sua protezione/calibrazione/sincronizzazione (TIS-7.7.1-03, -04, -05, -06,
  -09; TIS-7.7.2-01, -02, -03, -04, -05, -07, -08), sicurezza fisica e
  ambientale (OVR-7.8-01..12, incluso OVR-7.8-06 di registrazione degli
  accessi fisici, che e' un controllo di sicurezza fisica e non un obbligo di
  conservazione documentale), sicurezza di rete e delle zone sicure
  (OVR-7.10-01..04), distruzione delle chiavi private alla cessazione
  (OVR-7.14-03).
- "organizzativo" per gli obblighi di governance/pianificazione: le nove
  clausole di applicabilita' che rendono vincolante il corrispondente blocco
  di ETSI EN 319 401 (OVR-7.8-01, OVR-7.9-01, OVR-7.10-01, OVR-7.11-01,
  OVR-7.13-01, OVR-7.14-01, OVR-7.15-01, OVR-7.16-01), il monitoraggio e le
  proiezioni di capacita' (OVR-7.9-02) e il contenuto del piano di ripristino
  dopo disastri (OVR-7.13-02). Nota: OVR-7.12-01 (rinvio a EN 319 401
  clausola 7.10, "Collection of evidence") e' classificato "di
  conservazione" invece che "organizzativo", perche' il blocco di requisiti
  incorporato e' integralmente materia di registrazione e conservazione delle
  prove (coerente con le cinque righe di dettaglio che ne dipendono); il
  precedente piu' prossimo (ETSI TS 119 461 cap03.py, OVR-7.10-01) usa
  "organizzativo" per il medesimo rinvio, ma la classificazione per materia
  del blocco incorporato e' piu' informativa e non contraddice lo schema
  (nessuna delle due e' imposta dal testo).
- "procedurale" per le regole di condotta operativa con evento scatenante o
  termine: divieto di emissione a orologio fuori accuratezza (TIS-7.7.1-07),
  interruzione dell'emissione in caso di deriva/salto (TIS-7.7.2-06), revoca
  dei certificati non scaduti alla cessazione (OVR-7.14-02), divieto di
  emettere marche temporali fino al ripristino (OVR-7.13-04), divieto di
  nuove coppie di chiavi e nuovi token alla cessazione (OVR-7.14-04).
- "di conservazione" per gli obblighi di registrazione e mantenimento di
  record: TIS-7.7.2-09 (registrazione del momento esatto del cambio da
  secondo intercalare) e OVR-7.12-02..06 (registrazioni su ciclo di vita
  delle chiavi e dei certificati TSU, sincronizzazione e ricalibrazione
  dell'orologio, rilevamento della perdita di sincronizzazione).
- "informativo/trasparenza" per gli obblighi di messa a disposizione di
  informazioni ad abbonati e parti affidanti: OVR-7.13-03 (descrizione della
  compromissione) e OVR-7.13-05 (informazioni per identificare le marche
  temporali potenzialmente interessate).
- "sanzionatorio": nessun requisito di questo capitolo ha natura sanzionatoria.

`testo` e `testo_integrale`:

- `testo` e' la parafrasi italiana fedele e concisa del requisito (mai vuota,
  mai in inglese); `testo_integrale` e' la copia letterale in inglese,
  completa, con il requirement id in testa (convenzione gia' in uso negli
  altri moduli ETSI: l'id e' parte del testo ufficiale in grassetto e la
  formattazione markdown e' rimossa, mantenendo il testo piano).
- NOTE del testo ufficiale: mantenute integralmente quando aggiungono
  contenuto interpretativo o di contesto utile all'adempimento - NOTE 1 sotto
  TIS-7.7.1-04 (cosa sono UTC(k)/BIPM e dove sono riconosciuti), NOTE 1 sotto
  TIS-7.7.2-04 (esempi di minacce), NOTE 3 sotto TIS-7.7.2-09 (preferenze sul
  periodo dell'anno per il secondo intercalare) e la NOTE finale di clausola
  7.13 (valore dell'audit trail delle marche temporali e delle marche di due
  TSU distinte per distinguere marche autentiche da marche retrodatate). Le
  NOTE di mero rinvio a una clausola interna (NOTE 2 sotto TIS-7.7.1-08 "See
  clause 7.6.2"; NOTE 2 sotto TIS-7.7.2-05 "See clause 7.12") sono mantenute
  nel `testo_integrale` perche' non rientrano nella sola fattispecie di
  omissione ammessa (NOTE puramente bibliografiche che rimandano in blocco a
  uno standard esterno) e restano utili a ricostruire il contesto del
  requisito. Nessuna NOTE di questo capitolo e' stata scartata.
- Attribuzione della NOTE finale di clausola 7.13: nel testo ufficiale segue
  OVR-7.13-05 e precede il titolo di clausola 7.14, senza un requisito a cui
  sia agganciata esplicitamente. E' attribuita a OVR-7.13-05 (ultimo
  requisito della clausola, quello a cui tipograficamente segue), come
  chiarimento sul tema della compromissione delle chiavi trattato da 7.13-02/
  -05. Non genera un nodo ne' un item di indice proprio.
- Il testo ufficiale di OVR-7.8-02 contiene "the requirements of security of
  security cryptographic devices" (ripetizione di "security"): e' un refuso
  dell'originale, riportato verbatim senza correzione (non e' compito di
  questo censimento emendare il testo normativo). Analogamente il "TSAs" senza
  apostrofo in OVR-7.13-05 e' riportato come nel testo ufficiale.

RELAZIONI interne (solo citazioni letterali di requirement id, come da
criterio; nessuna relazione per meri rinvii di clausola, es. "See clause
7.6.2" o "See clause 7.12", e nessuna relazione verso fonti diverse dalla
18 - le costruira' la sessione principale in Fase 6/ADR-0009):

- TIS-7.7.1-07 -> TIS-7.7.2-04, TIS-7.7.1-05, TIS-7.7.1-06: il testo cita
  letteralmente "(see TIS-7.7.2-04)" e "(see TIS-7.7.1-05 and TIS-7.7.1-06)"
  -> tre relazioni "richiama".
- TIS-7.7.2-09 -> TIS-7.7.2-08: il testo cita letteralmente "the change
  referred to in TIS-7.7.2-08 occurred" -> una relazione "richiama", ammessa
  dallo stesso criterio della citazione letterale di requirement id. (L'
  incarico enumerava esplicitamente le tre relazioni di TIS-7.7.1-07;
  questa quarta citazione letterale e' stata aggiunta perche' ricade
  esattamente nella fattispecie ammessa dal criterio dichiarato - nessuna
  relazione per rinvii di clausola, relazione per citazione di id.)
- TIS-7.7.1-09: nessuna relazione (l'incarico lo esplicita; il suo testo non
  cita alcun requirement id).
- Tutte le relazioni sono interne alla Fonte 18 (`fonte_id_o_None = None`),
  con evidence_type "textual" e confidence 0.9.

Copertura di indice: `INDICE_ARTICOLI_LOCALE` elenca i 54 requirement id in
ordine di testo; nessun item per i titoli non numerati (System Planning, TSU
key management, Clock Synchronization) ne' per le NOTE. `MAPPATURA_LOCALE`
mappa ogni id su se stesso (nessun accorpamento: ogni riga copre esattamente
un item di indice).
"""

RIGHE_OBBLIGHI: list[dict] = [
    # --- 7.7.1 Time-stamp issuance -------------------------------------
    {
        "riferimento": "TIS-7.7.1-01",
        "testo": (
            "Le marche temporali devono essere conformi al profilo di marca temporale definito in ETSI EN 319 "
            "422."
        ),
        "testo_integrale": (
            "TIS-7.7.1-01: Time-stamps shall conform to the time-stamp profile as defined in ETSI EN 319 422 "
            "[5]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.7.1-02",
        "testo": "Le marche temporali devono essere emesse in modo sicuro.",
        "testo_integrale": "TIS-7.7.1-02: The time-stamps shall be issued securely.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.7.1-03",
        "testo": (
            "Le marche temporali devono includere il tempo corretto. In particolare, si applicano i requisiti "
            "particolari seguenti (TIS-7.7.1-04 e seguenti)."
        ),
        "testo_integrale": (
            "TIS-7.7.1-03: The time-stamps shall include the correct time. In particular:"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.7.1-04",
        "testo": (
            "I valori temporali che la TSU usa nella marca temporale devono essere tracciabili ad almeno uno dei "
            "valori di tempo reale distribuiti da un laboratorio UTC(k)."
        ),
        "testo_integrale": (
            "TIS-7.7.1-04: The time values the TSU uses in the time-stamp shall be traceable to at least one of "
            "the real time values distributed by a UTC(k) laboratory. NOTE 1: The Bureau International des Poids "
            "et Mesures (BIPM) computes UTC on the basis of its local representations UTC(k) from a large "
            "ensemble of atomic clocks in national metrology institutes and national astronomical observatories "
            "round the world. The BIPM disseminates UTC through its monthly Circular T [i.6] (list 1). This is "
            "available on the BIPM website (https://www.bipm.org/) and it officially identifies all those "
            "institutes having recognized UTC(k) time scales."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.7.1-05",
        "testo": (
            "Il tempo incluso nella marca temporale deve essere sincronizzato con UTC come definito nella "
            "Raccomandazione ITU-R TF.460-6, entro l'accuratezza definita nella policy."
        ),
        "testo_integrale": (
            "TIS-7.7.1-05: The time included in the time-stamp shall be synchronized with UTC as defined in "
            "Recommendation ITU-R TF.460-6 [1] within the accuracy defined in the policy."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.7.1-06",
        "testo": (
            "Se l'accuratezza e' definita nella marca temporale, il tempo incluso nella marca temporale deve "
            "essere sincronizzato con questa accuratezza."
        ),
        "testo_integrale": (
            "TIS-7.7.1-06 [CONDITIONAL]: if the accuracy is defined in the time-stamp, the time included in the "
            "time-stamp shall be synchronized with this accuracy."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "se l'accuratezza e' definita nella marca temporale",
    },
    {
        "riferimento": "TIS-7.7.1-07",
        "testo": (
            "Se l'orologio del fornitore di marche temporali e' rilevato (vedi TIS-7.7.2-04) come fuori "
            "dall'accuratezza dichiarata (vedi TIS-7.7.1-05 e TIS-7.7.1-06), le marche temporali non devono "
            "essere emesse."
        ),
        "testo_integrale": (
            "TIS-7.7.1-07 [CONDITIONAL]: If the time-stamp provider's clock is detected (see TIS-7.7.2-04) as "
            "being out of the stated accuracy (see TIS-7.7.1-05 and TIS-7.7.1-06) then time-stamps shall not be "
            "issued."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "se l'orologio del fornitore di marche temporali e' rilevato (vedi TIS-7.7.2-04) come fuori "
            "dall'accuratezza dichiarata (vedi TIS-7.7.1-05 e TIS-7.7.1-06)"
        ),
    },
    {
        "riferimento": "TIS-7.7.1-08",
        "testo": (
            "La marca temporale deve essere firmata usando una chiave generata esclusivamente per questo scopo."
        ),
        "testo_integrale": (
            "TIS-7.7.1-08: The time-stamp shall be signed using a key generated exclusively for this purpose. "
            "NOTE 2: See clause 7.6.2."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.7.1-09",
        "testo": (
            "Il sistema di generazione delle marche temporali deve rifiutare qualunque tentativo di emettere "
            "marche temporali quando la data di scadenza della chiave privata della TSU e' stata raggiunta."
        ),
        "testo_integrale": (
            "TIS-7.7.1-09: The time-stamp generation system shall reject any attempt to issue time-stamps when "
            "the expiration date of the TSU private key has been reached."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- 7.7.2 Clock synchronization with UTC --------------------------
    {
        "riferimento": "TIS-7.7.2-01",
        "testo": (
            "L'orologio della TSU deve essere sincronizzato con UTC come definito nella Raccomandazione ITU-R "
            "TF.460-6, entro l'accuratezza dichiarata, con almeno i seguenti requisiti particolari."
        ),
        "testo_integrale": (
            "TIS-7.7.2-01: The TSU clock shall be synchronized with UTC as defined in Recommendation ITU-R "
            "TF.460-6 [1] within the declared accuracy with at least the following particular requirements:"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.7.2-02",
        "testo": (
            "La calibrazione degli orologi della TSU deve essere mantenuta in modo che gli orologi non si "
            "discostino oltre l'accuratezza dichiarata."
        ),
        "testo_integrale": (
            "TIS-7.7.2-02: The calibration of the TSU clocks shall be maintained such that the clocks do not "
            "drift outside the declared accuracy."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.7.2-03",
        "testo": "L'accuratezza dichiarata deve essere di 1 secondo o migliore.",
        "testo_integrale": "TIS-7.7.2-03: The declared accuracy shall be of 1 second or better.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.7.2-04",
        "testo": (
            "Gli orologi della TSU devono essere protetti contro minacce che potrebbero causare una modifica non "
            "rilevata dell'orologio tale da portarlo fuori dalla sua calibrazione."
        ),
        "testo_integrale": (
            "TIS-7.7.2-04: The TSU clocks shall be protected against threats which could result in an undetected "
            "change to the clock that takes it outside its calibration. NOTE 1: Threats can include tampering by "
            "unauthorized personnel, radio or electrical shocks."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.7.2-05",
        "testo": (
            "Il TSA deve rilevare se il tempo che sarebbe indicato in una marca temporale si discosta o salta "
            "fuori sincronizzazione con UTC."
        ),
        "testo_integrale": (
            "TIS-7.7.2-05: The TSA shall detect if the time that would be indicated in a time-stamp drifts or "
            "jumps out of synchronization with UTC. NOTE 2: See clause 7.12 for notification requirements of "
            "such events to relying parties."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.7.2-06",
        "testo": (
            "Se e' rilevato che il tempo che sarebbe indicato in una marca temporale si discosta o salta fuori "
            "sincronizzazione con UTC, la TSU deve interrompere l'emissione di marche temporali."
        ),
        "testo_integrale": (
            "TIS-7.7.2-06 [CONDITIONAL]: If it is detected that the time that would be indicated in a time-stamp "
            "drifts or jumps out of synchronization with UTC, the TSU shall stop time-stamp issuance."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "se e' rilevato che il tempo che sarebbe indicato in una marca temporale si discosta o salta fuori "
            "sincronizzazione con UTC"
        ),
    },
    {
        "riferimento": "TIS-7.7.2-07",
        "testo": (
            "La sincronizzazione dell'orologio deve essere mantenuta quando si verifica un secondo intercalare "
            "come notificato dall'organismo competente."
        ),
        "testo_integrale": (
            "TIS-7.7.2-07: The clock synchronization shall be maintained when a leap second occurs as notified "
            "by the appropriate body."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.7.2-08",
        "testo": (
            "La modifica per tenere conto del secondo intercalare deve avvenire durante l'ultimo minuto del "
            "giorno in cui il secondo intercalare e' previsto."
        ),
        "testo_integrale": (
            "TIS-7.7.2-08: The change to take account of the leap second shall occur during the last minute of "
            "the day when the leap second is scheduled to occur."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.7.2-09",
        "testo": (
            "Deve essere mantenuto un record del momento esatto (entro l'accuratezza dichiarata) in cui si e' "
            "verificata la modifica di cui a TIS-7.7.2-08. Si veda l'allegato C per maggiori dettagli."
        ),
        "testo_integrale": (
            "TIS-7.7.2-09: A record shall be maintained of the exact time (within the declared accuracy) when "
            "the change referred to in TIS-7.7.2-08 occurred. See annex C for more details. NOTE 3: Regarding "
            "leap second, first preference is given to the end of December and June, and second preference is "
            "given to the end of March and September."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- 7.8 Physical and environmental security -----------------------
    {
        "riferimento": "OVR-7.8-01",
        "testo": (
            "Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.6 (sicurezza fisica e "
            "ambientale). In aggiunta si applicano i seguenti requisiti particolari."
        ),
        "testo_integrale": (
            "OVR-7.8-01: The requirements identified in ETSI EN 319 401 [4], clause 7.6 shall apply. In "
            "addition, the following particular requirements apply:"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.8-02",
        "testo": (
            "Devono essere applicati controlli di accesso al dispositivo crittografico sicuro per soddisfare i "
            "requisiti di sicurezza dei dispositivi crittografici sicuri identificati nella clausola 7.6. Alla "
            "gestione della marcatura temporale si applicano i seguenti controlli aggiuntivi."
        ),
        "testo_integrale": (
            "OVR-7.8-02: Access controls shall be applied to the secure cryptographic device to meet the "
            "requirements of security of security cryptographic devices as identified in clause 7.6. The "
            "following additional controls apply to time-stamping management:"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.8-03",
        "testo": (
            "Le strutture di gestione della marcatura temporale devono essere operate in un ambiente che "
            "protegga fisicamente e logicamente i servizi da compromissioni tramite accesso non autorizzato a "
            "sistemi o dati."
        ),
        "testo_integrale": (
            "OVR-7.8-03: The time-stamping management facilities shall be operated in an environment which "
            "physically and logically protects the services from compromise through unauthorized access to "
            "systems or data."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.8-04",
        "testo": "Ogni ingresso all'area fisicamente sicura deve essere soggetto a supervisione indipendente.",
        "testo_integrale": (
            "OVR-7.8-04: Every entry to the physically secure area shall be subject to independent oversight."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.8-05",
        "testo": (
            "Le persone non autorizzate devono essere accompagnate da una persona autorizzata mentre si trovano "
            "nell'area sicura."
        ),
        "testo_integrale": (
            "OVR-7.8-05: Non-authorized person shall be accompanied by an authorized person whilst in the "
            "secure area."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.8-06",
        "testo": "Ogni ingresso e uscita da e verso l'area fisicamente sicura deve essere registrato.",
        "testo_integrale": (
            "OVR-7.8-06: Every entry and exit to/from the physically secure area shall be logged."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.8-07",
        "testo": (
            "La protezione fisica deve essere realizzata attraverso la creazione di perimetri di sicurezza "
            "chiaramente definiti (cioe' barriere fisiche) attorno alla gestione della marcatura temporale."
        ),
        "testo_integrale": (
            "OVR-7.8-07: Physical protection shall be achieved through the creation of clearly defined security "
            "perimeters (i.e. physical barriers) around the time-stamping management."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.8-08",
        "testo": (
            "Qualunque parte dei locali condivisa con altre organizzazioni deve restare fuori da questo "
            "perimetro."
        ),
        "testo_integrale": (
            "OVR-7.8-08: Any parts of the premises shared with other organizations shall be outside this "
            "perimeter."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.8-09",
        "testo": (
            "I controlli di sicurezza fisica e ambientale devono proteggere la struttura che ospita le risorse "
            "di sistema, le risorse di sistema stesse e le strutture usate per supportarne l'operativita'."
        ),
        "testo_integrale": (
            "OVR-7.8-09: Physical and environmental security controls shall protect the facility that houses "
            "system resources, the system resources themselves, and the facilities used to support their "
            "operation."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.8-10",
        "testo": (
            "La politica di sicurezza fisica e ambientale del TSA per i sistemi concernenti la gestione della "
            "marcatura temporale deve affrontare come minimo: il controllo degli accessi fisici, la protezione "
            "da disastri naturali, i fattori di sicurezza antincendio, il guasto dei servizi di supporto (es. "
            "energia, telecomunicazioni), il crollo strutturale, le perdite degli impianti idrici, la protezione "
            "contro furti, effrazioni e intrusioni, e il ripristino dopo disastri."
        ),
        "testo_integrale": (
            "OVR-7.8-10: The TSA's physical and environmental security policy for systems concerned with "
            "time-stamping management shall address as a minimum the physical access control, natural disaster "
            "protection, fire safety factors, failure of supporting utilities (e.g. power, telecommunications), "
            "structure collapse, plumbing leaks, protection against theft, breaking and entering, and disaster "
            "recovery."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.8-11",
        "testo": (
            "I controlli devono proteggere dal trasferimento fuori sede non autorizzato di apparecchiature, "
            "informazioni, supporti e software relativi ai servizi di marcatura temporale."
        ),
        "testo_integrale": (
            "OVR-7.8-11: Controls shall protect against equipment, information, media and software relating to "
            "the time-stamping services being taken off-site without authorization."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.8-12",
        "testo": (
            "Altre funzioni possono essere supportate all'interno della stessa area sicura purche' l'accesso sia "
            "limitato a personale autorizzato."
        ),
        "testo_integrale": (
            "OVR-7.8-12: Other functions may be supported within the same secured area provided that the access "
            "is limited to authorized personnel."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- 7.9 Operation security ---------------------------------------
    {
        "riferimento": "OVR-7.9-01",
        "testo": (
            "Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.7 (sicurezza operativa). In "
            "aggiunta si applicano i seguenti requisiti particolari, relativi alla pianificazione dei sistemi."
        ),
        "testo_integrale": (
            "OVR-7.9-01: The requirements identified in ETSI EN 319 401 [4], clause 7.7 shall apply. In "
            "addition, the following particular requirements apply:"
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.9-02",
        "testo": (
            "Le richieste di capacita' devono essere monitorate e devono essere fatte proiezioni dei futuri "
            "fabbisogni di capacita', per garantire che siano disponibili potenza di elaborazione e capacita' di "
            "memorizzazione adeguate."
        ),
        "testo_integrale": (
            "OVR-7.9-02: Capacity demands shall be monitored and projections of future capacity requirements "
            "made to ensure that adequate processing power and storage are available."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- 7.10 Network security ----------------------------------------
    {
        "riferimento": "OVR-7.10-01",
        "testo": (
            "Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.8 (sicurezza di rete). In "
            "aggiunta si applicano i seguenti requisiti particolari."
        ),
        "testo_integrale": (
            "OVR-7.10-01: The requirements identified in ETSI EN 319 401 [4], clause 7.8 shall apply. In "
            "addition, the following particular requirements apply:"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.10-02",
        "testo": "Il TSA deve mantenere e proteggere tutti i sistemi della TSU in una zona sicura.",
        "testo_integrale": "OVR-7.10-02: The TSA shall maintain and protect all TSU systems in a secure zone.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.10-03",
        "testo": (
            "Il TSA deve configurare tutti i sistemi della TSU rimuovendo o disabilitando tutti gli account, le "
            "applicazioni, i servizi, i protocolli e le porte che non sono usati nelle operazioni del TSA."
        ),
        "testo_integrale": (
            "OVR-7.10-03: The TSA shall configure all TSU systems by removing or disabling all accounts, "
            "applications, services, protocols, and ports that are not used in the TSA's operations."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.10-04",
        "testo": "Solo i ruoli fidati devono accedere alle zone sicure e alle zone ad alta sicurezza.",
        "testo_integrale": (
            "OVR-7.10-04: Only trusted roles shall access secure zones and high security zones."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- 7.11 Incident management -------------------------------------
    {
        "riferimento": "OVR-7.11-01",
        "testo": (
            "Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.9 (gestione degli incidenti)."
        ),
        "testo_integrale": (
            "OVR-7.11-01: The requirements identified in ETSI EN 319 401 [4], clause 7.9 shall apply."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- 7.12 Collection of evidence ----------------------------------
    {
        "riferimento": "OVR-7.12-01",
        "testo": (
            "Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.10 (raccolta delle prove). In "
            "aggiunta si applicano i seguenti requisiti particolari, relativi alla gestione delle chiavi della "
            "TSU e alla sincronizzazione dell'orologio."
        ),
        "testo_integrale": (
            "OVR-7.12-01: The requirements identified in ETSI EN 319 401 [4], clause 7.10 shall apply. In "
            "addition, the following particular requirements apply:"
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.12-02",
        "testo": (
            "Devono essere registrati i record concernenti tutti gli eventi relativi al ciclo di vita delle "
            "chiavi della TSU."
        ),
        "testo_integrale": (
            "OVR-7.12-02: Records concerning all events relating to the life-cycle of TSU keys shall be logged."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.12-03",
        "testo": (
            "Devono essere registrati i record concernenti tutti gli eventi relativi al ciclo di vita dei "
            "certificati della TSU (se appropriato)."
        ),
        "testo_integrale": (
            "OVR-7.12-03: Records concerning all events relating to the life-cycle of TSU certificates (if "
            "appropriate) shall be logged."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.12-04",
        "testo": (
            "Devono essere registrati i record concernenti tutti gli eventi relativi alla sincronizzazione "
            "dell'orologio di una TSU con UTC."
        ),
        "testo_integrale": (
            "OVR-7.12-04: Records concerning all events relating to synchronization of a TSU's clock to UTC "
            "shall be logged."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.12-05",
        "testo": (
            "I record devono includere informazioni concernenti la normale ricalibrazione o sincronizzazione "
            "degli orologi usati nella marcatura temporale."
        ),
        "testo_integrale": (
            "OVR-7.12-05: Records shall include information concerning normal re-calibration or synchronization "
            "of clocks used in time-stamping."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.12-06",
        "testo": (
            "Devono essere registrati i record concernenti tutti gli eventi relativi al rilevamento della "
            "perdita di sincronizzazione."
        ),
        "testo_integrale": (
            "OVR-7.12-06: Records concerning all events relating to detection of loss of synchronization shall "
            "be logged."
        ),
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- 7.13 Business continuity management ---------------------------
    {
        "riferimento": "OVR-7.13-01",
        "testo": (
            "Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.11 (gestione della continuita' "
            "operativa). In aggiunta si applicano i seguenti requisiti particolari."
        ),
        "testo_integrale": (
            "OVR-7.13-01: The requirements identified in ETSI EN 319 401 [4], clause 7.11 shall apply. In "
            "addition, the following particular requirements apply:"
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.13-02",
        "testo": (
            "Il piano di ripristino dopo disastri del TSA deve affrontare la compromissione o la sospetta "
            "compromissione delle chiavi private della TSU o la perdita di calibrazione di un orologio della "
            "TSU, che possono aver interessato marche temporali gia' emesse."
        ),
        "testo_integrale": (
            "OVR-7.13-02: The TSA's disaster recovery plan shall address the compromise or suspected compromise "
            "of TSU's private keys or loss of calibration of a TSU clock, which may have affected time-stamps "
            "which have been issued."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.13-03",
        "testo": (
            "In caso di compromissione, o sospetta compromissione o perdita di calibrazione nell'emissione di "
            "marche temporali, il TSA deve mettere a disposizione di tutti gli abbonati e delle parti affidanti "
            "una descrizione della compromissione verificatasi."
        ),
        "testo_integrale": (
            "OVR-7.13-03 [CONDITIONAL]: In the case of a compromise, or suspected compromise or loss of "
            "calibration when issuing time-stamp the TSA shall make available to all subscribers and relying "
            "parties a description of compromise that occurred."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "in caso di compromissione, sospetta compromissione o perdita di calibrazione nell'emissione di "
            "marche temporali"
        ),
    },
    {
        "riferimento": "OVR-7.13-04",
        "testo": (
            "In caso di compromissione dell'operativita' di una TSU (es. compromissione della chiave della TSU), "
            "sospetta compromissione o perdita di calibrazione, la TSU non deve emettere marche temporali finche' "
            "non siano state adottate le misure per riprendersi dalla compromissione."
        ),
        "testo_integrale": (
            "OVR-7.13-04 [CONDITIONAL]: In the case of compromise to a TSU's operation (e.g. TSU key compromise), "
            "suspected compromise or loss of calibration the TSU shall not issue time-stamps until steps are "
            "taken to recover from the compromise."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "in caso di compromissione dell'operativita' di una TSU (es. compromissione della chiave della TSU), "
            "sospetta compromissione o perdita di calibrazione"
        ),
    },
    {
        "riferimento": "OVR-7.13-05",
        "testo": (
            "In caso di compromissione grave dell'operativita' del TSA o di perdita di calibrazione, il TSA deve "
            "mettere a disposizione di tutti gli abbonati e delle parti affidanti le informazioni utilizzabili "
            "per identificare le marche temporali che possono essere state interessate, salvo che cio' violi la "
            "privacy degli utenti del TSA o la sicurezza dei servizi del TSA."
        ),
        "testo_integrale": (
            "OVR-7.13-05 [CONDITIONAL]: In case of major compromise of the TSA's operation or loss of "
            "calibration, the TSA shall make available to all subscribers and relying parties information which "
            "can be used to identify the time-stamps which may have been affected, unless this breaches the "
            "privacy of the TSAs users or the security of the TSA services. NOTE: In case the private key does "
            "become compromised, an audit trail of all time-stamps generated by the TSU can provide a means to "
            "discriminate between genuine and false backdated time-stamps. Two time-stamps from two different "
            "TSUs can be another way to address this issue."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "in caso di compromissione grave dell'operativita' del TSA o di perdita di calibrazione"
        ),
    },
    # --- 7.14 TSA termination and termination plans --------------------
    {
        "riferimento": "OVR-7.14-01",
        "testo": (
            "Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.12 (cessazione del TSA e piani "
            "di cessazione). In aggiunta si applicano i seguenti requisiti particolari."
        ),
        "testo_integrale": (
            "OVR-7.14-01: The requirements identified in ETSI EN 319 401 [4], clause 7.12 shall apply. In "
            "addition, the following particular requirements apply:"
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.14-02",
        "testo": (
            "Quando il TSA cessa i propri servizi, il TSA deve revocare tutti i certificati non scaduti della "
            "TSU."
        ),
        "testo_integrale": (
            "OVR-7.14-02 [CONDITIONAL]: When the TSA terminates its services, the TSA shall revoke all "
            "non-expired TSU's certificates."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "alla cessazione dei servizi del TSA",
    },
    {
        "riferimento": "OVR-7.14-03",
        "testo": (
            "Quando il TSA cessa i propri servizi, le chiavi private della TSU, o qualunque parte di chiave, "
            "incluse le copie, devono essere distrutte in modo che le chiavi private non possano essere "
            "recuperate."
        ),
        "testo_integrale": (
            "OVR-7.14-03 [CONDITIONAL]: When the TSA terminates its services, the TSU private keys, or any key "
            "part, including any copies, shall be destroyed such that the private keys cannot be retrieved."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "alla cessazione dei servizi del TSA",
    },
    {
        "riferimento": "OVR-7.14-04",
        "testo": (
            "Quando il TSA cessa i propri servizi, alla TSU cessata non devono essere assegnate o generate nuove "
            "coppie di chiavi privata e pubblica e la TSU non deve emettere nuovi token di marca temporale."
        ),
        "testo_integrale": (
            "OVR-7.14-04 [CONDITIONAL]: When the TSA terminates its services, the terminated TSU shall not be "
            "allocated or generated new private and public key pair and shall not issue any new time-stamp "
            "tokens."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "alla cessazione dei servizi del TSA",
    },
    # --- 7.15 Compliance ----------------------------------------------
    {
        "riferimento": "OVR-7.15-01",
        "testo": "Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.13 (conformita').",
        "testo_integrale": (
            "OVR-7.15-01: The requirements identified in ETSI EN 319 401 [4], clause 7.13 shall apply."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    # --- 7.16 Supply chain --------------------------------------------
    {
        "riferimento": "OVR-7.16-01",
        "testo": (
            "Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.14 (catena di fornitura)."
        ),
        "testo_integrale": (
            "OVR-7.16-01: The requirements identified in ETSI EN 319 401 [4], clause 7.14 shall apply."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = []

INDICE_ARTICOLI_LOCALE: list[str] = [
    "TIS-7.7.1-01",
    "TIS-7.7.1-02",
    "TIS-7.7.1-03",
    "TIS-7.7.1-04",
    "TIS-7.7.1-05",
    "TIS-7.7.1-06",
    "TIS-7.7.1-07",
    "TIS-7.7.1-08",
    "TIS-7.7.1-09",
    "TIS-7.7.2-01",
    "TIS-7.7.2-02",
    "TIS-7.7.2-03",
    "TIS-7.7.2-04",
    "TIS-7.7.2-05",
    "TIS-7.7.2-06",
    "TIS-7.7.2-07",
    "TIS-7.7.2-08",
    "TIS-7.7.2-09",
    "OVR-7.8-01",
    "OVR-7.8-02",
    "OVR-7.8-03",
    "OVR-7.8-04",
    "OVR-7.8-05",
    "OVR-7.8-06",
    "OVR-7.8-07",
    "OVR-7.8-08",
    "OVR-7.8-09",
    "OVR-7.8-10",
    "OVR-7.8-11",
    "OVR-7.8-12",
    "OVR-7.9-01",
    "OVR-7.9-02",
    "OVR-7.10-01",
    "OVR-7.10-02",
    "OVR-7.10-03",
    "OVR-7.10-04",
    "OVR-7.11-01",
    "OVR-7.12-01",
    "OVR-7.12-02",
    "OVR-7.12-03",
    "OVR-7.12-04",
    "OVR-7.12-05",
    "OVR-7.12-06",
    "OVR-7.13-01",
    "OVR-7.13-02",
    "OVR-7.13-03",
    "OVR-7.13-04",
    "OVR-7.13-05",
    "OVR-7.14-01",
    "OVR-7.14-02",
    "OVR-7.14-03",
    "OVR-7.14-04",
    "OVR-7.15-01",
    "OVR-7.16-01",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "TIS-7.7.1-07"),
        "nodo_a": ("obbligo", None, "TIS-7.7.2-04"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", None, "TIS-7.7.1-07"),
        "nodo_a": ("obbligo", None, "TIS-7.7.1-05"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", None, "TIS-7.7.1-07"),
        "nodo_a": ("obbligo", None, "TIS-7.7.1-06"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", None, "TIS-7.7.2-09"),
        "nodo_a": ("obbligo", None, "TIS-7.7.2-08"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
]


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
