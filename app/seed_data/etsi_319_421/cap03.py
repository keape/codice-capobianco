"""ETSI EN 319 421 V1.3.1 (2025-07) - Electronic Signatures and Trust
Infrastructures (ESI); Policy and Security Requirements for Trust Service
Providers issuing Time-Stamps. Fonte 18 (fonte unica, non multi-parte; la
numerazione definitiva e' cablata dalla sessione principale in app/seed.py -
questo modulo NON tocca seed.py). Capitolo 3: clausola 7 (TSA management and
operation), sottoclausole 7.1 (Introduction), 7.2 (Internal organization),
7.3 (Personnel security), 7.4 (Asset management), 7.5 (Access control), 7.6
(Cryptographic controls: 7.6.1 General, 7.6.2 TSU key generation, 7.6.3 TSU
private key protection, 7.6.4 TSU public key certificate, 7.6.5 Rekeying
TSU's key, 7.6.6 Life cycle management of signing cryptographic hardware,
7.6.7 End of TSU key life cycle). Testo ufficiale in
app/.source_cache/etsi_319_421/cap03.txt. La clausola 7.7 (e le successive)
e' fuori dal perimetro di questo capitolo.

Modellazione (ADR-0007), stesso criterio gia' applicato a ETSI TS 119 461
(Fonte 9), ETSI EN 319 401 (Fonte 10), ETSI EN 319 412, ETSI TS 119 431 e
ETSI EN 319 411 (fonti 7/11/12/14-17) per uno standard tecnico ETSI a
clausole/sottoclausole invece che articoli/commi di un atto legislativo:

- Clausola 7.1 (Introduction) -> 1 Principio "scopo/ambito di applicazione",
  riferimento "clausola 7.1 (Introduction)". La clausola e' discorsiva e non
  contiene alcun requisito numerato: enuncia come vanno lette le prescrizioni
  del capitolo (non implicano restrizioni sull'addebito dei servizi del TSA;
  i requisiti sono dati in termini di obiettivi di sicurezza seguiti da
  controlli piu' specifici; la ETSI EN 319 401 [4] rinvia ad altri standard
  piu' generali come fonte di requisiti di controllo piu' dettagliati; la
  fornitura di una marca temporale e' a discrezione del TSA in funzione degli
  SLA con il sottoscrittore). E' quindi cornice di ambito/lettura del
  capitolo, non definizione di un concetto nuovo ne' effetto giuridico in
  senso stretto: "scopo/ambito di applicazione" e' piu' preciso di
  "definitorio" e di "altro". La NOTA attribuita alla clausola (bilanciamento
  tra fiducia necessaria e minimizzazione delle restrizioni sulle tecniche
  impiegabili dal TSA) e' interpretativa e riportata in `testo_integrale`. Il
  Principio non porta `oggetti_giuridici`: la clausola non dichiara un effetto
  giuridico specifico ne' individua un oggetto giuridico determinato.
- Clausola 7.2 (Internal organization) -> 4 Obblighi OVR-7.2-01..04, tutti
  "organizzativo" (assetto organizzativo del TSA: rinvio ai requisiti di
  internal organization della ETSI EN 319 401 [4] clausola 7.1; natura di
  persona giuridica di diritto nazionale; sistema di gestione per qualita' e
  sicurezza delle informazioni; adeguatezza numerica e professionale del
  personale).
- Clausole 7.3 (Personnel security) -> OVR-7.3-01, "organizzativo"; 7.4 (Asset
  management) -> OVR-7.4-01, "organizzativo"; 7.5 (Access control) ->
  OVR-7.5-01, "tecnico/sicurezza". Sono tutte e tre rinvii integrali a
  clausole della ETSI EN 319 401 [4] (rispettivamente 7.2, 7.3 e 7.4): la
  classificazione segue la materia della clausola richiamata (personale e
  asset = assetto organizzativo; controllo degli accessi = controllo di
  sicurezza), criterio gia' adottato nei capitoli omologhi delle altre fonti
  ETSI (es. etsi_119_431_1 cap01: OVR-6.4.2-01, rinvio alla clausola 7.6
  "Physical security controls", classificato "tecnico/sicurezza").
- Clausola 7.6.1 (General) -> OVR-7.6-01, "tecnico/sicurezza": rinvio
  integrale alla clausola 7.5 (cryptographic controls) della ETSI EN 319 401
  [4].
- Clausola 7.6.2 (TSU key generation) -> 8 Obblighi TIS-7.6.2-01..08, tutti
  "tecnico/sicurezza", salvo TIS-7.6.2-02 ("organizzativo": limitazione del
  personale autorizzato in base alle prassi del TSA). TIS-7.6.2-07 e' marcato
  "[CONDITIONAL]" nel testo ufficiale e porta `condizione_applicabilita`.
- Clausola 7.6.3 (TSU private key protection) -> 6 Obblighi TIS-7.6.3-01..06:
  "tecnico/sicurezza" per 01, 02, 03, 04 e 06; "organizzativo" per 05
  (limitazione del personale autorizzato alla funzione di backup). TIS-7.6.3-04
  e' formulato in modo condizionale nel testo ("If TSU private keys are backed
  up"), ma NON e' marcato "[CONDITIONAL]" nel testo ufficiale: coerentemente
  con il contratto del campo (`condizione_applicabilita` per i soli requisiti
  marcati), la riga non lo valorizza - la condizione resta esplicita nel testo
  del requisito stesso.
- Clausola 7.6.4 (TSU public key certificate) -> 5 Obblighi TIS-7.6.4-01..05,
  tutti "tecnico/sicurezza" (integrita'/autenticita' delle chiavi pubbliche di
  verifica, disponibilita' in certificato, CA emittente, divieto di emettere
  marche temporali prima del caricamento del certificato, verifica della
  firma del certificato ottenuto). TIS-7.6.4-05 e' marcato "[CONDITIONAL]" e
  porta `condizione_applicabilita`.
- Clausola 7.6.5 (Rekeying TSU's key) -> 1 Obbligo TIS-7.6.5-01,
  "tecnico/sicurezza" (durata di validita' del certificato del TSU non
  superiore al periodo di idoneita' riconosciuta di algoritmo e lunghezza
  chiave).
- Clausola 7.6.6 (Life cycle management of signing cryptographic hardware) ->
  4 Obblighi TIS-7.6.6-01..04, tutti "tecnico/sicurezza" (integrita' fisica
  dell'hardware in spedizione e in deposito; installazione/attivazione/
  duplicazione delle chiavi solo da ruoli fiduciari in ambiente protetto sotto
  controllo duale; cancellazione delle chiavi private alla dismissione del
  dispositivo).
- Clausola 7.6.7 (End of TSU key life cycle) -> 9 Obblighi TIS-7.6.7-01..09.
  Classificazioni: "organizzativo" per TIS-7.6.7-01 (definizione di una data
  di scadenza per le chiavi del TSU: decisione di assetto gestionale);
  "tecnico/sicurezza" per TIS-7.6.7-02, 03, 04, 05, 06 e 08 (vincoli e
  modalita' tecnico-crittografiche su scadenza, uso e distruzione delle
  chiavi); "procedurale" per TIS-7.6.7-07 (procedure operative o tecniche per
  la sostituzione della coppia di chiavi in prossimita' della scadenza);
  "informativo/trasparenza" per TIS-7.6.7-09 (pubblicazione della data di
  scadenza e delle procedure nella TSA policy o practice statement).

Frasi introduttive non numerate: "In addition, the following particular
requirements apply:" (in coda a OVR-7.2-01), "The following particular
requirements apply:" (in testa alle sottoclausole 7.6.2 e 7.6.6) sono
incorporate nella riga del requisito a cui il testo ufficiale le annette
(OVR-7.2-01, TIS-7.6.2-01, TIS-7.6.6-01), mantenendo l'ordine verbatim del
testo ufficiale anche quando la frase precede l'id del requisito. La frase
"with at least the following particular requirements:" di TIS-7.6.3-01 e
TIS-7.6.4-01, e "In particular:" di TIS-7.6.7-06, sono parte integrante del
requisito stesso e restano nella sua riga.

NOTE ed EXAMPLE: tutte le NOTE/EXAMPLE attribuite a un requisito del perimetro
sono riportate integralmente in `testo_integrale`, comprese le NOTE che si
limitano a rinviare a standard esterni (le liste di protection profile CEN
TS 419221-2/3/4 e EN 419221-5, il rinvio a EN 419231, il rinvio a ETSI TS 119
312): la facolta' di omissione prevista dal criterio di autoria non e' stata
esercitata, privilegiando la completezza del verbatim. La "NOTE 1: Void." di
TIS-7.6.5-01 e' conservata per non alterare il testo ufficiale. In `testo` le
NOTE non sono tradotte, salvo quando restringono l'ambito di applicazione
della prescrizione (OVR-7.2-04), nel qual caso sono sintetizzate.

Marcatore di carattere: il testo ufficiale usa in TIS-7.6.5-01 e TIS-7.6.7-03
la forma "TSU´s" con U+00B4 (acute accent) al posto dell'apostrofo tipografico;
il carattere e' riprodotto verbatim in `testo_integrale` senza normalizzazione.

RELAZIONI interne (solo citazioni letterali di un requirement id completo):
- TIS-7.6.5-01 -> TIS-7.6.2-05 ("see TIS-7.6.2-05"), "richiama", textual.
- TIS-7.6.7-09 -> OVR-6.2-02 e TIS-7.6.7-04 (NOTA 2: "See also OVR-6.2-02 and
  TIS-7.6.7-04"), "richiama", textual. OVR-6.2-02 appartiene alla clausola 6.2
  della stessa Fonte 18 (capitolo 2, altro modulo): `fonte_id_o_None=None`
  risolve alla fonte corrente nel registro di `inserisci_capitoli`.
Nessuna relazione cross-fonte (le costruira' la sessione principale in Fase 6
/ ADR-0009), e nessuna relazione per i rinvii di clausola o a standard
esterni: "(as per clause 7.8)", "(as per clause 7.3)", "(see clause 7.8)",
"NOTE 1: See clause 7.7.1-08", "as per TIS-7.6.2-03-a)", "as per
TIS-7.6.3-02-a)", "the requirements identified in ETSI EN 319 401 [4], clause
7.X" non citano un requirement id completo (manca il prefisso OVR-/TIS-) o
rinviano a un testo esterno, e restano quindi semplici rinvii testuali dentro
`testo_integrale`.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "OVR-7.2-01",
        "testo": (
            "Si applicano i requisiti identificati nella ETSI EN 319 401 [4], clausola 7.1. Si applicano "
            "inoltre i seguenti requisiti particolari."
        ),
        "testo_integrale": (
            "OVR-7.2-01: The requirements identified in ETSI EN 319 401 [4], clause 7.1 shall apply. In "
            "addition, the following particular requirements apply:"
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.2-02",
        "testo": "Il TSA deve essere una persona giuridica ai sensi del diritto nazionale.",
        "testo_integrale": "OVR-7.2-02: The TSA shall be a legal entity according to national law.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.2-03",
        "testo": (
            "Il TSA deve disporre di uno o piu' sistemi di gestione per la qualita' e la sicurezza delle "
            "informazioni adeguati ai servizi di marcatura temporale che fornisce."
        ),
        "testo_integrale": (
            "OVR-7.2-03: The TSA shall have a system or systems for quality and information security "
            "management appropriate for the time-stamping services it is providing."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.2-04",
        "testo": (
            "Il TSA deve impiegare un numero sufficiente di personale in possesso dell'istruzione, della "
            "formazione, delle conoscenze tecniche e dell'esperienza necessarie in relazione al tipo, alla "
            "portata e al volume di lavoro necessari a fornire i servizi di marcatura temporale. NOTA: il "
            "personale impiegato dal TSA comprende il personale individuale contrattualmente incaricato di "
            "svolgere funzioni a supporto dei servizi di marcatura temporale del TSA; il personale coinvolto "
            "soltanto nel monitoraggio dei servizi del TSA non deve necessariamente essere personale del TSA."
        ),
        "testo_integrale": (
            "OVR-7.2-04: It shall employ a sufficient number of personnel having the necessary education, "
            "training, technical knowledge and experience relating to the type, range and volume of work "
            "necessary to provide time-stamping services. NOTE: Personnel employed by a TSA include "
            "individual personnel contractually engaged in performing functions in support of the TSA's "
            "time-stamping services. Personnel who are involved only in monitoring the TSA services need not "
            "be TSA personnel."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.3-01",
        "testo": "Si applicano i requisiti identificati nella ETSI EN 319 401 [4], clausola 7.2.",
        "testo_integrale": (
            "OVR-7.3-01: The requirements identified in ETSI EN 319 401 [4], clause 7.2 shall apply."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.4-01",
        "testo": "Si applicano i requisiti identificati nella ETSI EN 319 401 [4], clausola 7.3.",
        "testo_integrale": (
            "OVR-7.4-01: The requirements identified in ETSI EN 319 401 [4], clause 7.3 shall apply."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.5-01",
        "testo": "Si applicano i requisiti identificati nella ETSI EN 319 401 [4], clausola 7.4.",
        "testo_integrale": (
            "OVR-7.5-01: The requirements identified in ETSI EN 319 401 [4], clause 7.4 shall apply."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "OVR-7.6-01",
        "testo": "Si applicano i requisiti identificati nella ETSI EN 319 401 [4], clausola 7.5.",
        "testo_integrale": (
            "OVR-7.6-01: The requirements identified in ETSI EN 319 401 [4], clause 7.5 shall apply."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.2-01",
        "testo": (
            "La generazione della o delle chiavi di firma del TSU deve avvenire in un ambiente fisicamente "
            "protetto (come da clausola 7.8) a opera di personale in ruoli fiduciari (come da clausola 7.3) "
            "sotto almeno controllo duale. NOTA 1: si veda la clausola 7.7.1-08."
        ),
        "testo_integrale": (
            "The following particular requirements apply: TIS-7.6.2-01: The generation of the TSU's signing "
            "key(s) shall be undertaken in a physically secured environment (as per clause 7.8) by personnel "
            "in trusted roles (as per clause 7.3) under, at least, dual control. NOTE 1: See clause 7.7.1-08."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.2-02",
        "testo": (
            "Il personale autorizzato a svolgere questa funzione deve essere limitato a quello necessario in "
            "base alle prassi del TSA."
        ),
        "testo_integrale": (
            "TIS-7.6.2-02: The personnel authorized to carry out this function shall be limited to those "
            "required to do so under the TSA's practices."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.2-03",
        "testo": (
            "La generazione della o delle chiavi di firma del TSU deve avvenire all'interno di un dispositivo "
            "crittografico sicuro che: a) sia un sistema affidabile con garanzia di livello EAL 4 o superiore "
            "secondo ISO/IEC 15408 [3], o criteri equivalenti nazionali o internazionalmente riconosciuti di "
            "valutazione della sicurezza IT, riferiti a un security target o protection profile che soddisfa i "
            "requisiti del presente documento sulla base di un'analisi dei rischi e tenendo conto delle misure "
            "di sicurezza fisiche e di altre misure non tecniche; oppure b) soddisfi i requisiti identificati "
            "in ISO/IEC 19790 [2], FIPS PUB 140-2 [6] livello 3 o FIPS PUB 140-3 [7] livello 3."
        ),
        "testo_integrale": (
            "TIS-7.6.2-03: The generation of the TSU's signing key(s) shall be carried out within a secure "
            "cryptographic device which: a) is a trustworthy system which is assured to EAL 4 or higher in "
            "accordance with ISO/IEC 15408 [3], or equivalent national or internationally recognized "
            "evaluation criteria for IT security. This shall be to a security target or protection profile "
            "which meets the requirements of the present document, based on a risk analysis and taking into "
            "account physical and other non-technical security measures; or NOTE 2: Standards specifying "
            "common criteria protection profiles for TSP cryptographic modules, in accordance with ISO/IEC "
            "15408 [3], are available within CEN as TS 419221-2 [i.13], TS 419221-3 [i.14], TS 419221-4 "
            "[i.15], or EN 419221-5 [i.16]. b) meets the requirements identified in ISO/IEC 19790 [2], FIPS "
            "PUB 140-2 [6] level 3 or FIPS PUB 140-3 [7] level 3."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.2-04",
        "testo": "Il suddetto dispositivo crittografico sicuro dovrebbe essere garantito come da TIS-7.6.2-03-a).",
        "testo_integrale": (
            "TIS-7.6.2-04: The above secure cryptographic device should be assured as per TIS-7.6.2-03-a), "
            "above. NOTE 3: FIPS PUB 140-2 [6] has been superseded by FIPS PUB 140-3 [7]. NIST currently "
            "proposes FIPS PUB 140-2 [6] modules can remain active for 5 years after validation or until "
            "September 21, 2026, when the FIPS PUB 140-2 [6] validations will be moved to the historical list."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.2-05",
        "testo": (
            "L'algoritmo di generazione delle chiavi del TSU, la lunghezza risultante della chiave di firma e "
            "l'algoritmo di firma usati rispettivamente per firmare le marche temporali e per firmare i "
            "certificati di chiave pubblica del TSU dovrebbero essere quelli specificati nella ETSI TS 119 "
            "312 [i.7]."
        ),
        "testo_integrale": (
            "TIS-7.6.2-05: The TSU key generation algorithm, the resulting signing key length and signature "
            "algorithm used for signing time-stamps and for signing TSU public key certificates respectively "
            "should be as specified in ETSI TS 119 312 [i.7]. NOTE 4: Cryptographic suites recommendations "
            "defined in ETSI TS 119 312 [i.7] can be superseded by national recommendations."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.2-06",
        "testo": (
            "Una chiave di firma del TSU non dovrebbe essere importata in dispositivi crittografici sicuri "
            "diversi."
        ),
        "testo_integrale": (
            "TIS-7.6.2-06: A TSU's signing key should not be imported into different secure cryptographic "
            "devices."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.2-07",
        "testo": (
            "Se le stesse chiavi sono presenti in dispositivi crittografici sicuri diversi, esse devono essere "
            "associate allo stesso certificato di chiave pubblica in tutti i diversi dispositivi crittografici "
            "sicuri."
        ),
        "testo_integrale": (
            "TIS-7.6.2-07 [CONDITIONAL]: If there are same keys in different secure cryptographic devices, "
            "they shall be associated with the same public key certificate into all the different secure "
            "cryptographic devices."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "Requisito applicabile se le stesse chiavi sono presenti in dispositivi crittografici sicuri "
            "diversi."
        ),
    },
    {
        "riferimento": "TIS-7.6.2-08",
        "testo": "Un TSU deve avere una sola chiave di firma di marche temporali attiva alla volta.",
        "testo_integrale": (
            "TIS-7.6.2-08: A TSU shall have a single time-stamp signing key active at a time. NOTE 5: A set of "
            "hardware and software can manage different TSUs."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.3-01",
        "testo": (
            "L'integrita' e la riservatezza delle chiavi private del TSU devono essere mantenute con almeno i "
            "seguenti requisiti particolari."
        ),
        "testo_integrale": (
            "TIS-7.6.3-01: Integrity and confidentiality of the TSU private keys shall be maintained with at "
            "least the following particular requirements:"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.3-02",
        "testo": (
            "La chiave privata del TSU deve essere detenuta e usata all'interno di un dispositivo "
            "crittografico sicuro che: a) sia un sistema affidabile con garanzia di livello EAL 4 o superiore "
            "secondo ISO/IEC 15408 [3], o criteri equivalenti nazionali o internazionalmente riconosciuti di "
            "valutazione della sicurezza IT, riferiti a un security target o protection profile che soddisfa i "
            "requisiti del presente documento sulla base di un'analisi dei rischi e tenendo conto delle misure "
            "di sicurezza fisiche e di altre misure non tecniche; oppure b) soddisfi i requisiti identificati "
            "in ISO/IEC 19790 [2], FIPS PUB 140-2 [6] livello 3 o FIPS PUB 140-3 [7] livello 3."
        ),
        "testo_integrale": (
            "TIS-7.6.3-02: The TSU private key shall be held and used within a secure cryptographic device "
            "which: a) is a trustworthy system which is assured to EAL 4 or higher in accordance with ISO/IEC "
            "15408 [3], or equivalent national or internationally recognized evaluation criteria for IT "
            "security. This shall be to a security target or protection profile which meets the requirements "
            "of the present document, based on a risk analysis and taking into account physical and other "
            "non-technical security measures; or NOTE 1: Standards specifying common criteria protection "
            "profiles for TSP cryptographic modules, in accordance with ISO/IEC 15408 [3], are available "
            "within CEN as TS 419221-2 [i.13], TS 419221-3 [i.14], TS 419221-4 [i.15], or EN 419221-5 "
            "[i.16]. b) meets the requirements identified in ISO/IEC 19790 [2], FIPS PUB 140-2 [6] level 3 or "
            "FIPS PUB 140-3 [7] level 3."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.3-03",
        "testo": "Il suddetto dispositivo crittografico sicuro dovrebbe essere garantito come da TIS-7.6.3-02-a).",
        "testo_integrale": (
            "TIS-7.6.3-03: The above secure cryptographic device should be assured as per TIS-7.6.3-02-a). "
            "NOTE 2: FIPS PUB 140-2 [6] has been superseded by FIPS PUB 140-3 [7]. NIST currently proposes "
            "FIPS PUB 140-2 [6] modules can remain active for 5 years after validation or until September 21, "
            "2026, when the FIPS PUB 140-2 [6] validations will be moved to the historical list."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.3-04",
        "testo": (
            "Se le chiavi private del TSU sono oggetto di copia di backup, esse devono essere copiate, "
            "conservate e ripristinate solo da personale in ruoli fiduciari usando almeno il controllo duale "
            "in un ambiente fisicamente protetto (si veda la clausola 7.8)."
        ),
        "testo_integrale": (
            "TIS-7.6.3-04: If TSU private keys are backed up, they shall be copied, stored and recovered only "
            "by personnel in trusted roles using, at least, dual control in a physically secured environment "
            "(see clause 7.8)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.3-05",
        "testo": (
            "Il personale autorizzato a svolgere la funzione di copia di backup deve essere limitato a quello "
            "necessario in base alle prassi del TSA."
        ),
        "testo_integrale": (
            "TIS-7.6.3-05: The personnel authorized to carry out the backup function shall be limited to "
            "those required to do so under the TSA's practices."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.3-06",
        "testo": (
            "Ogni copia di backup delle chiavi private del TSU deve essere protetta quanto a integrita' e "
            "riservatezza dal dispositivo crittografico sicuro prima di essere conservata al di fuori di tale "
            "dispositivo."
        ),
        "testo_integrale": (
            "TIS-7.6.3-06: Any backup copies of the TSU private keys shall be protected to ensure its "
            "integrity and confidentiality by the secure cryptographic device before being stored outside "
            "that device. NOTE 3: Additional requirements for private key protection are defined in the "
            "time-stamping protection profile EN 419231 [i.12]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.4-01",
        "testo": (
            "Il TSA deve garantire l'integrita' e l'autenticita' delle chiavi di verifica della firma (chiavi "
            "pubbliche) del TSU con almeno i seguenti requisiti particolari."
        ),
        "testo_integrale": (
            "TIS-7.6.4-01: The TSA shall guarantee the integrity and authenticity of the TSU signature "
            "verification (public) keys with at least the following particular requirements:"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.4-02",
        "testo": (
            "Le chiavi di verifica della firma (chiavi pubbliche) del TSU devono essere messe a disposizione "
            "delle parti affidanti in un certificato di chiave pubblica."
        ),
        "testo_integrale": (
            "TIS-7.6.4-02: TSU signature verification (public) keys shall be made available to relying "
            "parties in a public key certificate."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.4-03",
        "testo": (
            "Il certificato della chiave di verifica della firma (chiave pubblica) del TSU dovrebbe essere "
            "emesso da un'autorita' di certificazione operante secondo la ETSI EN 319 411-1 [8]."
        ),
        "testo_integrale": (
            "TIS-7.6.4-03: The TSU signature verification (public) key certificate should be issued by a "
            "certification authority operating under ETSI EN 319 411-1 [8]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.4-04",
        "testo": (
            "Il TSU non deve emettere marche temporali prima che il proprio certificato di verifica della "
            "firma (chiave pubblica) sia caricato nel TSU o nel suo dispositivo crittografico sicuro."
        ),
        "testo_integrale": (
            "TIS-7.6.4-04: The TSU shall not issue time-stamp before its signature verification (public key) "
            "certificate is loaded into the TSU or its secure cryptographic device."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.4-05",
        "testo": (
            "Quando ottiene un certificato di verifica della firma (chiave pubblica), il TSA dovrebbe "
            "verificare che tale certificato sia stato firmato correttamente (inclusa la verifica della "
            "catena di certificazione fino a un'autorita' di certificazione fidata)."
        ),
        "testo_integrale": (
            "TIS-7.6.4-05 [CONDITIONAL]: When obtaining a signature verification (public key) certificate, "
            "the TSA should verify that this certificate has been correctly signed (including verification of "
            "the certificate chain to a trusted certification authority)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": (
            "Requisito applicabile quando il TSA ottiene un certificato di verifica della firma (chiave "
            "pubblica)."
        ),
    },
    {
        "riferimento": "TIS-7.6.5-01",
        "testo": (
            "Il periodo di validita' del certificato del TSU non deve essere piu' lungo del periodo di tempo "
            "in cui l'algoritmo e la lunghezza della chiave scelti sono riconosciuti idonei allo scopo (si "
            "veda TIS-7.6.2-05)."
        ),
        "testo_integrale": (
            "TIS-7.6.5-01: The TSU´s certificate validity period shall not be longer than the period of time "
            "that the chosen algorithm and key length is recognized as being fit for purpose (see "
            "TIS-7.6.2-05). NOTE 1: Void. NOTE 2: TSU key compromise does not only depend on the "
            "characteristics of the secure cryptographic device being used but also on the procedures being "
            "used at system initialization and key export (when that function is supported)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.6-01",
        "testo": (
            "L'hardware crittografico di firma delle marche temporali non deve essere manomesso durante la "
            "spedizione."
        ),
        "testo_integrale": (
            "The following particular requirements apply: TIS-7.6.6-01: Time-stamp signing cryptographic "
            "hardware shall not be tampered with during shipment."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.6-02",
        "testo": (
            "L'hardware crittografico di firma delle marche temporali non deve essere manomesso durante il "
            "periodo in cui e' conservato."
        ),
        "testo_integrale": (
            "TIS-7.6.6-02: Time-stamp signing cryptographic hardware shall not be tampered with when and "
            "while stored."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.6-03",
        "testo": (
            "L'installazione, l'attivazione e la duplicazione delle chiavi di firma del TSU nell'hardware "
            "crittografico devono essere effettuate solo da personale in ruoli fiduciari usando almeno il "
            "controllo duale in un ambiente fisicamente protetto (si veda la clausola 7.8)."
        ),
        "testo_integrale": (
            "TIS-7.6.6-03: Installation, activation and duplication of TSU's signing keys in cryptographic "
            "hardware shall be done only by personnel in trusted roles using, at least, dual control in a "
            "physically secured environment (see clause 7.8)."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.6-04",
        "testo": (
            "Le chiavi private del TSU memorizzate sul dispositivo crittografico sicuro del TSU devono essere "
            "cancellate al momento della dismissione del dispositivo in modo che sia praticamente impossibile "
            "recuperarle."
        ),
        "testo_integrale": (
            "TIS-7.6.6-04: TSU private keys stored on TSU secure cryptographic device shall be erased upon "
            "device retirement in a way that it is practically impossible to recover them."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.7-01",
        "testo": "Il TSA deve definire una data di scadenza per le chiavi del TSU.",
        "testo_integrale": "TIS-7.6.7-01: The TSA shall define an expiration date for TSU's keys.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.7-02",
        "testo": (
            "La data di scadenza delle chiavi private del TSU non deve essere successiva alla data notAfter "
            "del periodo di validita' del certificato di chiave pubblica del TSU associato."
        ),
        "testo_integrale": (
            "TIS-7.6.7-02: The expiration date for TSU's private keys shall not be later than the notAfter "
            "date of the associated TSU public key certificate validity period."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.7-03",
        "testo": (
            "La data di scadenza delle chiavi private e pubbliche del TSU dovrebbe tenere conto della vita "
            "utile definita in 'recommended key sizes versus time' della ETSI TS 119 312 [i.7]."
        ),
        "testo_integrale": (
            "TIS-7.6.7-03: The expiration date for TSU´s private and public keys should take into account "
            "the lifetime defined in 'recommended key sizes versus time' from ETSI TS 119 312 [i.7]. NOTE 1: "
            "Cryptographic suites recommendations defined in ETSI TS 119 312 [i.7] can be superseded by "
            "national recommendations."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.7-04",
        "testo": (
            "Al fine di poter verificare per un lasso di tempo sufficiente la validita' delle marche "
            "temporali, la validita' delle chiavi private del TSU deve essere piu' breve del periodo di "
            "validita' del certificato di chiave pubblica del TSU associato. ESEMPIO: chiave pubblica valida "
            "4 anni e validita' della chiave privata ridotta a 1 anno mediante un'estensione "
            "privateKeyUsagePeriod nel certificato di chiave pubblica del TSU [i.18]."
        ),
        "testo_integrale": (
            "TIS-7.6.7-04: In order to be able to verify during a sufficient lapse of time the validity of "
            "the time-stamps, the validity of the TSU's private keys shall be shorter than the associated TSU "
            "public key certificate validity period. EXAMPLE: Public key valid 4 years, and private key "
            "validity reduced to 1 year by using a privateKeyUsagePeriod extension in the TSU public key "
            "certificate [i.18]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.7-05",
        "testo": (
            "La data di scadenza delle chiavi private e pubbliche del TSU puo' essere definita quando il "
            "dispositivo crittografico sicuro del TSU viene inizializzato oppure impostando un'estensione "
            "privateKeyUsagePeriod all'interno del certificato di chiave pubblica del TSU [i.18]."
        ),
        "testo_integrale": (
            "TIS-7.6.7-05: The expiration date for TSU's private and public keys may be defined when the TSU "
            "secure cryptographic device is initialized or by setting a privateKeyUsagePeriod extension "
            "within the TSU's public key certificate [i.18]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.7-06",
        "testo": "Le chiavi private del TSU non devono essere usate oltre la loro data di scadenza. In particolare:",
        "testo_integrale": (
            "TIS-7.6.7-06: The TSU private keys shall not be used beyond their expiration date. In "
            "particular:"
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.7-07",
        "testo": (
            "Devono essere in atto procedure operative o tecniche che assicurino la messa in opera di una "
            "nuova coppia di chiavi quando una chiave privata del TSU e' prossima alla scadenza."
        ),
        "testo_integrale": (
            "TIS-7.6.7-07: Operational or technical procedures shall be in place to ensure that a new key "
            "pair is put in place when a TSU private key is close to expire."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.7-08",
        "testo": (
            "Le chiavi private scadute del TSU, o qualsiasi loro parte, incluse eventuali copie, devono "
            "essere distrutte in modo che le chiavi private non possano essere recuperate."
        ),
        "testo_integrale": (
            "TIS-7.6.7-08: The expired TSU private keys, or any key part, including any copies shall be "
            "destroyed such that the private keys cannot be retrieved."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "TIS-7.6.7-09",
        "testo": (
            "Il TSA deve specificare la data di scadenza delle chiavi private e pubbliche del TSU nella "
            "propria TSA policy o practice statement, includendo una descrizione delle procedure operative o "
            "tecniche messe in atto per conformarsi ai requisiti della presente clausola."
        ),
        "testo_integrale": (
            "TIS-7.6.7-09: The TSA shall specify the expiration date of the TSU's private and public keys in "
            "its TSA policy or practice statement, including a description of the operational or technical "
            "procedures put in place to comply with the requirements of the present clause. NOTE 2: See also "
            "OVR-6.2-02 and TIS-7.6.7-04."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 7.1 (Introduction)",
        "testo": (
            "I presenti requisiti di policy non intendono implicare alcuna restrizione sull'addebito dei "
            "servizi del TSA. I requisiti sono indicati in termini di obiettivi di sicurezza, seguiti da "
            "requisiti piu' specifici per i controlli necessari a raggiungere tali obiettivi, ove ritenuto "
            "necessario per dare la fiducia necessaria che gli obiettivi siano raggiunti. NOTA: il dettaglio "
            "dei controlli richiesti per raggiungere un obiettivo e' un bilanciamento tra il conseguimento "
            "della fiducia necessaria e la minimizzazione delle restrizioni sulle tecniche che un TSA puo' "
            "impiegare nell'emissione delle marche temporali; la ETSI EN 319 401 [4] richiama altri standard "
            "piu' generali utilizzabili come fonte di requisiti di controllo piu' dettagliati. Per questi "
            "fattori il grado di specificita' dei requisiti dati sotto un certo tema puo' variare. La "
            "fornitura di una marca temporale in risposta a una richiesta e' a discrezione del TSA, in "
            "funzione degli eventuali accordi sul livello di servizio con il sottoscrittore."
        ),
        "testo_integrale": (
            "7.1 Introduction: These policy requirements are not meant to imply any restrictions on charging "
            "for TSA services. The requirements are indicated in terms of the security objectives followed by "
            "more specific requirements for controls to meet those objectives, where considered necessary to "
            "provide the necessary confidence that those objectives will be met. NOTE: The details of "
            "controls required to meet an objective is a balance between achieving the necessary confidence "
            "whilst minimizing the restrictions on the techniques that a TSA can employ in issuing "
            "time-stamps. In ETSI EN 319 401 [4], reference is made to other more general standards which "
            "can be used as a source of more detailed control requirements. Due to these factors the "
            "specificity of the requirements given under a given topic can vary. The provision of a "
            "time-stamp in response to a request is at the discretion of the TSA depending on any service "
            "level agreements with the subscriber."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 7.1 (Introduction)",
    "OVR-7.2-01",
    "OVR-7.2-02",
    "OVR-7.2-03",
    "OVR-7.2-04",
    "OVR-7.3-01",
    "OVR-7.4-01",
    "OVR-7.5-01",
    "OVR-7.6-01",
    "TIS-7.6.2-01",
    "TIS-7.6.2-02",
    "TIS-7.6.2-03",
    "TIS-7.6.2-04",
    "TIS-7.6.2-05",
    "TIS-7.6.2-06",
    "TIS-7.6.2-07",
    "TIS-7.6.2-08",
    "TIS-7.6.3-01",
    "TIS-7.6.3-02",
    "TIS-7.6.3-03",
    "TIS-7.6.3-04",
    "TIS-7.6.3-05",
    "TIS-7.6.3-06",
    "TIS-7.6.4-01",
    "TIS-7.6.4-02",
    "TIS-7.6.4-03",
    "TIS-7.6.4-04",
    "TIS-7.6.4-05",
    "TIS-7.6.5-01",
    "TIS-7.6.6-01",
    "TIS-7.6.6-02",
    "TIS-7.6.6-03",
    "TIS-7.6.6-04",
    "TIS-7.6.7-01",
    "TIS-7.6.7-02",
    "TIS-7.6.7-03",
    "TIS-7.6.7-04",
    "TIS-7.6.7-05",
    "TIS-7.6.7-06",
    "TIS-7.6.7-07",
    "TIS-7.6.7-08",
    "TIS-7.6.7-09",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "TIS-7.6.5-01"),
        "nodo_a": ("obbligo", None, "TIS-7.6.2-05"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", None, "TIS-7.6.7-09"),
        "nodo_a": ("obbligo", None, "OVR-6.2-02"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("obbligo", None, "TIS-7.6.7-09"),
        "nodo_a": ("obbligo", None, "TIS-7.6.7-04"),
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
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, {len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
