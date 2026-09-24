"""Estrazione granulare ETSI EN 319 411-2 V2.6.1 (2025-06) — Capitolo 2:
clausola 5 (General provisions on Certification Practice Statement and
Certificate Policies: 5.1-5.5, incl. 5.5.1-5.5.7 una per ciascuna delle 7
certificate policy per certificati qualificati EU) e clausola 6 (Trust
Service Providers practice: 6.1-6.9 con tutti i sottoparagrafi).

Fonte 18 (assegnata dalla sessione principale, non ancora scritta in Neo4j
al momento di questa estrazione — questo modulo NON tocca seed.py). Testo
ufficiale in app/.source_cache/etsi_319_411_2/cap02.txt. Manifest di split:
app/.source_cache/etsi_319_411_2/manifest.json.

Modellazione (ADR-0007), stesso criterio già applicato a ETSI EN 319 401
(fonte 10) e ETSI TS 119 461 (fonte 9) per un documento tecnico ETSI a
clausole/requisiti numerati, con un adattamento specifico al pattern di
EN 319 411-2 (documento "overlay" che quasi ovunque richiama per
equivalenza le clausole omologhe di EN 319 411-1 con testo del tipo "The
requirements identified in ETSI EN 319 411-1 [2], clause X.Y shall
apply", aggiungendo requisiti particolari propri dei certificati
qualificati EU):

REGOLA GENERALE: un nodo Obbligo per ogni identificatore di requisito
numerato che compare nel testo (prefisso a 3 lettere + clausola + numero,
es. OVR-5.1-01, REG-6.2.2-02, SDP-6.3.5-08, GEN-6.3.3-02, CSS-6.3.10-05,
REV-6.3.9-01), incluse le frasi di mera equivalenza/rinvio a EN 319 411-1
("the requirements identified in [...] shall apply") — anche quando
l'intero contenuto normativo del nodo consiste nel solo rinvio, il nodo va
comunque censito (istruzione 8 del task): è così che 411-2 costruisce le
sue policy QCP sopra le NCP/NCP+ di 411-1. Nessuna relazione viene creata
verso questi rinvii (vincolo di fase, vedi sotto), nemmeno quando il
rinvio è esplicito e puntuale.

SOTTOCLAUSOLE SENZA ID PROPRIO -> Principio: quando un titolo di
sottoclausola è seguito da testo puramente dichiarativo/di rinvio privo di
un proprio identificativo REQ (es. "5.4.2 Subscriber and subject ETSI EN
319 411-1 [2], clause 5.4.2 applies.", "6.2.1 Naming See ETSI EN 319 411-1
[2], clause 6.2.1.", "6.3.11 End of Subscription No policy requirement.",
"6.8.5 Intellectual Property Rights No policy requirement.", "6.5.8
Time-stamping NOTE: Not in the scope of the present document."), il nodo è
un Principio, non un Obbligo: non c'è un "shall"/"should" imposto da
*questo* documento, solo un rinvio o l'assenza di un requisito di policy
proprio. 27 nodi di questo tipo in questo capitolo, riferimento simbolico
"clausola X.Y" (premessa/etichetta) quando non esiste un identificativo
REQ testuale a cui agganciarsi. tipo_principio:
- "definitorio" per la clausola 5.3 (Certificate Policy name and
  identification): nomina e identifica con OID le 7 certificate policy
  QCP-n/QCP-l/QCP-n-qscd/QCP-l-qscd/QEVCP-w/QNCP-w/QNCP-w-gen — è una
  clausola di naming/identificazione, non un requisito comportamentale.
- "scopo/ambito di applicazione" per le 7 sottoclausole 5.5.1-5.5.7
  (Certificate Usage: ciascuna descrive l'uso/ambito di applicazione
  previsto per una specifica certificate policy, es. "Certificates issued
  under these requirements are aimed to support...") e per le due
  dichiarazioni esplicite di esclusione dall'ambito del documento (6.5.8
  Time-stamping, 6.8.14 Governing Law: "Not in the scope of the present
  document.").
- "altro" per tutte le altre premesse/rinvii/etichette senza contenuto
  prescrittivo proprio: 5.1 (premessa RFC 3647), 5.4.1 (premessa
  "concepts apply", distinta dal successivo OVR-5.4.1-01 che invece
  richiama i "requirements" — vedi sotto), 5.4.2, 6.2.1, 6.3.11, 6.4.7,
  6.7, 6.8.1/6.8.3/6.8.5/6.8.7/6.8.8/6.8.9/6.8.10/6.8.11/6.8.12/6.8.16, e
  tutti i requisiti "Void" (vedi sotto).

REQUISITI "Void": 12 identificatori REQ numerati nel testo (REG-6.3.6-01,
REG-6.3.8-01, OVR-6.4.5-02, OVR-6.4.5-04, OVR-6.4.5-05, SDP-6.4.5-06,
SDP-6.5.1-07, GEN-6.6.1-06, OVR-6.8.6-02, OVR-6.8.6-03, OVR-6.8.6-04a,
OVR-6.8.6-04b) sono interamente "Void" nel testo ufficiale — un requisito
identificato da un id ma soppresso/non più in vigore in questa versione
del documento. Modellati come Principio "altro" (non Obbligo: non
impongono alcun comportamento, anzi dichiarano l'assenza di un requisito),
riferimento = l'id stesso (es. "Parte 2: REG-6.3.6-01"), non uno pseudo-riferimento
"clausola X" — restano comunque un nodo per id numerato, come richiesto
dalla copertura completa. OVR-6.4.5-05 porta con sé, nel testo ufficiale,
una NOTE che cita per esteso l'art. 24.2(h) del Regolamento (UE) 910/2014
(motivo sostanziale per cui il requisito specifico è stato ritenuto
superfluo/soppresso): mantenuta in testo_integrale.

ELENCHI LETTERATI/PUNTATI SENZA ID PROPRIO PER VOCE: restano un solo nodo
(istruzione generale), es. OVR-5.1-02 (2 bullet CHOICE NCP/NCP+),
REG-6.2.2-02/03 (liste a)/b) di modalità di verifica), REG-6.2.2-04 (2
bullet CHOICE), GEN-6.3.3-02 e GEN-6.6.1-05 (7 bullet CHOICE, uno per
policy, identificatori di clausola 5.3), CSS-6.3.10-12 (lista a)/b)/c)),
clausola 5.3 stessa (lista a)-g) degli OID delle 7 policy, un solo
Principio "definitorio"). Quando invece un paragrafo introduttivo porta un
proprio id E il paragrafo che segue elenca voci con id propri distinti
(es. OVR-6.3.5-01 "Where the TSP manages the QSCD..." seguito da
SDP-6.3.5-02..06 con id propri), il paragrafo introduttivo resta comunque
un nodo a sé (ha contenuto prescrittivo proprio: "the general obligations
[...] shall apply"). Le etichette pure senza id e senza contenuto proprio
che introducono un elenco di voci con id propri ("Subscriber's
obligations:", "Notice to Relying Party:", "Where CRLs are used to
provide revocation status information [...]:" in 6.3.10, "Where OCSP is
used [...]:" in 6.3.10) NON generano un nodo a sé — sono pura punteggiatura
di sezione, non testo normativo.

NOTE informative: mantenute in testo_integrale quando aggiungono contenuto
interpretativo/tecnico sostanziale (es. OVR-5.4.1-01 — responsabilità del
QTSP ex art. 24 Regolamento; REG-6.2.2-02 NOTE 1/2 — rischio di
impersonificazione nella verifica remota; OVR-6.3.5-12 NOTE 1-3 — EU
trusted list, ETSI TS 119 615/172-4; SDP-6.5.1-07A/07B NOTE 3/4 —
monitoraggio stato QSCD, innesco di revoca; CSS-6.3.10-05/07/10/11 —
estensioni X.509/OCSP e relativa motivazione); omesse quando sono puro
rimando bibliografico/incrociato senza contenuto interpretativo proprio
(es. REG-6.2.2-03 NOTE 3 "See notes 1 and 2 above"; 6.3.1 NOTE "See also
clause 6.2.2"; GEN-6.6.1-07 NOTE "The rationales [...] are provided in
clause 4"; clausola 5.3 NOTE "See clause 4.2.2 for a general description
of the above policies") — mai sostituite da marcatori di elisione.

CASI PARTICOLARI verbatim (refusi/incongruenze del testo ufficiale,
riportati letteralmente senza correzione):
- REG-6.3.7-02 [QEVCP-w] cita testualmente "clause 6.3.6" (non 6.3.7) per
  i requisiti da cui deroga — refuso evidente nel testo ufficiale ETSI,
  mantenuto com'è in testo_integrale.
- REG-6.3.8-03 [QEVCP-w] ha una formulazione contorta ("except REG
  6.3.6-06 and REG 6.3.6-07 as referenced in ETSI EN 319 411-1 [2] through
  requirement REG-6.3.8-01A reference to clause 6.3.6") — riportata
  letteralmente; REG-6.3.8-01A e REV-6.3.9-02 sono id citati per rinvio
  interno a EN 319 411-1, non nodi propri di questo capitolo.
- SDP-6.5.1-07B NOTE 4 cita REV-6.3.9-02 b) di EN 319 411-1 (non un id
  proprio di 411-2) come innesco di revoca per perdita di stato QSCD.

tipo_obbligo: assegnato per dominio sostanziale della clausola richiamata,
stesso criterio di ETSI TS 119 461: "organizzativo" per 5.1/5.2/5.3
(equivalenza)/5.4/6.4 (Facility/Management/Personnel/Audit/Archival/
Disaster Recovery/Termination)/6.8.2/6.8.4/6.8.6/6.8.15/6.9.1/6.9.3;
"procedurale" per 6.2 (identificazione/autenticazione)/6.3.1-6.3.4/
6.3.6-6.3.9/6.3.10 lettera CSS-6.3.10-12 (che però è
"informativo/trasparenza", vedi sotto)/6.8.13; "tecnico/sicurezza" per
6.3.5 (uso di chiave/QSCD)/6.3.10 (CRL/OCSP salvo -12/-13)/6.3.12/6.5
(Technical Security Controls)/6.6 (profili certificato/CRL/OCSP)/6.9.2
(additional testing); "informativo/trasparenza" per 6.1 (Publication and
Repository)/OVR-6.3.5-12 (avviso alle relying party)/CSS-6.3.10-12/13
(documentazione verso l'esterno)/SDP-6.5.1-07B (documentazione in CPS)/6.9.4
(Terms and conditions, PKI disclosure statement).

condizione_applicabilita: valorizzata per tutti i nodi marcati
[CONDITIONAL]/[CHOICE] o con tag di policy esplicito ([QCP-n],
[QCP-n-qscd], [except QEVCP-w] ecc.), con sintesi breve della condizione o
della policy a cui il requisito è ristretto; marcatura mantenuta in
testo_integrale, omessa dal solo riferimento (istruzione 6).

RELAZIONI: vuoto per vincolo di fase — nessuna relazione, né interna al
capitolo né verso EN 319 411-1 (fonte 17) nonostante il testo di questo
capitolo sia quasi interamente costituito da rinvii espliciti a clausole
di EN 319 411-1 (istruzione esplicita del task). Verrà popolato dalla
pipeline cross-fonte dedicata (ADR-0009) in una sessione successiva.

Conteggio: 110 Obblighi, 39 Principi, 149 item di indice totali (verificato
1:1 con tutti gli identificativi di requisito numerati effettivamente
presenti nel testo di questo capitolo via controllo automatico per
regex nella sessione di estrazione).
"""

RIGHE_OBBLIGHI = [
    {
        'riferimento': 'Parte 2: OVR-5.1-01',
        'testo': 'Si applicano i requisiti generali di cui alla clausola 5.1 di ETSI EN 319 411-1.',
        'testo_integrale': 'OVR-5.1-01: The general requirements specified in ETSI EN 319 411-1 [2], clause 5.1 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-5.1-02',
        'testo': 'Per le policy QCP-n e QCP-l: se le condizioni del TSP non richiedono un dispositivo crittografico sicuro, si applicano i requisiti NCP di EN 319 411-1; se li richiedono, si applicano i requisiti NCP+. Dove un requisito NCP/NCP+ è specificato diversamente per persona fisica o giuridica, si applica di conseguenza a QCP-n o QCP-l.',
        'testo_integrale': "OVR-5.1-02 [QCP-n] and [QCP-l] [CHOICE]: - If the TSP's terms and conditions do not require a secure cryptographic device, all requirements defined for NCP in ETSI EN 319 411-1 [2] shall apply. Where a requirement for NCP is specified differently for natural person or legal person respectively, such requirement shall apply for QCP-n or QCP-l accordingly. - If the TSP's terms and conditions require a secure cryptographic device all requirements defined for NCP+ in ETSI EN 319 411-1 [2] shall apply. Where a requirement for NCP+ is specified differently for natural person or legal person respectively, such requirement shall apply for QCP-n or QCP-l accordingly.",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n e QCP-l; scelta tra requisiti NCP o NCP+ di EN 319 411-1 a seconda che le condizioni del TSP richiedano o meno un dispositivo crittografico sicuro',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-5.1-03',
        'testo': "Per la policy QEVCP-w si applicano tutti i requisiti definiti per EVCP in EN 319 411-1, il che implica la conformità con l'ultima versione della EVCG.",
        'testo_integrale': 'OVR-5.1-03 [QEVCP-w]: All requirements defined for [EVCP] in ETSI EN 319 411-1 [2] shall apply. NOTE 1: This implies compliance with the latest version of EVCG [i.7].',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica alla policy QEVCP-w',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-5.1-04',
        'testo': 'Per la policy QCP-n-qscd si applicano tutti i requisiti QCP-n, inclusi tutti i requisiti NCP+ di EN 319 411-1; dove un requisito NCP+ è specificato diversamente per persona fisica o giuridica, si applica quello per persona fisica.',
        'testo_integrale': 'OVR-5.1-04 [QCP-n-qscd]: All requirements defined for [QCP-n], including all requirements defined for NCP+ in ETSI EN 319 411-1 [2], shall apply. Where a requirement for NCP+ is specified differently for natural person or legal person respectively, the requirement for natural person shall apply for QCP-n-qscd.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica alla policy QCP-n-qscd',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-5.1-05',
        'testo': 'Per la policy QCP-l-qscd si applicano tutti i requisiti QCP-l, inclusi tutti i requisiti NCP+ di EN 319 411-1; dove un requisito NCP+ è specificato diversamente per persona fisica o giuridica, si applica quello per persona giuridica.',
        'testo_integrale': 'OVR-5.1-05 [QCP-l-qscd]: All requirements defined for [QCP-l], including all requirements defined for NCP+ in ETSI EN 319 411-1 [2], shall apply. Where a requirement for NCP+ is specified differently for natural person or legal person respectively, the requirement for legal person shall apply for QCP-l-qscd.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica alla policy QCP-l-qscd',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-5.1-06',
        'testo': 'Per le policy QNCP-w e QNCP-w-gen si applicano tutti i requisiti definiti per NCP in EN 319 411-1.',
        'testo_integrale': 'OVR-5.1-06 [QNCP-w], [QNCP-w-gen]: All requirements defined for NCP in ETSI EN 319 411-1 [2] shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica alle policy QNCP-w e QNCP-w-gen',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-5.1-07',
        'testo': 'Per la policy QNCP-w-gen si applicano tutti i requisiti contrassegnati come [WEB] in EN 319 411-1.',
        'testo_integrale': 'OVR-5.1-07 [QNCP-w-gen]: All requirements tagged as [WEB] in ETSI EN 319 411-1 [2] shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica alla policy QNCP-w-gen',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-5.1-08',
        'testo': "Per la policy QNCP-w si applicano tutti i requisiti definiti per IVCP o OVCP in EN 319 411-1, il che implica la conformità con l'ultima versione della BRG.",
        'testo_integrale': 'OVR-5.1-08 [QNCP-w]: All requirements defined for [IVCP] or [OVCP] in ETSI EN 319 411-1 [2] shall apply. NOTE 2: This implies compliance with the latest version of BRG [i.3].',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica alla policy QNCP-w',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-5.1-09',
        'testo': 'Per le policy QNCP-w e QEVCP-w, in caso di conflitto tra i requisiti del presente documento e le ultime versioni di BRG o EVCG, prevalgono i requisiti BRG o EVCG.',
        'testo_integrale': "OVR-5.1-09 [QNCP-w], [QEVCP-w]: [CONDITIONAL]: In case of conflict between the present document's requirements and the latest versions of BRG or EVCG, the BRG or EVCG requirements shall take precedence. NOTE 3: Implications of the above condition do not constitute non-conformities against the ETSI certificate policies defined by the present document.",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QNCP-w e QEVCP-w in caso di conflitto tra i requisiti del presente documento e le versioni più recenti di BRG o EVCG',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-5.2-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 5.2 di ETSI EN 319 411-1 (Certification Practice Statement Requirements).',
        'testo_integrale': 'OVR-5.2-01: The requirements identified in ETSI EN 319 411-1 [2], clause 5.2 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-5.3-01',
        'testo': 'Si applica il requisito di cui alla clausola 5.3 di ETSI EN 319 411-1 (Certificate Policy name and identification).',
        'testo_integrale': 'OVR-5.3-01: The requirement identified in ETSI EN 319 411-1 [2], clause 5.3 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-5.4.1-01',
        'testo': "Si applicano i requisiti di cui alla clausola 5.4.1 di ETSI EN 319 411-1. Il Regolamento (UE) n. 910/2014 disciplina la responsabilità dei trust service provider: il TSP identificato come QTSP che emette certificati qualificati EU nella trusted list dei servizi qualificati mantiene la responsabilità complessiva per l'emissione dei certificati come richiesto dal Regolamento.",
        'testo_integrale': 'NOTE: Regulation (EU) No 910/2014 [i.1] addresses liability of trust service providers. In particular, the TSP identified as the qualified TSP issuing EU qualified certificates in the trusted list of qualified services, maintains overall responsibility for meeting liability for the issuing of certificates as required in Regulation (EU) No 910/2014 [i.1]. OVR-5.4.1-01: The requirements identified in ETSI EN 319 411-1 [2], clause 5.4.1 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-5.4.3-01',
        'testo': 'Si applica il requisito di cui alla clausola 5.4.3 di ETSI EN 319 411-1 (Others).',
        'testo_integrale': '5.4.3 Others: OVR-5.4.3-01: The requirement identified in ETSI EN 319 411-1 [2], clause 5.4.3 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.1-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.1 di ETSI EN 319 411-1 (Publication and Repository Responsibilities).',
        'testo_integrale': 'OVR-6.1-01: The requirements specified in ETSI EN 319 411-1 [2], clause 6.1 shall apply.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.2.2-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.2.2 di ETSI EN 319 411-1 (Initial Identity Validation); si applicano inoltre i requisiti particolari seguenti.',
        'testo_integrale': '6.2.2 Initial Identity Validation: REG-6.2.2-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.2.2 shall apply. In addition the following particular requirements apply:',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.2.2-02',
        'testo': "Per QCP-n e QCP-n-qscd, l'identità della persona fisica e, se applicabile, i suoi attributi specifici, devono essere verificati mediante presenza fisica, oppure con metodi che offrano un livello di affidabilità equivalente e di cui il TSP possa dimostrare l'equivalenza.",
        'testo_integrale': 'REG-6.2.2-02 [QCP-n] and [QCP-n-qscd]: The identity of the natural person and, if applicable, any specific attributes of the person, shall be verified: a) by the physical presence of the natural person; or b) using methods which provide equivalent assurance in terms of reliability to the physical presence and for which the TSP can prove the equivalence. NOTE 1: The proof of equivalence can be done according to the Regulation (EU) No 910/2014 [i.1]. NOTE 2: The proof of equivalence needs to consider the impersonation risks inherent to remote applications. In particular, an uninterrupted chain of subsequent remote registrations can increase such risks, because the person can never be actually seen for years, and/or because the traceability with the initial face to face is weakened.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica alle policy QCP-n e QCP-n-qscd',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.2.2-03',
        'testo': "Per QCP-l e QCP-l-qscd, l'identità della persona giuridica e, se applicabile, i suoi attributi specifici, devono essere verificati mediante presenza fisica di un rappresentante autorizzato della persona giuridica, oppure con metodi che offrano un livello di affidabilità equivalente e di cui il TSP possa dimostrare l'equivalenza.",
        'testo_integrale': 'REG-6.2.2-03 [QCP-l] and [QCP-l-qscd]: The identity of the legal person and, if applicable, any specific attributes of the person, shall be verified: a) by the physical presence of an authorized representative of the legal person; or b) using methods which provide equivalent assurance in terms of reliability to the physical presence of an authorized representative of the legal person and for which the TSP can prove the equivalence.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica alle policy QCP-l e QCP-l-qscd',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.2.2-04',
        'testo': "Per QEVCP-w, QNCP-w e QNCP-w-gen: se il sottoscrittore è una persona fisica, l'identità del sottoscrittore e il suo legame con il nome di dominio da certificare devono essere verificati come indicato per QCP-n; se è una persona giuridica, come indicato per QCP-l.",
        'testo_integrale': 'REG-6.2.2-04 [QEVCP-w], [QNCP-w] and [QNCP-w-gen] [CHOICE]: - if the subscriber is a natural person the identity of the subscriber and her/his link with the domain name to be certified and, if applicable, any specific attributes of the person shall be verified as indicated above for [QCP-n]; - if the subscriber is a legal person the identity of the subscriber and its link with the domain name to be certified and, if applicable, any specific attributes of the person shall be verified as indicated above for [QCP-l].',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QEVCP-w, QNCP-w e QNCP-w-gen; scelta della modalità di verifica in base al tipo di sottoscrittore (persona fisica o giuridica)',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.2.3-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.2.3 di ETSI EN 319 411-1 (Identification and authentication for Re-key requests).',
        'testo_integrale': '6.2.3 Identification and authentication for Re-key requests: REG-6.2.3-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.2.3 shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REV-6.2.4-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.2.4 di ETSI EN 319 411-1 (Identification and authentication for revocation requests).',
        'testo_integrale': '6.2.4 Identification and authentication for revocation requests: REV-6.2.4-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.2.4 shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.3.1-01',
        'testo': "Si applicano i requisiti di cui alla clausola 6.3.1 di ETSI EN 319 411-1 (Certificate Application); si veda anche la clausola 6.2.2 per la validazione dell'identità.",
        'testo_integrale': '6.3.1 Certificate Application: REG-6.3.1-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.3.1 shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.3.2-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.3.2 di ETSI EN 319 411-1 (Certificate application processing).',
        'testo_integrale': '6.3.2 Certificate application processing: REG-6.3.2-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.3.2 shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: GEN-6.3.3-01',
        'testo': 'Si applicano i requisiti da GEN-6.3.3-01 a GEN-6.3.3-11 identificati alla clausola 6.3.3 di ETSI EN 319 411-1 (Certificate issuance).',
        'testo_integrale': '6.3.3 Certificate issuance: GEN-6.3.3-01: The requirements GEN-6.3.3-01 to GEN-6.3.3-11 identified in ETSI EN 319 411-1 [2], clause 6.3.3 shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: GEN-6.3.3-02',
        'testo': "La CP identificata nel certificato deve essere, per ciascuna policy, l'identificatore definito alla clausola 5.3 e/o un OID assegnato dal TSP (o da altro stakeholder rilevante) per una certificate policy che arricchisce i corrispondenti requisiti di policy applicabili definiti nel presente documento.",
        'testo_integrale': 'GEN-6.3.3-02: The CP identified shall be [CHOICE]: - [QCP-n] -as specified in clause 5.3, item (a), and/or -an OID, allocated by the TSP, other relevant stakeholder or further standardization for a certificate policy enhancing the corresponding applicable policy requirements defined in the present document. - [QCP-l] -as specified in clause 5.3, item (b), and/or -an OID, allocated by the TSP, other relevant stakeholder or further standardization for a certificate policy enhancing the corresponding applicable policy requirements defined in the present document. - [QCP-n-qscd] -as specified in clause 5.3, item (c), and/or -an OID, allocated by the TSP, other relevant stakeholder or further standardization for a certificate policy enhancing the corresponding applicable policy requirements defined in the present document. - [QCP-l-qscd] -as specified in clause 5.3, item (d), and/or -an OID, allocated by the TSP, other relevant stakeholder or further standardization for a certificate policy enhancing the corresponding applicable policy requirements defined in the present document. - [QEVCP-w] -as specified in clause 5.3, item (e), and/or -an OID, allocated by the TSP, other relevant stakeholder or further standardization for a certificate policy enhancing the corresponding applicable policy requirements defined in the present document. - [QNCP-w] -as specified in clause 5.3, item (f), and/or -an OID, allocated by the TSP, other relevant stakeholder or further standardization for a certificate policy enhancing the corresponding applicable policy requirements defined in the present document. - [QNCP-w-gen] -as specified in clause 5.3, item (g), and/or -an OID, allocated by the TSP, other relevant stakeholder or further standardization for a certificate policy enhancing the corresponding applicable policy requirements defined in the present document.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "scelta dell'identificatore di CP in base alla policy applicata (QCP-n/QCP-l/QCP-n-qscd/QCP-l-qscd/QEVCP-w/QNCP-w/QNCP-w-gen)",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.3.4-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.3.4 di ETSI EN 319 411-1 (Certificate acceptance).',
        'testo_integrale': '6.3.4 Certificate acceptance: OVR-6.3.4-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.3.4 shall apply. In addition:',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.3.4-02',
        'testo': "Se l'accordo con il sottoscrittore è in forma elettronica, dovrebbe essere firmato con una firma elettronica avanzata o un sigillo elettronico avanzato come specificato dal Regolamento (UE) n. 910/2014.",
        'testo_integrale': 'OVR-6.3.4-02 [CONDITIONAL]: If the subscriber agreement is in electronic form, it should be signed with an Advanced Electronic Signature or an Advanced Electronic Seal as specified by Regulation (EU) No 910/2014 [i.1]. NOTE: During the process of issuance of the certificate to the subscriber confirmation of agreement can use an Advanced Electronic Signature supported by the qualified certificate being issued.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': "si applica se l'accordo con il sottoscrittore è stipulato in forma elettronica",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.3.5-01',
        'testo': 'Si applicano gli obblighi generali di cui alla clausola 6.3.5 di ETSI EN 319 411-1 (Key Pair and Certificate Usage); si applicano inoltre i requisiti seguenti quando il TSP gestisce il QSCD per conto del soggetto.',
        'testo_integrale': '6.3.5 Key Pair and Certificate Usage: OVR-6.3.5-01: The general obligations specified in ETSI EN 319 411-1 [2], clause 6.3.5 shall apply. In addition: Where the TSP manages the QSCD for the subject:',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.3.5-02',
        'testo': "Se il TSP gestisce il QSCD per il soggetto, la chiave privata non deve essere usata per firmare se non all'interno di un QSCD, per le policy QCP-n-qscd e QCP-l-qscd.",
        'testo_integrale': 'SDP-6.3.5-02 [QCP-n-qscd] and [QCP-l-qscd] [CONDITIONAL]: If the TSP manages the QSCD for the subject, the private key shall not be used for signing except within a QSCD.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n-qscd e QCP-l-qscd se il TSP gestisce il QSCD per conto del soggetto',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.3.5-03',
        'testo': 'Se il TSP gestisce il QSCD per il soggetto, la chiave privata del soggetto deve essere usata sotto il controllo esclusivo del soggetto, per la policy QCP-n-qscd.',
        'testo_integrale': "SDP-6.3.5-03 [QCP-n-qscd] [CONDITIONAL]: If the TSP manages the QSCD for the subject, the subject's private key shall be used under the subject's sole control.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n-qscd se il TSP gestisce il QSCD per conto del soggetto',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.3.5-04',
        'testo': 'Se il TSP gestisce il QSCD per il soggetto, la chiave privata del soggetto deve essere usata sotto il controllo del soggetto, per la policy QCP-l-qscd.',
        'testo_integrale': "SDP-6.3.5-04 [QCP-l-qscd] [CONDITIONAL]: If the TSP manages the QSCD for the subject, the subject's private key shall be used under the subject's control.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-l-qscd se il TSP gestisce il QSCD per conto del soggetto',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.3.5-05',
        'testo': 'Se il TSP gestisce il QSCD per il soggetto, la coppia di chiavi del soggetto dovrebbe essere usata solo per firme elettroniche, per la policy QCP-n-qscd.',
        'testo_integrale': "SDP-6.3.5-05 [QCP-n-qscd] [CONDITIONAL]: If the TSP manages the QSCD for the subject, the subject's key pair should be used only for electronic signatures.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n-qscd se il TSP gestisce il QSCD per conto del soggetto',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.3.5-06',
        'testo': 'Se il TSP gestisce il QSCD per il soggetto, la coppia di chiavi del soggetto dovrebbe essere usata solo per sigilli elettronici, per la policy QCP-l-qscd.',
        'testo_integrale': "SDP-6.3.5-06 [QCP-l-qscd]: [CONDITIONAL]: If the TSP manages the QSCD for the subject, the subject's key pair should be used only for electronic seals.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-l-qscd se il TSP gestisce il QSCD per conto del soggetto',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.3.5-07',
        'testo': 'Per QCP-n-qscd e QCP-l-qscd, gli obblighi del sottoscrittore (o del TSP che gestisce la chiave per conto del soggetto) devono richiedere che le firme digitali siano create solo da un dispositivo QSCD.',
        'testo_integrale': "OVR-6.3.5-07 [QCP-n-qscd] and [QCP-l-qscd]: The subscriber's obligations (see clause 6.3.4) (or respectively the obligations on the TSP managing the key on behalf of the subject) shall require that digital signatures are only created by a QSCD device.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n-qscd e QCP-l-qscd',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.3.5-08',
        'testo': 'Per QCP-n e QCP-n-qscd, gli obblighi del sottoscrittore (o del TSP che gestisce la chiave per conto del soggetto) devono richiedere che la chiave privata del soggetto sia mantenuta (o usata) sotto il controllo esclusivo del soggetto.',
        'testo_integrale': "SDP-6.3.5-08 [QCP-n] and [QCP-n-qscd]: The subscriber's obligations (see clause 6.3.4) (or respectively the obligations on the TSP managing the key on behalf of the subject) shall require that the subject's private key is maintained (or respectively is used) under the subject's sole control.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n e QCP-n-qscd',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.3.5-09',
        'testo': 'Per QCP-l e QCP-l-qscd, gli obblighi del sottoscrittore (o del TSP che gestisce la chiave per conto del soggetto) devono richiedere che la chiave privata del soggetto sia usata sotto il controllo del soggetto.',
        'testo_integrale': "SDP-6.3.5-09 [QCP-l] and [QCP-l-qscd]: The subscriber's obligations (see clause 6.3.4) (or respectively the obligations on the TSP managing the key on behalf of the subject) shall require that the subject's private key is used under the subject's control.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-l e QCP-l-qscd',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.3.5-10',
        'testo': 'Per QCP-n e QCP-n-qscd, gli obblighi del sottoscrittore (o del TSP che gestisce la chiave per conto del soggetto) dovrebbero raccomandare che la coppia di chiavi del soggetto sia usata solo per firme elettroniche.',
        'testo_integrale': "SDP-6.3.5-10 [QCP-n] and [QCP-n-qscd]: The subscriber's obligations (see clause 6.3.4) or the obligations on the TSP managing the key on behalf of the subject should recommend that the subject's key pair is used only for electronic signatures.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n e QCP-n-qscd',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.3.5-11',
        'testo': 'Per QCP-l e QCP-l-qscd, gli obblighi del sottoscrittore (o del TSP che gestisce la chiave per conto del soggetto) dovrebbero raccomandare che la coppia di chiavi del soggetto sia usata solo per sigilli elettronici.',
        'testo_integrale': "SDP-6.3.5-11 [QCP-l] and [QCP-l-qscd]: The subscriber's obligations (see clause 6.3.4) or the obligations on the TSP managing the key on behalf of the subject should recommend that the subject's key pair is used only for electronic seals.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-l e QCP-l-qscd',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.3.5-12',
        'testo': "L'avviso alle relying party deve informarle che, tra le condizioni per fare affidamento su un certificato come EU Qualified Certificate, l'ancora di fiducia per la validazione del certificato deve essere identificata come voce dell'EU trusted list appropriata per un QTSP.",
        'testo_integrale': 'OVR-6.3.5-12: The notice to relying parties shall inform them that, as part of the conditions for a certificate to be relied upon as an EU Qualified Certificate, the trust anchor for the validation of the certificate shall be as identified in a service digital identifier of an appropriate EU trusted list entry for a QTSP (see ETSI TS 119 612 [i.8]). NOTE 1: Technical specifications and formats for EU trusted lists are laid down in commission implementing decision (EU) 2015/1505 [i.11] pursuant to Article 22(5) of Regulation (EU) No 910/2014 [i.1]. NOTE 2: ETSI TS 119 615 [i.12] provides guidance on how to validate a digital certificate against the EU trusted lists, in order to determine whether it can be considered as an EU qualified certificate. NOTE 3: ETSI TS 119 172-4 [i.13] defines a signature validation policy describing how to validate a digital signature against the EU trusted lists, in order to determine whether it can be considered as an EU qualified electronic signature or seal.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.3.6-02',
        'testo': 'Per tutte le policy tranne QEVCP-w si applicano i requisiti di cui alla clausola 6.3.6 di ETSI EN 319 411-1 (Certificate Renewal).',
        'testo_integrale': 'REG-6.3.6-02 [except QEVCP-w]: The requirements identified in ETSI EN 319 411-1 [2], clause 6.3.6 shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a tutte le policy eccetto QEVCP-w',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.3.6-03',
        'testo': 'Per QEVCP-w si applicano i requisiti di cui alla clausola 6.3.6 di EN 319 411-1, eccetto REG 6.3.6-06 e REG 6.3.6-07, sostituiti dai requisiti seguenti.',
        'testo_integrale': 'REG-6.3.6-03 [QEVCP-w]: The requirements identified in ETSI EN 319 411-1 [2], clause 6.3.6 shall apply, except REG 6.3.6-06 and REG 6.3.6-07. Instead of them the following requirements apply:',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QEVCP-w',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.3.6-04',
        'testo': 'Le informazioni di validazione ottenute dal TSP possono essere riutilizzate se compatibili con la clausola 3.2.2.14.3 della EVCG.',
        'testo_integrale': 'REG-6.3.6-04: Validation information obtained by the TSP may be reused if compatible with clause 3.2.2.14.3 of EVCG [4].',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QEVCP-w in sostituzione di REG 6.3.6-06',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.3.6-05',
        'testo': 'Si applica la clausola 6.3.2 della EVCG, che specifica il periodo massimo di validità.',
        'testo_integrale': 'REG-6.3.6-05: Clause 6.3.2 of EVCG [4], specifying the maximum validity period, shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QEVCP-w in sostituzione di REG 6.3.6-07',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.3.7-01',
        'testo': 'Per tutte le policy tranne QEVCP-w si applicano i requisiti di cui alla clausola 6.3.7 di ETSI EN 319 411-1 (Certificate Re-key).',
        'testo_integrale': '6.3.7 Certificate Re-key: REG-6.3.7-01 [except QEVCP-w]: The requirements identified in ETSI EN 319 411-1 [2], clause 6.3.7 shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a tutte le policy eccetto QEVCP-w',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.3.7-02',
        'testo': 'Per QEVCP-w si applicano i requisiti di cui alla clausola 6.3.6 di EN 319 411-1, eccetto REG 6.3.7-05 e REG 6.3.6-06, sostituiti dai requisiti seguenti (testo ufficiale così formulato, con riferimento incrociato a clausola 6.3.6).',
        'testo_integrale': 'REG-6.3.7-02 [QEVCP-w]: The requirements identified in ETSI EN 319 411-1 [2], clause 6.3.6 shall apply, except REG 6.3.7-05 and REG 6.3.6-06. Instead of them the following requirements apply:',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QEVCP-w',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.3.7-03',
        'testo': 'Le informazioni di validazione ottenute dal TSP possono essere riutilizzate se compatibili con la clausola 3.2.2.14.3 della EVCG.',
        'testo_integrale': 'REG-6.3.7-03: Validation information obtained by the TSP may be reused if compatible with clause 3.2.2.14.3 of EVCG [4].',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QEVCP-w in sostituzione di REG 6.3.7-05',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.3.7-04',
        'testo': 'Si applica la clausola 6.3.2 della EVCG, che specifica il periodo massimo di validità.',
        'testo_integrale': 'REG-6.3.7-04: Clause 6.3.2 of EVCG [4], specifying the maximum validity period, shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QEVCP-w in sostituzione di REG 6.3.6-06',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.3.8-02',
        'testo': 'Per tutte le policy tranne QEVCP-w si applicano i requisiti di cui alla clausola 6.3.8 di ETSI EN 319 411-1 (Certificate Modification).',
        'testo_integrale': 'REG-6.3.8-02 [except QEVCP-w]: The requirements identified in ETSI EN 319 411-1 [2], clause 6.3.8 shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a tutte le policy eccetto QEVCP-w',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.3.8-03',
        'testo': 'Per QEVCP-w si applicano i requisiti di cui alla clausola 6.3.8 di EN 319 411-1, eccetto REG 6.3.6-06 e REG 6.3.6-07 come richiamati in EN 319 411-1 tramite il requisito REG-6.3.8-01A con riferimento alla clausola 6.3.6; sostituiti dai requisiti seguenti.',
        'testo_integrale': 'REG-6.3.8-03 [QEVCP-w]: The requirements identified in ETSI EN 319 411-1 [2], clause 6.3.8 shall apply, except REG 6.3.6-06 and REG 6.3.6-07 as referenced in ETSI EN 319 411-1 [2] through requirement REG-6.3.8-01A reference to clause 6.3.6. Instead of them the following requirements apply:',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QEVCP-w',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.3.8-04',
        'testo': 'Le informazioni di validazione ottenute dal TSP possono essere riutilizzate se compatibili con la clausola 3.2.2.14.3 della EVCG.',
        'testo_integrale': 'REG-6.3.8-04: Validation information obtained by the TSP may be reused if compatible with clause 3.2.2.14.3 of EVCG [4].',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QEVCP-w in sostituzione di REG 6.3.6-06',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REG-6.3.8-05',
        'testo': 'Si applica la clausola 6.3.2 della EVCG, che specifica il periodo massimo di validità.',
        'testo_integrale': 'REG-6.3.8-05: Clause 6.3.2 of EVCG [4], specifying the maximum validity period, shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QEVCP-w in sostituzione di REG 6.3.6-07',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: REV-6.3.9-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.3.9 di ETSI EN 319 411-1 (Certificate Revocation and Suspension).',
        'testo_integrale': '6.3.9 Certificate Revocation and Suspension: REV-6.3.9-01: The requirements specified in ETSI EN 319 411-1 [2], clause 6.3.9 shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.3.10 di ETSI EN 319 411-1 (Certificate Status Services); il Regolamento (UE) n. 910/2014 prevede che questo servizio sia fornito gratuitamente. Si applicano inoltre i requisiti particolari seguenti.',
        'testo_integrale': '6.3.10 Certificate Status Services: CSS-6.3.10-01: The requirements specified in ETSI EN 319 411-1 [2], clause 6.3.10 shall apply. NOTE 1: Regulation (EU) No 910/2014 [i.1] states that this service is to be provided free of charge. In addition, the following particular requirements apply:',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-02',
        'testo': 'Le informazioni sullo stato di revoca devono essere disponibili oltre il periodo di validità del certificato con almeno uno dei metodi usati durante il periodo di validità del certificato (CRL o OCSP).',
        'testo_integrale': 'CSS-6.3.10-02: Revocation status information shall be made available beyond the validity period of the certificate with at least one of the methods used during the period of validity of the certificate (i.e. CRL or OCSP).',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-02A',
        'testo': 'Un TSP può astenersi dal fornire servizi di informazione sullo stato di revoca per verificare lo stato di certificati a breve durata con validità assicurata.',
        'testo_integrale': 'CSS-6.3.10-02A: A TSP may abstain from providing revocation status information services for checking the status of validity-assured short certificates.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-02B',
        'testo': "Un certificato a breve durata con validità assicurata deve indicarlo mediante l'inclusione dell'estensione validity assured short term certificate, come definita in ETSI EN 319 412-1.",
        'testo_integrale': 'CSS-6.3.10-02B: A validity assured short term certificate shall indicate this with the inclusion of validity assured short term certificate extension, as defined in ETSI EN 319 412-1 [5].',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-03',
        'testo': 'Se sono fornite CRL, il TSP dovrebbe non rimuovere dalla CRL i certificati revocati dopo la loro scadenza.',
        'testo_integrale': 'CSS-6.3.10-03 [CONDITIONAL]: If CRLs are provided, the TSP should not remove from the CRL revoked certificates after they have expired.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica se il TSP fornisce CRL',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-04',
        'testo': 'Se sono fornite CRL e non sono forniti mezzi alternativi (es. OCSP) per le informazioni sullo stato di revoca di certificati scaduti, il TSP non deve rimuovere dalla CRL i certificati revocati dopo la loro scadenza.',
        'testo_integrale': 'CSS-6.3.10-04 [CONDITIONAL]: If CRLs are provided and no alternative means (e.g. OCSP) are provided for revocation status information on expired certificates, the TSP shall not remove from the CRL revoked certificates after they have expired.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica se il TSP fornisce CRL senza mezzi alternativi per certificati scaduti',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-05',
        'testo': "Se sono fornite CRL e il TSP non rimuove dalla CRL i certificati revocati dopo la loro scadenza, la CRL deve includere l'estensione X.509 'ExpiredCertsOnCRL'.",
        'testo_integrale': 'CSS-6.3.10-05 [CONDITIONAL]: If CRLs are provided and the TSP does not remove from the CRL revoked certificates after they have expired, the CRL shall include the X.509 "ExpiredCertsOnCRL" extension as defined in ISO/IEC 9594-8/Recommendation ITU-T X.509 [4]. NOTE 2: The ad-hoc Trusted List expiredCertsRevocationInfo Extension [i.8], specifying that the TSP keeps expired certificates in CRLs, can be set by the supervisory body in charge of the TSP in complement to CSS-6.3.10-04 or CSS-6.3-05 above.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica se il TSP fornisce CRL e non rimuove i certificati revocati scaduti',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-06',
        'testo': "Se sono fornite CRL e il TSP rimuove dalla CRL i certificati revocati dopo la loro scadenza, la CRL non deve includere l'estensione X.509 'ExpiredCertsOnCRL'.",
        'testo_integrale': 'CSS-6.3.10-06 [CONDITIONAL]: If CRLs are provided and the TSP removes from the CRL revoked certificates after they have expired, the CRL shall not include the X.509 "ExpiredCertsOnCRL" extension as defined in ISO/IEC 9594-8/Recommendation ITU-T X.509 [4].',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica se il TSP fornisce CRL e rimuove i certificati revocati scaduti',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-07',
        'testo': "Se sono fornite CRL e il TSP decide o è tenuto a terminare una CRL, dovrebbe emettere e pubblicare al CRL Distribution Point corrispondente un'ultima CRL con un valore del campo nextUpdate come definito alla clausola 6.3.9 di EN 319 411-1, requisito CSS-6.3.9-06.",
        'testo_integrale': "CSS-6.3.10-07 [CONDITIONAL]: If CRLs are provided and the TSP decides or is required to terminate a CRL, the TSP should issue and publish at the corresponding CRL Distribution Point a last CRL with a nextUpdate field value as defined in ETSI EN 319 411-1 [2], clause 6.3.9 Requirement CSS-6.3.9-06. NOTE 3: CRL termination can occur when there are no more valid certificates in the scope of the CRL, and e.g. potentially in addition, when the CRL's signing entity certificate expires or when the CRL's signing entity private key is decommissioned.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica se il TSP fornisce CRL e decide/è tenuto a terminarle',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-08',
        'testo': "Se sono fornite CRL, il TSP dovrebbe preservare l'integrità e la disponibilità dell'ultima CRL almeno per il periodo specificato nella CPS come richiesto da CSS-6.3.10-12.",
        'testo_integrale': 'CSS-6.3.10-08 [CONDITIONAL]: If CRLs are provided, the TSP should preserve the integrity and the availability of the last CRL at least for the period specified in the CPS as requested in CSS-6.3.10-12. NOTE 4: ETSI specifies formats for long term preservation of signed data in other documents.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica se il TSP fornisce CRL',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-09',
        'testo': "Se sono fornite CRL, il TSP non deve emettere un'ultima CRL finché tutti i certificati nell'ambito della CRL non sono scaduti o revocati.",
        'testo_integrale': 'CSS-6.3.10-09 [CONDITIONAL]: If CRLs are provided, the TSP shall not issue a last CRL until all certificates in the scope of the CRL are either expired or revoked.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica se il TSP fornisce CRL',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-10',
        'testo': "Se è fornito OCSP, il responder OCSP dovrebbe usare l'estensione ArchiveCutOff come specificato in IETF RFC 6960, con la data archiveCutOff impostata al valore 'notBefore' del certificato della CA.",
        'testo_integrale': 'CSS-6.3.10-10 [CONDITIONAL]: If OCSP is provided, the OCSP responder should use the ArchiveCutOff extension as specified in IETF RFC 6960 [i.9], with the archiveCutOff date set to the CA\'s certificate "notBefore" time and date value.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica se il TSP fornisce OCSP',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-11',
        'testo': "Se è fornito OCSP e il certificato della CA sta per scadere, il TSP può calcolare un'ultima risposta OCSP per ciascun certificato emesso (revocato o meno), con il campo 'nextUpdate' impostato a '99991231235959Z'.",
        'testo_integrale': 'CSS-6.3.10-11 [CONDITIONAL]: If OCSP is provided and the CA\'s certificate is about to expire, the TSP may compute a last OCSP answer for each and every issued certificate (whether revoked or not), with the "nextUpdate" field set to "99991231235959Z". NOTE 5: Pre-computing OCSP answers prevents the use of the nonce extension. NOTE 6: The ad-hoc Trusted List expiredCertsRevocationInfo Extension [i.8], specifying that the OSCP provides info on expired certificates can be set by the supervisory body in charge of the TSP in complement to CSS-6.3.10-10 above.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica se il TSP fornisce OCSP e il certificato della CA sta per scadere',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-12',
        'testo': 'Il TSP deve documentare precisamente nelle proprie practice statement e nei propri termini e condizioni come sono soddisfatti i requisiti CSS-6.3.10-02 a CSS-6.3.10-11, incluso: a) il periodo durante il quale le informazioni sullo stato di revoca sono disponibili; b) come sono fornite le informazioni sullo stato di revoca in caso di compromissione della chiave della CA; c) come sono fornite le informazioni sullo stato di revoca in caso di cessazione del TSP.',
        'testo_integrale': "CSS-6.3.10-12: The TSP shall document precisely in its practices statements and in its terms and conditions how requirements CSS-6.3.10-02 to CSS-6.3.10-11 are met, including: a) the period over which the revocation status information is made available; b) how the revocation status information is provided in the case of CA's key compromise; c) how the revocation status information is provided in the case of TSP termination (see clause 6.4.9).",
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.3.10-13',
        'testo': "Se il TSP gestisce la chiave privata del soggetto e garantisce che il certificato sia valido al momento dell'uso della chiave privata, questa informazione dovrebbe essere indicata nelle sue practice statement o certificate policy, e può anche essere derivata dal certificato del soggetto.",
        'testo_integrale': "CSS-6.3.10-13 [CONDITIONAL]: If the TSP is managing the subject's private key and assures that the certificate is valid at the time of use of the private key, this information should be indicated in its practices statements or certificate policy, and may also be derived from the subject's certificate.",
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'condizione_applicabilita': "si applica se il TSP gestisce la chiave privata del soggetto e garantisce la validità del certificato al momento dell'uso",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.3.12-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.3.12 di ETSI EN 319 411-1 (Key Escrow and Recovery).',
        'testo_integrale': '6.3.12 Key Escrow and Recovery: SDP-6.3.12-01: The requirements specified in ETSI EN 319 411-1 [2], clause 6.3.12 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.4.1-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.4.1 di ETSI EN 319 411-1 (General).',
        'testo_integrale': '6.4.1 General: OVR-6.4.1-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.4.1 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.4.2-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.4.2 di ETSI EN 319 411-1 (Physical Security Controls).',
        'testo_integrale': '6.4.2 Physical Security Controls: OVR-6.4.2-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.4.2 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.4.3-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.4.3 di ETSI EN 319 411-1 (Procedural Controls).',
        'testo_integrale': '6.4.3 Procedural Controls: OVR-6.4.3-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.4.3 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.4.4-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.4.4 di ETSI EN 319 411-1 (Personnel Controls).',
        'testo_integrale': '6.4.4 Personnel Controls: OVR-6.4.4-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.4.4 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.4.5-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.4.5 di ETSI EN 319 411-1 (Audit Logging Procedures); si applicano inoltre, per la registrazione delle informazioni relative ai certificati qualificati EU, i requisiti particolari seguenti.',
        'testo_integrale': '6.4.5 Audit Logging Procedures: OVR-6.4.5-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.4.5 shall apply. In addition, for the recording of information concerning EU qualified certificates, the following particular requirements apply:',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.4.5-03',
        'testo': "Le informazioni devono essere conservate per quanto necessario a soddisfare i requisiti di legge anche oltre la cessazione dell'attività del TSP.",
        'testo_integrale': 'OVR-6.4.5-03: The information shall be maintained as necessary to meet legal requirements beyond the termination of the TSP (see clause 6.4.9).',
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.4.6-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.4.6 di ETSI EN 319 411-1 (Records Archival).',
        'testo_integrale': '6.4.6 Records Archival: OVR-6.4.6-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.4.6 shall apply.',
        'tipo_obbligo': 'di conservazione',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.4.8-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.4.8 di ETSI EN 319 411-1 (Compromise and Disaster Recovery).',
        'testo_integrale': '6.4.8 Compromise and Disaster Recovery: OVR-6.4.8-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.4.8 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.4.9-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.4.9 di ETSI EN 319 411-1 (CA or RA Termination).',
        'testo_integrale': '6.4.9 CA or RA Termination: OVR-6.4.9-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.4.9 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.5.1-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.5.1 di ETSI EN 319 411-1 (Key Pair Generation and Installation); si applicano inoltre i requisiti seguenti.',
        'testo_integrale': '6.5.1 Key Pair Generation and Installation: OVR-6.5.1-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.5.1 shall apply. In addition:',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.5.1-02',
        'testo': "Sia che il dispositivo sia preparato dal TSP o meno, il TSP deve verificare che il dispositivo sia certificato come QSCD, per le policy QCP-n-qscd e QCP-l-qscd. Il Regolamento (UE) n. 910/2014 prevede che il QSCD sia certificato come conforme ai requisiti dell'allegato II tramite un certificato secondo le regole delle sezioni 4 e 5 del Regolamento; ulteriori standard potranno essere emanati in questo ambito.",
        'testo_integrale': 'SDP-6.5.1-02 [QCP-n-qscd] and [QCP-l-qscd]: Whether the device is prepared by the TSP or not, the TSP shall verify that the device is certified as a QSCD. NOTE 1: Regulation (EU) No 910/2014 [i.1] states that the QSCD is to be certified as meeting the requirements of annex II through a certificate following the rules expressed in sections 4 and 5 of this Regulation. NOTE 2: Further standards may be issued in this area.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n-qscd e QCP-l-qscd',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.5.1-03',
        'testo': "Se il dispositivo è gestito da un TSP terzo per conto del soggetto e non dal TSP che emette il certificato, quest'ultimo deve verificare che il TSP terzo soddisfi i requisiti appropriati in termini di qualificazione, per le policy QCP-n-qscd e QCP-l-qscd.",
        'testo_integrale': 'SDP-6.5.1-03 [QCP-n-qscd] and [QCP-l-qscd] [CONDITIONAL]: If the device is managed by a third party TSP on behalf of the subject which is not the TSP issuing the certificate itself, the TSP issuing the certificate shall verify that this third party TSP is meeting the appropriate requirements in terms of qualification.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n-qscd e QCP-l-qscd se il dispositivo è gestito da un TSP terzo',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.5.1-04',
        'testo': 'Il processo di richiesta del certificato deve assicurare che la chiave pubblica da certificare provenga da una coppia di chiavi generata da un QSCD, per le policy QCP-n-qscd e QCP-l-qscd.',
        'testo_integrale': 'SDP-6.5.1-04 [QCP-n-qscd] and [QCP-l-qscd]: The certificate request process shall ensure that the public key to be certified is from a key pair generated by a QSCD.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n-qscd e QCP-l-qscd',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.5.1-05',
        'testo': 'Se la coppia di chiavi del soggetto è generata da un TSP e importata nel QSCD usato per la creazione di firma/sigillo, le assunzioni ambientali e gli obiettivi di sicurezza per il dispositivo certificato (QSCD di generazione e QSCD di creazione) devono essere soddisfatti dal TSP, per le policy QCP-n-qscd e QCP-l-qscd.',
        'testo_integrale': "SDP-6.5.1-05 [QCP-n-qscd] and [QCP-l-qscd] [CONDITIONAL]: If the subject's key pair is generated by a TSP and imported into the QSCD used for signature/seal creation, the environmental assumptions and security objectives for the certified device (QSCD used for key generation and QSCD used for signature/seal creation) shall be met by the TSP.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n-qscd e QCP-l-qscd se la coppia di chiavi è generata dal TSP e importata nel QSCD',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.5.1-06',
        'testo': 'Se la chiave privata del soggetto viene spostata tra dispositivi, le potenziali vulnerabilità a compromissione della chiave devono essere determinate e devono essere implementati meccanismi adeguati per mitigarle, per le policy QCP-n-qscd e QCP-l-qscd.',
        'testo_integrale': "SDP-6.5.1-06 [QCP-n-qscd] and [QCP-l-qscd] [CONDITIONAL]: If the subject's private key is moved between devices potential vulnerabilities to key compromise shall be determined and adequate mechanisms implemented to mitigate any vulnerabilities.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n-qscd e QCP-l-qscd se la chiave privata viene spostata tra dispositivi',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.5.1-07A',
        'testo': "Il TSP deve adottare misure appropriate in caso di modifica dello stato di certificazione del QSCD che intervenga prima della fine del periodo di validità del certificato, per le policy QCP-n-qscd e QCP-l-qscd. Le notifiche ufficiali degli Stati membri sugli organismi designati e sui dispositivi di creazione di firma/sigillo qualificati certificati, incluse quelle relative alla misura transitoria dell'articolo 51(1) del Regolamento, possono essere usate per monitorare lo stato del QSCD.",
        'testo_integrale': "SDP-6.5.1-07A [QCP-n-qscd] and [QCP-l-qscd]: The TSP shall take appropriate measures in case of modification of the QSCD status occurring before the end of the validity period of the certificate. NOTE 3: The official Member States' notifications on Designated Bodies under Articles 30(2) and 39(2) of Regulation (EU) 910/2014 and Certified Qualified Signature Creation Devices under Article 31(1)-(2), and Certified Qualified Seal Creation Devices under Article 39(3) of Regulation (EU) 910/2014, and information from Member States on Secure Signature Creation Devices benefiting from the transitional measure set in article 51(1) of Regulation (EU) 910/2014 [i.1] can be used to monitor the QSCD status.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n-qscd e QCP-l-qscd',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.5.1-07B',
        'testo': 'Il TSP deve documentare nella propria CPS le misure adottate in caso di modifica dello stato di certificazione del QSCD prima della fine del periodo di validità del certificato, per le policy QCP-n-qscd e QCP-l-qscd. Lo qcStatement per QSCD (esi4-qcStatement-4) definito in EN 319 412-5 deve essere incluso nel certificato come da GEN-6.6.1-03; REV-6.3.9-01, tramite rinvio ai requisiti della clausola 6.3.9 di EN 319 411-1 (in particolare REV-6.3.9-02 b)), fa scattare la revoca di qualsiasi certificato non scaduto di cui il TSP sia a conoscenza di modifiche che ne compromettono la validità: la perdita dello stato di certificazione QSCD per un certificato con esi4-qcStatement-4 costituisce tale modifica.',
        'testo_integrale': 'SDP-6.5.1-07B [QCP-n-qscd] and [QCP-l-qscd]: The TSP shall document in its CPS the measures it takes in case of modification of the QSCD status occurring before the end of the validity period of the certificate. NOTE 4: The qcStatement for QSCD (esi4-qcStatement-4) defined in ETSI EN 319 412-5 [3] is to be included in the certificate as per GEN-6.6.1-03, and REV-6.3.9-01, by reference to requirements specified in ETSI EN 319 411-1 [2], clause 6.3.9, REV-6.3.9-02 b) in particular, triggers the revocation of any non-expired certificate that the TSP is aware of changes which impact the validity of the certificate. The loss of QSCD certification status for certificate bearing the esi4-qcStatement-4 is such a change.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n-qscd e QCP-l-qscd',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: GEN-6.5.2-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.5.2 di ETSI EN 319 411-1 (Private Key Protection and Cryptographic Module Engineering Controls).',
        'testo_integrale': '6.5.2 Private Key Protection and Cryptographic Module Engineering Controls: GEN-6.5.2-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.5.2 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: GEN-6.5.3-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.5.3 di ETSI EN 319 411-1 (Other Aspects of Key Pair Management).',
        'testo_integrale': '6.5.3 Other Aspects of Key Pair Management: GEN-6.5.3-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.5.3 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: SDP-6.5.4-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.5.4 di ETSI EN 319 411-1 (Activation Data).',
        'testo_integrale': '6.5.4 Activation Data: SDP-6.5.4-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.5.4 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.5.5-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.5.5 di ETSI EN 319 411-1 (Computer Security Controls).',
        'testo_integrale': '6.5.5 Computer Security Controls: OVR-6.5.5-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.5.5 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.5.6-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.5.6 di ETSI EN 319 411-1 (Life Cycle Security Controls).',
        'testo_integrale': '6.5.6 Life Cycle Security Controls: OVR-6.5.6-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.5.6 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.5.7-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.5.7 di ETSI EN 319 411-1 (Network Security Controls).',
        'testo_integrale': '6.5.7 Network Security Controls: OVR-6.5.7-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.5.7 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: GEN-6.6.1-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.6.1 di ETSI EN 319 411-1 (Certificate Profile); si applicano inoltre i requisiti particolari seguenti.',
        'testo_integrale': '6.6.1 Certificate Profile: GEN-6.6.1-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.6.1 shall apply. In addition the following particular requirements apply:',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: GEN-6.6.1-02',
        'testo': 'Il certificato deve includere tutti i qcStatement appropriati come definiti in ETSI EN 319 412-5.',
        'testo_integrale': 'GEN-6.6.1-02: The certificate shall include all appropriate qcStatements as defined in ETSI EN 319 412-5 [3].',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: GEN-6.6.1-03',
        'testo': 'Il certificato deve includere il qcStatement per QSCD (esi4-qcStatement-4) definito in ETSI EN 319 412-5, per le policy QCP-n-qscd e QCP-l-qscd.',
        'testo_integrale': 'GEN-6.6.1-03 [QCP-n-qscd] and [QCP-l-qscd]: The certificate shall include the qcStatement for QSCD (esi4-qcStatement-4) defined in ETSI EN 319 412-5 [3].',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica a QCP-n-qscd e QCP-l-qscd',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: GEN-6.6.1-04',
        'testo': 'Il qcStatement per QSCD (esi4-qcStatement-4) non deve essere incluso nei certificati non emessi secondo i requisiti QCP-n-qscd o QCP-l-qscd.',
        'testo_integrale': 'GEN-6.6.1-04: The qcStatement for QSCD (esi4-qcStatement-4) shall not be included in certificates that are not issued according to [QCP-n-qscd] or [QCP-l-qscd] requirements.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: GEN-6.6.1-05',
        'testo': "Il certificato deve includere almeno uno degli identificatori di policy elencati: per ciascuna policy (QCP-n, QCP-l, QCP-n-qscd, QCP-l-qscd, QEVCP-w, QNCP-w, QNCP-w-gen), l'identificatore definito alla clausola 5.3 e/o un OID relativo, e per QEVCP-w/QNCP-w anche un OID come specificato rispettivamente in EVCG o BRG.",
        'testo_integrale': 'GEN-6.6.1-05: The certificate shall include at least one of the following policy identifier [CHOICE]: - [QCP-n]: -the policy identifier defined in clause 5.3 item a); and/or -an OID, allocated by the TSP (or any relevant stakeholder) to the certificate policy applied to issue the certificate. - [QCP-l]: -the policy identifier defined in clause 5.3 item b); and/or -an OID allocated by the TSP (or any relevant stakeholder) to the certificate policy applied to issue the certificate. - [QCP-n-qscd]: -the policy identifier defined in clause 5.3 item c); and/or -an OID, allocated by the TSP (or any relevant stakeholder) to the certificate policy applied to issue the certificate. - [QCP-l-qscd]: -the policy identifier defined in clause 5.3 item d); and/or -an OID allocated by the TSP (or any relevant stakeholder) to the certificate policy applied to issue the certificate. - [QEVCP-w]: -an OID as specified in EVCG [i.7], clause 7.1.6.1; and at least one of the following policy identifiers: as defined in clause 5.3 item e); and/or an OID allocated by the TSP (or any relevant stakeholder) to the certificate policy applied to issue the certificate. - [QNCP-w]: -an OID as specified in BRG [i.3], clause 1.2 or 7.1.6.1; and at least one of the following policy identifiers: as defined in clause 5.3 item f); and/or an OID allocated by the TSP (or any relevant stakeholder) to the certificate policy applied to issue the certificate. - [QNCP-w-gen]: -the policy identifier defined in clause 5.3 item g); and/or -an OID allocated by the TSP (or any relevant stakeholder) to the certificate policy applied to issue the certificate.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': "scelta dell'identificatore di policy da includere nel certificato in base alla policy applicata",
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: GEN-6.6.1-07',
        'testo': 'Se il certificato contiene solo un OID assegnato dal TSP, la certificate policy a cui si riferisce deve essere costruita secondo la clausola 7, identificando chiaramente quale delle certificate policy definite nel presente documento adotta come base.',
        'testo_integrale': 'GEN-6.6.1-07 [CONDITIONAL]: If the certificate contains only an OID allocated by the TSP, the referred certificate policy shall be built according to clause 7. In particular it shall clearly identify which of the certificate policy defined in the present document it adopts as the basis. NOTE: The rationales for writing a certificate policy are provided in clause 4.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'condizione_applicabilita': 'si applica se il certificato contiene solo un OID assegnato dal TSP',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.6.2-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.6.2 di ETSI EN 319 411-1 (CRL Profile).',
        'testo_integrale': '6.6.2 CRL Profile: CSS-6.6.2-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.6.2 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: CSS-6.6.3-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.6.3 di ETSI EN 319 411-1 (OCSP Profile).',
        'testo_integrale': '6.6.3 OCSP Profile: CSS-6.6.3-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.6.3 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.8.2-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.8.2 di ETSI EN 319 411-1 (Financial Responsibility).',
        'testo_integrale': '6.8.2 Financial Responsibility: OVR-6.8.2-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.8.2 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.8.4-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.8.4 di ETSI EN 319 411-1 (Privacy of Personal Information).',
        'testo_integrale': '6.8.4 Privacy of Personal Information: OVR-6.8.4-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.8.4 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.8.6-01',
        'testo': 'Si applicano gli obblighi generali di cui alla clausola 6.8.6 di ETSI EN 319 411-1 (Representations and Warranties).',
        'testo_integrale': '6.8.6 Representations and Warranties: OVR-6.8.6-01: The general obligations specified in ETSI EN 319 411-1 [2], clause 6.8.6 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.8.13-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.8.13 di ETSI EN 319 411-1 (Dispute Resolution Procedures).',
        'testo_integrale': '6.8.13 Dispute Resolution Procedures: OVR-6.8.13-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.8.13 shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.8.15-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.8.15 di ETSI EN 319 411-1 (Compliance with Applicable Law).',
        'testo_integrale': '6.8.15 Compliance with Applicable Law: OVR-6.8.15-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.8.15 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.9.1-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.9.1 di ETSI EN 319 411-1 (Organizational).',
        'testo_integrale': '6.9.1 Organizational: OVR-6.9.1-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.9.1 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.9.2-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.9.2 di ETSI EN 319 411-1 (Additional testing).',
        'testo_integrale': '6.9.2 Additional testing: OVR-6.9.2-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.9.2 shall apply.',
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.9.3-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.9.3 di ETSI EN 319 411-1 (Disabilities).',
        'testo_integrale': '6.9.3 Disabilities: OVR-6.9.3-01: The requirements identified in ETSI EN 319 411-1 [2], clause 6.9.3 shall apply.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.9.4-01',
        'testo': 'Si applicano i requisiti di cui alla clausola 6.9.4 di ETSI EN 319 411-1 (Terms and conditions); si applicano inoltre i requisiti particolari seguenti.',
        'testo_integrale': '6.9.4 Terms and conditions: OVR-6.9.4-01: The requirements specified in ETSI EN 319 411-1 [2], clause 6.9.4 shall apply. In addition the following particular requirements apply:',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.9.4-02',
        'testo': "La certificate policy deve includere una dichiarazione chiara che indichi che la policy è per certificati qualificati EU e se la policy richiede l'uso di un QSCD.",
        'testo_integrale': 'OVR-6.9.4-02: The certificate policy shall include a clear statement indicating that the policy is for EU qualified certificates and whether the policy requires use of a QSCD.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.9.4-03',
        'testo': 'Deve essere supportata una PKI disclosure statement.',
        'testo_integrale': 'OVR-6.9.4-03: A PKI disclosure statement shall be supported.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 2: OVR-6.9.4-04',
        'testo': "La PKI disclosure statement dovrebbe essere strutturata secondo l'allegato A di ETSI EN 319 411-1; questa dichiarazione può assistere il TSP nel rispondere a requisiti normativi e preoccupazioni, in particolare quelle relative alla tutela dei consumatori e ai requisiti dell'articolo 24.2 del Regolamento (UE) n. 910/2014.",
        'testo_integrale': 'OVR-6.9.4-04: The PKI disclosure statement should be structured according to annex A in ETSI EN 319 411-1 [2]. NOTE: This PKI disclosure statement can assist a TSP to respond to regulatory requirements and concerns, particularly those related to consumer deployment and the requirements of Regulation (EU) No 910/2014 [i.1], article 24 2.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
]

RIGHE_PRINCIPI = [
    {
        'riferimento': 'Parte 2: clausola 5.1 (premessa)',
        'testo': "Il presente documento è strutturato in linea con IETF RFC 3647 per assistere i TSP nell'applicare questi requisiti alla propria documentazione CP e CPS.",
        'testo_integrale': 'The present document is structured broadly in line with IETF RFC 3647 [i.4] to assist TSPs in applying these requirements to their own CP and CPS documentation.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 5.3 (identificatori delle policy)',
        'testo': "Definisce gli identificatori (OID) delle 7 certificate policy per certificati qualificati EU previste dal documento: QCP-n, QCP-l, QCP-n-qscd, QCP-l-qscd, QEVCP-w, QNCP-w, QNCP-w-gen. L'inclusione di uno di questi identificatori in un certificato qualificato EU indica che il certificato è emesso e gestito secondo il presente documento per quella policy; l'identificatore può essere usato dalle relying party per determinarne l'idoneità e l'affidabilità nel quadro del Regolamento (UE) n. 910/2014.",
        'testo_integrale': "As described in IETF RFC 3647 [i.4], clause 3.3, certificates include a certificate policy identifier which can be used by relying parties in determining the certificates suitability and trustworthiness for a particular application. The identifiers for the EU qualified certificate policies specified in the present document are: a) QCP-n: certificate policy for EU qualified certificates issued to natural persons; itu-t(0) identified-organization(4) etsi(0) qualified-certificate-policies(194112) policy-identifiers(1) qcp-natural (0) b) QCP-l: certificate policy for EU qualified certificates issued to legal persons; itu-t(0) identified-organization(4) etsi(0) qualified-certificate-policies(194112) policy-identifiers(1) qcp-legal (1) c) QCP-n-qscd: certificate policy for EU qualified certificates issued to natural persons with private key related to the certified public key in a QSCD; itu-t(0) identified-organization(4) etsi(0) qualified-certificate-policies(194112) policy-identifiers(1) qcp-natural-qscd (2) d) QCP-l-qscd: certificate policy for EU qualified certificates issued to legal persons with private key related to the certified public key in a QSCD; itu-t(0) identified-organization(4) etsi(0) qualified-certificate-policies(194112) policy-identifiers(1) qcp-legal-qscd (3) e) QEVCP-w: certificate policy for EU qualified website authentication certificates based on EVCP; itu-t(0) identified-organization(4) etsi(0) qualified-certificate-policies(194112) policy-identifiers(1) qcp-web (4) f) QNCP-w: certificate policy for EU qualified website authentication certificates based on NCP, and OVCP or IVCP; itu-t(0) identified-organization(4) etsi(0) qualified-certificate-policies(194112) policy-identifiers(1) qncp-web (5) g) QNCP-w-gen: certificate policy for EU qualified website authentication based on NCP and requirements tagged as [WEB] in ETSI EN 319 411-1 [2]. itu-t(0) identified-organization(4) etsi(0) qualified-certificate-policies(194112) policy-identifiers(1) qncp-web-gen (6) Including one of the policy identifiers defined above in an EU qualified certificate indicates that the certificate is issued and managed according to the present document for that policy. The policy identifier can be used by relying parties in determining the certificate's suitability and trustworthiness in the framework of Regulation (EU) No 910/2014 [i.1].",
        'tipo_principio': 'definitorio',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 5.4.1 (premessa)',
        'testo': 'Si applicano i concetti descritti alla clausola 5.4.1 di ETSI EN 319 411-1 riguardo alla Certification Authority.',
        'testo_integrale': '5.4.1 Certification authority: The concepts described in ETSI EN 319 411-1 [2], clause 5.4.1 apply.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 5.4.2',
        'testo': 'Si applica la clausola 5.4.2 di ETSI EN 319 411-1 (Subscriber and subject).',
        'testo_integrale': '5.4.2 Subscriber and subject: ETSI EN 319 411-1 [2], clause 5.4.2 applies.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 5.5.1',
        'testo': 'I certificati emessi secondo la policy QCP-n sono destinati a supportare le firme elettroniche avanzate basate su un certificato qualificato, come definite dagli articoli 26 e 28 del Regolamento (UE) n. 910/2014.',
        'testo_integrale': '5.5.1 QCP-n: Certificates issued under these requirements are aimed to support the advanced electronic signatures based on a qualified certificate defined in articles 26 and 28 of the Regulation (EU) No 910/2014 [i.1].',
        'tipo_principio': 'scopo/ambito di applicazione',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 5.5.2',
        'testo': 'I certificati emessi secondo la policy QCP-l sono destinati a supportare i sigilli elettronici avanzati basati su un certificato qualificato, come definiti dagli articoli 36 e 38 del Regolamento (UE) n. 910/2014.',
        'testo_integrale': '5.5.2 QCP-l: Certificates issued under these requirements are aimed to support the advanced electronic seals based on a qualified certificate defined in articles 36 and 38 of the Regulation (EU) No 910/2014 [i.1].',
        'tipo_principio': 'scopo/ambito di applicazione',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 5.5.3',
        'testo': "I certificati emessi secondo la policy QCP-n-qscd sono destinati a supportare le firme elettroniche qualificate come definite dall'articolo 3(12) del Regolamento (UE) n. 910/2014.",
        'testo_integrale': '5.5.3 QCP-n-qscd: Certificates issued under these requirements are aimed to support qualified electronic signatures such as defined in article 3 (12) of the Regulation (EU) No 910/2014 [i.1].',
        'tipo_principio': 'scopo/ambito di applicazione',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 5.5.4',
        'testo': "I certificati emessi secondo la policy QCP-l-qscd sono destinati a supportare i sigilli elettronici qualificati come definiti dall'articolo 3(27) del Regolamento (UE) n. 910/2014.",
        'testo_integrale': '5.5.4 QCP-l-qscd: Certificates issued under these requirements are aimed to support qualified electronic seals such as defined in article 3 (27) of the Regulation (EU) No 910/2014 [i.1].',
        'tipo_principio': 'scopo/ambito di applicazione',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 5.5.5',
        'testo': "I certificati emessi secondo la policy QEVCP-w sono destinati a supportare l'autenticazione di siti web basata su un certificato qualificato, come definita dagli articoli 3(38) e 45 del Regolamento (UE) n. 910/2014, per gli usi descritti alla clausola 4.2.2 punto 5).",
        'testo_integrale': '5.5.5 QEVCP-w: Certificates issued under these requirements are aimed to support website authentication based on a qualified certificate defined in articles 3 (38) and 45 of the Regulation (EU) No 910/2014 [i.1], for uses described in clause 4.2.2 5).',
        'tipo_principio': 'scopo/ambito di applicazione',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 5.5.6',
        'testo': "I certificati emessi secondo la policy QNCP-w sono destinati a supportare l'autenticazione di siti web basata su un certificato qualificato, come definita dagli articoli 3(38) e 45 del Regolamento (UE) n. 910/2014, per gli usi descritti alla clausola 4.2.2 punto 6).",
        'testo_integrale': '5.5.6 QNCP-w: Certificates issued under these requirements are aimed to support website authentication based on a qualified certificate defined in articles 3 (38) and 45 of the Regulation (EU) No 910/2014 [i.1], for uses described in clause 4.2.2 6).',
        'tipo_principio': 'scopo/ambito di applicazione',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 5.5.7',
        'testo': "I certificati emessi secondo la policy QNCP-w-gen sono destinati a supportare l'autenticazione di siti web basata su un certificato qualificato, come definita dagli articoli 3(38) e 45 del Regolamento (UE) n. 910/2014, per gli usi descritti alla clausola 4.2.2 punto 7).",
        'testo_integrale': '5.5.7 QNCP-w-gen: Certificates issued under these requirements are aimed to support website authentication based on a qualified certificate defined in articles 3 (38) and 45 of the Regulation (EU) No 910/2014 [i.1], for uses described in clause 4.2.2 7).',
        'tipo_principio': 'scopo/ambito di applicazione',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.2.1',
        'testo': 'Si applica la clausola 6.2.1 di ETSI EN 319 411-1 (Naming); si veda anche la clausola 6.6.1 del presente documento.',
        'testo_integrale': '6.2.1 Naming: See ETSI EN 319 411-1 [2], clause 6.2.1. See also clause 6.6.1 of the present document.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: REG-6.3.6-01',
        'testo': 'Requisito soppresso (Void) in questa versione del documento.',
        'testo_integrale': '6.3.6 Certificate Renewal: REG-6.3.6-01: Void.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: REG-6.3.8-01',
        'testo': 'Requisito soppresso (Void) in questa versione del documento.',
        'testo_integrale': '6.3.8 Certificate Modification: REG-6.3.8-01: Void.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.3.11',
        'testo': 'Nessun requisito di policy per la clausola End of Subscription.',
        'testo_integrale': '6.3.11 End of Subscription: No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: OVR-6.4.5-02',
        'testo': 'Requisito soppresso (Void) in questa versione del documento.',
        'testo_integrale': 'OVR-6.4.5-02: Void.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: OVR-6.4.5-04',
        'testo': 'Requisito soppresso (Void) in questa versione del documento.',
        'testo_integrale': 'OVR-6.4.5-04: Void.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: OVR-6.4.5-05',
        'testo': "Requisito soppresso (Void) in questa versione del documento. L'articolo 24.2(h) del Regolamento (UE) n. 910/2014 richiede a un QTSP di registrare e mantenere accessibili, per un periodo di tempo adeguato, anche dopo la cessazione delle attività, tutte le informazioni rilevanti relative ai dati emessi e ricevuti dal QTSP, in particolare ai fini della prova in procedimenti legali e della continuità del servizio; tale registrazione può avvenire elettronicamente.",
        'testo_integrale': 'OVR-6.4.5-05: Void. NOTE: Regulation (EU) No 910/2014 [i.1] article 24.2 (h) requires a qualified TSP to "record and keep accessible for an appropriate period of time, including after the activities of the qualified trust service provider have ceased, all relevant information concerning data issued and received by the qualified trust service provider, in particular, for the purpose of providing evidence in legal proceedings and for the purpose of ensuring continuity of the service. Such recording may be done electronically".',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: SDP-6.4.5-06',
        'testo': 'Requisito soppresso (Void) in questa versione del documento.',
        'testo_integrale': 'SDP-6.4.5-06: Void.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.4.7',
        'testo': 'Nessun requisito di policy per la clausola Key Changeover.',
        'testo_integrale': '6.4.7 Key Changeover: No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: SDP-6.5.1-07',
        'testo': 'Requisito soppresso (Void) in questa versione del documento.',
        'testo_integrale': 'SDP-6.5.1-07: Void.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.5.8',
        'testo': "Il time-stamping non rientra nell'ambito di applicazione del presente documento.",
        'testo_integrale': '6.5.8 Time-stamping: NOTE: Not in the scope of the present document.',
        'tipo_principio': 'scopo/ambito di applicazione',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: GEN-6.6.1-06',
        'testo': 'Requisito soppresso (Void) in questa versione del documento.',
        'testo_integrale': 'GEN-6.6.1-06: Void.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.7',
        'testo': "Per l'audit di conformità e le altre valutazioni si veda ETSI EN 319 403.",
        'testo_integrale': '6.7 Compliance Audit and Other Assessment: NOTE: See ETSI EN 319 403 [i.6].',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.8.1',
        'testo': "Questi requisiti di policy non intendono implicare alcuna restrizione sull'addebito dei servizi del TSP.",
        'testo_integrale': "6.8.1 Fees: These policy requirements are not meant to imply any restrictions on charging for TSP's services.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.8.3',
        'testo': 'Nessun requisito di policy per la riservatezza delle informazioni commerciali.',
        'testo_integrale': '6.8.3 Confidentiality of Business Information: No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.8.5',
        'testo': 'Nessun requisito di policy per i diritti di proprietà intellettuale.',
        'testo_integrale': '6.8.5 Intellectual Property Rights: No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: OVR-6.8.6-02',
        'testo': 'Requisito soppresso (Void) in questa versione del documento.',
        'testo_integrale': 'OVR-6.8.6-02: Void.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: OVR-6.8.6-03',
        'testo': 'Requisito soppresso (Void) in questa versione del documento.',
        'testo_integrale': 'OVR-6.8.6-03: Void.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: OVR-6.8.6-04a',
        'testo': 'Requisito soppresso (Void) in questa versione del documento.',
        'testo_integrale': 'OVR-6.8.6-04a: Void.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: OVR-6.8.6-04b',
        'testo': 'Requisito soppresso (Void) in questa versione del documento.',
        'testo_integrale': 'OVR-6.8.6-04b: Void.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.8.7',
        'testo': 'Per i disclaimer di garanzia si veda la clausola 6.8.6; si veda anche la clausola A.2 di ETSI EN 319 411-1 per ulteriori informazioni.',
        'testo_integrale': '6.8.7 Disclaimers of Warranties: See clause 6.8.6. See also clause A.2 in ETSI EN 319 411-1 [2] for additional information.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.8.8',
        'testo': "Le limitazioni di responsabilità sono disciplinate dai termini e condizioni secondo la clausola 6.9.4; si veda l'articolo 13 del Regolamento (UE) n. 910/2014.",
        'testo_integrale': '6.8.8 Limitations of Liability: Limitations on liability are covered in the terms and conditions as per clause 6.9.4. NOTE: See article 13 of the Regulation (EU) No 910/2014 [i.1].',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.8.9',
        'testo': 'Nessun requisito di policy per le indennità.',
        'testo_integrale': '6.8.9 Indemnities: No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.8.10',
        'testo': 'Nessun requisito di policy per durata e cessazione.',
        'testo_integrale': '6.8.10 Term and Termination: No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.8.11',
        'testo': 'Nessun requisito di policy per le comunicazioni individuali con i partecipanti.',
        'testo_integrale': '6.8.11 Individual notices and communications with participants: No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.8.12',
        'testo': 'Nessun requisito di policy per gli emendamenti.',
        'testo_integrale': '6.8.12 Amendments: No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.8.14',
        'testo': "Il diritto applicabile (Governing Law) non rientra nell'ambito di applicazione del presente documento.",
        'testo_integrale': '6.8.14 Governing Law: Not in the scope of the present document.',
        'tipo_principio': 'scopo/ambito di applicazione',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 2: clausola 6.8.16',
        'testo': 'Nessun requisito di policy per le disposizioni varie.',
        'testo_integrale': '6.8.16 Miscellaneous Provisions: No policy requirement.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
]

INDICE_ARTICOLI_LOCALE = [
    'Parte 2: OVR-5.1-01',
    'Parte 2: OVR-5.1-02',
    'Parte 2: OVR-5.1-03',
    'Parte 2: OVR-5.1-04',
    'Parte 2: OVR-5.1-05',
    'Parte 2: OVR-5.1-06',
    'Parte 2: OVR-5.1-07',
    'Parte 2: OVR-5.1-08',
    'Parte 2: OVR-5.1-09',
    'Parte 2: OVR-5.2-01',
    'Parte 2: OVR-5.3-01',
    'Parte 2: OVR-5.4.1-01',
    'Parte 2: OVR-5.4.3-01',
    'Parte 2: OVR-6.1-01',
    'Parte 2: REG-6.2.2-01',
    'Parte 2: REG-6.2.2-02',
    'Parte 2: REG-6.2.2-03',
    'Parte 2: REG-6.2.2-04',
    'Parte 2: REG-6.2.3-01',
    'Parte 2: REV-6.2.4-01',
    'Parte 2: REG-6.3.1-01',
    'Parte 2: REG-6.3.2-01',
    'Parte 2: GEN-6.3.3-01',
    'Parte 2: GEN-6.3.3-02',
    'Parte 2: OVR-6.3.4-01',
    'Parte 2: OVR-6.3.4-02',
    'Parte 2: OVR-6.3.5-01',
    'Parte 2: SDP-6.3.5-02',
    'Parte 2: SDP-6.3.5-03',
    'Parte 2: SDP-6.3.5-04',
    'Parte 2: SDP-6.3.5-05',
    'Parte 2: SDP-6.3.5-06',
    'Parte 2: OVR-6.3.5-07',
    'Parte 2: SDP-6.3.5-08',
    'Parte 2: SDP-6.3.5-09',
    'Parte 2: SDP-6.3.5-10',
    'Parte 2: SDP-6.3.5-11',
    'Parte 2: OVR-6.3.5-12',
    'Parte 2: REG-6.3.6-02',
    'Parte 2: REG-6.3.6-03',
    'Parte 2: REG-6.3.6-04',
    'Parte 2: REG-6.3.6-05',
    'Parte 2: REG-6.3.7-01',
    'Parte 2: REG-6.3.7-02',
    'Parte 2: REG-6.3.7-03',
    'Parte 2: REG-6.3.7-04',
    'Parte 2: REG-6.3.8-02',
    'Parte 2: REG-6.3.8-03',
    'Parte 2: REG-6.3.8-04',
    'Parte 2: REG-6.3.8-05',
    'Parte 2: REV-6.3.9-01',
    'Parte 2: CSS-6.3.10-01',
    'Parte 2: CSS-6.3.10-02',
    'Parte 2: CSS-6.3.10-02A',
    'Parte 2: CSS-6.3.10-02B',
    'Parte 2: CSS-6.3.10-03',
    'Parte 2: CSS-6.3.10-04',
    'Parte 2: CSS-6.3.10-05',
    'Parte 2: CSS-6.3.10-06',
    'Parte 2: CSS-6.3.10-07',
    'Parte 2: CSS-6.3.10-08',
    'Parte 2: CSS-6.3.10-09',
    'Parte 2: CSS-6.3.10-10',
    'Parte 2: CSS-6.3.10-11',
    'Parte 2: CSS-6.3.10-12',
    'Parte 2: CSS-6.3.10-13',
    'Parte 2: SDP-6.3.12-01',
    'Parte 2: OVR-6.4.1-01',
    'Parte 2: OVR-6.4.2-01',
    'Parte 2: OVR-6.4.3-01',
    'Parte 2: OVR-6.4.4-01',
    'Parte 2: OVR-6.4.5-01',
    'Parte 2: OVR-6.4.5-03',
    'Parte 2: OVR-6.4.6-01',
    'Parte 2: OVR-6.4.8-01',
    'Parte 2: OVR-6.4.9-01',
    'Parte 2: OVR-6.5.1-01',
    'Parte 2: SDP-6.5.1-02',
    'Parte 2: SDP-6.5.1-03',
    'Parte 2: SDP-6.5.1-04',
    'Parte 2: SDP-6.5.1-05',
    'Parte 2: SDP-6.5.1-06',
    'Parte 2: SDP-6.5.1-07A',
    'Parte 2: SDP-6.5.1-07B',
    'Parte 2: GEN-6.5.2-01',
    'Parte 2: GEN-6.5.3-01',
    'Parte 2: SDP-6.5.4-01',
    'Parte 2: OVR-6.5.5-01',
    'Parte 2: OVR-6.5.6-01',
    'Parte 2: OVR-6.5.7-01',
    'Parte 2: GEN-6.6.1-01',
    'Parte 2: GEN-6.6.1-02',
    'Parte 2: GEN-6.6.1-03',
    'Parte 2: GEN-6.6.1-04',
    'Parte 2: GEN-6.6.1-05',
    'Parte 2: GEN-6.6.1-07',
    'Parte 2: CSS-6.6.2-01',
    'Parte 2: CSS-6.6.3-01',
    'Parte 2: OVR-6.8.2-01',
    'Parte 2: OVR-6.8.4-01',
    'Parte 2: OVR-6.8.6-01',
    'Parte 2: OVR-6.8.13-01',
    'Parte 2: OVR-6.8.15-01',
    'Parte 2: OVR-6.9.1-01',
    'Parte 2: OVR-6.9.2-01',
    'Parte 2: OVR-6.9.3-01',
    'Parte 2: OVR-6.9.4-01',
    'Parte 2: OVR-6.9.4-02',
    'Parte 2: OVR-6.9.4-03',
    'Parte 2: OVR-6.9.4-04',
    'Parte 2: clausola 5.1 (premessa)',
    'Parte 2: clausola 5.3 (identificatori delle policy)',
    'Parte 2: clausola 5.4.1 (premessa)',
    'Parte 2: clausola 5.4.2',
    'Parte 2: clausola 5.5.1',
    'Parte 2: clausola 5.5.2',
    'Parte 2: clausola 5.5.3',
    'Parte 2: clausola 5.5.4',
    'Parte 2: clausola 5.5.5',
    'Parte 2: clausola 5.5.6',
    'Parte 2: clausola 5.5.7',
    'Parte 2: clausola 6.2.1',
    'Parte 2: REG-6.3.6-01',
    'Parte 2: REG-6.3.8-01',
    'Parte 2: clausola 6.3.11',
    'Parte 2: OVR-6.4.5-02',
    'Parte 2: OVR-6.4.5-04',
    'Parte 2: OVR-6.4.5-05',
    'Parte 2: SDP-6.4.5-06',
    'Parte 2: clausola 6.4.7',
    'Parte 2: SDP-6.5.1-07',
    'Parte 2: clausola 6.5.8',
    'Parte 2: GEN-6.6.1-06',
    'Parte 2: clausola 6.7',
    'Parte 2: clausola 6.8.1',
    'Parte 2: clausola 6.8.3',
    'Parte 2: clausola 6.8.5',
    'Parte 2: OVR-6.8.6-02',
    'Parte 2: OVR-6.8.6-03',
    'Parte 2: OVR-6.8.6-04a',
    'Parte 2: OVR-6.8.6-04b',
    'Parte 2: clausola 6.8.7',
    'Parte 2: clausola 6.8.8',
    'Parte 2: clausola 6.8.9',
    'Parte 2: clausola 6.8.10',
    'Parte 2: clausola 6.8.11',
    'Parte 2: clausola 6.8.12',
    'Parte 2: clausola 6.8.14',
    'Parte 2: clausola 6.8.16',
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from seed_data.lib import verifica_copertura, verifica_completezza_testo_integrale

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)

    class _Modulo:
        pass

    _m = _Modulo()
    _m.RIGHE_OBBLIGHI = RIGHE_OBBLIGHI
    _m.RIGHE_PRINCIPI = RIGHE_PRINCIPI
    verifica_completezza_testo_integrale([_m])

    print(
        f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
        f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti."
    )
