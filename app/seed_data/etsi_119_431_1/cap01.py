"""ETSI TS 119 431-1 V1.3.1 (2024-12) - Policy and security requirements for
trust service providers; Part 1: TSP services operating a remote QSCD /
SCDev. Capitolo 1: clausole 1 (Scope), 2 (References), 3 (Definition of
terms, symbols, abbreviations and notations), 4 (General concepts), 5
(General provisions on practice statement and policies), 6 (Trust Service
Providers practice - requisiti OVR/GEN/LNK/SIG/DEL/EID di generazione
chiave, linking eID/certificato, attivazione firma, cancellazione chiave,
backup/recovery, controlli facility/tecnici, business/legal matters, altre
disposizioni). Testo ufficiale: app/.source_cache/etsi_119_431_1/cap01.txt
(354 righe). Fonte 11 (numerazione definitiva cablata dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py).

Modellazione (ADR-0007), stesso criterio gia' applicato a ETSI EN 319 401
(Fonte 10) e ETSI TS 119 461 (Fonte 9) per uno standard tecnico ETSI a
clausole/sottoclausole e requisiti numerati (non un atto legislativo ad
articoli/commi):

- Ogni requisito con id proprio nel formato <3 lettere componente>-<clausola>
  -<numero progressivo> (legenda completa nel nodo "clausola 3.4
  (Notations)": OVR/GEN/LNK/SIG/DEL/EID) -> un nodo Obbligo, `riferimento`
  = id esatto come appare nel testo (es. "GEN-6.2.1-02A", "LNK-6.2.2-03B").
  Incluso il caso limite dei requisiti puramente permissivi ("may", es.
  LNK-6.2.2-04/-06): il documento li classifica comunque come "requirement"
  a tutti gli effetti nella propria legenda di clausola 3.4, per cui
  seguono lo stesso trattamento (Obbligo, non Principio).
- Requisiti "Void" (segnaposto di redazione per requisiti soppressi in
  edizioni precedenti: LNK-6.2.2-01/-02/-03/-07/-10, OVR-6.4.3-01,
  OVR-6.5.3-01, OVR-6.7.2-01, OVR-6.7.13-01) -> ESCLUSI dall'indice, non
  sono una disposizione (ADR-0007). Quando un "Void" e' accompagnato da una
  NOTE con contenuto normativo autonomo (es. OVR-6.7.2-01: Void + NOTE che
  rinvia a OVR-6.8.1-01; OVR-6.7.13-01: Void + NOTE che rinvia a 6.8.1/6.8.4)
  quella NOTE e' comunque coperta da un nodo Principio "altro" sul
  riferimento della clausola contenitrice (es. "clausola 6.7.2 (Financial
  responsibility)"), con relazione "richiama" verso il/i riferimenti
  verificabili nello stesso capitolo.
- Sottoclausole senza requisito numerato ma con enunciato normativo
  esplicito (es. "6.7.1 Fees: These policy requirements are not meant to
  imply any restrictions...", "6.4.7 Key changeover: No policy
  requirement.", "6.7.14 Governing law: Not in the scope of the present
  document.") -> nodo Principio tipo "altro", riferimento = "clausola X.Y
  (Titolo)". Clausole di puro rinvio interno ("6.7.7: See clause 6.7.6.")
  -> Principio "altro" + relazione "richiama" verso l'altro riferimento
  (presente nello stesso capitolo).
- Clausola 1 (Scope) -> Principio "scopo/ambito di applicazione", testo
  integrale completo (2 paragrafi + 5 NOTE assorbite).
- Clausola 2 (References, 2.1 Normative + 2.2 Informative) -> NESSUN nodo:
  bibliografia/paratesto puro, stesso trattamento gia' riservato alla
  clausola 2 di ETSI EN 319 401/119 461/319 412-5.
- Clausola 3.1 (Terms) -> 1 Principio "definitorio" riassuntivo (15
  termini, glossario piatto senza struttura a lettere/numeri propria,
  coerente col criterio "nodo aggregato quando i termini non hanno una
  struttura numerata propria" gia' applicato a Fonte 9/Fonte 10). Clausola
  3.2 (Symbols) -> "Void." puro, NESSUN nodo (stesso trattamento delle
  clausole "Void" prive di contenuto autonomo). Clausola 3.3
  (Abbreviations) -> 1 Principio "definitorio" (20 abbreviazioni, tabella
  ben formattata nel testo assegnato, nessuna ricostruzione necessaria).
  Clausola 3.4 (Notations) -> 1 Principio "definitorio", nodo CRUCIALE:
  riporta la legenda completa e verbatim del formato id, delle 3
  marcature ([CONDITIONAL]/[CHOICE]/[LSP]-[NSP]-[EUSPv2]) e delle regole di
  gestione tra edizioni - referenziata da tutti gli altri capitoli/fonti
  che citano un id di requisito di questo documento.
- Clausola 4.1 (General policy requirements concepts) -> Principio "altro"
  (nota metodologica su incorporazione per riferimento di EN 419241-1/ETSI
  EN 319 401, equivalenza "sole control"="control" mutatis mutandis per i
  sigilli). Clausola 4.2 = "Void" puro -> NESSUN nodo. Clausola 4.3.1 (SSAS
  practice statement) e 4.3.3 (Terms and conditions) -> Principio "altro"
  (descrizioni procedurali, chi le produce/possiede, destinatari). Clausola
  4.3.2 (SSAS policy) -> Principio "definitorio": DEFINISCE le tre SSAS
  policy LSP/NSP/EUSPv2 richiamate pervasivamente dalle marcature dei
  requisiti in clausola 6 (v. sotto). Clausola 4.4 (SSAS component
  services) -> Principio "definitorio": definisce semanticamente i sei
  componenti di servizio (generazione chiave, certificate linking, eID/
  identity linking, signature activation, key deletion, eID provision) i
  cui prefissi (GEN/LNK/SIG/DEL/EID) sono gia' elencati sintatticamente in
  3.4; include le didascalie delle Figure 1-3 (illustrative, nessun
  contenuto normativo autonomo oltre il testo riportato) e le NOTE 2/3 che
  le seguono.
- Marcature [LSP]/[NSP]/[EUSPv2]/[CONDITIONAL] sui singoli requisiti: non
  esiste un campo dedicato nel contratto dati - riportate letteralmente in
  apertura di `testo`/`testo_integrale` (es. "[NSP] ...") e, per i
  requisiti [CONDITIONAL], anche in `condizione_applicabilita` con la
  condizione testuale esatta (es. "In caso di chiave di firma monouso.").
  Nessun requisito di questo capitolo porta la marcatura [CHOICE].
- Clausola 5.2 (SP name and identification): lo schema OID delle policy
  LSP/NSP e' descrittivo/definitorio (Principio "definitorio", riferimento
  "clausola 5.2 (SP name and identification)"), distinto dal requisito
  OVR-5.2-01 (obbligo di aggiornare l'identificativo quando cambia
  l'applicabilita' della SP) che e' un Obbligo a se'.
- Clausola 5.3.2 (Subscriber and signer): descrive chi puo' essere il
  firmatario (persona fisica, persona fisica in associazione con persona
  giuridica, persona giuridica, dispositivo/sistema) -> Principio
  "definitorio".
- categoria_soggetto "QTSP/gestore", ruolo "obbligato" per TUTTI i 93
  Obblighi: il soggetto obbligato e' sempre il TSP/SSASP (mai un
  organismo di certificazione esterno in questo capitolo - le clausole che
  citano organismi di valutazione compaiono solo nello Scope come
  esclusione, non come requisito).
- tipo_obbligo: "tecnico/sicurezza" per la stragrande maggioranza (clausole
  6.2.1/6.2.2/6.2.3/6.2.4/6.3.1/6.3.2/6.3.3/6.4.2/6.4.5/6.5.1-6.5.5 - core
  tecnico di generazione/linking/attivazione/cancellazione/backup delle
  chiavi e controlli di sicurezza fisici/logici/di rete); "organizzativo"
  per le clausole di governance generale (6.4.1, 6.4.4, 6.4.8, 6.4.9,
  6.7.4, 6.7.15, 6.8.1, 6.8.3, 6.8.4, 5.1, 5.3.1, 5.2); "procedurale" per i
  passaggi di processo/delega non intrinsecamente crittografici (LNK-6.2.2
  -02C/-04/-06, OVR-6.4.3-01A); "informativo/trasparenza" per gli obblighi
  di pubblicazione/disponibilita' (6.1.x); "di conservazione" per
  OVR-6.4.6-01 (conservazione dei record di audit per almeno 7 anni) -
  unico requisito di questo capitolo con quella natura specifica.
- EN 419241-1/EN 419241-2/EN 419221-5 (standard CEN, non ETSI) e ETSI EN
  319 401/ETSI EN 319 411-1/ETSI EN 319 403/ETSI TS 119 432 sono citati
  pervasivamente come riferimenti normativi ma NESSUNA relazione cross-
  fonte e' stata creata verso di essi in questo modulo (anche quando gia'
  censiti nel grafo, es. ETSI EN 319 401 = Fonte 10): il rinvio resta
  descritto nel testo del nodo, la risoluzione cross-fonte e' deferita alla
  Fase 6 (istruzione esplicita del batch). Allo stesso modo nessuna
  relazione e' stata creata verso l'altro capitolo di questo stesso
  documento (clausola 7/Annex A-D, Fonte 11 cap02) ne' verso l'altra fonte
  del batch (ETSI TS 119 431-2, Fonte 12): nessun rinvio testuale esplicito
  a un id di requisito preciso di quei capitoli e' presente nel testo di
  clausole 1-6.
- Ricostruzione testuale (necessaria per rispettare ADR-0010 - mai un
  `testo_integrale` troncato): il testo ufficiale assegnato (conversione
  PDF->markdown) presenta, SOLO nella porzione di clausola 6.1-6.2.2, 5
  frammenti orfani spostati fuori sequenza rispetto al requisito a cui
  appartengono (verificato per confronto testuale/grammaticale, nessun
  contenuto inventato - solo riassemblato nell'ordine corretto):
  "time as denoted in the SSAS practice statement." completa OVR-6.1-03;
  "EN 419221-5 [5]." completa GEN-6.2.1-02A; "apply." completa
  GEN-6.2.1-03; "session." completa GEN-6.2.1-09; "directly to the
  identity instead of the linking to the eID means." (frammento incastrato
  subito dopo il titolo "6.2.2 eID means or identity linking" e prima di
  "LNK-6.2.2-01: Void.") completa LNK-6.2.2-00; "clause A.1.1 of EN
  419241-1 [3]." completa LNK-6.2.2-02C. Il resto del capitolo (clausole
  1-5, 6.2.3-6.8) e' testualmente pulito (nessun'altra ricostruzione).
  Un solo residuo non ricostruibile: l'ultima definizione di clausola 3.1
  ("Trust Service Provider (TSP): entity which provides one or more trust
  service") termina cosi' nel file assegnato, senza "s" finale ne' punto -
  probabile artefatto di estrazione a fine pagina PDF senza alcun
  frammento di completamento altrove nel documento (a differenza dei 5 casi
  sopra). Riportato letteralmente come nel file assegnato (vincolo:
  "testo_integrale copiato SOLO dal proprio file di testo assegnato, mai
  riscritto"): non e' un marcatore di elisione ("..."/"…"/"[...]"), quindi
  non attiva la guardia ADR-0010, ma e' segnalato qui per trasparenza.
  Analogamente, la NOTE sotto OVR-6.7.13-01 ("clause 6.8.1 and 6.8.1 ...
  OVR-6.8.1-01 and OVR-6.8.4-04") contiene un'evidente imprecisione del
  testo ufficiale (ripetizione "6.8.1" invece di "6.8.1 e 6.8.4"; citazione
  di un id "OVR-6.8.4-04" inesistente nel documento, che ha solo
  OVR-6.8.4-01) - riportata verbatim senza correzione (non e' compito di
  questo censimento emendare il testo normativo); la relazione "richiama"
  creata da questo nodo punta solo a OVR-6.8.1-01 (riferimento verificato
  esistente), non al riferimento "OVR-6.8.4-04" inventato dalla fonte (per
  evitare di propagare un id inventato in una relazione, come da istruzione
  esplicita in caso di dubbio).

RELAZIONI (5, tutte interne a questo capitolo, evidence_type "textual"):
richiama da clausola 6.7.2 verso OVR-6.8.1-01; da clausola 6.7.6 verso
OVR-6.5.4-01; da clausola 6.7.7 verso clausola 6.7.6; da clausola 6.7.8
verso OVR-6.8.4-01; da clausola 6.7.13 verso OVR-6.8.1-01. Tutte derivano
da un rinvio testuale esplicito del documento verso un riferimento
verificato esistente in questo stesso capitolo. Nessun'altra relazione
interna e' stata creata: i numerosi rinvii tra requisiti dello stesso
gruppo (es. LNK-6.2.2-07A che cita "LNK-6.2.2-01A and LNK-6.2.2-03A or
LNK-6.2.2-03B") sono gia' parte integrante del testo del requisito
citante (relazione di composizione implicita, non un rinvio a clausola
esterna) e non generano una relazione tipizzata separata, per coerenza col
criterio gia' adottato in ETSI TS 119 461 cap03.py ("si preferisce
omettere una relazione arbitraria piuttosto che inventarla").
"""


RIGHE_OBBLIGHI: list[dict] = [
    {
        'riferimento': 'OVR-5.1-01',
        'testo': "Si applicano i requisiti generali specificati in ETSI EN 319 401, clausola 6.1; in aggiunta si applicano i requisiti particolari seguenti. Un TSP puo' documentare le prassi relative a specifici requisiti di SSAS policy separatamente dal documento di practice statement principale.",
        'testo_integrale': 'OVR-5.1-01: The general requirements specified in ETSI EN 319 401 [1], clause 6.1 shall apply. In addition, the following particular requirements apply: NOTE 1: A TSP can document practices relating to specific SSAS policy requirements separate from the main practice statement document.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-5.1-02',
        'testo': "La practice statement del TSP deve includere gli algoritmi di firma e i parametri applicati, gli algoritmi applicati per la generazione della coppia di chiavi e ogni altro algoritmo e parametro critico per la sicurezza dell'operazione SSAS.",
        'testo_integrale': "OVR-5.1-02: The TSP's practice statement shall include the signature algorithms and parameters applied, the algorithms applied for key pair generation and any other algorithms and parameters that are critical to the security of the SSAS operation.",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-5.1-03',
        'testo': "Il TSP deve rendere pubblicamente disponibile la propria practice statement tramite mezzi online disponibili su base 24x7. Il TSP non e' obbligato a divulgare aspetti contenenti informazioni sensibili.",
        'testo_integrale': 'OVR-5.1-03: The TSP shall publicly disclose its practice statement through an online means that is available on a 24×7 basis. NOTE 2: The TSP is not obliged to disclose any aspects containing sensitive information.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-5.2-01',
        'testo': "Se vengono apportate modifiche a una SP come descritta in clausola 4.3.2 che ne influenzano l'applicabilita', l'identificativo di policy dovrebbe essere modificato.",
        'testo_integrale': 'OVR-5.2-01: If any changes are made to a SP as described in clause 4.3.2 which affects the applicability then the policy identifier should be changed.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-5.3.1-01',
        'testo': "Il SSASP puo' avvalersi di altre parti per fornire parti del servizio; tuttavia il SSASP mantiene sempre la responsabilita' complessiva e deve assicurare che i requisiti di policy identificati nel documento siano soddisfatti. Se la parte esterna usa un mezzo di identificazione elettronica emesso nell'ambito di uno schema notificato incluso nell'elenco pubblicato dalla Commissione ai sensi dell'articolo 9 del Regolamento (UE) n. 910/2014, non e' necessario dimostrare la conformita' al livello richiesto: la conformita' ai requisiti regolamentari puo' essere presunta.",
        'testo_integrale': 'OVR-5.3.1-01: The SSASP may make use of other parties to provide parts of the service, however, the SSASP always maintains overall responsibility and shall ensure that the policy requirements identified in the present document are met. NOTE: If the external party uses an eID means issued under a notified scheme that is included in the list published by the Commission pursuant to Article 9 of Regulation (EU) No 910/2014 [i.1], there is no need to demonstrate the conformance to the required level, conformance to the regulatory requirements can be assumed.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.1-01',
        'testo': "Il TSP deve rendere disponibili a sottoscrittori e parti facenti affidamento le SP applicabili, le practice statement e i termini e condizioni relativi all'uso delle chiavi di firma.",
        'testo_integrale': 'OVR-6.1-01: The TSP shall make available to subscribers and relying parties the applicable SPs, practice statements and terms and conditions regarding the use of signing keys.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.1-02',
        'testo': 'I termini e condizioni applicabili devono essere prontamente identificabili per una data chiave di firma o per il certificato associato.',
        'testo_integrale': 'OVR-6.1-02: The applicable terms and conditions shall be readily identifiable for a given signing key or for the associated certificate.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.1-03',
        'testo': 'Le informazioni identificate in OVR-6.1-01 e OVR-6.1-02 devono essere disponibili 24 ore su 24, 7 giorni su 7. In caso di guasto di sistema, di servizio o di altri fattori non sotto il controllo del TSP, il TSP deve applicare la massima diligenza per assicurare che questo servizio informativo non sia indisponibile per un periodo superiore al massimo indicato nella practice statement SSAS.',
        'testo_integrale': 'OVR-6.1-03: The information identified in OVR-6.1-01 and OVR-6.1-02 above shall be available 24 hours per day, 7 days per week. Upon system failure, service or other factors which are not under the control of the TSP, the TSP shall apply best endeavours to ensure that this information service is not unavailable for longer than a maximum period of time as denoted in the SSAS practice statement.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.1-04',
        'testo': 'Le informazioni identificate in OVR-6.1-01 dovrebbero essere disponibili pubblicamente e a livello internazionale.',
        'testo_integrale': 'OVR-6.1-04: The information identified in OVR-6.1-01 above should be publicly and internationally available.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'GEN-6.2.1-01',
        'testo': "[LSP] Si applica la clausola SRG_KM.1.1 di EN 419241-1, che specifica l'ambiente delle chiavi di firma.",
        'testo_integrale': 'GEN-6.2.1-01 [LSP]: Clause SRG_KM.1.1 of EN 419241-1 [3], specifying signing keys environment, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'GEN-6.2.1-02',
        'testo': "[NSP] Si applica la clausola SRA_SKM.1.1 di EN 419241-1, che specifica l'ambiente delle chiavi di firma.",
        'testo_integrale': 'GEN-6.2.1-02 [NSP]: Clause SRA_SKM.1.1 of EN 419241-1 [3], specifying signing keys environment, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'GEN-6.2.1-02A',
        'testo': '[NSP] La chiave di firma del firmatario deve essere generata e usata in uno SCDev certificato conforme a EN 419221-5.',
        'testo_integrale': "GEN-6.2.1-02A [NSP]: Signer's signing key shall be generated and used in a SCDev certified conformant to EN 419221-5 [5].",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'GEN-6.2.1-03',
        'testo': 'Si applica la clausola SRG_KM.1.2 di EN 419241-1, che specifica gli algoritmi crittografici e le lunghezze di chiave.',
        'testo_integrale': 'GEN-6.2.1-03: Clause SRG_KM.1.2 of EN 419241-1 [3], specifying cryptographic algorithms and key lengths, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'GEN-6.2.1-04',
        'testo': 'Si applica la clausola SRG_KM.1.3 di EN 419241-1, che specifica la protezione della chiave.',
        'testo_integrale': 'GEN-6.2.1-04: Clause SRG_KM.1.3 of EN 419241-1 [3], specifying key protection, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'GEN-6.2.1-05',
        'testo': "Si applica la clausola SRG_KM.1.4 di EN 419241-1, che specifica l'inizializzazione del dispositivo.",
        'testo_integrale': 'GEN-6.2.1-05: Clause SRG_KM.1.4 of EN 419241-1 [3], specifying device initialization, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'GEN-6.2.1-06',
        'testo': "Si applica la clausola SRC_SKS.1.1 di EN 419241-1, che specifica i parametri dell'algoritmo.",
        'testo_integrale': 'GEN-6.2.1-06: Clause SRC_SKS.1.1 of EN 419241-1 [3], specifying algorithm parameters, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'GEN-6.2.1-07',
        'testo': 'Si applica la clausola SRC_SKS.1.3 di EN 419241-1, che specifica il momento della generazione.',
        'testo_integrale': 'GEN-6.2.1-07: Clause SRC_SKS.1.3 of EN 419241-1 [3], specifying time of generation, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'GEN-6.2.1-08',
        'testo': "Se il SSAS e il servizio di generazione dei certificati sono gestiti separatamente, il SSAS deve supportare il requisito definito nella clausola REG-6.3.1-01 di ETSI EN 319 411-1 (ad es. fornendo un'attestazione dell'autenticazione del firmatario collegata alla chiave privata).",
        'testo_integrale': 'GEN-6.2.1-08 [CONDITIONAL]: If the SSAS and the certificate generation service are managed separately, then the SSAS shall support the requirement defined in clause REG-6.3.1-01 of ETSI EN 319 411-1 [2]. EXAMPLE: By providing an assertion of the authentication of the signer that is linked to the private key.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': '[CONDITIONAL] Se il SSAS e il servizio di generazione dei certificati sono gestiti separatamente.',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'GEN-6.2.1-09',
        'testo': 'In caso di chiave di firma monouso, la chiave deve essere vincolata a esattamente una sessione di firma.',
        'testo_integrale': 'GEN-6.2.1-09 [CONDITIONAL]: In case of a one-time signing key, the key shall be bound to exactly one signature session.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': '[CONDITIONAL] In caso di chiave di firma monouso.',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-00',
        'testo': "La chiave di firma e' collegata a un mezzo di identificazione elettronica a sua volta collegato all'identita', oppure direttamente all'identita' (quest'ultimo solo possibile in un processo che usa una chiave di firma monouso). In caso di uso di una chiave di firma monouso, la chiave e l'autenticazione possono essere collegate direttamente all'identita' invece che tramite collegamento al mezzo di identificazione elettronica.",
        'testo_integrale': 'NOTE 1: The signing key is either linked to an eID means which is linked to the identity or directly to the identity. The latter is only possible in a process using a one-time signing key. LNK-6.2.2-00 [CONDITIONAL]: In case a one-time signing key is used, the key and the authentication may be linked directly to the identity instead of the linking to the eID means.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': '[CONDITIONAL] In caso di uso di una chiave di firma monouso.',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-01A',
        'testo': "[LSP] Si applica la clausola SRC_SA.1.1 di EN 419241-1, che specifica l'arruolamento (enrolment).",
        'testo_integrale': 'LNK-6.2.2-01A [LSP]: Clause SRC_SA.1.1 of EN 419241-1 [3], specifying enrolment, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-02A',
        'testo': "[NSP] Se il firmatario e' una persona fisica, l'identity proofing e la verifica devono essere come specificati nella clausola A.1.2 di EN 419241-1, per livello di assicurazione sostanziale o superiore.",
        'testo_integrale': 'LNK-6.2.2-02A [NSP] [CONDITIONAL]: If the signer is a natural person, the identity proofing and verification shall be as specified in clause A.1.2 of EN 419241-1 [3], for assurance level substantial or higher.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Se il firmatario e' una persona fisica.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-02B',
        'testo': "[NSP] Se il firmatario e' una persona giuridica, l'identity proofing e la verifica devono essere come specificati nella clausola A.1.3 di EN 419241-1, per livello di assicurazione sostanziale o superiore.",
        'testo_integrale': 'LNK-6.2.2-02B [NSP] [CONDITIONAL]: If the signer is a legal person, the identity proofing and verification shall be as specified in clause A.1.3 of EN 419241-1 [3], for assurance level substantial or higher.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Se il firmatario e' una persona giuridica.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-02C',
        'testo': "[NSP] La domanda e la registrazione durante l'arruolamento del firmatario devono essere come specificate nella clausola A.1.1 di EN 419241-1.",
        'testo_integrale': 'LNK-6.2.2-02C [NSP]: The application and registration during enrolment of the signer shall be as specified in clause A.1.1 of EN 419241-1 [3].',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-02D',
        'testo': "[NSP] Nel caso in cui l'autenticazione sia collegata a un mezzo di identificazione elettronica, le caratteristiche e la progettazione del mezzo di identificazione elettronica devono essere come specificate nella clausola A.2.1 di EN 419241-1, per livello di assicurazione sostanziale o superiore.",
        'testo_integrale': 'LNK-6.2.2-02D [NSP] [CONDITIONAL]: In case the authentication is linked to an eID means, the electronic identification means characteristics and design shall be as specified in clause A.2.1 of EN 419241-1 [3], for assurance level substantial or higher.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Nel caso in cui l'autenticazione sia collegata a un mezzo di identificazione elettronica.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-02E',
        'testo': "[NSP] Nel caso in cui l'autenticazione sia collegata a un mezzo di identificazione elettronica, il meccanismo di autenticazione deve essere come specificato nella clausola A.2.2 di EN 419241-1, per livello di assicurazione sostanziale o superiore.",
        'testo_integrale': 'LNK-6.2.2-02E [NSP] [CONDITIONAL]: In case the authentication is linked to an eID means, the authentication mechanism shall be as specified in clause A.2.2 of EN 419241-1 [3], for assurance level substantial or higher.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Nel caso in cui l'autenticazione sia collegata a un mezzo di identificazione elettronica.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-03A',
        'testo': "Nel caso in cui l'autenticazione sia collegata a un mezzo di identificazione elettronica, il SSASP deve collegare le chiavi di firma con l'appropriato riferimento al mezzo di identificazione elettronica del firmatario.",
        'testo_integrale': "LNK-6.2.2-03A [CONDITIONAL]: In case the authentication is linked to an eID means, the SSASP shall link signing keys with the appropriate signer's eID means reference.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Nel caso in cui l'autenticazione sia collegata a un mezzo di identificazione elettronica.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-03B',
        'testo': "Nel caso in cui l'autenticazione sia collegata direttamente all'identita', il SSASP deve collegare la chiave di firma monouso alla specifica identita'.",
        'testo_integrale': 'LNK-6.2.2-03B [CONDITIONAL]: In case the authentication is linked directly to the identity, the SSASP shall link the one-time signing key with the specific identity.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Nel caso in cui l'autenticazione sia collegata direttamente all'identita'.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-04',
        'testo': "Il SSASP puo' generare il riferimento al mezzo di identificazione elettronica e fornire il corrispondente mezzo di identificazione elettronica al firmatario (v. clausola 6.2.4).",
        'testo_integrale': 'LNK-6.2.2-04: The SSASP may generate eID means reference and provide the corresponding eID means to the signer (see clause 6.2.4).',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-05',
        'testo': "Il SSASP deve assicurare che i dati di identificazione personale collegati al riferimento del mezzo di identificazione elettronica o all'identita' siano gli stessi collegati al soggetto del certificato associato. Quando il riferimento del mezzo di identificazione elettronica e' fornito dal servizio di registrazione del TSP che emette i certificati, la conformita' a questo requisito puo' essere presunta.",
        'testo_integrale': 'LNK-6.2.2-05: The SSASP shall ensure that the person identification data linked to the eID means reference or the identity is the same as the one linked to the subject of the associated certificate. NOTE 2: When the eID means reference is provided by the TSP issuing certificates registration service, the conformance to this requirement can be assumed.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-06',
        'testo': "Il riferimento al mezzo di identificazione elettronica del firmatario puo' essere fornito da una parte (esterna) autorizzata.",
        'testo_integrale': "LNK-6.2.2-06: The signer's eID means reference may be provided by an authorized (external) party.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-07A',
        'testo': "[LSP] Se tutto o parte del processo di autenticazione e' delegato a una parte esterna, il SSASP deve assicurare che la parte esterna soddisfi i requisiti specificati in LNK-6.2.2-01A e LNK-6.2.2-03A o LNK-6.2.2-03B. Se la parte esterna usa un mezzo di identificazione elettronica emesso nell'ambito di uno schema notificato incluso nell'elenco pubblicato dalla Commissione ai sensi dell'articolo 9 del Regolamento (UE) n. 910/2014, o un EUDI wallet come definito nell'articolo 5a del Regolamento (UE) 2024/1183, corrispondente al livello di assicurazione richiesto, non e' necessario dimostrare la conformita' al livello richiesto: la conformita' ai requisiti regolamentari puo' essere presunta.",
        'testo_integrale': 'LNK-6.2.2-07A [LSP] [CONDITIONAL]: If all or part of the authentication process is delegated to an external party the SSASP shall ensure the external party meets the requirements specified in LNK-6.2.2-01A and LNK-6.2.2-03A or LNK-6.2.2-03B. NOTE 3: If the external party uses an eID means issued under a notified scheme that is included in the list published by the Commission pursuant to Article 9 of Regulation (EU) No 910/2014 [i.1] or an EUDI wallet as defined in article 5a in Regulation (EU) 2024/1183 [i.11] amending Regulation (EU) No 910/2014 [i.1] and which correspond to the needed level of assurance, there is no need to demonstrate the conformance to the required level, conformance to the regulatory requirements can be assumed.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Se tutto o parte del processo di autenticazione e' delegato a una parte esterna.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-08',
        'testo': "[NSP] Se tutto o parte del processo di autenticazione e' delegato a una parte esterna, il SSASP deve assicurare che la parte esterna soddisfi i requisiti specificati in LNK-6.2.2-02A, LNK-6.2.2-02B, LNK-6.2.2-02C, LNK-6.2.2-02D, LNK-6.2.2-02E e LNK-6.2.2-03A o LNK-6.2.2-03B.",
        'testo_integrale': 'LNK-6.2.2-08 [NSP] [CONDITIONAL]: If all or part of the authentication process is delegated to an external party the SSASP shall ensure that the external party meets the requirements specified in LNK-6.2.2-02A, LNK-6.2.2-02B, LNK-6.2.2-02C, LNK-6.2.2-02D, LNK-6.2.2-02E and LNK-6.2.2-03A or LNK-6.2.2-03B.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Se tutto o parte del processo di autenticazione e' delegato a una parte esterna.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-08A',
        'testo': "[NSP] Se tutto il processo di autenticazione e' delegato a una parte esterna, il SSASP deve assicurare che il materiale di chiave segreta usato per autenticare la parte delegata al SAM risieda in un modulo crittografico certificato conforme al requisito definito in SRG_KM.1.1 di EN 419241-1 (ad es. l'autenticazione della parte delegata puo' essere effettuata usando un'asserzione firmata il cui materiale di chiave risiede in un modulo crittografico certificato; nel caso in cui l'autenticazione sia collegata direttamente all'identita', la parte esterna puo' essere un identity service provider a cui e' delegato il processo di autenticazione, autenticato tramite il materiale di chiave). Una delega ha luogo se il processo di autenticazione e' svolto al di fuori del servizio fiduciario qualificato.",
        'testo_integrale': 'LNK-6.2.2-08A [NSP] [CONDITIONAL]: If all of the authentication process is delegated to an external party the SSASP shall ensure that the secret key material used to authenticate the delegated party to the SAM shall reside in a certified cryptographic module consistent with the requirement as defined in SRG_KM.1.1 of EN 419241-1 [3]. EXAMPLE 1: The authentication of the delegated party can be done by using a signed assertion where the key material resides in a certified cryptographic module. EXAMPLE 2: In case the authentication is linked directly to the identity, the external party can be an identity service provider to whom the authentication process is delegated. In that case the identity service provider is authenticated using the key material. NOTE 4: A delegation takes place if the authentication process is done outside of the qualified trust service.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Se tutto il processo di autenticazione e' delegato a una parte esterna.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-09',
        'testo': "[NSP] Se tutto o parte del processo di autenticazione e' delegato a una parte esterna, il SSASP deve assicurare che: la parte esterna soddisfi tutti i requisiti pertinenti del documento e i requisiti per la registrazione secondo i requisiti regolamentari applicabili (nel contesto dell'Unione Europea, definiti nel Regolamento (UE) 2024/1183); oppure il processo di autenticazione delegato alla parte esterna usi un mezzo di identificazione elettronica emesso nell'ambito di uno schema notificato conforme ai requisiti regolamentari applicabili. Nel contesto dell'Unione Europea, l'elenco dei mezzi di identificazione elettronica emessi nell'ambito di schemi notificati e' pubblicato dalla Commissione Europea ai sensi dell'articolo 9 del Regolamento (UE) 2024/1183. L'EUDI wallet come definito nell'articolo 5a del Regolamento (UE) 2024/1183 rispetta i requisiti di un mezzo di identificazione elettronica di livello elevato.",
        'testo_integrale': 'LNK-6.2.2-09 [NSP] [CONDITIONAL]: If all or part of the authentication process is delegated to an external party the SSASP shall ensure that: - the external party fulfils all the relevant requirements of the present document and the requirements for registration according to the applicable regulatory requirements; or NOTE 5: In the context of the European Union, the applicable regulatory requirements are defined in Regulation (EU) 2024/1183 [i.11] amending Regulation (EU) No 910/2014 [i.1]. - the authentication process delegated to the external party uses an eID means issued under a notified scheme in accordance with the applicable regulatory requirements. NOTE 6: In the context of the European Union, the list of electronic identification means, issued under notified schemes, is published by the European Commission pursuant to Article 9 of Regulation (EU) 2024/1183 [i.11] amending Regulation (EU) No 910/2014 [i.1]. NOTE 7: The EUDI wallet as defined in article 5a in Regulation (EU) 2024/1183 [i.11] amending Regulation (EU) No 910/2014 [i.1] respects the requirements of an electronic identification means of level high.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Se tutto o parte del processo di autenticazione e' delegato a una parte esterna.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.2-10A',
        'testo': "Il SSASP deve proteggere l'integrita' dei collegamenti tra la chiave di firma del firmatario e il suo riferimento al mezzo di identificazione elettronica, se usato, o l'identita' fornita altrimenti.",
        'testo_integrale': "LNK-6.2.2-10A: The SSASP shall protect the integrity of links between signer's signing key and its eID means reference if this is used or the provided identity otherwise.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.3-01',
        'testo': 'Si applica al SSAS la clausola SRC_SKS.1.2 di EN 419241-1, che specifica il collegamento del certificato.',
        'testo_integrale': 'LNK-6.2.3-01: Clause SRC_SKS.1.2 of EN 419241-1 [3], specifying certificate linking, shall apply to the SSAS.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.3-02',
        'testo': 'Si applica al SSAS la clausola SRC_SKS.1.4 di EN 419241-1, che specifica il collegamento del certificato.',
        'testo_integrale': 'LNK-6.2.3-02: Clause SRC_SKS.1.4 of EN 419241-1 [3], specifying certificate linking, shall apply to the SSAS.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'LNK-6.2.3-03',
        'testo': 'Si applica al SSAS la clausola SRC_SKS.1.5 di EN 419241-1, che specifica la protezione dei collegamenti.',
        'testo_integrale': 'LNK-6.2.3-03: Clause SRC_SKS.1.5 of EN 419241-1 [3], specifying links protection, shall apply to the SSAS.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'EID-6.2.4-01',
        'testo': 'Se il SSASP fornisce il mezzo di identificazione elettronica del firmatario, il mezzo deve essere trasmesso in modo sicuro al firmatario.',
        'testo_integrale': "EID-6.2.4-01 [CONDITIONAL]: If the SSASP provides the signer's eID means, the eID means shall be securely passed to the signer.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': '[CONDITIONAL] Se il SSASP fornisce il mezzo di identificazione elettronica del firmatario.',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'EID-6.2.4-02',
        'testo': 'Se il SSASP personalizza il mezzo di identificazione elettronica del firmatario con dati di attivazione utente associati (ad es. codice PIN), i dati di attivazione devono essere preparati e distribuiti in modo sicuro separatamente dal mezzo di identificazione elettronica del firmatario.',
        'testo_integrale': "EID-6.2.4-02 [CONDITIONAL]: If the SSASP personalizes the signer's eID means with an associated user activation data (e.g. PIN code), the activation data shall be securely prepared and distributed separately from the signer's eID means.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': '[CONDITIONAL] Se il SSASP personalizza il mezzo di identificazione elettronica del firmatario con dati di attivazione utente associati.',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-01',
        'testo': "Si applica la clausola SRC_SA.1.2 di EN 419241-1, che specifica l'autenticazione.",
        'testo_integrale': 'SIG-6.3.1-01: Clause SRC_SA.1.2 of EN 419241-1 [3], specifying authentication, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-02',
        'testo': 'Si applica la clausola SRC_SA.1.3 di EN 419241-1, che specifica la sicurezza del protocollo.',
        'testo_integrale': 'SIG-6.3.1-02: Clause SRC_SA.1.3 of EN 419241-1 [3], specifying protocol security, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-03',
        'testo': 'Si applica la clausola SRC_SA.1.4 di EN 419241-1, che specifica il controllo degli accessi.',
        'testo_integrale': 'SIG-6.3.1-03: Clause SRC_SA.1.4 of EN 419241-1 [3], specifying access control, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-04',
        'testo': 'Si applica la clausola SRC_SA.1.5 di EN 419241-1, che specifica il controllo della chiave di firma.',
        'testo_integrale': 'SIG-6.3.1-04: Clause SRC_SA.1.5 of EN 419241-1 [3], specifying signing key control, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-05',
        'testo': "[NSP] Si applica la clausola SRA_SKM.2.1 di EN 419241-1, che specifica l'attivazione della chiave di firma.",
        'testo_integrale': 'SIG-6.3.1-05 [NSP]: Clause SRA_SKM.2.1 of EN 419241-1 [3], specifying signing key activation, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-06',
        'testo': '[NSP] Si applica la clausola SRA_SAP.1.2 di EN 419241-1, che specifica la sicurezza del protocollo.',
        'testo_integrale': 'SIG-6.3.1-06 [NSP]: Clause SRA_SAP.1.2 of EN 419241-1 [3], specifying protocol security, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-07',
        'testo': '[NSP] Si applica la clausola SRA_SKM.2.5 di EN 419241-1, che specifica il controllo della chiave di firma.',
        'testo_integrale': 'SIG-6.3.1-07 [NSP]: Clause SRA_SKM.2.5 of EN 419241-1 [3], specifying signing key control, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-08',
        'testo': "Il SSASP dovrebbe assicurare che il certificato a chiave pubblica sia valido prima di usare la corrispondente chiave di firma ('valido' = non scaduto, non revocato, non sospeso; il rispetto puo' essere raggiunto applicando DEL-6.3.2-01 se la sospensione non e' usata).",
        'testo_integrale': 'SIG-6.3.1-08: The SSASP should ensure that the public key certificate is valid before using the corresponding signing key. NOTE 1: valid = not expired not revoked not suspended, can be met by applying DEL-6.3.2-01 if suspension is not used.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-09',
        'testo': "Le chiavi di firma devono essere utilizzabili solo nei casi per cui e' stato ottenuto il consenso del firmatario.",
        'testo_integrale': "SIG-6.3.1-09: Signing keys shall be usable in only those cases for which the signer's consent has been obtained.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-10',
        'testo': "Si applica la clausola SRC_DSC.1.1 di EN 419241-1, che specifica i parametri dell'algoritmo di creazione della firma.",
        'testo_integrale': "SIG-6.3.1-10: Clause SRC_DSC.1.1 of EN 419241-1 [3], specifying signature creation's algorithm parameters, shall apply.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-11',
        'testo': "Nel caso in cui l'autenticazione sia collegata direttamente all'identita', il SAD deve contenere l'identificatore univoco della sessione di firma, univocamente collegato al SSAS.",
        'testo_integrale': 'SIG-6.3.1-11 [CONDITIONAL]: In case the authentication is linked directly to the identity, the SAD shall contain the unique identifier of the signature session which shall be uniquely linked to the SSAS.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Nel caso in cui l'autenticazione sia collegata direttamente all'identita'.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-12',
        'testo': "Nel caso in cui l'autenticazione sia collegata direttamente all'identita', il SAD deve contenere l'identificatore univoco del processo di verifica dell'identita'.",
        'testo_integrale': 'SIG-6.3.1-12 [CONDITIONAL]: In case the authentication is linked directly to the identity, the SAD shall contain the unique identifier of the identity verification process.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Nel caso in cui l'autenticazione sia collegata direttamente all'identita'.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-13',
        'testo': "Nel caso in cui l'autenticazione sia collegata direttamente all'identita', la sessione di firma deve essere collegata: 1) esattamente a un SAD che contenga i riferimenti di tutti i documenti da firmare in quella sessione; oppure 2) a piu' valori SAD se e solo se piu' firme consecutive sono applicate allo stesso documento, dove ciascuna firma copre le precedenti (es. in PAdES ogni nuova firma copre le precedenti). L'identificatore univoco della sessione di firma puo' essere usato per identificare la chiave di firma 'predefinita o selezionata' nel SAD come richiesto in SRA_SAP.2.3 di EN 419241-1; l'identificatore univoco del processo di verifica dell'identita' puo' essere usato per identificare il firmatario autenticato nel SAD come richiesto in SRA_SAP.2.3 di EN 419241-1.",
        'testo_integrale': 'SIG-6.3.1-13 [CONDITIONAL]: In case the authentication is linked directly to the identity, the signature session shall be linked: 1) either exactly to one SAD which contains the references of all documents that shall be signed within this session; 2) or to multiple SAD values if and only if multiple consecutive signatures are applied to the same document, where each signature covers the previous ones. EXAMPLE 1: In PAdES each new signature covers the previous ones. NOTE 2: The unique identifier of the signature session can be used to identify the "default or selected" signing key in the SAD as requested in SRA_SAP.2.3 of EN 419241-1 [3]. NOTE 3: The unique identifier of the identity verification process can be used to identify the authenticated signer in the SAD as requested in SRA_SAP.2.3 of EN 419241-1 [3].',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Nel caso in cui l'autenticazione sia collegata direttamente all'identita'.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-14',
        'testo': "Nel caso in cui l'autenticazione sia collegata direttamente all'identita', la sessione di firma deve terminare al massimo 2 ore dopo la fine del processo di verifica dell'identita'. Il processo di verifica dell'identita' comprende non solo l'interazione con il soggetto della verifica dell'identita', ma anche tutta l'elaborazione necessaria per avere un risultato verificato. Nel caso in cui l'autenticazione sia collegata a un eID, la verifica dell'identita' del collegamento eID puo' essere usata per periodi piu' lunghi, perche' i fattori di autenticazione consentono di garantire un collegamento forte con l'identita'.",
        'testo_integrale': 'SIG-6.3.1-14 [CONDITIONAL]: In case the authentication is linked directly to the identity, the signature session shall end at most 2 hours after the end of the identity verification process. NOTE 4: The identity verification process includes not only the interaction with the subject of the identity verification, but also all processing needed to have a verified result in the end. NOTE 5: In case the authentication is linked to an eID, then identity verification of the eID link can be used for longer periods of time, because the authentication factors allow to guarantee a strong link to the identity.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Nel caso in cui l'autenticazione sia collegata direttamente all'identita'.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-15',
        'testo': "[NSP] Nel caso in cui il firmatario sia una persona fisica e l'autenticazione sia collegata direttamente all'identita', il SAP deve includere un'azione esplicita (non una semplice casella di spunta) del firmatario per approvare l'autorizzazione a firmare il contenuto degli specifici documenti referenziati nel SAD.",
        'testo_integrale': 'SIG-6.3.1-15 [NSP] [CONDITIONAL]: In case the signer is a natural person and the authentication is linked directly to the identity, the SAP shall include an explicit action (not just a checkbox) of the signer to approve the authorization to sign the content of the specific documents referenced in the SAD.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Nel caso in cui il firmatario sia una persona fisica e l'autenticazione sia collegata direttamente all'identita'.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'SIG-6.3.1-16',
        'testo': "[NSP] Nel caso in cui il firmatario sia una persona giuridica e l'autenticazione sia collegata direttamente all'identita', il SAP deve includere un'azione esplicita (non una semplice casella di spunta) della persona fisica identificata durante il processo di verifica dell'identita' e autorizzata a firmare in nome della persona giuridica, per approvare l'autorizzazione a confermare origine e integrita' degli specifici documenti referenziati nel SAD (es. scorrere fino alla fine del documento prima di cliccare su un pulsante di accettazione, oppure digitare 'I agree to sign this contract').",
        'testo_integrale': 'SIG-6.3.1-16 [NSP] [CONDITIONAL]: In case the signer is a legal person and the authentication is linked directly to the identity, the SAP shall include an explicit action (not just a checkbox) of the natural person identified during the identity verification process and which is allowed to sign in the name of the legal person to approve the authorization to confirm the origin and integrity of the specific documents referenced in the SAD. EXAMPLE 2: An explicit action can be scrolling to the end of the document before clicking on an acceptance button or typing "I agree to sign this contract".',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "[CONDITIONAL] Nel caso in cui il firmatario sia una persona giuridica e l'autenticazione sia collegata direttamente all'identita'.",
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'DEL-6.3.2-01',
        'testo': "Si applica la clausola SRG_KM.7.1 di EN 419241-1; se il certificato a chiave pubblica e' revocato, la corrispondente chiave di firma deve essere distrutta.",
        'testo_integrale': 'DEL-6.3.2-01: Clause SRG_KM.7.1 of EN 419241-1 [3] shall apply. If the public key certificate is revoked, the corresponding signing key shall be destroyed.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'DEL-6.3.2-02',
        'testo': 'Il SSASP deve distruggere una chiave di firma quando richiesto dal firmatario.',
        'testo_integrale': 'DEL-6.3.2-02: The SSASP shall destroy a signing key when requested by the signer.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'DEL-6.3.2-03',
        'testo': 'Si applica la clausola SRG_KM.7.2 di EN 419241-1, che specifica la gestione delle sessioni.',
        'testo_integrale': 'DEL-6.3.2-03: Clause SRG_KM.7.2 of EN 419241-1 [3], specifying session management, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'DEL-6.3.2-04',
        'testo': 'Si applica la clausola SRG_KM.7.3 di EN 419241-1, che specifica la cancellazione del backup della chiave.',
        'testo_integrale': 'DEL-6.3.2-04: Clause SRG_KM.7.3 of EN 419241-1 [3], specifying key backup deletion, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'DEL-6.3.2-05',
        'testo': 'In caso di chiave di firma monouso, la chiave deve essere cancellata immediatamente dopo la fine della sessione di firma.',
        'testo_integrale': 'DEL-6.3.2-05 [CONDITIONAL]: In case of a one-time signing key, the key shall be deleted immediately after the end of the signature session.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': '[CONDITIONAL] In caso di chiave di firma monouso.',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'GEN-6.3.3-01',
        'testo': 'Si applica la clausola SRG_KM.2.1 di EN 419241-1, che specifica il backup della chiave.',
        'testo_integrale': 'GEN-6.3.3-01: Clause SRG_KM.2.1 of EN 419241-1 [3], specifying key backup, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'GEN-6.3.3-02',
        'testo': 'Si applica la clausola SRG_KM.2.2 di EN 419241-1, che specifica la protezione del backup.',
        'testo_integrale': 'GEN-6.3.3-02: Clause SRG_KM.2.2 of EN 419241-1 [3], specifying backup protection, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'GEN-6.3.3-03',
        'testo': 'Si applica la clausola SRG_KM.2.3 di EN 419241-1, che specifica i controlli sul backup.',
        'testo_integrale': 'GEN-6.3.3-03: Clause SRG_KM.2.3 of EN 419241-1 [3], specifying backup controls, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'GEN-6.3.3-04',
        'testo': "Il numero di dataset duplicati non deve eccedere il minimo necessario per assicurare la continuita' del servizio.",
        'testo_integrale': 'GEN-6.3.3-04: The number of duplicated datasets shall not exceed the minimum needed to ensure continuity of the service.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.1-01',
        'testo': 'Si applicano i requisiti identificati in ETSI EN 319 401, clausole 5, 6.3 e 7.3.',
        'testo_integrale': '6.4.1 General OVR-6.4.1-01: The requirements identified in ETSI EN 319 401 [1], clauses 5, 6.3 and 7.3 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.2-01',
        'testo': 'Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.6. In aggiunta si applicano i seguenti requisiti particolari.',
        'testo_integrale': '6.4.2 Physical security controls OVR-6.4.2-01: The requirements identified in ETSI EN 319 401 [1], clause 7.6 shall apply. In addition, the following particular requirements apply:',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.2-02',
        'testo': "Si applicano mutatis mutandis ai servizi di generazione delle chiavi di firma e di gestione dell'attivazione i requisiti identificati in ETSI EN 319 411-1, dalla clausola OVR-6.4.2-02 a OVR-6.4.2-10.",
        'testo_integrale': 'OVR-6.4.2-02: The requirements identified in ETSI EN 319 411-1 [2], clause OVR-6.4.2-02 to OVR-6.4.2-10 shall apply mutatis mutandis to signing key generation and activation management services.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.3-01A',
        'testo': 'Si applicano i requisiti REQ-7.4-03X, REQ-7.4-04X e da REQ-7.4-07X a REQ-7.4-12X di ETSI EN 319 401.',
        'testo_integrale': '6.4.3 Procedural controls OVR-6.4.3-01: Void. OVR-6.4.3-01A: The requirements REQ-7.4-03X, REQ-7.4-04X and REQ-7.4-07X to REQ-7.4-12X in ETSI EN 319 401 [1] shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.4-01',
        'testo': 'Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.2.',
        'testo_integrale': '6.4.4 Personnel controls OVR-6.4.4-01: The requirements identified in ETSI EN 319 401 [1], clause 7.2 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.5-01',
        'testo': 'Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.10.',
        'testo_integrale': '6.4.5 Audit logging procedures OVR-6.4.5-01: The requirements identified in ETSI EN 319 401 [1], clause 7.10 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.5-02',
        'testo': "Tutti gli eventi di sicurezza devono essere registrati, incluse le modifiche relative alla security policy, l'avvio e l'arresto del sistema, i crash di sistema e i guasti hardware, le attivita' di firewall e router e i tentativi di accesso al sistema SSAS.",
        'testo_integrale': 'OVR-6.4.5-02: All security events shall be logged, including changes relating to the security policy, system start-up and shutdown, system crashes and hardware failures, firewall and router activities and SSAS system access attempts.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.5-03',
        'testo': 'Si applica la clausola SRG_AA.1 di EN 419241-1, che specifica la generazione dei dati di audit.',
        'testo_integrale': 'OVR-6.4.5-03: Clause SRG_AA.1 of EN 419241-1 [3], specifying audit data generation, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.5-04',
        'testo': "Si applica la clausola SRG_AA.2 di EN 419241-1, che specifica la disponibilita' dei dati di audit.",
        'testo_integrale': 'OVR-6.4.5-04: Clause SRG_AA.2 of EN 419241-1 [3], specifying audit data availability, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.5-05',
        'testo': 'Si applica la clausola SRG_AA.3 di EN 419241-1, che specifica i parametri dei dati di audit.',
        'testo_integrale': 'OVR-6.4.5-05: Clause SRG_AA.3 of EN 419241-1 [3], specifying audit data parameters, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.5-06',
        'testo': "Si applica la clausola SRG_AA.7 di EN 419241-1, che specifica l'integrita' dei dati di audit.",
        'testo_integrale': 'OVR-6.4.5-06: Clause SRG_AA.7 of EN 419241-1 [3], specifying audit data integrity, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.5-07',
        'testo': 'Si applica la clausola SRG_AA.8 di EN 419241-1, che specifica la temporizzazione dei dati di audit.',
        'testo_integrale': 'OVR-6.4.5-07: Clause SRG_AA.8 of EN 419241-1 [3], specifying audit data timing, shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.6-01',
        'testo': 'Il SSASP deve conservare i record dei dati di audit per almeno sette anni dopo che qualunque certificato basato su tali record cessa di essere valido, entro i limiti della legislazione applicabile.',
        'testo_integrale': '6.4.6 Records archival OVR-6.4.6-01: The SSASP shall retain the audit data records for at least seven years after any certificate based on these records ceases to be valid and within the constraint of applicable legislation.',
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.8-01',
        'testo': 'Si applicano i requisiti identificati in ETSI EN 319 401, clausole 7.9 e 7.11.',
        'testo_integrale': '6.4.8 Compromise and disaster recovery OVR-6.4.8-01: The requirements identified in ETSI EN 319 401 [1], clauses 7.9 and 7.11 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.4.9-01',
        'testo': 'Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.12.',
        'testo_integrale': '6.4.9 SSASP service termination OVR-6.4.9-01: The requirements identified in ETSI EN 319 401 [1], clause 7.12 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.5.1-01',
        'testo': 'Si applicano i requisiti identificati in EN 419241-1, clausola SRG_M.1.',
        'testo_integrale': '6.5.1 Systems and security management OVR-6.5.1-01: The requirements identified in EN 419241-1 [3], clause SRG_M.1 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.5.2-01',
        'testo': 'Si applicano i requisiti identificati in EN 419241-1, clausola SRG_SO.1.',
        'testo_integrale': '6.5.2 Systems and operations OVR-6.5.2-01: The requirements identified in EN 419241-1 [3], clause SRG_SO.1 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.5.2-02',
        'testo': 'Si applicano i requisiti identificati in EN 419241-1, clausola SRG_SO.2.',
        'testo_integrale': 'OVR-6.5.2-02: The requirements identified in EN 419241-1 [3], clause SRG_SO.2 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.5.3-01A',
        'testo': "Si applicano i requisiti REQ-7.4-01, REQ-7.4-02X, REQ-7.4-05X, REQ-7.4-06X e REQ-7.4-13X di ETSI EN 319 401. I requisiti per i sistemi affidabili possono essere assicurati usando, ad esempio, sistemi conformi a EN 419241-1 o a un profilo di protezione adeguato (o piu' profili), definito in conformita' a ISO/IEC 15408.",
        'testo_integrale': '6.5.3 Computer security controls OVR-6.5.3-01: Void. OVR-6.5.3-01A: The requirements REQ-7.4-01, REQ-7.4-02X, REQ-7.4-05X, REQ-7.4-06X and REQ-7.4-13X in ETSI EN 319 401 [1] shall apply. NOTE: Requirements for the trustworthy systems can be ensured using, for example, systems conforming to EN 419241-1 [3] or to a suitable protection profile (or profiles), defined in accordance with ISO/IEC 15408 [i.6].',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.5.3-02',
        'testo': 'Si applica la clausola SRG_AA.6.1 di EN 419241-1, relativa al monitoraggio del sistema.',
        'testo_integrale': 'OVR-6.5.3-02: Clause SRG_AA.6.1 of EN 419241-1 [3], regarding system monitoring shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.5.4-01',
        'testo': 'Si applicano i requisiti identificati in ETSI EN 319 401, clausole 7.7 e 7.14.',
        'testo_integrale': '6.5.4 Life cycle security controls OVR-6.5.4-01: The requirements identified in ETSI EN 319 401 [1], clause 7.7 and 7.14 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.5.5-01',
        'testo': 'Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.8.',
        'testo_integrale': '6.5.5 Network security controls OVR-6.5.5-01: The requirements identified in ETSI EN 319 401 [1], clause 7.8 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.7.4-01',
        'testo': 'Si applica il requisito REQ 7.13-05 identificato in ETSI EN 319 401.',
        'testo_integrale': '6.7.4 Privacy of personal information OVR-6.7.4-01: The requirement REQ 7.13-05 identified in ETSI EN 319 401 [1] shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.7.15-01',
        'testo': 'Si applicano i requisiti REQ-7.13-01 e REQ-7.13-02 identificati in ETSI EN 319 401.',
        'testo_integrale': '6.7.15 Compliance with applicable law OVR-6.7.15-01: The requirements REQ-7.13-01 and REQ-7.13-02 identified in ETSI EN 319 401 [1] shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.8.1-01',
        'testo': 'Si applicano i requisiti identificati in ETSI EN 319 401, clausola 7.1.',
        'testo_integrale': '6.8.1 Organizational OVR-6.8.1-01: The requirements identified in ETSI EN 319 401 [1], clause 7.1 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.8.3-01',
        'testo': 'Si applicano i requisiti REQ-7.13-03 e REQ-7.13-04 identificati in ETSI EN 319 401.',
        'testo_integrale': '6.8.3 Disabilities OVR-6.8.3-01: The requirements REQ-7.13-03 and REQ-7.13-04 identified in ETSI EN 319 401 [1] shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
    {
        'riferimento': 'OVR-6.8.4-01',
        'testo': 'Si applicano i requisiti identificati in ETSI EN 319 401, clausola 6.2.',
        'testo_integrale': '6.8.4 Terms and conditions OVR-6.8.4-01: The requirements identified in ETSI EN 319 401 [1], clause 6.2 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [
            {'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'},
        ],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        'riferimento': 'clausola 1 (Scope)',
        'testo': "Il documento specifica requisiti generali di policy e sicurezza per i Trust Service Provider (TSP) che operano un dispositivo di creazione di firma remoto (SCDev). Requisiti specifici si applicano quando il dispositivo e' un QSCD remoto ai sensi del Regolamento (UE) 2024/1183 che modifica il Regolamento (UE) n. 910/2014. Il servizio consiste in un'applicazione server di firma e un QSCD/SCDev, denominato Server Signing Application Service (SSAS). Il documento supporta i quadri regolatori europei e non, e' rivolto ai servizi fiduciari qualificati e non qualificati che gestiscono QSCD/SCDev remoti per firme e sigilli elettronici (avanzati e qualificati). L'Annex A contiene i requisiti specifici per un SSAS nel contesto del Regolamento (UE) 2024/1183. Il documento non specifica come la conformita' ai requisiti possa essere valutata da un organismo di valutazione della conformita' indipendente, ne' i requisiti sulle informazioni da mettere a disposizione di tali valutatori, ne' i requisiti sui valutatori stessi; non specifica i protocolli di accesso al SSAS (rinvio a ETSI TS 119 432). Identifica i controlli specifici necessari per affrontare i rischi associati ai servizi che operano QSCD/SCDev remoti.",
        'testo_integrale': "The present document specifies generally applicable policy and security requirements for Trust Service Providers (TSPs) operating a remote Signature Creation Device (SCDev). Specific requirements apply when the device is a remote QSCD as defined in Regulation (EU) 2024/1183 [i.11] amending Regulation (EU) No 910/2014 [i.1]. The service consists of a server signing application and a QSCD / SCDev. The term used in the present document is Server Signing Application Service (SSAS). NOTE 1: Regulation (EU) 2024/1183 [i.11] (eIDASv2) defines the management of remote electronic signature/seal creation devices as a trust service. In addition, it introduces the qualified trust service for the management of remote qualified electronic signature/seal creation devices. The policy and security requirements are defined in terms of requirements for creation, maintenance, life-cycle management and use of signing keys used to create digital signatures. The present document is aimed to be used by independent bodies as the basis for a conformity assessment that a TSP can be trusted for operating a remote QSCD / SCDev. [i.1]. The present document supports European and other regulatory frameworks. NOTE 2: Specifically, but not exclusively, the present document is aimed at qualified and non-qualified trust service managing remote qualified and non-qualified electronic signature/seal creation devices supporting electronic signatures and electronic seals (both advanced and qualified) in accordance with the requirements of Regulation (EU) 2024/1183 [i.11] amending Regulation (EU) No 910/2014 [i.1]. Annex A contains requirements specific for an SSAS in the context of Regulation (EU) 2024/1183 [i.11] amending Regulation (EU) No 910/2014 [i.1]. The present document does neither specify how fulfilment of the requirements can be assessed by an independent conformity assessment body, nor requirements for information to be made available to such independent assessors, or requirements on such assessors. NOTE 3: See ETSI EN 319 403 [i.3] for guidance on assessment of a TSP's processes and services. NOTE 4: The present document references ETSI EN 319 401 [1] for general policy requirements common to all TSP services covered by ETSI standards. The present document does not specify protocols used to access the SSAS. NOTE 5: Protocols for remote digital signature creation are defined in ETSI TS 119 432 [i.4]. The present document identifies specific controls needed to address risks associated with services operating remote QSCD / SCDev.",
        'tipo_principio': 'scopo/ambito di applicazione',
        'stato': 'vigente',
        'oggetti_giuridici': ['dispositivo qualificato di creazione di firma elettronica', 'dispositivo qualificato di creazione di sigillo elettronico'],
    },
    {
        'riferimento': 'clausola 3.1 (Terms)',
        'testo': "La clausola definisce 15 termini specifici del documento: 'authentication' (fornitura di assicurazione dell'identita' dichiarata di un'entita', come da ISO/IEC 18014-2); 'digital signature value' (risultato della trasformazione crittografica di un'unita' di dati che consente al destinatario di provarne origine e integrita' e protegge da contraffazione); 'electronic identification (eID)' (processo di uso di dati di identificazione personale in forma elettronica che rappresentano univocamente una persona fisica o giuridica, o una persona fisica che rappresenta una persona giuridica, come da Regolamento (UE) n. 910/2014); 'electronic identification means' (unita' materiale e/o immateriale contenente dati di identificazione personale usata per l'autenticazione a un servizio online, come da Regolamento (UE) n. 910/2014); 'electronic identification means reference' (dato usato nel SSAS come riferimento a un mezzo di identificazione elettronica per autenticare il firmatario, con esempi: chiave pubblica per chiavi asimmetriche, id dell'asserzione firmata e id utente per asserzioni firmate, chiave segreta per generatori di password monouso); 'one-time signing key' (chiave di firma vincolata, certificata, usata e smaltita sulla base di una singola autorizzazione, collegata a un singolo DTBS/R di sessione di firma - definizione leggermente diversa da EN 419241-2 per consentire chiavi pre-generate, a differenza delle chiavi di firma generali usabili in piu' sessioni); 'person identification data' (insieme di dati che consente di stabilire l'identita' di una persona fisica o giuridica, o di una persona fisica che rappresenta una persona giuridica, come da Regolamento (UE) n. 910/2014); 'Qualified electronic Signature/seal Creation Device (QSCD)' (come specificato nel Regolamento (UE) n. 910/2014); 'Remote QSCD' (come specificato nel Regolamento (UE) 2024/1183 che modifica il Regolamento (UE) n. 910/2014); 'remote signature creation device' (dispositivo di creazione di firma usato da remoto rispetto al firmatario, che fornisce il controllo dell'operazione di firma per conto del firmatario); 'Server Signing Application Service (SSAS)' (servizio fiduciario costituito da un'applicazione server di firma e un QSCD/SCDev per creare un valore di firma digitale per conto di un firmatario); 'Server Signing Application Service Provider (SSASP)' (TSP che opera un componente di servizio SSAS); 'Signature Creation device (SCDev)' (software o hardware configurato usato per implementare i dati di creazione della firma e creare un valore di firma digitale); 'trust service' (servizio elettronico che accresce fiducia e affidabilita' nelle transazioni elettroniche); 'Trust Service Provider (TSP)' (entita' che fornisce uno o piu' servizi fiduciari).",
        'testo_integrale': "For the purposes of the present document, the terms given in ETSI TR 119 001 [i.2] and the following apply: NOTE: Where a definition is copied from a referenced document this is indicated by inclusion of the reference identifier number at the end of the definition or in a note. authentication: provision of assurance in the claimed identity of an entity NOTE: As defined in ISO/IEC 18014-2 [i.7]. digital signature value: result of the cryptographic transformation of a data unit that allows a recipient of the data unit to prove the source and integrity of the data unit and protect against forgery e.g. by the recipient electronic identification (eID): process of using person identification data in electronic form uniquely representing either a natural or legal person, or a natural person representing a legal person NOTE: As defined in Regulation (EU) No 910/2014 [i.1]. electronic identification means: material and/or immaterial unit containing person identification data and which is used for authentication for an online service NOTE: As defined in Regulation (EU) No 910/2014 [i.1]. electronic identification means reference: data used in the SSAS as a reference to an electronic identification means in order to authenticate the signer EXAMPLE: When the eID means uses asymmetric keys, the public key can be the reference. When a signed assertion is generated after a successful authentication of the signer, the assertion signer id and the user id can be the reference. When the eID means uses a secret key (e.g. one time password generator) the secret key can be the reference. one-time signing key: signing key bound, certified, used and disposed based on a single authorization, linked to a single session signing DTBS/R(s) NOTE 1: The definition is slightly different from the one in EN 419241-2 [4] to allow the usage of pre-generated signing keys. NOTE 2: Contrary to general signing keys, which may be used in several signing sessions. person identification data: set of data enabling the identity of a natural or legal person, or a natural person representing a legal person to be established. NOTE: As defined in Regulation (EU) No 910/2014 [i.1]. Qualified electronic Signature/seal Creation Device (QSCD): As specified in Regulation (EU) No 910/2014 [i.1]. Remote QSCD: As specified in Regulation (EU) 2024/1183 [i.11] amending Regulation (EU) No 910/2014 [i.1]. remote signature creation device: signature creation device used remotely from signer perspective and provides control of signing operation on the signer's behalf Server Signing Application Service (SSAS): trust service consisting of a server signing application and a QSCD / SCDev to create a digital signature value on behalf of a signer Server Signing Application Service Provider (SSASP): TSP operating a server signing application service component Signature Creation device (SCDev): configured software or hardware used to implement the signature creation data and to create a digital signature value trust service: electronic service that enhances trust and confidence in electronic transactions Trust Service Provider (TSP): entity which provides one or more trust service",
        'tipo_principio': 'definitorio',
        'stato': 'vigente',
        'oggetti_giuridici': ['dispositivo qualificato di creazione di firma elettronica', 'dispositivo qualificato di creazione di sigillo elettronico'],
    },
    {
        'riferimento': 'clausola 3.3 (Abbreviations)',
        'testo': 'Elenco delle 20 abbreviazioni usate nel documento: CA (Certificate Authority), CID (Commission Implementing Decision), DTBS/R (Data To Be Signed Representation), eID (electronic IDentification), EUDI wallet (European Digital Identity wallet), EUSPv2 (EU SSAS Policy), LSP (Lightweight SSAS Policy), NSP (Normalized SSAS Policy), OID (Object IDentifier), PIN (Personal Identification Number), QSCD (Qualified electronic Signature/Seal Creation Device), SAD (Signature Activation Data), SAM (Signature Activation Module), SAP (Signature Activation Protocol), SCDev (Signature Creation Device), SP (SSAS Policy), SSAS (Server Signing Application Service), SSASP (Server Signing Application Service Provider), TSP (Trust Service Provider), URI (Uniform Resource Identifier).',
        'testo_integrale': 'For the purposes of the present document, the following abbreviations apply: CA Certificate Authority\nCID Commission Implementing Decision\nDTBS/R Data To Be Signed Representation\neID electronic IDentification\nEUDI wallet European Digital Identity wallet\nEUSPv2 EU SSAS Policy\nLSP Lightweight SSAS Policy\nNSP Normalized SSAS Policy\nOID Object IDentifier\nPIN Personal Identification Number\nQSCD Qualified electronic Signature/Seal Creation Device\nSAD Signature Activation Data\nSAM Signature Activation Module\nSAP Signature Activation Protocol\nSCDev Signature Creation Device\nSP SSAS Policy\nSSAS Server Signing Application Service\nSSASP Server Signing Application Service Provider\nTSP Trust Service Provider\nURI Uniform Resource Identifier',
        'tipo_principio': 'definitorio',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 3.4 (Notations)',
        'testo': "I requisiti identificati nel documento comprendono: a) requisiti applicabili a qualunque SSAS policy, indicati da clausole senza marcatura aggiuntiva; b) requisiti applicabili solo a certe condizioni, marcati '[CONDITIONAL]'; c) requisiti che comprendono piu' scelte da selezionare secondo la situazione applicabile, marcati '[CHOICE]'; d) requisiti applicabili ai servizi offerti nell'ambito della SSAS policy applicabile, marcati con la policy applicabile: '[LSP]', '[NSP]' e '[EUSPv2]'. I requisiti sono identificati secondo il formato <3 lettere componente di servizio>-<numero di clausola>-<numero progressivo a 2 cifre>. I componenti di servizio SSAS sono: OVR (requisito generale applicabile a piu' di un componente di servizio), GEN (Signing Key Generation Service), LNK (Certificate/eID means Linking Service), SIG (Signature Activation Service), DEL (Signing Key Deletion Service), EID (eID Means Provision, opzionale). La gestione degli identificativi dei requisiti nelle edizioni successive del documento segue queste regole: quando un requisito e' inserito alla fine di una clausola, il numero progressivo a 2 cifre e' incrementato al successivo disponibile; quando un requisito e' inserito tra due requisiti esistenti, si usano lettere maiuscole aggiunte all'identificativo del requisito precedente per distinguere il nuovo requisito; l'identificativo dei requisiti soppressi resta e viene completato con 'Void'; l'identificativo dei requisiti modificati resta vuoto (void) e il requisito modificato e' identificato da lettera(e) maiuscola(e) aggiunta(e) al numero del requisito iniziale.",
        'testo_integrale': 'The requirements identified in the present document include: a) requirements applicable to any SSAS policies. Such requirements are indicated by clauses without any additional marking; b) requirements applicable under certain conditions. Such requirements are indicated by clauses marked by "[CONDITIONAL]"; c) requirements that include several choices which ought to be selected according to the applicable situation. Such requirements are indicated by clauses marked by "[CHOICE]"; d) requirements applicable to the services offered under the applicable SSAS policy. Such requirements are indicated by clauses marked by the applicable SSAS policy as follows: -"[LSP]", "[NSP]" and "[EUSPv2]". The requirements in the present document are identified as follows: - <3 letters service component> - < the clause number> - <2 digit number-incremental> The SSAS service components are: - OVR: General requirement (requirement applicable to more than 1 service component) - GEN: Signing Key Generation Service - LNK: Certificate/eID means Linking Service - SIG: Signature Activation Service - DEL: Signing Key Deletion Service - EID: eID Means Provision (optional) The management of the requirement identifiers throughout subsequent editions of the present document is as follows: - When a requirement is inserted at the end of a clause, the 2 digit number above is incremented to the next available digit. - When a requirement is inserted between two existing requirements, capital letters appended to the previous requirement identifier are used to distinguish a new requirement. - The requirement identifier for deleted requirements are left and completed with "Void". - The requirement identifier for modified requirement are left void and the modified requirement is identified by capital letter(s) appended to the initial requirement number.',
        'tipo_principio': 'definitorio',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 4.1 (General policy requirements concepts)',
        'testo': "Il documento e' strutturato in linea con ETSI EN 319 411-1 per assistere i TSP nell'applicare questi requisiti alla propria documentazione di policy e practice statement. Il documento incorpora per riferimento i requisiti di EN 419241-1, che definisce i livelli di assicurazione per il 'sole control'; il termine 'sole control' non implica che i requisiti si applichino solo alle firme elettroniche come definite nel Regolamento (UE) n. 910/2014: i requisiti possono essere applicati mutatis mutandis ai sigilli elettronici, sostituendo 'sole control' con 'control' come spiegato in EN 419241-1 clausola 5.3. Ogni requisito applicabile e richiamato sul Trustworthy System Supporting Server Signing (TW4S) in EN 419241-1 e' un requisito sul SSAS. Il documento incorpora per riferimento anche i requisiti di ETSI EN 319 401 aggiungendo requisiti rilevanti per un SSASP (rinvio a EN 319 401 clausola 4 e IETF RFC 3647 clausole 3.1 e 3.4 per guida). I requisiti sono indicati in termini di obiettivi di sicurezza seguiti da requisiti piu' specifici per i controlli necessari a soddisfare tali obiettivi, dove ritenuto necessario per fornire la confidenza necessaria. Il livello di dettaglio dei controlli richiesti per soddisfare un obiettivo e' un equilibrio tra la confidenza necessaria e la minimizzazione delle restrizioni sulle tecniche che un TSP puo' impiegare nell'operare i dispositivi di firma; in alcuni casi si fa riferimento a standard piu' generali come fonte di requisiti di controllo piu' dettagliati, per cui la specificita' dei requisiti su un dato argomento puo' variare. Il documento comprende la fornitura di servizi di generazione della chiave, collegamento del certificato, collegamento del mezzo di identificazione elettronica, attivazione della firma, cancellazione della chiave e fornitura del dispositivo (v. clausola 4.4).",
        'testo_integrale': 'The present document is structured broadly in line with ETSI EN 319 411-1 [2] to assist TSPs in applying these requirements to their own policy and practice statement documentation. The present document incorporates EN 419241-1 [3] requirements by reference. EN 419241-1 [3] defines levels of assurance for sole control. The term "sole control" does not mean that the requirements are only applicable to electronic signatures as defined in Regulation (EU) No 910/2014 [i.1]. The requirements may be applied mutatis mutandis to electronic seals. In other words, the reader may replace the term "sole control" with "control" as explained in EN 419241-1 [3] clause 5.3. NOTE 1: Any applicable and referenced requirements on the Trustworthy System Supporting Server Signing (TW4S) in EN 419241-1 [3] is a requirement on the SSAS. The present document incorporates ETSI EN 319 401 [1] requirements by reference and adds requirements relevant for a SSASP. See ETSI EN 319 401 [1], clause 4 and IETF RFC 3647 [i.5], clauses 3.1 and 3.4 for guidance. The requirements are indicated in terms of the security objectives followed by more specific requirements for controls to meet those objectives where considered necessary to provide the necessary confidence that those objectives will be met. NOTE 2: The details of controls required to meet an objective is a balance between achieving the necessary confidence whilst minimizing the restrictions on the techniques that a TSP can employ in operating signing devices. In some cases, reference is made to other more general standards which can be used as a source of more detailed control requirements. Due to these factors the specificity of the requirements given under a given topic can vary. The present document includes the provision of services for key generation, certificate linking, eID means linking, signature activation, key deletion and device provisioning (see clause 4.4).',
        'tipo_principio': 'altro',
        'stato': 'vigente',
        'oggetti_giuridici': ['dispositivo qualificato di creazione di firma elettronica', 'dispositivo qualificato di creazione di sigillo elettronico'],
    },
    {
        'riferimento': 'clausola 4.3.1 (SSAS practice statement)',
        'testo': "Il Server Signing Application Service Provider (SSASP) sviluppa, implementa, applica e aggiorna una SSAS practice statement, che e' una trust service practice statement come definita in ETSI EN 319 401, istanziata per un SSAS (v. clausola 6.1). La SSAS practice statement descrive come il SSASP opera il proprio servizio ed e' di proprieta' del SSASP, adattata alla struttura organizzativa, alle procedure operative, alle strutture e all'ambiente informatico del TSP. I destinatari della practice statement possono essere revisori, sottoscrittori e parti facenti affidamento. La presenza di alcuni elementi e' obbligatoria nella SSAS practice statement come richiesto dal documento; tuttavia il documento non pone restrizioni sulla forma della SSAS practice statement, che puo' essere inclusa in una practice statement generale del TSP che copre altri servizi, oppure essere un documento autonomo. Il documento fornisce i requisiti identificati come necessari per le SSAS policy definite in clausola 4.3.2, da recepire da parte del SSASP e riflettere nella propria practice statement.",
        'testo_integrale': '4.3.1 SSAS practice statement The Server Signing Application Service Provider (SSASP) develops, implements, enforces, and updates a SSAS practice statement, which is a trust service practice statement as defined in ETSI EN 319 401 [1], instantiated for a SSAS. See clause 6.1. The SSAS practice statement describes how the SSASP operates its service and is owned by the SSASP. The SSAS practice is tailored to the organizational structure, operating procedures, facilities, and computing environment of a TSP. The recipients of the practice statement can be auditors, subscribers and relying parties. NOTE: The presence of some elements is mandatory in the SSAS practice statement as requested in the present document, however the present document places no restriction on the form of the SSAS practice statement; it can be included in a general TSP practice statement document that covers other services delivered by that TSP or be a standalone document. The present document provides requirements identified as necessary for SSAS policies defined in clause 4.3.2, to be endorsed by a SSASP and reflected in its practice statement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 4.3.2 (SSAS policy)',
        'testo': "Una SSAS Policy (SP) descrive cosa e' offerto e puo' contenere informazioni diverse, oltre l'ambito del documento, per indicare l'applicabilita' del SSAS; e' definita indipendentemente dai dettagli specifici dell'ambiente operativo del SSASP. I destinatari della SP possono essere revisori, sottoscrittori e parti facenti affidamento. Il documento definisce tre SP: 1) una Lightweight SSAS Policy (LSP), che offre una qualita' del servizio meno onerosa della NSP (requisiti meno stringenti) per i casi in cui una valutazione del rischio non giustifichi l'onere aggiuntivo di soddisfare tutti i requisiti della NSP (es. uso di un modulo di attivazione della firma); 2) una Normalized SSAS Policy (NSP), che soddisfa la best practice generalmente riconosciuta per i TSP che operano un SCDev remoto a supporto di qualunque tipo di transazione; 3) una EU SSAS v2 Policy (EUSPv2), che offre la stessa qualita' della NSP ma con requisiti specifici del Regolamento (UE) 2024/1183 relativi alla gestione dei QSCD remoti (i requisiti specifici EUSPv2 sono definiti nell'Annex A). Una SP non fa necessariamente parte della documentazione del SSASP (secondo ETSI EN 319 401 sono sufficienti una practice statement e termini e condizioni generali); ad es. una SP puo' essere condivisa da una comunita' e non di proprieta' del SSASP. Il documento non pone vincoli sulla forma della SP, che puo' essere un documento autonomo o essere fornita come parte della practice statement e/o dei termini e condizioni generali.",
        'testo_integrale': "4.3.2 SSAS policy A SSAS Policy (SP) describes what is offered and can contain diverse information beyond the scope of the present document to indicate the applicability of the SSAS. A SP is defined independently of the specific details of the specific operating environment of a SSASP. The recipients of the SP can be auditors, subscribers and relying parties. The present document defines three SPs: 1) A Lightweight SSAS Policy (LSP) offering a quality of service less onerous than the NSP (requiring less demanding policy requirements) for use where a risk assessment does not justify the additional burden of meeting all requirements of the NSP (e.g. use of a signature activation module). 2) A Normalized SSAS Policy (NSP) which meets general recognized best practice for TSPs operating a remote SCDev used in support of any type of transaction. 3) An EU SSAS v2 Policy (EUSPv2) which offers the same quality as that offered by the NSP but with specific requirements from the Regulation (EU) 2024/1183 [i.11] amending Regulation (EU) No 910/2014 [i.1] related to remote QSCD management. NOTE: EUSPv2 specific requirements are defined in Annex A. A SP is not necessarily part of the SSASP's documentation (as per ETSI EN 319 401 [1] a practice statement and general terms and conditions are sufficient); e.g. a SP can be shared by a community and not owned by the SSASP. Also, the present document does not put constraints on the form of the SP; a SP can be a stand-alone document or be provided as part of the practice statement and/or the general terms and conditions.",
        'tipo_principio': 'definitorio',
        'stato': 'vigente',
        'oggetti_giuridici': ['dispositivo qualificato di creazione di firma elettronica', 'dispositivo qualificato di creazione di sigillo elettronico'],
    },
    {
        'riferimento': 'clausola 4.3.3 (Terms and conditions)',
        'testo': "In aggiunta, o come parte, della SP e della SSAS practice statement, un TSP emette termini e condizioni, che possono coprire un'ampia gamma di condizioni commerciali o tecniche e sono specifici del SSASP. I destinatari dei termini e condizioni sono sottoscrittori e parti facenti affidamento. La presenza di alcuni elementi e' obbligatoria nei termini e condizioni come richiesto dal documento; tuttavia il documento non pone restrizioni sulla loro forma: possono essere un documento autonomo per un pubblico generico, oppure essere ripartiti tra accordo/i col sottoscrittore e informazioni per le parti facenti affidamento. La forma e il contenuto dei termini e condizioni possono anche dipendere dalle normative nazionali.",
        'testo_integrale': "4.3.3 Terms and conditions In addition to, or as part of, the SCP and the SSAS practice statement, a TSP issues terms and conditions. Terms and conditions can cover a broad range of commercial terms or technical terms. The terms and conditions are specific to a SSASP. The recipients of the terms and conditions are subscribers and relying parties. NOTE: The presence of some elements is mandatory in the terms and conditions as requested in the present document, however the present document places no restriction on the form of terms and conditions; it can be a standalone document for a public audience, or it can be split over subscriber's agreement(s) and information to relying parties. The form and content of the terms and conditions can also depend on national regulations.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 4.4 (SSAS component services)',
        'testo': "Il documento non impone alcuna suddivisione dei servizi di un TSP; i requisiti sono enunciati nelle clausole successive. I servizi SSAS sono suddivisi, ai fini della classificazione dei requisiti, nei seguenti servizi componenti: servizio di generazione della chiave di firma (genera le chiavi di firma nel dispositivo remoto; la prova del possesso delle chiavi generate e' trasmessa al servizio di registrazione del TSP che emette il certificato associato); servizio di collegamento del certificato (collega i certificati generati dal servizio di generazione certificati di un TSP con le corrispondenti chiavi di firma); servizio di collegamento del mezzo di identificazione elettronica/identita' (collega un riferimento al mezzo di identificazione elettronica o un'identita' con le corrispondenti chiavi di firma per fornire il sole control; la seconda possibilita' e' applicabile solo nel caso di una chiave di firma monouso in cui si assicura che l'identita' nel certificato sia la stessa del firmatario; il servizio puo' essere usato a supporto del requisito REG-6.3.1-01 di ETSI EN 319 411-1 per un TSP che emette certificati, ad es. fornendo un'attestazione dell'autenticazione del firmatario collegata alla chiave privata); servizio di attivazione della firma (verifica i dati di attivazione della firma e attiva la corrispondente chiave di firma per creare una firma digitale); servizio di cancellazione della chiave di firma (distrugge le chiavi di firma in modo da assicurare che non possano piu' essere usate); servizio di fornitura del mezzo di identificazione elettronica (opzionale; prepara e fornisce o rende disponibile il mezzo di identificazione elettronica ai firmatari, ad es. generando la chiave di autenticazione e distribuendola al soggetto del certificato, incluse chiavi 'soft' protette da ambiente software, oppure preparando il dispositivo di autenticazione e i codici di attivazione e distribuendoli al soggetto del certificato, incluse chiavi protette da ambiente hardware). Questa suddivisione dei servizi ha finalita' esclusivamente di chiarimento dei requisiti di policy e non pone restrizioni ad alcuna suddivisione dell'implementazione dei servizi del TSP. La Figura 1 illustra le interrelazioni tra i componenti di servizio del documento e le relazioni con componenti esterni del TSP che emette i certificati di firma. La Figura 2 illustra le interrelazioni tra i servizi del documento e le relazioni con un processo di autenticazione delegato a una parte esterna. La Figura 3 illustra la suddivisione dei componenti SSAS per chiavi di firma monouso con identity proofing senza uso di mezzi di identificazione elettronica. Nel caso di una chiave di firma monouso, la chiave e' cancellata direttamente dopo l'uso, non sulla base di una revoca; la CA puo' comunque fornire un servizio di revoca e di stato di certificazione, ma questi non sono piu' collegati alla gestione del (Q)SCD. Le Figure 1, 2 e 3 hanno finalita' puramente illustrativa e non rappresentano un flusso di processo. La clausola 6 specifica i requisiti specifici per ciascuno dei servizi.",
        'testo_integrale': '4.4 SSAS component services NOTE 1: The present document does not mandate any subdivision of the services of a TSP. Requirements are stated in subsequent clauses. The SSAS services are broken down in the present document into the following component services for the purposes of classifying requirements: - Signing key generation service: generates signing keys in the remote device. The proof of possession of generated signing keys are passed to the registration service of the TSP issuing the associated certificate. - Certificate linking service: links the certificates generated by the certificate generation service of a TSP with the corresponding signing keys. - eID means / identity linking service: links either an eID means references or an identity with the corresponding signing keys in order to provide sole control. The second possibility is only applicable in case of a one-time signing key where it is assured that the identity in the certificate is the same as the one of the signer. The service can be used to support requirement REG-6.3.1-01 in ETSI EN 319 411-1 [2] for a TSP issuing certificates. EXAMPLE 1: By providing an assertion of the authentication of the signer that is linked to the private key. - Signature activation service: verifies the signature activation data and activates the corresponding signing key in order to create a digital signature. - Signing key deletion service: destroys signing keys in a way that ensures that the signing keys cannot be used anymore. - eID means provision service (optional): prepares and provides or makes eID means available to the signers. EXAMPLE 2: A service which generates the authentication key and distributes the key to the subject of the certificate (this includes "soft" keys i.e. keys protected by software environment). A service which prepares the authentication device and enabling codes, and distributes them to the subject of the certificate (this includes keys protected by hardware environment). This subdivision of services is only for the purposes of clarification of policy requirements and places no restrictions on any subdivision of an implementation of the TSP\'s services. Figure 1 illustrates the interrelationships between the service components of the present document and relations with external components of the TSP issuing the signing certificates. Figure 1: Illustration of subdivision of SSAS components Figure 2 illustrates the interrelationships between the services of the present document and relations with an authentication process delegated to an external party. Figure 2: Illustration of subdivision of SSAS components with delegated authentication Figure 3: Illustration of subdivision of SSAS components for one-time signing keys with identity proofing without usage of eID means NOTE 2: In the case of a one-time signing key, the key is deleted directly after the usage, not based on a revocation. The CA can still provide a revocation service and certification status service, but they are not linked to the (Q)SCD management anymore. NOTE 3: Figures 1, 2 and 3 are for illustrative purposes and do not show a processing flow. Clause 6 specifies the specific requirements for each of the services.',
        'tipo_principio': 'definitorio',
        'stato': 'vigente',
        'oggetti_giuridici': ['dispositivo qualificato di creazione di firma elettronica', 'dispositivo qualificato di creazione di sigillo elettronico'],
    },
    {
        'riferimento': 'clausola 5.2 (SP name and identification)',
        'testo': "I SSASP conformi al documento possono dichiarare la conformita' tramite il seguente OID di trust service policy specifico: a) LSP (Lightweight SSAS Policy): itu-t(0) identified-organization(4) etsi(0) SIGNATURE CREATION SERVICE-policies(19431) ops(1) policy-identifiers(1) lightweight(1); b) NSP (Normalized SSAS Policy): itu-t(0) identified-organization(4) etsi(0) SIGNATURE CREATION SERVICE-policies(19431) ops(1) policy-identifiers(1) normalized(2). L'Annex A definisce una SSAS policy aggiuntiva (EUSPv2) con requisiti specifici relativi al Regolamento (UE) n. 910/2014.",
        'testo_integrale': 'SSASPs following the present document can claim conformance to the present document via the following specific trust service policy OID: a) LSP: Lightweight SSAS Policy ```itu-t(0) identified-organization(4) etsi(0) SIGNATURE CREATION SERVICE-policies(19431) ops (1) policy-identifiers(1) lightweight (1)``` b) NSP: Normalized SSAS Policy ```itu-t(0) identified-organization(4) etsi(0) SIGNATURE CREATION SERVICE-policies(19431) ops(1) policy-identifiers(1) normalized (2)``` NOTE: Annex A defines an additional SSAS policy with specific requirements related to Regulation (EU) No 910/2014 [i.1].',
        'tipo_principio': 'definitorio',
        'stato': 'vigente',
        'oggetti_giuridici': ['dispositivo qualificato di creazione di firma elettronica', 'dispositivo qualificato di creazione di sigillo elettronico'],
    },
    {
        'riferimento': 'clausola 5.3.2 (Subscriber and signer)',
        'testo': "Nell'ambito delle presenti policy, il firmatario associato alla chiave di firma puo' essere: una persona fisica; una persona fisica identificata in associazione con una persona giuridica; una persona giuridica (che puo' essere un'organizzazione, un'unita' o un dipartimento identificato in associazione con un'organizzazione); oppure un dispositivo o sistema operato da o per conto di una persona fisica o giuridica. Il documento non pone restrizioni specifiche sulla rappresentanza legale implicata da una firma o sigillo elettronico creati usando il documento. Il rapporto tra il firmatario e il sottoscrittore e' equivalente al rapporto tra soggetto e sottoscrittore descritto in ETSI EN 319 411-1, clausola 5.4.2.",
        'testo_integrale': '5.3.2 Subscriber and signer In the framework of the present policies, the signer associated to the signing key can be: - a natural person; - a natural person identified in association with a legal person; - a legal person (that can be an organization or a unit or a department identified in association with an organization); or - a device or system operated by or on behalf of a natural or legal person. NOTE: The present document does not place any specific restrictions on the legal representation implied by an electronic signature or seal created using the present document. The relationship between the signer and the subscriber is equivalent to the relationship between subject and subscriber as described in ETSI EN 319 411-1 [2], clause 5.4.2.',
        'tipo_principio': 'definitorio',
        'stato': 'vigente',
        'oggetti_giuridici': ['dispositivo qualificato di creazione di firma elettronica', 'dispositivo qualificato di creazione di sigillo elettronico'],
    },
    {
        'riferimento': 'clausola 6.4.7 (Key changeover)',
        'testo': "La clausola 'Key changeover' non prevede alcun requisito di policy.",
        'testo_integrale': '6.4.7 Key changeover No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.6 (Compliance audit and other assessment)',
        'testo': "La clausola rinvia interamente a ETSI EN 319 403 per i requisiti di audit di conformita' e altre forme di valutazione.",
        'testo_integrale': '6.6 Compliance audit and other assessment NOTE: See ETSI EN 319 403 [i.3].',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.7.1 (Fees)',
        'testo': "Questi requisiti di policy non intendono implicare alcuna restrizione sull'addebito dei servizi del TSP.",
        'testo_integrale': "6.7.1 Fees These policy requirements are not meant to imply any restrictions on charging for TSP's services.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.7.2 (Financial responsibility)',
        'testo': "Il requisito OVR-6.7.2-01 e' soppresso (Void); la responsabilita' finanziaria e' coperta dalla clausola 6.8.1 del documento tramite il requisito OVR-6.8.1-01.",
        'testo_integrale': '6.7.2 Financial responsibility OVR-6.7.2-01: Void. NOTE: Financial responsibility is covered in clause 6.8.1 of the present document by OVR-6.8.1-01.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.7.3 (Confidentiality of business information)',
        'testo': "La clausola 'Confidentiality of business information' non prevede alcun requisito di policy.",
        'testo_integrale': '6.7.3 Confidentiality of business information No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.7.5 (Intellectual property rights)',
        'testo': "La clausola 'Intellectual property rights' non prevede alcun requisito di policy.",
        'testo_integrale': '6.7.5 Intellectual property rights No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.7.6 (Representations and warranties)',
        'testo': "Le dichiarazioni e garanzie sono coperte dalla clausola 6.5.4 del documento tramite il requisito OVR-6.5.4-01, che copre anche i requisiti REQ-7.14.3-01X e REQ-7.14.3-02X di ETSI EN 319 401. Il SSASP ha la responsabilita' della conformita' alle procedure prescritte in questa policy, anche quando la funzionalita' del SSASP e' svolta da fornitori esterni (outsourcer).",
        'testo_integrale': "6.7.6 Representations and warranties NOTE 1: Representations and warranties is covered in clause 6.5.4 of the present document by OVR-6.5.4-01 which covers also REQ-7.14.3-01X and REQ-7.14.3-02X identified in ETSI EN 319 401 [1]. NOTE 2: The SSASP has the responsibility for conformance with the procedures prescribed in this policy, even when the SSASP's functionality is undertaken by outsourcers.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.7.7 (Disclaimers of warranties)',
        'testo': 'Per le esclusioni di garanzia si rinvia alla clausola 6.7.6.',
        'testo_integrale': '6.7.7 Disclaimers of warranties See clause 6.7.6.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.7.8 (Limitations of liability)',
        'testo': "Le limitazioni di responsabilita' sono coperte dai termini e condizioni ai sensi della clausola 6.8.4.",
        'testo_integrale': '6.7.8 Limitations of liability Limitations on liability are covered in the terms and conditions as per clause 6.8.4.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.7.9 (Indemnities)',
        'testo': "La clausola 'Indemnities' non prevede alcun requisito di policy.",
        'testo_integrale': '6.7.9 Indemnities No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.7.10 (Term and termination)',
        'testo': "La clausola 'Term and termination' non prevede alcun requisito di policy.",
        'testo_integrale': '6.7.10 Term and termination No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.7.11 (Individual notices and communications with participants)',
        'testo': "La clausola 'Individual notices and communications with participants' non prevede alcun requisito di policy.",
        'testo_integrale': '6.7.11 Individual notices and communications with participants No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.7.12 (Amendments)',
        'testo': "La clausola 'Amendments' non prevede alcun requisito di policy.",
        'testo_integrale': '6.7.12 Amendments No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.7.13 (Dispute resolution procedures)',
        'testo': "Il requisito OVR-6.7.13-01 e' soppresso (Void); le procedure di risoluzione delle controversie sono coperte dalle clausole 6.8.1 e 6.8.1 del documento tramite OVR-6.8.1-01 e OVR-6.8.4-04 (testo della fonte ufficiale riportato letteralmente, incluso il doppio riferimento alla stessa clausola 6.8.1).",
        'testo_integrale': '6.7.13 Dispute resolution procedures OVR-6.7.13-01: Void. NOTE: Dispute resolution procedures is covered in clause 6.8.1 and 6.8.1 of the present document by OVR-6.8.1-01 and OVR-6.8.4-04.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.7.14 (Governing law)',
        'testo': "La legge applicabile (governing law) non rientra nell'ambito del documento.",
        'testo_integrale': '6.7.14 Governing law Not in the scope of the present document.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.7.16 (Miscellaneous provisions)',
        'testo': "La clausola 'Miscellaneous provisions' non prevede alcun requisito di policy.",
        'testo_integrale': '6.7.16 Miscellaneous provisions No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'clausola 6.8.2 (Additional testing)',
        'testo': "La clausola 'Additional testing' non prevede alcun requisito di policy.",
        'testo_integrale': '6.8.2 Additional testing No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    'clausola 1 (Scope)',
    'clausola 3.1 (Terms)',
    'clausola 3.3 (Abbreviations)',
    'clausola 3.4 (Notations)',
    'clausola 4.1 (General policy requirements concepts)',
    'clausola 4.3.1 (SSAS practice statement)',
    'clausola 4.3.2 (SSAS policy)',
    'clausola 4.3.3 (Terms and conditions)',
    'clausola 4.4 (SSAS component services)',
    'OVR-5.1-01',
    'OVR-5.1-02',
    'OVR-5.1-03',
    'clausola 5.2 (SP name and identification)',
    'OVR-5.2-01',
    'OVR-5.3.1-01',
    'clausola 5.3.2 (Subscriber and signer)',
    'OVR-6.1-01',
    'OVR-6.1-02',
    'OVR-6.1-03',
    'OVR-6.1-04',
    'GEN-6.2.1-01',
    'GEN-6.2.1-02',
    'GEN-6.2.1-02A',
    'GEN-6.2.1-03',
    'GEN-6.2.1-04',
    'GEN-6.2.1-05',
    'GEN-6.2.1-06',
    'GEN-6.2.1-07',
    'GEN-6.2.1-08',
    'GEN-6.2.1-09',
    'LNK-6.2.2-00',
    'LNK-6.2.2-01A',
    'LNK-6.2.2-02A',
    'LNK-6.2.2-02B',
    'LNK-6.2.2-02C',
    'LNK-6.2.2-02D',
    'LNK-6.2.2-02E',
    'LNK-6.2.2-03A',
    'LNK-6.2.2-03B',
    'LNK-6.2.2-04',
    'LNK-6.2.2-05',
    'LNK-6.2.2-06',
    'LNK-6.2.2-07A',
    'LNK-6.2.2-08',
    'LNK-6.2.2-08A',
    'LNK-6.2.2-09',
    'LNK-6.2.2-10A',
    'LNK-6.2.3-01',
    'LNK-6.2.3-02',
    'LNK-6.2.3-03',
    'EID-6.2.4-01',
    'EID-6.2.4-02',
    'SIG-6.3.1-01',
    'SIG-6.3.1-02',
    'SIG-6.3.1-03',
    'SIG-6.3.1-04',
    'SIG-6.3.1-05',
    'SIG-6.3.1-06',
    'SIG-6.3.1-07',
    'SIG-6.3.1-08',
    'SIG-6.3.1-09',
    'SIG-6.3.1-10',
    'SIG-6.3.1-11',
    'SIG-6.3.1-12',
    'SIG-6.3.1-13',
    'SIG-6.3.1-14',
    'SIG-6.3.1-15',
    'SIG-6.3.1-16',
    'DEL-6.3.2-01',
    'DEL-6.3.2-02',
    'DEL-6.3.2-03',
    'DEL-6.3.2-04',
    'DEL-6.3.2-05',
    'GEN-6.3.3-01',
    'GEN-6.3.3-02',
    'GEN-6.3.3-03',
    'GEN-6.3.3-04',
    'OVR-6.4.1-01',
    'OVR-6.4.2-01',
    'OVR-6.4.2-02',
    'OVR-6.4.3-01A',
    'OVR-6.4.4-01',
    'OVR-6.4.5-01',
    'OVR-6.4.5-02',
    'OVR-6.4.5-03',
    'OVR-6.4.5-04',
    'OVR-6.4.5-05',
    'OVR-6.4.5-06',
    'OVR-6.4.5-07',
    'OVR-6.4.6-01',
    'clausola 6.4.7 (Key changeover)',
    'OVR-6.4.8-01',
    'OVR-6.4.9-01',
    'OVR-6.5.1-01',
    'OVR-6.5.2-01',
    'OVR-6.5.2-02',
    'OVR-6.5.3-01A',
    'OVR-6.5.3-02',
    'OVR-6.5.4-01',
    'OVR-6.5.5-01',
    'clausola 6.6 (Compliance audit and other assessment)',
    'clausola 6.7.1 (Fees)',
    'clausola 6.7.2 (Financial responsibility)',
    'clausola 6.7.3 (Confidentiality of business information)',
    'OVR-6.7.4-01',
    'clausola 6.7.5 (Intellectual property rights)',
    'clausola 6.7.6 (Representations and warranties)',
    'clausola 6.7.7 (Disclaimers of warranties)',
    'clausola 6.7.8 (Limitations of liability)',
    'clausola 6.7.9 (Indemnities)',
    'clausola 6.7.10 (Term and termination)',
    'clausola 6.7.11 (Individual notices and communications with participants)',
    'clausola 6.7.12 (Amendments)',
    'clausola 6.7.13 (Dispute resolution procedures)',
    'clausola 6.7.14 (Governing law)',
    'OVR-6.7.15-01',
    'clausola 6.7.16 (Miscellaneous provisions)',
    'OVR-6.8.1-01',
    'clausola 6.8.2 (Additional testing)',
    'OVR-6.8.3-01',
    'OVR-6.8.4-01',
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ('principio', None, 'clausola 6.7.2 (Financial responsibility)'),
        "nodo_a": ('obbligo', None, 'OVR-6.8.1-01'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.95,
    },
    {
        "nodo_da": ('principio', None, 'clausola 6.7.6 (Representations and warranties)'),
        "nodo_a": ('obbligo', None, 'OVR-6.5.4-01'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.95,
    },
    {
        "nodo_da": ('principio', None, 'clausola 6.7.7 (Disclaimers of warranties)'),
        "nodo_a": ('principio', None, 'clausola 6.7.6 (Representations and warranties)'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.95,
    },
    {
        "nodo_da": ('principio', None, 'clausola 6.7.8 (Limitations of liability)'),
        "nodo_a": ('obbligo', None, 'OVR-6.8.4-01'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.9,
    },
    {
        "nodo_da": ('principio', None, 'clausola 6.7.13 (Dispute resolution procedures)'),
        "nodo_a": ('obbligo', None, 'OVR-6.8.1-01'),
        "tipo_relazione": 'richiama',
        "evidence_type": 'textual',
        "confidence": 0.85,
    },
]
