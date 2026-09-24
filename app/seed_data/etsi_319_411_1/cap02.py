"""Estrazione granulare ETSI EN 319 411-1 V1.5.1 (2025-04) — Capitolo 2:
clausola 4 (General concepts: 4.1, 4.2 con 4.2.1/4.2.2/4.2.3, 4.3) e clausola 5
(General provisions on CPS/CP: 5.1-5.5, inclusi i sottoparagrafi PKI
participants 5.4.1-5.4.3).

Fonte 17 (numerazione definitiva cablata dalla sessione principale in
app/seed.py — questo modulo NON tocca seed.py). Testo ufficiale in
app/.source_cache/etsi_319_411_1/cap02.txt (e raw.txt per il recupero delle
porzioni corrotte dall'estrazione PDF, vedi sotto). Manifest di split:
app/.source_cache/etsi_319_411_1/manifest.json.

Modellazione (ADR-0007), stesso criterio già applicato a ETSI EN 319 401
(Fonte 10) e ETSI TS 119 461 (Fonte 9) per un capitolo tecnico ETSI a
clausole/requisiti numerati con prefisso <SIGLA>-<clausola>-<NN> (qui
"OVR-"):

Clausola 4 "General concepts" (4.1, 4.2.1, 4.2.2, 4.2.3, 4.3) è interamente
priva di identificatori REQ propri: ogni sottoclausola è prosa concettuale
che introduce/definisce un concetto (CPS, CP, termini e condizioni/PKI
disclosure statement, scomposizione dei servizi di certificazione) e
rinvia esplicitamente alla clausola dove il requisito normativo vero e
proprio è enunciato (es. 4.2.1 rinvia a "clause 5.2" per la CPS; 4.2.3
rinvia a "clause 6.9.4" per i termini e condizioni). Per esplicita
istruzione dell'incarico, "General concepts" e "General provisions"
(clausole 4 e 5 di questo documento) ricadono nella categoria "altro" di
tipo_principio (non "definitorio", riservato alla clausola 3
Definizioni/abbreviazioni/notazioni in questo censimento) — applicato
uniformemente a tutti i nodi Principio di questo capitolo, inclusi 4.2.x
(che pure "definiscono" CPS/CP) e 5.3/5.4.2 (che pure enumerano
identificatori/categorie di soggetto), poiché appartengono strutturalmente
a "General concepts"/"General provisions", non alla clausola Definizioni.

4.2.2 "Certificate Policy": nessun identificatore REQ nell'intera
sottoclausola (verificato sul testo integrale), inclusa l'enumerazione
delle sette CP (1-7, marcatori numerici senza prefisso REQ proprio) — resta
quindi UN SOLO nodo Principio "altro" per l'intera sottoclausola, per la
regola generale "lista senza propri identificatori di requisito -> unico
nodo" (qui applicata a un'enumerazione numerata anziché a lettere, stesso
principio). Nessuna frase della sottoclausola impone direttamente un
comportamento al TSP in modo autonomo dal documento richiamato (la frase
"it is mandatory for a TSP to identify the trust service policies it
supports" ripete testualmente un obbligo già stabilito da ETSI EN 319 401,
non lo crea qui) — coerente con la scelta Principio anziché Obbligo.

RICOSTRUZIONE DI TESTO CORROTTO DALL'ESTRAZIONE PDF (due punti, entrambi
documentati per trasparenza, stesso trattamento già riservato alla Figura 2
di ETSI TS 119 461 cap02.py — "il testo estratto dal PDF per quella tabella
è visibilmente corrotto dall'estrazione ... la sintesi discorsiva del
contenuto informativo è più fedele del testo grezzo"):

1. Pagine 17-18 (dopo la clausola 4.3, prima di "OVR-5.1-01"): il testo
   grezzo (app/.source_cache/etsi_319_411_1/raw.txt, righe 427-431)
   contiene una tabella markdown di 2 righe x 10 celle risultante dalla
   conversione PDF->testo della Figura 1 (diagramma illustrativo, didascalia
   "Figure 1: Illustration of subdivision of certification services"), con
   le celle mescolate senza ordine di lettura coerente e intrecciate con il
   titolo/premessa della clausola 5 (che nel testo pulito NON compare affatto
   come intestazione "## 5"/"#### 5.1" — è recuperabile solo da questa
   tabella). Due nodi Principio "altro" separati ricostruiscono il
   contenuto: "Parte 1: clausola 4.3 (Figura 1)" (contenuto del diagramma: il sesto
   servizio componente opzionale "Subject device provision service", non
   elencato nei cinque bullet di 4.3; NOTE 3; NOTE 4; rinvio alla clausola
   6) e "Parte 1: clausola 5 (premessa)" (titolo di clausola 5 + le due frasi di
   premessa sul suo allineamento a IETF RFC 3647 e sull'ambito dei servizi
   trattati). La ricostruzione unisce letteralmente frammenti di frase
   spezzati a metà tra celle adiacenti (es. "...and distributes" + "the
   module to the registered subject." sono chiaramente la stessa frase
   spezzata dalla tabella); le etichette pure di diagramma (nomi di attori/
   frecce già impliciti nei 5 servizi di 4.3, es. "Subscriber/Subject",
   "Relying Party", "Certification Request") sono elencate sinteticamente
   anziché ripetute come prosa piena, per non affermare come "verbatim" un
   ordine di lettura che il diagramma originale non specificava linearmente.
2. Pagine 20-21 (clausola 5.4.2, elenco "To request a certificate for
   natural person the subscriber is:"): la lista a tre voci (persona fisica
   stessa; persona fisica mandataria; ente associato alla persona fisica) è
   spezzata da un'interruzione di pagina in una tabella markdown di 2 celle
   con marcatori di bullet "-"/"- -" anomali; ricostruita nell'ordine di
   lettura naturale (nessuna parola aggiunta, solo la formattazione a bullet
   corretta) nel nodo "Parte 1: clausola 5.4.2".

Requisiti "Void" (OVR-5.1-01, OVR-5.1-02, OVR-5.2-03): segnaposto di
redazione per requisiti soppressi in edizioni precedenti, senza NOTE
autonoma di rinvio -> ESCLUSI dall'indice, stesso trattamento
sistematicamente riservato a ogni altro requisito "Void" puro nelle fonti
precedenti (ETSI TS 119 461, ETSI EN 319 431-1/2).

tipo_obbligo: "procedurale" per i requisiti di pura ereditarietà/rinvio tra
policy o verso altri documenti normativi (OVR-5.1-01A/02A "unless otherwise
specified... shall apply"; OVR-5.2-01/06/07/07A/07B/08/08A/08B/09, tutti
"clause X of BRG/EVCG shall apply" o obblighi di monitoraggio/conformità
verso BRG/EVCG), stesso criterio già applicato in ETSI EN 319 431-1 cap02.py
per OVR-6.4.3-01A ("The requirements REQ-... in ETSI EN 319 401 shall
apply" -> procedurale); "organizzativo" per i requisiti sul contenuto/
struttura della documentazione di governance (OVR-5.1-03, OVR-5.2-02/03A/04,
OVR-5.3-01, OVR-5.4.1-01/02/03, OVR-5.4.3-01); "informativo/trasparenza" per
gli obblighi di pubblicazione/divulgazione esplicita verso l'esterno
(OVR-5.2-05 pubblicazione online 24x7 della CPS; OVR-5.2-11 dichiarazione
dei limiti di lunghezza applicati); "tecnico/sicurezza" per il requisito
sulla prassi di uso delle chiavi CA (OVR-5.2-10).

Marcature [NCP+, EVCP]/[OVCP]/[CONDITIONAL] ecc.: mantenute in
`testo_integrale`, sintetizzate in `condizione_applicabilita`, omesse dal
solo `riferimento` (OVR-5.1-01A/02A, OVR-5.2-06/07/07A/07B/08/08A/08B/09,
OVR-5.4.1-03).

RELAZIONI: vuoto per vincolo di fase — nessuna relazione, né interna al
capitolo né cross-capitolo/cross-fonte (incluso il potenziale legame con
ETSI EN 319 401 [9] richiamato ripetutamente in questo capitolo, e con
ETSI EN 319 411-2 che costruisce le proprie QCP policy su queste NCP/NCP+).
Verrà eventualmente popolato dalla pipeline dedicata (ADR-0009) o da una
cura editoriale successiva.

Conteggio finale: 12 Principio, 23 Obbligo (35 nodi totali, copertura
completa delle clausole 4 e 5 verificata da verifica_copertura).
"""

RIGHE_OBBLIGHI = [
    {
        'riferimento': 'Parte 1: OVR-5.1-01A',
        'testo': 'Per le policy NCP+ ed EVCP si applicano, salvo diversa indicazione, tutti i requisiti previsti per la policy NCP.',
        'testo_integrale': 'OVR-5.1-01A [NCP+, EVCP]: Unless otherwise specified, all requirements specified for [NCP] shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'Si applica alle policy NCP+ ed EVCP.',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.1-02A',
        'testo': 'Per le policy DVCP, IVCP e OVCP si applicano, salvo diversa indicazione, tutti i requisiti previsti per la policy LCP.',
        'testo_integrale': 'OVR-5.1-02A [DVCP], [IVCP], [OVCP]: Unless otherwise specified, all requirements specified for [LCP] shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'Si applica alle policy DVCP, IVCP e OVCP.',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.1-03',
        'testo': "La CP del TSP dovrebbe specificare i requisiti per l'uso dei profili di certificato.",
        'testo_integrale': "OVR-5.1-03: The TSP's CP should specify the requirements for the use of certificate profiles.",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-01',
        'testo': 'Si applicano i requisiti generali di ETSI EN 319 401, clausola 6.1, oltre ai particolari requisiti seguenti; il TSP può documentare le prassi relative a requisiti CP specifici separatamente dal documento CPS principale.',
        'testo_integrale': 'OVR-5.2-01: The general requirements specified in ETSI EN 319 401 [9], clause 6.1 shall apply. In addition the following particular requirements apply: NOTE 1: A TSP can document practices relating to specific CP requirements separate from the main CPS document.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-02',
        'testo': 'La CPS del TSP dovrebbe essere strutturata in conformità a IETF RFC 3647.',
        'testo_integrale': "OVR-5.2-02: The TSP's CPS should be structured in accordance with IETF RFC 3647 [i.3].",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-03A',
        'testo': 'La/le CP identificate dalla documentazione del TSP dovrebbero specificare i requisiti sui profili di certificato da usare.',
        'testo_integrale': "OVR-5.2-03A: The CP(s) identified by the TSP's documentation should specify the requirements on certificate profiles to be used.",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-04',
        'testo': 'La CPS del TSP deve includere gli algoritmi di firma e i parametri impiegati.',
        'testo_integrale': "OVR-5.2-04: The TSP's CPS shall include the signature algorithms and parameters employed.",
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-05',
        'testo': 'Il TSP deve pubblicare la propria CPS tramite un mezzo online disponibile 24 ore su 24, 7 giorni su 7; non è obbligato a divulgare aspetti che contengano informazioni sensibili.',
        'testo_integrale': 'OVR-5.2-05: The TSP shall publicly disclose its CPS through an online means that is available on a 24×7 basis. NOTE 2: The TSP is not obliged to disclose any aspects containing sensitive information.',
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-06',
        'testo': 'Per le policy OVCP, IVCP e DVCP si applica il requisito che precede la clausola 2.1 nella clausola 2 della BRG.',
        'testo_integrale': 'OVR-5.2-06 [OVCP], [IVCP] and [DVCP]: The requirement preceding clause 2.1 in clause 2 of the BRG [6] shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'Si applica alle policy OVCP, IVCP e DVCP.',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-07',
        'testo': 'Per le policy OVCP, IVCP e DVCP si applica la clausola 2.2 della BRG.',
        'testo_integrale': 'OVR-5.2-07 [OVCP], [IVCP] and [DVCP]: Clause 2.2 of BRG [6] shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'Si applica alle policy OVCP, IVCP e DVCP.',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-07A',
        'testo': "Per le policy OVCP, DVCP e IVCP, il TSP deve verificare l'esistenza di revisioni più recenti della BRG e garantire la conformità all'ultima versione, non appena efficace secondo quanto specificato dal CAB Forum.",
        'testo_integrale': 'OVR-5.2-07A [OVCP], [DVCP], [IVCP]: The TSP shall check for newer revisions of BRG [6] and ensure compliance to the latest version of BRG documents as they become effective as specified by the CAB Forum.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'Si applica alle policy OVCP, DVCP e IVCP.',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-07B',
        'testo': 'In caso di conflitto tra i requisiti del presente documento e le ultime versioni della BRG, prevalgono i requisiti BRG, salvo che un requisito del presente documento sia più stringente, nel qual caso resta applicabile; ciò non costituisce non conformità rispetto alle policy ETSI DVCP, OVCP o IVCP.',
        'testo_integrale': "OVR-5.2-07B [CONDITIONAL]: In case of conflict between the present document's requirements and the latest versions of BRG [6], the BRG [6] requirements shall take precedence unless a requirement in the present document is more stringent, in which case it remains applicable. NOTE 3: Implications of the above condition do not constitute non-conformities against the ETSI DVCP, OVCP, or IVCP policies.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'Si applica in caso di conflitto tra i requisiti del presente documento e le ultime versioni della BRG.',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-08',
        'testo': 'Per la policy EVCP si applica la clausola 2.2 della EVCG.',
        'testo_integrale': 'OVR-5.2-08 [EVCP]: Clause 2.2 of EVCG [4] shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'Si applica alla policy EVCP.',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-08A',
        'testo': "Per la policy EVCP, il TSP deve verificare l'esistenza di revisioni più recenti della EVCG e garantire la conformità all'ultima versione, non appena efficace secondo quanto specificato dal CAB Forum.",
        'testo_integrale': 'OVR-5.2-08A [EVCP]: The TSP shall check for newer revisions of EVCG and ensure compliance to the latest version of EVCG documents as they become effective as specified by the CAB Forum.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'Si applica alla policy EVCP.',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-08B',
        'testo': 'In caso di conflitto tra i requisiti del presente documento e le ultime versioni della EVCG, prevalgono i requisiti EVCG, salvo che un requisito del presente documento sia più stringente, nel qual caso resta applicabile; ciò non costituisce non conformità rispetto alla policy ETSI EVCP.',
        'testo_integrale': "OVR-5.2-08B [CONDITIONAL]: In case of conflict between the present document's requirements and the latest versions of EVCG, the EVCG requirements shall take precedence unless a requirement in the present document is more stringent, in which case it remains applicable. NOTE 4: Implications of the above condition do not constitute non-conformities against the ETSI EVCP policy.",
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'Si applica in caso di conflitto tra i requisiti del presente documento e le ultime versioni della EVCG.',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-09',
        'testo': 'Per la policy EVCP si applica la clausola 2 della EVCG.',
        'testo_integrale': 'OVR-5.2-09 [EVCP]: Clause 2 of EVCG [4] shall apply.',
        'tipo_obbligo': 'procedurale',
        'stato': 'vigente',
        'condizione_applicabilita': 'Si applica alla policy EVCP.',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-10',
        'testo': "La CPS del TSP deve specificare la prassi relativa all'uso delle chiavi della CA per la firma di certificati, CRL e OCSP.",
        'testo_integrale': "OVR-5.2-10: The TSP's CPS shall specify the practice regarding the use of CA keys for signing certificates, CRLs and OCSP.",
        'tipo_obbligo': 'tecnico/sicurezza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.2-11',
        'testo': 'Se il TSP applica limiti di lunghezza a qualsiasi attributo di naming del soggetto superiori ai limiti indicati in IETF RFC 5280, tali limiti applicati dovrebbero essere indicati nella CPS pubblicata dal TSP o nei termini e condizioni.',
        'testo_integrale': "OVR-5.2-11: If the TSP applies size limits on any subject naming attributes which are longer than the limits stated in IETF RFC 5280 [8] then the applied size limits should be stated in the TSP's published certification practice statement or terms and conditions.",
        'tipo_obbligo': 'informativo/trasparenza',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.3-01',
        'testo': "Se sono apportate modifiche a una CP di cui alla clausola 4.2.2 che ne alterano l'applicabilità, l'identificatore di policy dovrebbe essere cambiato.",
        'testo_integrale': 'OVR-5.3-01: If any changes are made to a CP as described in clause 4.2.2 which affects the applicability then the policy identifier should be changed.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.4.1-01',
        'testo': 'Il TSP può avvalersi di altre parti per fornire componenti del servizio di certificazione, mantenendo comunque la responsabilità complessiva del rispetto dei requisiti di policy (ETSI EN 319 401, requisiti REQ-7.14.3-01X e REQ-7.14.3-02X): ad es. può subappaltare tutti i servizi componenti, incluso il servizio di generazione dei certificati (la CA), ma la chiave usata per firmare i certificati resta identificata come appartenente alla CA e il TSP resta responsabile del rispetto dei requisiti del documento.',
        'testo_integrale': 'OVR-5.4.1-01: The TSP may make use of other parties to provide parts of the certification service. NOTE: However, the TSP always maintains overall responsibility and ensures that the policy requirements identified in the present document are met (ETSI EN 319 401 [9], requirements REQ-7.14.3-01X and REQ-7.14.3-02X). EXAMPLE: A TSP can sub-contract all the component services, including the certificate generation service (referred to as the CA in the present document). However, the key used to sign the certificates is identified as belonging to the CA, and the TSP maintains overall responsibility for meeting the requirements defined in the present document.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.4.1-02',
        'testo': 'Il TSP può prevedere una gerarchia di CA.',
        'testo_integrale': 'OVR-5.4.1-02: A TSP may include a hierarchy of CAs.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.4.1-03',
        'testo': 'Quando il TSP prevede una gerarchia di CA subordinate fino a una CA radice, il TSP è responsabile di garantire che le CA subordinate rispettino i requisiti di policy applicabili.',
        'testo_integrale': 'OVR-5.4.1-03 [CONDITIONAL]: Where a TSP includes a hierarchy of subordinate CAs up to a root CA, the TSP shall be responsible for ensuring the subordinate-CAs comply with the applicable policy requirements.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'condizione_applicabilita': 'Si applica quando il TSP prevede una gerarchia di CA subordinate fino a una CA radice.',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
    {
        'riferimento': 'Parte 1: OVR-5.4.3-01',
        'testo': 'Altri partecipanti, non coperti dal presente documento, possono essere identificati dal TSP.',
        'testo_integrale': 'OVR-5.4.3-01: Other participants, not covered by the present document, may be identified by the TSP.',
        'tipo_obbligo': 'organizzativo',
        'stato': 'vigente',
        'soggetti': [{'categoria': 'QTSP/gestore', 'ruolo': 'obbligato'}],
    },
]

RIGHE_PRINCIPI = [
    {
        'riferimento': 'Parte 1: clausola 4.1',
        'testo': "Per l'inquadramento concettuale generale sui requisiti di policy si rimanda a ETSI EN 319 401 (clausola 4) e a IETF RFC 3647 (clausole 3.1 e 3.4).",
        'testo_integrale': '4.1 General policy requirements concepts: See ETSI EN 319 401 [9], clause 4 and IETF RFC 3647 [i.3], clauses 3.1 and 3.4 for guidance.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 1: clausola 4.2.1',
        'testo': 'La Certification Practice Statement (CPS) descrive COME il TSP eroga il proprio servizio di certificazione (a differenza della Certificate Policy, che descrive COSA deve essere rispettato): è di proprietà del TSP, definisce come sono soddisfatti i requisiti tecnici/organizzativi/procedurali della CP applicabile (v. clausola 5.2), e può essere integrata da documentazione operativa di dettaglio a diffusione interna, riservata e fuori scopo del presente documento.',
        'testo_integrale': '4.2.1 Certification Practice Statement: In general, the Certificate Policy (CP) (see clause 4.2.2), referenced by a policy identifier in a certificate, states "what is to be adhered to", while a Certification Practice Statement (CPS) states "how it is adhered to", i.e. the processes the TSP will use in creating and maintaining the certificate. The TSP issuing certificates develops, implements, enforces, and updates a Certification Practice Statement (CPS) which is a trust service practice statement such as defined in ETSI EN 319 401 [9]. See clause 5.2. The CPS describes how the TSP operates its service and is owned by the TSP: it is tailored to the organizational structure, operating procedures, facilities, and computing environment of the TSP. The CPS defines how the TSP meets the technical, organizational and procedural requirements identified in a Certificate Policy (CP) (see clause 4.2.2). For example, where the CP requires secure management of the private key(s), the CPS can describe the dual-control, secure storage practices, and so on, relying on operational procedures that in turn can provide the details with locations, access lists and access procedures. NOTE: The operational procedures mentioned above can be in low-level documents providing the specific details necessary to complete the practices identified in the CPS. This documentation is generally regarded as internal, e.g. defining specific tasks and responsibilities within the organization. Such documentation can be used in the daily operation of the TSP and reviewed by those doing a process review, but due to its internal nature it is considered private and proprietary and therefore beyond the scope of the present document. The published CPS can thus be limited to the information useful for subscribers/subject and relying parties, and be completed by (confidential) elements that do not have to be disclosed. The target audience of the practice statements can be the auditors, the subscribers, the subjects and the relying parties. The present document provides requirements identified as necessary to support state-of-the-art certification services built on best practices.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 1: clausola 4.2.2',
        'testo': 'La Certificate Policy (CP) descrive COSA è il certificato in termini di qualità/profilo/applicabilità; può essere definita dal TSP, da terzi, da governi/organizzazioni internazionali, dai sottoscrittori o dagli utenti dei servizi di certificazione, e non deve necessariamente far parte della documentazione del TSP. Il documento definisce sette CP: tre CP di riferimento — NCP (best practice generalmente riconosciuta), NCP+ (come NCP, ma con dispositivo crittografico sicuro) e LCP (qualità meno onerosa della NCP) — più quattro CP per certificati SSL/TLS allineate ai requisiti CAB Forum (EVCG/BRG): EVCP (Extended Validation, basata su NCP), DVCP (Domain Validation, basata su LCP), OVCP (Organizational Validation, basata su LCP) e IVCP (Individual Validation, basata su LCP). In caso di conflitto tra il presente documento e le ultime versioni di BRG/EVCG prevale BRG/EVCG.',
        'testo_integrale': "4.2.2 Certificate Policy: A Certificate Policy (CP) describes what the certificate is in terms of quality (requirements to be adhered to), profile, applicability, etc. It can contain diverse information beyond the scope of the present document to indicate the applicability of the service (e.g. the detailed description of the certificate profile). A CP is a specific type of trust service policy as defined in ETSI EN 319 401 [9]. According to ETSI EN 319 401 [9], it is mandatory for a TSP to identify the trust service policies it supports. Such policy is defined independently of the specific details of the specific operating environment of a TSP and is not necessarily part of the TSP's documentation; practice statement and general terms and conditions are sufficient. Following ETSI EN 319 401 [9], a CP can apply to several TSPs supporting a user community that abide by the common set of rules specified in that CP. A CP can be defined, for example: by the TSP, by a third party (e.g. standardization organizations such as ETSI), by national government or international organizations, by the customers (subscribers) of the TSP or by the users of certification services. The CPS is defined by the TSP. When the TSP does not issue its own CP, it is expected that the TSP provides minimal information about the certification service it offers in its documentation (CPS or terms and conditions (see clause 4.2.3), including the indication that it complies with all rules valid for a given referred CP, in the case of the present document as specified in clause 5 or clause 7. The present document does not put constraints on the form of the CPs; a CP can be a stand-alone document or be provided as part of the practice statements and/or the general terms and conditions. The target audience of the CP can be the subscribers, the subjects and the relying parties. NOTE: Subscribers and relying parties can consult the CPS and/or terms and conditions of the issuing TSP to obtain details how the CP is implemented by the TSP. These documents can refer to each other. For certification services, the identification of the CP is communicated through the documentation provided to the subscribers and relying parties and in addition, as described in IETF RFC 3647 [i.3], clause 3.3, certificates include a CP identifier which can be used by relying parties in determining the certificates' suitability and trustworthiness for a particular application. TSP conforming to the present document's normative requirements may use OIDs defined in the present document in its documentation and in the certificates it issues. The present document defines seven CPs. Three reference CPs: 1) A Normalized Certificate Policy (NCP) which meets general recognized best practice for TSPs issuing certificates used in support of any type of transaction. 2) An extended Normalized Certificate Policy (NCP+) which offers the same quality as that offered by the NCP for use where a secure cryptographic device (signing or decrypting) is considered necessary. The requirements for this CP include the policy requirements for the issuance and management of NCP certificates. 3) A Lightweight Certificate Policy (LCP) offering a quality of service less onerous than the NCP (requiring less demanding policy requirements) for use where a risk assessment does not justify the additional burden of meeting all requirements of the NCP (e.g. physical presence), for certificates used in support of any type of transaction (such as digital signatures, web authentication). The following four CPs for SSL/TLS certificates based on the reference CPs and offering the level of assurance required by CAB Forum documents EVCG [4] and BRG [6]: NOTE: The intent of the present document is to include requirements so that a TSP that asserts the ETSI DVCP, OVCP, IVCP or EVCP policy OIDs in the IETF RFC 5280 [8] certificatePolicies extension of SSL/TLS certificates, also adheres to the corresponding CAB Forum policies for DV, OV, IV Certificates as defined in [6] or EV certificates as defined in EVCG [4]. Following one of the below CPs requires to follow the full and latest version of BRG [6] or EVCG [4]. As a consequence, for compliance with BRG/EVCG the TSP is required to augment the policy requirements defined in the present document with any additional requirements specific to the identified BRG [6] or EVCG [4] policy. It is recognized that further updates of BRG/EVCG may occur after the publication of the present document. In case of conflict between any requirement in the current version of the present document, be it a [LCP], [OVCP], [IVCP]or [DVCP] or a [NCP] or [EVCP] labelled requirement, the latest version of BRG [6] or EVCG [4] takes precedence. In case of conflicting requirements between latest version of CA/Browser Forum [4] policies for SSL/TLS Certificates and the present document, it is requested that this is brought to the attention of ETSI TC ESI and the CAB Forum. ETSI TC ESI will endeavour to monitor revisions to the BRG/EVCG and reference the latest version within the revision cycle of the present document. 4) An Extended Validation Certificate Policy (EVCP) for TLS/SSL certificates offering the level of assurance required by CAB Forum for EVC. The requirements for this CP are built on the policy requirements for the issuance and management of NCP certificates, enhanced to refer to requirements from EVCG [4]. It includes, except where explicitly indicated, all the Normalized Certificate Policy (NCP) requirements, plus additional provisions suited to support EVC issuance and management as specified in EVCG [4]. 5) A Domain Validation Certificate Policy (DVCP) for TLS/SSL certificates offering the level of assurance required by CAB Forum for DVC. The policy requirements for this CP are built on the policy requirements for the issuance and management of LCP certificates, enhanced to refer to requirements from the BRG [6] as applicable to domain validation certificates. It includes, except where explicitly indicated, all the Lightweight Certificate Policy (LCP) requirements, plus additional provisions suited to support DVC issuance and management as specified in BRG [6]. 6) An Organizational Validation Certificate Policy (OVCP) for TLS/SSL certificates offering the level of assurance required by CAB Forum for OVC. The policy requirements for this CP are built on the policy requirements for the issuance and management of LCP certificates, enhanced to refer to requirements from BRG [6] as applicable to organizational validation certificates. It includes, except where explicitly indicated, all the Lightweight Certificate Policy (LCP) requirements, plus additional provisions suited to support OVC issuance and management as specified in BRG [6]. 7) An Individual Validation Certificate Policy (IVCP) for TLS/SSL certificates offering the level of assurance required by CAB Forum for IVC. The policy requirements for this CP are built on the policy requirements for the issuance and management of LCP certificates, enhanced to refer to requirements from the BRG [6] as applicable to individual validation certificates. It includes, except where explicitly indicated, all the Lightweight Certificate Policy (LCP) requirements, plus additional provisions suited to support IVC issuance and management as specified in BRG [6]. The above CPs can be used as they are without amendments but can also be used as a basis for creating more elaborate policies; clause 7 specifies a framework for other CPs which enhance or further constrain the above policies.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 1: clausola 4.2.3',
        'testo': 'Il TSP è tenuto a pubblicare termini e condizioni (v. clausola 6.9.4), come parte di CPS/CP o come documento a sé stante, rivolti a sottoscrittori, soggetti e relying party. Il PKI disclosure statement è la parte dei termini e condizioni del TSP relativa al funzionamento della PKI. Il presente documento impone la presenza di alcuni elementi minimi nei termini e condizioni ma non ne vincola la forma, che può anche dipendere dalla normativa nazionale.',
        'testo_integrale': "4.2.3 Terms and conditions and PKI disclosure statement: A TSP is required to issue terms and conditions (see clause 6.9.4). This can be as part of the CPS or the CP if issued by the TSP. Alternatively, this can be a standalone document. The terms and conditions are specific to a TSP. The target audience of the terms and conditions can be the subscribers, the subjects and the relying parties. The PKI disclosure statement is that part of the TSP's terms and conditions which relate to the operation of the PKI. NOTE: The presence of some elements is mandatory in the terms and conditions as requested in the present document, however the present document places no restriction on the form of terms and conditions; it can be a standalone document for a public audience, or it can be split over subscriber's agreement(s) and information to relying parties. The form and content of the terms and conditions can also depend on national regulations.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 1: clausola 4.3',
        'testo': 'Il documento non impone alcuna suddivisione dei servizi del TSP; ai soli fini di classificare i requisiti, i servizi di certificazione sono scomposti in: servizio di registrazione (verifica identità/attributi del soggetto, incluso il possesso/controllo delle chiavi private non generate dalla CA); servizio di generazione dei certificati (crea e firma i certificati, può includere la generazione delle chiavi); servizio di diffusione (rende disponibili i certificati a soggetti/relying party, nonché termini e condizioni e informazioni di policy/practice); servizio di gestione delle revoche (elabora richieste/segnalazioni di revoca); servizio di stato della revoca (fornisce alle relying party le informazioni sullo stato di revoca).',
        'testo_integrale': "4.3 Certification services: NOTE 1: The present document does not mandate any subdivision of the services of a TSP. Requirements are stated in subsequent clauses. The certification services are broken down in the present document into the following component services for the purposes of classifying requirements: Registration service: verifies the identity and if applicable, any specific attributes of a subject. The results of this service are passed to the certificate generation service. NOTE 2: This service includes proof of possession of, or control over, non-CA generated subject private keys. Certificate generation service: creates and signs certificates based on the identity and other attributes verified by the registration service. This can include key generation. Dissemination service: disseminates certificates to subjects, and if the subject consents, makes them available to relying parties. This service also makes available the TSP's terms and conditions, and any published policy and practice information, to subscribers and relying parties. Revocation management service: processes requests and reports relating to revocation to determine the necessary action to be taken. The results of this service are distributed through the revocation status service. Revocation status service: provides certificate revocation status information to relying parties.",
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 1: clausola 4.3 (Figura 1)',
        'testo': 'Contenuto ricostruito da una tabella di estrazione PDF corrotta (pagina 17 del testo ufficiale, diagramma Figura 1): illustra le relazioni tra i servizi di clausola 4.3 e introduce un ulteriore servizio componente opzionale, il "Subject device provision service" (fornitura al soggetto di un modulo di creazione della firma con relativi codici di attivazione, oppure generazione della coppia di chiavi del soggetto con distribuzione della chiave privata anche in forma "soft", oppure messa a disposizione di dispositivi crittografici sicuri). Questa suddivisione è solo a fini di classificazione dei requisiti e non vincola l\'implementazione del TSP. NOTE 3 elenca esempi di output del servizio di diffusione (certificato, termini e condizioni della CA); NOTE 4 chiarisce che la Figura 1 è puramente illustrativa; la clausola 6 reca i requisiti specifici per ciascun servizio.',
        'testo_integrale': 'Figure 1 illustrates the interrelationship between the services described in clause 4.3, adding a further, optional component service: Subject device provision service (optional): a service which prepares the subject\'s signature-creation module and enabling codes and distributes the module to the registered subject; or a service which generates the subject\'s key pair and distributes the private key to the subject (this includes "soft" keys i.e. keys protected by software environment); or a service which prepares, and provides or makes available, secure cryptographic devices, or other secure devices, to subjects. This subdivision of services is only for the purposes of clarification of policy requirements and places no restrictions on any subdivision of an implementation of the TSP\'s services. The diagram identifies the following actors and flows: Subscriber/Subject, Relying Party and Authorized party; Certification Request and Revocation Request; Registration Service, Certificate Generation Service, Dissemination Service, Revocation Management Service and Certificate Revocation Status Service; Secure cryptographic device and Subject Device Provision Service; Revocation Status Information; and the output of the Dissemination Service (Certificate, CA terms and conditions). NOTE 3: Examples of this service are: Certificate, CA terms and conditions. Figure 1: Illustration of subdivision of certification services used in the present document. NOTE 4: Figure 1 is for illustrative purposes. Clause 6 specifies the specific requirements for each of the services.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 1: clausola 5 (premessa)',
        'testo': 'Titolo e premessa della clausola 5 ("Disposizioni generali su Certification Practice Statement e Certificate Policy"), ricostruiti da una tabella di estrazione PDF corrotta a cavallo delle pagine 17-18: il documento è strutturato in linea con IETF RFC 3647 per assistere i TSP nell\'applicare i requisiti alla propria documentazione, e comprende la fornitura dei servizi di registrazione, generazione dei certificati, diffusione, gestione delle revoche e stato della revoca (v. clausola 4.3).',
        'testo_integrale': '5 General provisions on Certification Practice Statement and Certificate Policies. The present document is structured broadly in line with IETF RFC 3647 [i.3] to assist TSPs in applying these requirements to their own documentation. The present document includes the provision of services for registration, certificate generation, dissemination, revocation management and revocation status (see clause 4.3).',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 1: clausola 5.1 (premessa)',
        'testo': 'I requisiti sono espressi in termini di obiettivi di sicurezza seguiti, ove necessario, da requisiti più specifici sui controlli per raggiungerli. Il dettaglio dei controlli richiesti bilancia la necessaria fiducia con la minimizzazione delle restrizioni sulle tecniche impiegabili dal TSP; in alcuni casi si rinvia a standard più generali per requisiti di controllo più dettagliati, per cui la specificità dei requisiti può variare da argomento ad argomento.',
        'testo_integrale': '5.1 General requirements: The requirements are indicated in terms of the security objectives followed by more specific requirements for controls to meet those objectives where considered necessary to provide the necessary confidence that those objective will be met. NOTE: The details of controls required to meet an objective is a balance between achieving the necessary confidence whilst minimizing the restrictions on the techniques that a TSP can employ in issuing certificates. In some cases reference is made to other more general standards which can be used as a source of more detailed control requirements. Due to these factors the specificity of the requirements given under a given topic can vary.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 1: clausola 5.3',
        'testo': 'Come descritto in IETF RFC 3647 clausola 3.3, i certificati includono un identificatore di CP utilizzabile dalle relying party per valutarne idoneità e affidabilità per una data applicazione. Il documento definisce sette identificatori (OID), tutti nel ramo itu-t(0) identified-organization(4) etsi(0) other-certificate-policies(2042) policy-identifiers(1): a) NCP = ncp(1); b) NCP+ = ncpplus(2); c) LCP = lcp(3); d) EVCP = evcp(4); e) DVCP = dvcp(6); f) OVCP = ovcp(7); g) IVCP = ivcp(8).',
        'testo_integrale': '5.3 Certificate Policy name and identification: As described in IETF RFC 3647 [i.3], clause 3.3, certificates include a CP identifier which can be used by relying parties in determining the certificates suitability and trustworthiness for a particular application. The identifiers for the certificate policies specified in the present document are: a) NCP: Normalized Certificate Policy: itu-t(0) identified-organization(4) etsi(0) other-certificate-policies(2042) policy-identifiers(1) ncp (1). b) NCP+: Normalized Certificate Policy requiring a secure cryptographic device: itu-t(0) identified-organization(4) etsi(0) other-certificate-policies(2042) policy-identifiers(1) ncpplus (2). c) LCP: Lightweight Certificate Policy: itu-t(0) identified-organization(4) etsi(0) other-certificate-policies(2042) policy-identifiers(1) lcp (3). d) EVCP: Extended Validation Certificate Policy: itu-t(0) identified-organization(4) etsi(0) other-certificate-policies(2042) policy-identifiers(1) evcp (4). e) DVCP: Domain Validation Certificate Policy: itu-t(0) identified-organization(4) etsi(0) other-certificate-policies(2042) policy-identifiers(1) dvcp (6). f) OVCP: Organizational Validation Certificate Policy: itu-t(0) identified-organization(4) etsi(0) other-certificate-policies(2042) policy-identifiers(1) ovcp (7). g) IVCP: Individual Validation Certificate Policy: itu-t(0) identified-organization(4) etsi(0) other-certificate-policies(2042) policy-identifiers(1) ivcp (8).',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 1: clausola 5.4.1 (premessa)',
        'testo': "La CA è comunemente intesa come un tipo di TSP ai sensi del Regolamento (UE) n. 910/2014, ed anche come una forma di prestatore di servizi di certificazione ai sensi della direttiva 1999/93/CE, che emette certificati a chiave pubblica; nel presente documento il termine indica più propriamente la componente tecnica del TSP dedicata all'emissione dei certificati. L'autorità riconosciuta come fidata dagli utenti dei servizi di certificazione (sottoscrittori e relying party) per l'assegnazione dei certificati è il TSP, che ha la responsabilità complessiva dei servizi di certificazione di cui alla clausola 4.3; sia la CA sia il TSP possono essere identificati nel certificato come emittente, e la chiave privata della CA è usata per firmare i certificati.",
        'testo_integrale': '5.4.1 Certification Authority: A CA is commonly understood to be a type of Trust Service Provider (TSP), as defined in the Regulation (EU) No 910/2014 [i.14], and also a form of certification service provider as defined in the Electronic Signatures Directive 1999/93/EC [i.1], which issues public key certificates. However, in the present document the term is used more to reference the technical component of the TSP concerned with certificate issuance. The authority trusted by the users of the certification services (i.e. subscribers as well as relying parties) to assign certificates is the TSP. The TSP has overall responsibility for the provision of the certification services identified in clause 4.3. The CA, as well as the TSP, can be identified in the certificate as the issuer and its private key is used to sign certificates.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 1: clausola 5.4.2',
        'testo': "Il soggetto (subject) può essere: una persona fisica; una persona fisica identificata in associazione a una persona giuridica; una persona giuridica (organizzazione, unità o dipartimento identificato in associazione a un'organizzazione); oppure un dispositivo o sistema operato da o per conto di una persona fisica o giuridica. Se il sottoscrittore coincide col soggetto, risponde direttamente degli obblighi non correttamente adempiuti; se il sottoscrittore agisce per conto di uno o più soggetti distinti cui è collegato, le responsabilità di sottoscrittore e soggetto sono trattate alla clausola 6.3.4 (REG-6.3.4-09 - REG-6.3.4-17). Il legame sottoscrittore-soggetto segue tre schemi secondo il tipo di certificato richiesto (persona fisica, persona giuridica, dispositivo/sistema), con indicazione di chi può agire da sottoscrittore in ciascun caso; le disposizioni legali locali possono disciplinare il trasferimento di responsabilità a un terzo.",
        'testo_integrale': 'In the framework of the present policies, the subject can be: a natural person; a natural person identified in association with a legal person; a legal person (that can be an Organization or a unit or a department identified in association with an Organization); or a device or system operated by or on behalf of a natural or legal person. When a subscriber is the subject it will be held directly responsible if its obligations are not correctly fulfilled. When the subscriber is acting on behalf of one or more distinct subjects to whom it is linked (e.g. the subscriber is a company requiring certificates for its employees to allow them to participate in electronic business on behalf of the company), responsibilities of the subscriber and of the subject are addressed in clause 6.3.4, REG-6.3.4-09 to REG-6.3.4-17. The link between the subscriber and the subject is one of the following: To request a certificate for natural person the subscriber is: the natural person itself; a natural person mandated to represent the subject; or any entity with which the natural person is associated (such as the company employing the natural person or a non-profit legal person the natural person is member of). NOTE: The local legal dispositions can address the handover of responsibility to a third person. To request a certificate for legal person the subscriber is: any entity as allowed under the relevant legal system to represent the legal person; or a legal representative of a legal person subscribing for its subsidiaries or units or departments. To request a certificate for a device or system operated by or on behalf of a natural or legal person the subscriber is: the natural or legal person operating the device or system; any entity as allowed under the relevant legal system to represent the legal person; or a legal representative of a legal person subscribing for its subsidiaries or units or departments.',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
    {
        'riferimento': 'Parte 1: clausola 5.5',
        'testo': "Le policy NCP, NCP+ e LCP non pongono vincoli sulla comunità di utenti e sull'ambito di applicabilità del certificato. Per gli altri certificati l'ambito è più specifico: lo scopo degli EV Certificates è descritto in EVCG clausola 1.4; lo scopo dei certificati DV/OV/IV è descritto in BRG clausola 1.4.1. I certificati emessi secondo OVCP, DVCP, IVCP o EVCP sono certificati pubblicamente fidati usati per identificare server web accessibili tramite protocollo TLS o SSL (IETF RFC 5246).",
        'testo_integrale': '5.5 Certificate usage: The policies NCP, NCP+ and LCP place no constraints on the user community and applicability of the certificate. The applicability of other certificates is as described below. The specific purpose of EV Certificates is described in EVCG [4], clause 1.4. The specific purpose of DV, OV, IV Certificates is described in BRG [6], clause 1.4.1. Certificates issued under OVCP, DVCP, IVCP or EVCP are for publicly trusted certificates used to identify web servers accessed via the TLS or SSL protocol as per IETF RFC 5246 [i.11].',
        'tipo_principio': 'altro',
        'stato': 'vigente',
    },
]

INDICE_ARTICOLI_LOCALE = [
    'Parte 1: clausola 4.1',
    'Parte 1: clausola 4.2.1',
    'Parte 1: clausola 4.2.2',
    'Parte 1: clausola 4.2.3',
    'Parte 1: clausola 4.3',
    'Parte 1: clausola 4.3 (Figura 1)',
    'Parte 1: clausola 5 (premessa)',
    'Parte 1: clausola 5.1 (premessa)',
    'Parte 1: clausola 5.3',
    'Parte 1: clausola 5.4.1 (premessa)',
    'Parte 1: clausola 5.4.2',
    'Parte 1: clausola 5.5',
    'Parte 1: OVR-5.1-01A',
    'Parte 1: OVR-5.1-02A',
    'Parte 1: OVR-5.1-03',
    'Parte 1: OVR-5.2-01',
    'Parte 1: OVR-5.2-02',
    'Parte 1: OVR-5.2-03A',
    'Parte 1: OVR-5.2-04',
    'Parte 1: OVR-5.2-05',
    'Parte 1: OVR-5.2-06',
    'Parte 1: OVR-5.2-07',
    'Parte 1: OVR-5.2-07A',
    'Parte 1: OVR-5.2-07B',
    'Parte 1: OVR-5.2-08',
    'Parte 1: OVR-5.2-08A',
    'Parte 1: OVR-5.2-08B',
    'Parte 1: OVR-5.2-09',
    'Parte 1: OVR-5.2-10',
    'Parte 1: OVR-5.2-11',
    'Parte 1: OVR-5.3-01',
    'Parte 1: OVR-5.4.1-01',
    'Parte 1: OVR-5.4.1-02',
    'Parte 1: OVR-5.4.1-03',
    'Parte 1: OVR-5.4.3-01',
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []
