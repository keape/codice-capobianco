"""ETSI EN 319 421 V1.3.1 (2025-07) - Electronic Signatures and Trust
Infrastructures (ESI); Policy and Security Requirements for Trust Service
Providers issuing Time-Stamps. Fonte 18 (numerazione definitiva cablata
dalla sessione principale in app/seed.py - questo modulo NON tocca
seed.py). Capitolo 5: clausola 8 (Additional requirements for qualified
electronic time-stamps as per Regulation (EU) No 910/2014), sottoclausole
8.1 (TSU public key certificate) e 8.2 (TSA issuing non-qualified and
qualified electronic time-stamps as per Regulation (EU) No 910/2014).
Testo ufficiale in app/.source_cache/etsi_319_421/cap05.txt. Manifest di
split: app/.source_cache/etsi_319_421/manifest.json.

Modellazione (ADR-0007), stesso criterio già applicato alle altre fonti
ETSI (TS 119 461, EN 319 401, EN 319 411-1/-2, EN 319 412, TS 119 431-1/-2):

- Il perimetro e' composto ESCLUSIVAMENTE da requisiti numerati: nessun
  Principio. La clausola 8 non contiene testo normativo autonomo oltre i
  requisiti (nessuna definizione, nessuna disposizione di scopo/ambito
  propria: l'ambito e' gia' coperto dalla clausola 1, capitolo 1). Le due
  intestazioni di sottoclausola (`#### 8.1 TSU public key certificate`,
  `#### 8.2 TSA issuing non-qualified and qualified electronic
  time-stamps as per Regulation (EU) No 910/2014`) sono pure etichette di
  raggruppamento dei requisiti che seguono, senza contenuto normativo
  proprio: NON generano un item di indice, coerentemente con il
  trattamento riservato alle intestazioni di sottoclausola prive di
  requisito in ETSI EN 319 411-1/-2 e TS 119 431.
- La formula di raccordo "The following requirements apply:" in testa alla
  clausola 8.1 e' un mero connettivo redazionale privo di contenuto
  prescrittivo: nessun nodo, nessun item di indice (non e' una clausola
  discorsiva nel senso di ADR-0007, e' un'introduzione all'elenco).
- Un Obbligo per ciascuno dei 5 requisiti numerati:
  - 8.1 -> TIS-8.1-01, TIS-8.1-02 (emissione del certificato della chiave
    pubblica di verifica della firma della TSU in conformita' a una
    certificate policy: NCP+ di ETSI EN 319 411-1 e, rispettivamente,
    policy appropriata di ETSI EN 319 411-2);
  - 8.2 -> TIS-8.2-01, TIS-8.2-02, TIS-8.2-03 (separazione tra marche
    temporali qualificate e non qualificate: divieto di emissione mista da
    parte della stessa TSU, TSU distinte identificate da subject name
    distinti nel certificato, TSU distinte accessibili via service access
    point separati).
- Tutti e cinque i requisiti portano la marcatura testuale [CONDITIONAL]:
  la marcatura e' mantenuta in `testo_integrale` (parte del testo
  ufficiale), sintetizzata in `condizione_applicabilita` e omessa dal solo
  `riferimento` (nessun suffisso aggiunto all'id), secondo la convenzione
  gia' adottata in ETSI EN 319 411-1/-2. Le condizioni sono di due tipi:
  requisiti 8.1-01/8.1-02 e 8.2-01 subordinati alla DICHIARAZIONE della
  marca temporale come qualificata da parte del TSA (requisito
  "dichiarativo": si applica solo a fronte di una pretesa di
  qualificazione ai sensi del Regolamento (UE) n. 910/2014); requisiti
  8.2-02/8.2-03 subordinati alla coesistenza, nella stessa TSA, di
  emissione qualificata e non qualificata.
- TIS-8.1-02 e' formulato con "should" (raccomandazione, non obbligo
  cogente) e TIS-8.2-01/02/03 con "shall": tutti sono modellati come
  Obbligo perche' lo schema ha un solo tipo prescrittivo (precedente
  identico per tutti i REQ e gli OVR di ETSI EN 319 401 e EN 319 411-1/-2,
  che includono requisiti "should"/"may" e marcature [CONDITIONAL]/[CHOICE]
  come Obblighi). La differenza di cogenza resta visibile in
  `testo_integrale` ("should not"/"should"), dove e' testo ufficiale, e non
  viene tradotta in un campo strutturato inesistente.
- `tipo_obbligo`:
  - TIS-8.1-01, TIS-8.1-02: "tecnico/sicurezza" (conformita' tecnica del
    certificato della chiave pubblica della TSU a un profilo/certificate
    policy specificato: requisito sul contenuto e sul profilo del
    certificato emesso).
  - TIS-8.2-01: "organizzativo" (delimitazione dell'offerta di servizio
    della TSU: se emette marche temporali dichiarate qualificate, non puo'
    emetterne di non qualificate - regola sull'assetto del servizio, non
    controllo tecnico puntuale).
  - TIS-8.2-02, TIS-8.2-03: "tecnico/sicurezza" (separazione tecnica di
    identita' crittografiche - TSU distinte con certificati/subject name
    distinti - e di punti di accesso al servizio).
- Soggetto obbligato: in tutti e cinque i casi il TSA/TSU, quindi
  categoria "QTSP/gestore" con ruolo "obbligato". `oggetti_giuridici` non
  pertinente (righe tutte di tipo Obbligo).
- NOTE. In 8.1 la NOTE 1 (ETSI EN 319 411-2 incorpora i requisiti di ETSI
  EN 319 411-1) e la NOTE 2 (uso di una trusted list conforme alla CID (EU)
  2015/1505 e di ETSI TS 119 615 per stabilire la qualificazione della
  marca temporale; il qcStatement "esi4-qtstStatement-1" di ETSI EN 319 422
  e' solo un'indizio della pretesa di qualificazione) sono interpretative:
  precisano l'effetto dei requisiti e avvertono esplicitamente che il
  qcStatement non e' prova della qualificazione. Sono mantenute per intero
  in `testo_integrale` di TIS-8.1-02, requisito che immediatamente le
  precede. In 8.2 la NOTE 1 (TSU distinte non implicano hardware/software
  distinti, solo certificati distinti e service access point separati) e la
  NOTE 2 (rinvio a ETSI TS 119 612, clausola 5.5.3 nota 5, sull'uso di una
  chiave pubblica di Root CA come "Service digital identifiers" nella
  trusted list) sono parimenti interpretative e sono mantenute per intero in
  `testo_integrale` di TIS-8.2-03. Nessuna NOTE di questo capitolo e' stata
  scartata come puramente bibliografica.
- Il testo ufficiale della NOTE 2 di 8.2 contiene la locuzione "regarding
  use a Root CA public key" (senza "of"/"the"): e' un refuso dell'edizione
  ufficiale, riportato verbatim in `testo_integrale` senza correzioni
  (ADR-0010 impone la copia letterale, non una sua normalizzazione).
- Paratesto escluso: i marcatori di impaginazione `***ETSI***` e
  `<!-- Page 22 -->` / `<!-- Page 23 -->` sono artefatti della conversione
  PDF->markdown, non testo normativo. Le intestazioni `## 8 ...` e
  `#### 8.1 ...` / `#### 8.2 ...` sono trattate come sopra (etichette di
  raggruppamento, nessun nodo).

RELAZIONI interne: nessuna. Nel perimetro di questo capitolo nessun testo di
requisito cita letteralmente l'id di un altro requisito (le NOTE rinviano a
clausole di standard esterni - ETSI EN 319 411-1/411-2, ETSI TS 119 615,
ETSI EN 319 422 clausola 9.1, ETSI TS 119 612 clausola 5.5.3 nota 5 - non a
requirement id interni): la relazione "richiama" sarebbe arbitraria.

NIENTE relazioni verso altre Fonti in questa fase, per esplicita consegna.
Anche dove il testo cita ETSI EN 319 411-1 (Fonte 17), ETSI EN 319 411-2,
il Regolamento (UE) n. 910/2014 (eIDAS) o ETSI EN 319 422, il collegamento
cross-fonte NON e' autorato qui: e' demandato alla Fase 6 (ADR-0009), la
pipeline a tre stadi (candidati a zero token LLM, classificazione LLM sullo
shortlist, validazione e inserimento come capitolo virtuale) eseguita dalla
sessione principale a valle dell'import di tutti i capitoli. In questa fase
`fonte_id_o_None` non compare quindi mai valorizzato con un intero
riferimento a un'altra fonte, e la lista `RELAZIONI` resta vuota.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "TIS-8.1-01",
        "testo": (
            "Se una marca temporale e' dichiarata dal TSA come marca temporale elettronica qualificata ai "
            "sensi del Regolamento (UE) n. 910/2014, il certificato della chiave pubblica di verifica della "
            "firma della TSU deve essere emesso in conformita' alla certificate policy NCP+ specificata "
            "nella ETSI EN 319 411-1."
        ),
        "testo_integrale": (
            "TIS-8.1-01 [CONDITIONAL]: If a time-stamp is declared by the TSA to be a qualified electronic "
            "time-stamp as per Regulation (EU) No 910/2014 [i.4], the TSU signature verification (public) "
            "key certificate shall be issued in compliance with the NCP+ certificate policy as specified in "
            "ETSI EN 319 411-1 [8]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Si applica se la marca temporale e' dichiarata dal TSA come marca temporale elettronica "
            "qualificata ai sensi del Regolamento (UE) n. 910/2014."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-8.1-02",
        "testo": (
            "Se una marca temporale e' dichiarata dal TSA come marca temporale elettronica qualificata ai "
            "sensi del Regolamento (UE) n. 910/2014, il certificato della chiave pubblica di verifica della "
            "firma della TSU dovrebbe essere emesso in conformita' a una certificate policy appropriata "
            "specificata nella ETSI EN 319 411-2."
        ),
        "testo_integrale": (
            "TIS-8.1-02 [CONDITIONAL]: If a time-stamp is declared by the TSA to be a qualified electronic "
            "time-stamp as per Regulation (EU) No 910/2014 [i.4], the TSU signature verification (public) "
            "key certificate should be issued in compliance with an appropriate certificate policy as "
            "specified in ETSI EN 319 411-2 [i.11]. "
            "NOTE 1: ETSI EN 319 411-2 [i.11] incorporates requirements from ETSI EN 319 411-1 [8]. "
            "NOTE 2: The relying party is expected to use a trusted list compliant with CID (EU) 2015/1505 "
            "and to use ETSI TS 119 615 [i.19] to establish whether the time-stamp is qualified in "
            "accordance with Regulation (EU) 910/2014. The qcStatement \"esi4-qtstStatement-1\" as defined "
            "in ETSI EN 319 422 [5], clause 9.1 can only be an indication that the time-stamp is claimed to "
            "be a qualified electronic time-stamp."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Si applica se la marca temporale e' dichiarata dal TSA come marca temporale elettronica "
            "qualificata ai sensi del Regolamento (UE) n. 910/2014."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-8.2-01",
        "testo": (
            "Se una TSU emette marche temporali dichiarate come marche temporali elettroniche qualificate ai "
            "sensi del Regolamento (UE) n. 910/2014, la medesima TSU non deve emettere marche temporali "
            "elettroniche non qualificate."
        ),
        "testo_integrale": (
            "TIS-8.2-01 [CONDITIONAL]: If a TSU issues time-stamps that are claimed to be qualified "
            "electronic time-stamps as per Regulation (EU) No 910/2014 [i.4], this TSU shall not issue "
            "non-qualified electronic time-stamps."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Si applica se la TSU emette marche temporali dichiarate come marche temporali elettroniche "
            "qualificate ai sensi del Regolamento (UE) n. 910/2014."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-8.2-02",
        "testo": (
            "Nel caso di una TSA che emette sia marche temporali qualificate sia marche temporali non "
            "qualificate, essa deve utilizzare TSU distinte, identificate da nomi di soggetto diversi nei "
            "rispettivi certificati di chiave pubblica."
        ),
        "testo_integrale": (
            "TIS-8.2-02 [CONDITIONAL]: In the case of a TSA issuing both qualified and non-qualified "
            "time-stamps it shall use different TSUs identified by different subject names in their public "
            "key certificate."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Si applica nel caso di una TSA che emette sia marche temporali qualificate sia marche "
            "temporali non qualificate."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-8.2-03",
        "testo": (
            "Nel caso di una TSA che emette sia marche temporali qualificate sia marche temporali non "
            "qualificate, essa deve utilizzare TSU distinte, accessibili tramite service access point "
            "separati."
        ),
        "testo_integrale": (
            "TIS-8.2-03 [CONDITIONAL]: In the case of a TSA issuing both qualified and non-qualified "
            "time-stamps it shall use different TSUs accessible via separate service access points. "
            "NOTE 1: Having different TSUs does not imply different hardware/software, only different "
            "public key certificates and separate service access points. "
            "NOTE 2: Attention is drawn to ETSI TS 119 612 [i.17], clause 5.5.3 note 5, regarding use a "
            "Root CA public key as \"Service digital identifiers\" value in the trusted list."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "Si applica nel caso di una TSA che emette sia marche temporali qualificate sia marche "
            "temporali non qualificate."
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = []

INDICE_ARTICOLI_LOCALE = [
    "TIS-8.1-01",
    "TIS-8.1-02",
    "TIS-8.2-01",
    "TIS-8.2-02",
    "TIS-8.2-03",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Nessuna relazione interna: nel perimetro della clausola 8 nessun requisito
# cita letteralmente l'id di un altro requisito (i rinvii testuali sono a
# clausole di standard esterni). Nessuna relazione cross-fonte: la Fase 6
# (ADR-0009) e' della sessione principale - vedi docstring di modulo.
RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_copertura
    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, {len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
