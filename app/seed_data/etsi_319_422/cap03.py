"""ETSI EN 319 422 V1.1.1 (2016-03) - Electronic Signatures and Trust
Infrastructures (ESI); Time-stamping protocol and time-stamp token profiles.
Fonte 19 (la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 3:
clausola 6 (TSU certificate profile: 6.1 General requirements, 6.2 Subject
name requirements, 6.3 Key lengths requirements, 6.4 Key usage requirements,
6.5 Algorithm requirements), clausola 7 (Profiles for the transport protocols
to be supported), clausola 8 (Object identifiers of the cryptographic
algorithms). Testo ufficiale in app/.source_cache/etsi_319_422/cap03.txt
(letto sempre con selettore `:raw`, altrimenti il tool tronca le righe lunghe
a 768 caratteri introducendo "…" e mutilando la copia verbatim). Manifest di
split: app/.source_cache/etsi_319_422/manifest.json.

Modellazione (ADR-0007), stesso criterio gia' applicato agli standard ETSI
gia' censiti (ETSI EN 319 421, ETSI EN 319 412, ETSI EN 319 401, ETSI TS
119 461) e adattato alle clausole/sottoclausole di uno standard tecnico: un
nodo per ogni clausola numerata che porta contenuto normativo proprio. Questo
capitolo contiene 6 Obblighi e 1 Principio. Scelte voce per voce:

- Clausola 6 (TSU certificate profile) -> NESSUN nodo, NESSUN item di indice:
  intestazione di puro raggruppamento delle sottoclausole 6.1-6.5, senza testo
  proprio (nel sorgente il titolo e' seguito direttamente dal titolo della
  clausola 6.1). Stesso trattamento riservato alle clausole di
  raggruppamento dei moduli ETSI gia' censiti.
- Clausola 6.1 (General requirements) -> 1 Obbligo "tecnico/sicurezza". Il
  "shall" impone che il certificato della TSU (Time-Stamping Unit) rispetti i
  requisiti di profilo di ETSI EN 319 412-2 quando la TSA e' una persona
  fisica, o di ETSI EN 319 412-3 quando la TSA e' una persona giuridica, con
  le modifiche introdotte dalle clausole 6.2-6.5 di questo stesso documento.
  Soggetto obbligato: la TSA che emette/gestisce il certificato della TSU, in
  questo censimento "QTSP/gestore" (il documento non introduce un soggetto
  diverso dal TSP che eroga il servizio di marcatura temporale). La scelta
  tra i due profili di rinvio dipende dalla natura (fisica/giuridica) della
  TSA: NON e' stata modellata come `condizione_applicabilita`, perche' non
  condiziona l'applicabilita' dell'obbligo (che vale per ogni certificato di
  TSU) ma solo lo standard di rinvio applicabile; la distinzione e'
  integralmente riportata in `testo` e `testo_integrale`.
- Clausola 6.2 (Subject name requirements) -> 1 Obbligo "tecnico/sicurezza".
  Un solo nodo per l'intera clausola (nessuna suddivisione in lettere/numeri
  nel testo, un solo item di indice): la clausola contiene quattro
  prescrizioni omogenee sul campo subject del certificato della TSU, tutte a
  carico della TSA - countryName "shall" indicare il paese di stabilimento
  della TSA (non necessariamente quello in cui si trova la TSU);
  organizationName "shall" contenere il nome registrato completo della TSA
  responsabile della gestione della TSU (per TSA persona giuridica o persona
  fisica associata a una persona giuridica), nome che "should" essere
  ufficialmente registrato; il commonName specifica un identificatore della
  TSU e la identifica univocamente all'interno della TSA; per una TSA persona
  fisica "should" essere inclusa una sola istanza dell'attributo
  serialNumber. Le raccomandazioni "should" restano dentro l'Obbligo, stessa
  convenzione gia' adottata nei moduli ETSI del censimento (la sfumatura
  "should" vs "shall" e' preservata in `testo`).
- Clausola 6.3 (Key lengths requirements) -> 1 Obbligo "tecnico/sicurezza":
  la lunghezza della chiave per l'algoritmo di firma selezionato del
  certificato della TSU "should" essere quella raccomandata nella clausola
  9.3 di ETSI TS 119 312 [i.5]. La NOTE ufficiale ("Cryptographic suites
  recommendations defined in ETSI TS 119 312 [i.5] can be superseded by
  national recommendations") e' mantenuta verbatim in `testo_integrale`:
  non e' bibliografia decorativa, perimetra la portata del rinvio (le
  raccomandazioni di suite crittografiche possono essere superate da
  raccomandazioni nazionali, es. quelle emanate in ambito AgID).
- Clausola 6.4 (Key usage requirements) -> 1 Obbligo "tecnico/sicurezza": due
  prescrizioni omogenee sull'uso della chiave e sul suo periodo di validita' -
  l'impostazione dell'extended key usage del certificato della TSU "shall"
  essere quella definita nella clausola 2.3 di IETF RFC 3161 (ExtendedKeyUsage
  id-kp-timeStamping), e l'estensione private key usage period "should"
  essere usata per limitare la validita' della chiave di firma della TSU.
- Clausola 6.5 (Algorithm requirements) -> 1 Obbligo "tecnico/sicurezza": la
  chiave pubblica della TSU e la firma del certificato della TSU "should"
  usare gli algoritmi specificati nella clausola A.9 di ETSI TS 119 312
  [i.5]. Anche qui la NOTE ufficiale sulle raccomandazioni nazionali e'
  mantenuta verbatim (stesso ragionamento della clausola 6.3).
- Clausola 7 (Profiles for the transport protocols to be supported) -> 1
  Obbligo "tecnico/sicurezza". E' l'unica clausola del capitolo con due
  soggetti obbligati distinti, entrambi espliciti nel testo: il
  time-stamping client e il time-stamping server "shall" supportare il
  protocollo di marcatura temporale via HTTP (IETF RFC 7230 to RFC 7235) o
  HTTPS (IETF RFC 2818), come definito nella clausola 3.4 di IETF RFC 3161;
  HTTPS "should" essere usato al posto di HTTP. Nella tassonomia del
  censimento il time-stamping server (lato TSA/TSU) e' "QTSP/gestore" e il
  time-stamping client (lato richiedente l'emissione della marca) e'
  "Utente/titolare": la riga porta quindi entrambi i soggetti, entrambi con
  ruolo "obbligato", perche' il testo non distingue fra obbligo principale e
  destinatario ma impone il supporto del profilo a entrambe le parti
  dell'interazione.
- Clausola 8 (Object identifiers of the cryptographic algorithms) -> 1
  Principio "definitorio", NESSUN Obbligo. La clausola e' puramente
  referenziale: non contiene alcun verbo prescrittivo ("shall"/"should") ne'
  impone un comportamento a un soggetto identificabile; si limita a
  dichiarare dove sono specificati gli Object Identifier degli algoritmi di
  hashing e di firma raccomandati (ETSI TS 119 312 [i.5], clausola 11). Nel
  vocabolario chiuso del censimento il valore piu' preciso e' "definitorio":
  la clausola fissa il riferimento tecnico autoritativo degli OID usati dalle
  clausole 6.3 e 6.5, cioe' il perimetro tecnico di un requisito, ed e' lo
  stesso trattamento gia' riservato al modulo ASN.1 di Annex B di ETSI EN 319
  412-5 (disposizione normativa ma referenziale -> "definitorio");
  "scopo/ambito di applicazione" sarebbe improprio (non delimita il campo di
  applicazione del documento) e "altro" sarebbe meno informativo, non
  trattandosi di una mera facolta' ma di un rinvio normativo puntuale.
- Nessun nodo porta `oggetti_giuridici`: le clausole di questo capitolo
  riguardano il profilo tecnico del certificato della TSU, le suite
  crittografiche e il profilo di trasporto del protocollo, non qualificano la
  marca temporale come qualificata ne' il certificato della TSU come
  certificato qualificato di firma elettronica (la qualificazione e' materia
  di ETSI EN 319 421/eIDAS, non di questo profilo di protocollo). Nessuna
  riga porta `severita`/`sanzioni`: uno standard tecnico ETSI non prevede
  sanzioni.
- Nessuna riga porta `condizione_applicabilita`: tutte le prescrizioni di
  questo capitolo si applicano incondizionatamente a chi emette/usa il
  certificato della TSU e a chi implementa il protocollo (unica variazione, in
  6.1, e' lo standard di rinvio, v. sopra).
- Nota sul formato del riferimento: questo documento non usa identificatori
  di requisito propri (formato <service component>-<clausola>-<progressivo>
  di ETSI EN 319 421): numera le prescrizioni solo per clausola, quindi ogni
  `riferimento` e' "clausola X.Y (Titolo ufficiale)" oppure "clausola N
  (Titolo ufficiale)".
- Artefatti di conversione PDF->markdown esclusi dal testo: i marcatori di
  impaginazione "***ETSI***", "<!-- Page 9 -->" e "<!-- Page 10 -->" (non
  fanno parte del testo normativo; nessun altro contenuto e' stato omesso).
- RELAZIONI: vuote per istruzione di capitolo (l'import granulare produce
  sottografi per fonte; il collegamento cross-fonte e' la Fase 6/ADR-0009
  della sessione principale, NON di questo modulo). Nota di coordinamento per
  la sessione principale sui rinvii contenuti in questo capitolo: ETSI EN 319
  412-2 e ETSI EN 319 412-3 (clausola 6.1) sono Parti 2 e 3 di ETSI EN 319
  412, Fonte 7 gia' censita -> candidati naturali per relazioni cross-fonte
  dal nodo di 6.1 verso i nodi di quei profili; ETSI TS 119 312 [i.5]
  (clausole 6.3, 6.5, 8) NON e' una Fonte di questo censimento e quindi non
  puo' produrre relazioni (stessa constatazione gia' registrata in
  docs/fonti-censite.md), i rinvii a IETF RFC 3161/2818/7230-7235 restano
  citazioni a standard esterni non censiti, e i rinvii interni ("the
  amendments defined in the following clauses") sono di cornice, non
  citazioni di un identificatore di requisito di un altro nodo.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "clausola 6.1 (General requirements)",
        "testo": (
            "Il certificato della TSU (Time-Stamping Unit) deve rispettare i requisiti di profilo "
            "definiti in ETSI EN 319 412-2 quando la TSA e' una persona fisica, o in ETSI EN 319 412-3 "
            "quando la TSA e' una persona giuridica, con le modifiche introdotte dalle clausole 6.2-6.5 "
            "del presente documento."
        ),
        "testo_integrale": (
            "6.1 General requirements — The TSU certificate shall meet the requirements defined in ETSI "
            "EN 319 412-2 [2] for the TSA being a natural person or defined in ETSI EN 319 412-3 [3] for "
            "the TSA being a legal person with the amendments defined in the following clauses."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.2 (Subject name requirements)",
        "testo": (
            "L'attributo countryName deve indicare il paese in cui la TSA e' stabilita (che non e' "
            "necessariamente il paese in cui si trova la TSU); per una TSA persona giuridica, o persona "
            "fisica associata a una persona giuridica, l'organizationName deve contenere il nome "
            "registrato completo della TSA responsabile della gestione della TSU, nome che dovrebbe "
            "essere un nome ufficialmente registrato; il commonName specifica un identificatore della TSU "
            "e, all'interno della TSA, identifica univocamente la TSU utilizzata; per una TSA persona "
            "fisica dovrebbe essere inclusa nel campo subject una sola istanza dell'attributo "
            "serialNumber."
        ),
        "testo_integrale": (
            "6.2 Subject name requirements — The countryName attribute shall specify the country in "
            "which the TSA is established (which is not necessarily the name of the country where the TSU "
            "is located). For a TSA being a legal person or a natural person associated with a legal "
            "person the organizationName shall contain the full registered name of the TSA responsible "
            "for managing the TSU. That name should be an officially registered name of the TSA. The "
            "commonName specifies an identifier for the TSU. Within the TSA, the attribute commonName "
            "uniquely identifies the TSU used. For a TSA being a natural person, one instance of the "
            "attribute serialNumber should be included in the subject field."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.3 (Key lengths requirements)",
        "testo": (
            "La lunghezza della chiave per l'algoritmo di firma selezionato del certificato della TSU "
            "dovrebbe essere quella raccomandata nella clausola 9.3 di ETSI TS 119 312; le raccomandazioni "
            "di suite crittografiche di ETSI TS 119 312 possono essere superate da raccomandazioni "
            "nazionali."
        ),
        "testo_integrale": (
            "6.3 Key lengths requirements — The key length for the selected signature algorithm of the "
            "TSU certificate should be as recommended in clause 9.3 of ETSI TS 119 312 [i.5]. NOTE: "
            "Cryptographic suites recommendations defined in ETSI TS 119 312 [i.5] can be superseded by "
            "national recommendations."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.4 (Key usage requirements)",
        "testo": (
            "L'impostazione dell'extended key usage del certificato della TSU deve essere quella definita "
            "nella clausola 2.3 di IETF RFC 3161, e l'estensione private key usage period del certificato "
            "della TSU dovrebbe essere usata per limitare la validita' della chiave di firma della TSU."
        ),
        "testo_integrale": (
            "6.4 Key usage requirements — The TSU certificate extended key usage setting shall be as "
            "defined in IETF RFC 3161 [1], clause 2.3. The TSU certificate private key usage period "
            "extension should be used in order to limit the validity of the TSU's signing key."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 6.5 (Algorithm requirements)",
        "testo": (
            "La chiave pubblica della TSU e la firma del certificato della TSU dovrebbero usare gli "
            "algoritmi specificati nella clausola A.9 di ETSI TS 119 312; le raccomandazioni di suite "
            "crittografiche di ETSI TS 119 312 possono essere superate da raccomandazioni nazionali."
        ),
        "testo_integrale": (
            "6.5 Algorithm requirements — The TSU public key and the TSU certificate signature should use "
            "the algorithms as specified in clause A.9 of ETSI TS 119 312 [i.5]. NOTE: Cryptographic "
            "suites recommendations defined in ETSI TS 119 312 [i.5] can be superseded by national "
            "recommendations."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "clausola 7 (Profiles for the transport protocols to be supported)",
        "testo": (
            "Il time-stamping client e il time-stamping server devono supportare il protocollo di "
            "marcatura temporale via HTTP (IETF RFC 7230 to RFC 7235) o HTTPS (IETF RFC 2818) come "
            "definito nella clausola 3.4 di IETF RFC 3161; HTTPS dovrebbe essere usato al posto di HTTP."
        ),
        "testo_integrale": (
            "7 Profiles for the transport protocols to be supported — The time-stamping client and the "
            "time-stamping server shall support the time-stamping protocol via HTTP (IETF RFC 7230 to RFC "
            "7235 [5]) or HTTPS (IETF RFC 2818 [6]) as defined in clause 3.4 of IETF RFC 3161 [1]. HTTPS "
            "(IETF RFC 2818 [6]) should be used instead of HTTP (IETF RFC 7230 to RFC 7235 [5])."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
        ],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 8 (Object identifiers of the cryptographic algorithms)",
        "testo": (
            "Gli Object Identifier degli algoritmi di hashing e di firma raccomandati sono specificati "
            "nella clausola 11 di ETSI TS 119 312."
        ),
        "testo_integrale": (
            "8 Object identifiers of the cryptographic algorithms — Object identifiers for the "
            "recommended hashing and signature algorithms are specified in ETSI TS 119 312 [i.5], clause "
            "11."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 6.1 (General requirements)",
    "clausola 6.2 (Subject name requirements)",
    "clausola 6.3 (Key lengths requirements)",
    "clausola 6.4 (Key usage requirements)",
    "clausola 6.5 (Algorithm requirements)",
    "clausola 7 (Profiles for the transport protocols to be supported)",
    "clausola 8 (Object identifiers of the cryptographic algorithms)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
