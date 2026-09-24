"""Estrazione granulare ETSI TS 119 431-1 V1.3.1 (2024-12) — Capitolo 2:
clausola 7 (Framework for definition of SP built on the present document) +
Annex A normativo (requisiti EUSPv2 legati al Regolamento (EU) 2024/1183) +
Annex B informativo (mapping regolamento/policy) + Annex C informativo
(scope degli standard di firma da remoto). Annex D (Change history) ed
"History" finale ESCLUSI: puro paratesto editoriale (log di versione del
documento), stesso trattamento riservato a "History"/"Change history" in
tutte le fonti precedenti (eIDAS, CAD, DPCM, SPID, ETSI TS 119 461, ...).

Fonte 11 (numerazione definitiva cablata dalla sessione principale in
app/seed.py — questo modulo NON tocca seed.py). Testo ufficiale in
app/.source_cache/etsi_119_431_1/cap02.txt. Manifest di split:
app/.source_cache/etsi_119_431_1/manifest.json. Cap01 (clausole 1-6, letto
solo per verificare i riferimenti citati da questo capitolo, MAI copiato)
in app/.source_cache/etsi_119_431_1/cap01.txt.

Modellazione (ADR-0007), stesso criterio già applicato alle fonti ETSI
precedenti (319 412-5, 119 461, 319 401):

Clausola 7 "Framework for definition of SP built on the present document"
— dieci requisiti OVR-7-01..OVR-7-10, tutti marcati [CONDITIONAL] (si
applicano solo quando un TSP costruisce una propria Signature Policy (SP) a
partire dai requisiti del presente documento, invece di seguire
direttamente uno dei tre profili LSP/NSP/EUSPv2 già definiti) -> un Obbligo
per requisito, soggetto "QTSP/gestore" ruolo "obbligato" (l'entità che
costruisce/gestisce la SP), con `condizione_applicabilita` valorizzata.
OVR-7-03/08/09 hanno anche un destinatario "Utente/titolare" (sottoscrittori
/ comunità di utenti informati o a cui sono rese disponibili le policy).
Nessuna Void in questa clausola. tipo_obbligo: "organizzativo" per governo/
contenuto/processo di revisione della policy (01,02,04,05,06,07,10),
"informativo/trasparenza" per gli obblighi di pubblicazione verso i
sottoscrittori (03,08,09).

Annex A (normative) "Specific requirements related to Regulation (EU)
2024/1183" — requisiti del profilo EUSPv2:
- A.1 "SSASP as a Qualified TSP": la sola frase introduttiva (scopo
  dell'annesso) diventa un Principio "scopo/ambito di applicazione",
  riferimento "Parte 1: A.1". Il requisito numerato associato, OVR-A.1-01, è
  "Void." (segnaposto di redazione per un requisito rimosso in
  un'edizione precedente) -> ESCLUSO dall'indice, stesso trattamento già
  riservato ad ogni altro "Void." puntuale nelle fonti precedenti.
- A.2 "Policy name and identification": pura prosa (OID EUSPv2), nessun
  requisito numerato -> Principio "definitorio", riferimento "Parte 1: A.2".
- A.3 "General requirements" (OVR-A.3-01/02/03), A.4 "Signing key
  generation" (GEN-A.4-01/02), A.5 "Signature activation" (SIG-A.5-01..09),
  A.6 "Signature activation data management" (SIG-A.6-01..05, 06A, 07,
  07A, 08 — SIG-A.6-06 è "Void." ESCLUSO), A.7 "eID means linking"
  (LNK-A.7-01): nessuna di queste sottoclausole ha prosa introduttiva
  propria oltre ai requisiti numerati -> un Obbligo per requisito, soggetto
  "QTSP/gestore" ruolo "obbligato", tutti tipo_obbligo "tecnico/sicurezza"
  (requisiti EUSPv2 di sicurezza/QSCD/SAM/SAD/identity-linking) tranne
  OVR-A.3-02 ("informativo/trasparenza": contenuto del practice statement).
  SIG-A.5-09, SIG-A.6-07 e SIG-A.6-07A sono [CONDITIONAL] ->
  `condizione_applicabilita` valorizzata. LNK-A.7-01 cita ETSI TS 119 461
  (Fonte 9, già censita): nessuna relazione cross-fonte creata (deferita a
  Fase 6/ADR-0009), solo menzione testuale.

Annex B (informative) "Regulation and EU SSAS policy mapping":
- "B.1 Void" + "Table B.1: Void" + "Table B.2: Void": l'intera sottoclausola
  B.1 e le sue due tabelle sono un segnaposto di redazione (mappatura verso
  il precedente Regolamento (EU) n. 910/2014 ante-eIDAS2, rimossa in questa
  edizione) -> stesso trattamento di un requisito "Void" puntuale, ESCLUSA
  dall'indice (non è una disposizione, non enuncia alcun fatto giuridico
  nuovo).
- "B.2 Regulation (EU) 2024/1183" (Tabella B.3): mappa gli artt. 29/29a/39/
  39a e l'Allegato II del Regolamento (EU) 2024/1183 sui requisiti EUSPv2 di
  Annex A e su due requisiti di clausola 6.3.3 (cap01). Per istruzione
  esplicita del batch, NESSUN nodo duplicato per riga della tabella (il
  contenuto è già coperto dai nodi dei requisiti citati, presenti in questo
  stesso capitolo) -> UN SOLO Principio "altro", riferimento "Parte 1: B.2",
  `testo_integrale` = intera Tabella B.3 verbatim (nessuna riga omessa,
  ADR-0010). Le uniche relazioni interne create dal nodo B.2 sono le due
  citazioni esplicite e verificate verso requisiti del CAPITOLO 1
  (GEN-6.3.3-02, GEN-6.3.3-04 — confermati presenti in
  app/.source_cache/etsi_119_431_1/cap01.txt, clausola 6.3.3): relazione
  "richiama", evidence_type "textual". Le citazioni verso requisiti Annex A
  (già in questo stesso file) non generano archi separati per evitare
  ridondanza grafica: sono già nodi pienamente censiti in questo capitolo,
  discoverable senza bisogno di un arco dedicato dalla riga di mapping.
  NOTA testuale (non un arco): la tabella riporta due riferimenti con
  probabile errata di redazione del documento ETSI stesso — "GEN-A.3-03"
  (il requisito realmente esistente con quel contenuto è "Parte 1: OVR-A.3-03") e
  "SIG-A.7-01" (il requisito realmente esistente è "Parte 1: LNK-A.7-01", coerente
  con la rubrica "eID means linking"); riportati verbatim così come scritti
  nella tabella ufficiale (mai "corretti" nel testo_integrale), ma non usati
  come target di una relazione per non inventare un riferimento che non
  esiste con quell'id esatto (istruzione del batch: ometti se non sei
  certo). Nessuna relazione creata verso gli articoli del Regolamento (EU)
  2024/1183/eIDAS2 citati: cross-fonte, deferita alla pipeline ADR-0009.
- L'annesso B non contiene altro testo oltre a B.1/B.2.

Annex C (informative) "Scope of remote signing standards": diversamente da
Annex D (vedi sotto), il batch assegna esplicitamente Annex C a questo
capitolo senza marcarlo come escluso — per ADR-0007 ("mai omettere la
clausola") viene quindi creato un Principio "altro" minimale, riferimento
"Parte 1: C.1": il contenuto testuale disponibile si limita al rinvio alla Figura
C.1 (il contenuto grafico della figura non è estratto come testo nel file
assegnato, quindi non riproducibile in `testo_integrale` oltre alla didascalia
letterale).

Annex D (informative) "Change history" + la sezione "History"/"Document
history" finale del documento (tabella versione/data/changelog e cronologia
delle edizioni): ESCLUSI per istruzione esplicita del batch — puro
paratesto editoriale (nessun requisito, nessun principio giuridico), stesso
trattamento sistematicamente riservato a "History"/"Change history" in
tutte le fonti precedenti (eIDAS, CAD, DPCM, SPID, ETSI TS 119 461, ETSI EN
319 401, ETSI EN 319 412-5).

RELAZIONI interne (tutte fonte_id_o_None=None, risolto alla fonte corrente):
- OVR-A.3-01 ("All requirements specified for [NSP] shall apply.")
  "richiede come precondizione" verso ciascuno dei 15 requisiti marcati
  [NSP] nel capitolo 1 (clausole 6.2/6.3.1: GEN-6.2.1-02, GEN-6.2.1-02A,
  LNK-6.2.2-02A/02B/02C/02D/02E, LNK-6.2.2-08, LNK-6.2.2-08A, LNK-6.2.2-09,
  SIG-6.3.1-05/06/07, SIG-6.3.1-15/16 — elenco esaustivo verificato
  leggendo per intero app/.source_cache/etsi_119_431_1/cap01.txt, nessun
  altro requisito porta il tag [NSP]): il profilo EUSPv2 non può dirsi
  soddisfatto se uno qualsiasi di questi requisiti NSP non è già
  rispettato. evidence_type "textual" (citazione esplicita e delimitata
  del tag "[NSP]", non un rinvio generico).
- SIG-A.5-09 "specifica" SIG-6.3.1-14 (cap01): stesso presupposto
  condizionale letterale ("In case the authentication is linked directly
  to the identity, the signature session shall end at most ... after the
  end of the identity verification process"), ma il profilo EUSPv2
  restringe il termine generale NSP di 2 ore a 30 minuti — specializzazione
  dello stesso requisito per il profilo EUSPv2. evidence_type "inferred"
  (stesso presupposto e stessa struttura di frase, nessuna citazione
  testuale diretta dell'id), confidence 0.75.
- B.2 "richiama" GEN-6.3.3-02 e GEN-6.3.3-04 (cap01): vedi sopra.

Nessuna relazione cross-fonte (eIDAS2, ETSI TS 119 461, EN 419241-1/2 — non
censiti come Fonte separata in questo grafo) e nessuna relazione verso il
capitolo 2 di ETSI TS 119 431-2 (Fonte 12): quest'ultima è deferita alla
Fase 6, non essendoci nel testo di questo capitolo alcuna citazione
esplicita e univoca verso un riferimento di quella fonte.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "Parte 1: OVR-7-01",
        "testo": "Quando si costruisce una Signature Policy (SP) a partire dai requisiti definiti nel presente documento, la policy deve incorporare, o restringere ulteriormente, tutti i requisiti individuati nelle clausole 5 e 6.",
        "testo_integrale": "OVR-7-01 [CONDITIONAL]: When building a SP from requirements defined in the present document, the policy shall incorporate, or further constrain, all the requirements identified in clauses 5 and 6.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "Si applica solo quando un TSP costruisce una propria Signature Policy (SP) a partire dai requisiti del presente documento, invece di seguire direttamente uno dei profili LSP/NSP/EUSPv2 già definiti.",
    },
    {
        "riferimento": "Parte 1: OVR-7-02",
        "testo": "Quando si costruisce una SP a partire dai requisiti del presente documento, la policy deve identificare ogni scostamento (variance) che intende applicare.",
        "testo_integrale": "OVR-7-02 [CONDITIONAL]: When building a SP from requirements defined in the present document, the policy shall identify any variances it chooses to apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "Si applica solo quando un TSP costruisce una propria SP a partire dai requisiti del presente documento.",
    },
    {
        "riferimento": "Parte 1: OVR-7-03",
        "testo": "Quando si costruisce una SP a partire dai requisiti del presente documento, i sottoscrittori devono essere informati, nell'ambito dell'attuazione dei termini e condizioni, del modo in cui la policy specifica si aggiunge o restringe ulteriormente i requisiti della policy definita nel presente documento.",
        "testo_integrale": "OVR-7-03 [CONDITIONAL]: When building a SP from requirements defined in the present document, subscribers shall be informed, as part of implementing the terms and conditions, of the ways in which the specific policy adds to or further constrains the requirements of the policy as defined in the present document.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
        "condizione_applicabilita": "Si applica solo quando un TSP costruisce una propria SP a partire dai requisiti del presente documento.",
    },
    {
        "riferimento": "Parte 1: OVR-7-04",
        "testo": "Quando si costruisce una SP a partire dai requisiti del presente documento, deve esistere un organismo (es. una policy management authority) con autorità e responsabilità finale per la definizione e l'approvazione della policy.",
        "testo_integrale": "OVR-7-04 [CONDITIONAL]: When building a SP from requirements defined in the present document, there shall be a body (e.g. a policy management authority) with final authority and responsibility for specifying and approving the policy.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "Si applica solo quando un TSP costruisce una propria SP a partire dai requisiti del presente documento.",
    },
    {
        "riferimento": "Parte 1: OVR-7-05",
        "testo": "Quando si costruisce una SP a partire dai requisiti del presente documento, dovrebbe essere condotta una valutazione del rischio per valutare i requisiti di business e determinare i requisiti di sicurezza da includere nella policy per la comunità e l'ambito di applicabilità dichiarati.",
        "testo_integrale": "OVR-7-05 [CONDITIONAL]: When building a SP from requirements defined in the present document, a risk assessment should be carried out to evaluate business requirements and determine the security requirements to be included in the policy for the stated community and applicability.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "Si applica solo quando un TSP costruisce una propria SP a partire dai requisiti del presente documento.",
    },
    {
        "riferimento": "Parte 1: OVR-7-06",
        "testo": "Quando si costruisce una SP a partire dai requisiti del presente documento, la policy dovrebbe essere approvata e modificata secondo un processo di revisione definito, incluse le responsabilità per il suo mantenimento.",
        "testo_integrale": "OVR-7-06 [CONDITIONAL]: When building a SP from requirements defined in the present document, the policy should be approved and modified in accordance with a defined review process, including responsibilities for maintaining the policy.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "Si applica solo quando un TSP costruisce una propria SP a partire dai requisiti del presente documento.",
    },
    {
        "riferimento": "Parte 1: OVR-7-07",
        "testo": "Quando si costruisce una SP a partire dai requisiti del presente documento, dovrebbe esistere un processo di revisione definito per assicurare che la policy sia supportata dalle dichiarazioni delle pratiche (practice statement).",
        "testo_integrale": "OVR-7-07 [CONDITIONAL]: When building a SP from requirements defined in the present document, a defined review process should exist to ensure that the policy is supported by the practices statements.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "Si applica solo quando un TSP costruisce una propria SP a partire dai requisiti del presente documento.",
    },
    {
        "riferimento": "Parte 1: OVR-7-08",
        "testo": "Quando si costruisce una SP a partire dai requisiti del presente documento, il TSP dovrebbe rendere disponibili alla propria comunità di utenti le policy che supporta.",
        "testo_integrale": "OVR-7-08 [CONDITIONAL]: When building a SP from requirements defined in the present document, the TSP should make available the policies supported by the TSP to its user community.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
        "condizione_applicabilita": "Si applica solo quando un TSP costruisce una propria SP a partire dai requisiti del presente documento.",
    },
    {
        "riferimento": "Parte 1: OVR-7-09",
        "testo": "Quando si costruisce una SP a partire dai requisiti del presente documento, le revisioni delle policy supportate dal TSP dovrebbero essere rese disponibili ai sottoscrittori.",
        "testo_integrale": "OVR-7-09 [CONDITIONAL]: When building a SP from requirements defined in the present document, revisions to policies supported by the TSP should be made available to subscribers.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
        "condizione_applicabilita": "Si applica solo quando un TSP costruisce una propria SP a partire dai requisiti del presente documento.",
    },
    {
        "riferimento": "Parte 1: OVR-7-10",
        "testo": "Quando si costruisce una SP a partire dai requisiti del presente documento, deve essere ottenuto un identificatore di oggetto univoco (OID o URI) per la policy.",
        "testo_integrale": "OVR-7-10 [CONDITIONAL]: When building a SP from requirements defined in the present document, a unique object identifier shall be obtained for the policy (e.g. OID or URI).",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "Si applica solo quando un TSP costruisce una propria SP a partire dai requisiti del presente documento.",
    },
    {
        "riferimento": "Parte 1: OVR-A.3-01",
        "testo": "Per il profilo EUSPv2, si applicano tutti i requisiti specificati per il profilo NSP (Normalized SSAS Policy).",
        "testo_integrale": "OVR-A.3-01 [EUSPv2]: All requirements specified for [NSP] shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: OVR-A.3-02",
        "testo": "La dichiarazione delle pratiche (practice statement) del TSP deve includere il riferimento alla certificazione del QSCD impiegato rispetto ai requisiti del Regolamento (EU) 2024/1183 che modifica il Regolamento (EU) n. 910/2014, allegato II. Nota: la Decisione di esecuzione (EU) 2016/650 definisce gli standard per la valutazione di sicurezza dei dispositivi qualificati di creazione di firma/sigillo ai sensi degli articoli 30(3) e 39(2) del Regolamento (EU) n. 910/2014, ma è stata pubblicata prima di EN 419241-1 ed EN 419241-2, che non sono presi in considerazione.",
        "testo_integrale": "OVR-A.3-02 [EUSPv2]: The TSP's practice statement shall include the reference to the certification that the QSCD employed against the requirements of Regulation (EU) 2024/1183 [i.11] amending Regulation (EU) No 910/2014 [i.1], annex II. NOTE: CID (EU) 2016/650 [i.12] lays down standards for the security assessment of qualified signature and seal creation devices pursuant to Articles 30(3) and 39(2) of Regulation (EU) No 910/2014. However, it was published before the publication of EN 419241-1 [3] and EN 419241-2 [4] which are not taken into account.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: OVR-A.3-03",
        "testo": "Il SSASP deve rispettare ogni requisito individuato nel rapporto di certificazione del dispositivo qualificato di creazione di firma elettronica remoto.",
        "testo_integrale": "OVR-A.3-03 [EUSPv2]: The SSASP shall comply with any requirements identified in the certification report of the specific remote qualified electronic signature creation device.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: GEN-A.4-01",
        "testo": "La chiave di firma del firmatario deve essere generata in un QSCD.",
        "testo_integrale": "GEN-A.4-01 [EUSPv2]: Signer's signing key shall be generated in a QSCD.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "oggetti_giuridici": ["dispositivo qualificato di creazione di firma elettronica"],
    },
    {
        "riferimento": "Parte 1: GEN-A.4-02",
        "testo": "Il QSCD deve essere utilizzato nella configurazione descritta nella documentazione di guida alla certificazione applicabile, o in una configurazione equivalente che raggiunga il medesimo obiettivo di sicurezza.",
        "testo_integrale": "GEN-A.4-02 [EUSPv2]: The QSCD shall be operated in its configuration as described in the appropriate certification guidance documentation or in an equivalent configuration which achieves the same security objective.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "oggetti_giuridici": ["dispositivo qualificato di creazione di firma elettronica"],
    },
    {
        "riferimento": "Parte 1: SIG-A.5-01",
        "testo": "La chiave di firma del firmatario deve essere utilizzata in un QSCD.",
        "testo_integrale": "SIG-A.5-01 [EUSPv2]: Signer's signing key shall be used in a QSCD.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "oggetti_giuridici": ["dispositivo qualificato di creazione di firma elettronica"],
    },
    {
        "riferimento": "Parte 1: SIG-A.5-02",
        "testo": "Il QSCD deve essere utilizzato nella configurazione descritta nella documentazione di guida alla certificazione applicabile, o in una configurazione equivalente che raggiunga il medesimo obiettivo di sicurezza.",
        "testo_integrale": "SIG-A.5-02 [EUSPv2]: The QSCD shall be operated in its configuration as described in the appropriate certification guidance documentation or in an equivalent configuration which achieves the same security objective.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "oggetti_giuridici": ["dispositivo qualificato di creazione di firma elettronica"],
    },
    {
        "riferimento": "Parte 1: SIG-A.5-03",
        "testo": "Si applica la clausola SRA_SAP.1.3 di EN 419241-1, relativa alla robustezza crittografica.",
        "testo_integrale": "SIG-A.5-03 [EUSPv2]: Clause SRA_SAP.1.3 of EN 419241-1 [3], specifying cryptographic strength, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: SIG-A.5-04",
        "testo": "Si applica la clausola SRA_SAP.1.4 di EN 419241-1, relativa alla mitigazione delle minacce.",
        "testo_integrale": "SIG-A.5-04 [EUSPv2]: Clause SRA_SAP.1.4 of EN 419241-1 [3], specifying threats mitigation, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: SIG-A.5-05",
        "testo": "Si applica la clausola SRA_SAP.1.5 di EN 419241-1, relativa alla protezione dell'ambiente.",
        "testo_integrale": "SIG-A.5-05 [EUSPv2]: Clause SRA_SAP.1.5 of EN 419241-1 [3], specifying environment protection, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: SIG-A.5-06",
        "testo": "Si applica la clausola SRA_SAP.1.6 di EN 419241-1, relativa alla protezione dalla manomissione.",
        "testo_integrale": "SIG-A.5-06 [EUSPv2]: Clause SRA_SAP.1.6 of EN 419241-1 [3], specifying protection against tampering, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: SIG-A.5-07",
        "testo": "Si applica la clausola SRA_SAP.1.7 di EN 419241-1, relativa alla protezione dall'attaccante.",
        "testo_integrale": "SIG-A.5-07 [EUSPv2]: Clause SRA_SAP.1.7 of EN 419241-1 [3], specifying protection against attacker, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: SIG-A.5-08",
        "testo": "Il SAM (Signature Activation Module) dovrebbe essere certificato conforme a EN 419241-2.",
        "testo_integrale": "SIG-A.5-08 [EUSPv2]: The SAM should be certified to be conformant to EN 419241-2 [4].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: SIG-A.5-09",
        "testo": "Se l'autenticazione è collegata direttamente all'identità, la sessione di firma deve terminare al più tardi 30 minuti dopo la fine del processo di verifica dell'identità.",
        "testo_integrale": "SIG-A.5-09 [EUSPv2] [CONDITIONAL]: In case the authentication is linked directly to the identity, the signature session shall end at most 30 minutes after the end of the identity verification process.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "Si applica solo se l'autenticazione del firmatario è collegata direttamente all'identità (invece che a un mezzo di eID).",
    },
    {
        "riferimento": "Parte 1: SIG-A.6-01",
        "testo": "Si applica la clausola SRA_SAP.2.1 di EN 419241-1, relativa al formato dei dati di attivazione della firma (SAD).",
        "testo_integrale": "SIG-A.6-01 [EUSPv2]: Clause SRA_SAP.2.1 of EN 419241-1 [3], specifying signature activation data format, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: SIG-A.6-02",
        "testo": "Si applica la clausola SRA_SAP.2.2 di EN 419241-1, relativa alla raccolta e generazione dei dati di attivazione della firma (SAD).",
        "testo_integrale": "SIG-A.6-02 [EUSPv2]: Clause SRA_SAP.2.2 of EN 419241-1 [3], specifying signature activation data collection and generation, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: SIG-A.6-03",
        "testo": "Si applica la clausola SRA_SAP.2.3 di EN 419241-1, relativa ai parametri dei dati di attivazione della firma (SAD).",
        "testo_integrale": "SIG-A.6-03 [EUSPv2]: Clause SRA_SAP.2.3 of EN 419241-1 [3], specifying signature activation data parameters, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: SIG-A.6-04",
        "testo": "Si applica la clausola SRA_SAP.2.4 di EN 419241-1, relativa all'uso dei dati di attivazione della firma (SAD).",
        "testo_integrale": "SIG-A.6-04 [EUSPv2]: Clause SRA_SAP.2.4 of EN 419241-1 [3], specifying signature activation data usage, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: SIG-A.6-05",
        "testo": "Si applica la clausola SRA_SAP.2.5 di EN 419241-1, relativa alla destinazione dei dati di attivazione della firma (SAD).",
        "testo_integrale": "SIG-A.6-05 [EUSPv2]: Clause SRA_SAP.2.5 of EN 419241-1 [3], specifying signature activation data destination, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: SIG-A.6-06A",
        "testo": "Si applica la clausola SRA_SAP.2.6 di EN 419241-1, relativa alla raccolta e protezione dei dati di attivazione della firma (SAD).",
        "testo_integrale": "SIG-A.6-06A [EUSPv2]: Clause SRA_SAP.2.6 of EN 419241-1 [3], specifying signature activation data collection and protection, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: SIG-A.6-07",
        "testo": "Se il firmatario è una persona fisica, si applica la clausola SRA_SAP.2.7 di EN 419241-1, relativa alla trasmissione dei dati di attivazione della firma (SAD) sotto controllo esclusivo (sole control).",
        "testo_integrale": "SIG-A.6-07 [EUSPv2] [CONDITIONAL]: If the signer is a natural person, clause SRA_SAP.2.7 of EN 419241-1 [3], specifying signature activation data submission under sole control, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "Si applica solo se il firmatario è una persona fisica.",
    },
    {
        "riferimento": "Parte 1: SIG-A.6-07A",
        "testo": 'Se il firmatario è una persona giuridica, si applica la clausola SRA_SAP.2.7 di EN 419241-1 relativa alla trasmissione dei dati di attivazione della firma (SAD), con il termine "controllo esclusivo" (sole control) sostituito da "controllo" (control).',
        "testo_integrale": 'SIG-A.6-07A [EUSPv2] [CONDITIONAL]: If the signer is a legal person, clause SRA_SAP.2.7 of EN 419241-1 [3], specifying signature activation data submission shall apply where "sole control" is replaced by "control".',
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
        "condizione_applicabilita": "Si applica solo se il firmatario è una persona giuridica.",
    },
    {
        "riferimento": "Parte 1: SIG-A.6-08",
        "testo": "Si applica la clausola SRA_SAP.2.8 di EN 419241-1, relativa alla protezione dei dati di attivazione della firma (SAD) dopo l'attivazione.",
        "testo_integrale": "SIG-A.6-08 [EUSPv2]: Clause SRA_SAP.2.8 of EN 419241-1 [3], specifying signature activation data protection after activation, shall apply.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: LNK-A.7-01",
        "testo": "L'identity proofing del firmatario deve soddisfare i requisiti del livello Extended di Level of Identity Proofing (LoIP), come definito in ETSI TS 119 461.",
        "testo_integrale": "LNK-A.7-01 [EUSPv2]: The identity proofing of the signer shall fulfil the requirements of extended Level of Identity Proofing (LoIP) as defined in ETSI TS 119 461 [6].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "Parte 1: A.1",
        "testo": "Il presente annesso specifica i requisiti di policy e sicurezza generalmente applicabili a un TSP qualificato che gestisce un QSCD da remoto.",
        "testo_integrale": "The present annex specifies generally applicable policy and security requirements for a Qualified TSP managing a remote QSCD.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": [
            "dispositivo qualificato di creazione di firma elettronica",
            "dispositivo qualificato di creazione di sigillo elettronico",
        ],
    },
    {
        "riferimento": "Parte 1: A.2",
        "testo": "I SSASP conformi al presente documento possono dichiarare conformità tramite lo specifico OID di trust service policy EUSPv2 (EU SSAS Policy): itu-t(0) identified-organization(4) etsi(0) SIGNATURE CREATION SERVICE-policies(19431) ops(1) policy-identifiers(1) eu-remote-qscd-v2(4).",
        "testo_integrale": "SSASPs following the present document can claim conformance to the present document via the following specific trust service policy OID: EUSPv2: EU SSAS Policy. itu-t(0) identified-organization(4) etsi(0) SIGNATURE CREATION SERVICE-policies(19431) ops (1) policy-identifiers(1) eu-remote-qscd-v2 (4)",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": [
            "dispositivo qualificato di creazione di firma elettronica",
            "dispositivo qualificato di creazione di sigillo elettronico",
        ],
    },
    {
        "riferimento": "Parte 1: B.2",
        "testo": (
            "La Tabella B.3 individua come gli obiettivi dei controlli di sicurezza e le altre parti della policy "
            "EU SSAS (EUSPv2) definita nel presente documento indirizzino i requisiti del TSP che gestisce un QSCD "
            "da remoto ai sensi del Regolamento (EU) 2024/1183, sia nel contesto delle firme elettroniche sia in "
            "quello dei sigilli elettronici: mappa gli artt. 29 (requisiti dei dispositivi qualificati di creazione "
            "di firma elettronica), 29a (requisiti per il servizio qualificato di gestione di tali dispositivi da "
            "remoto), 39 e 39a (disposizioni equivalenti per i sigilli elettronici) e l'Allegato II (requisiti dei "
            "dispositivi qualificati di creazione di firma elettronica) sui requisiti EUSPv2 di Annex A del presente "
            "documento (GEN-A.4, SIG-A.5, SIG-A.6, LNK-A.7) e, per la sola duplicazione delle chiavi a fini di "
            "backup, sui requisiti GEN-6.3.3-02 e GEN-6.3.3-04 della clausola 6.3.3 del presente documento (clausola "
            "6, capitolo 1). Non viene creato un nodo per ciascuna riga della tabella: il contenuto è già coperto dai "
            "nodi dei singoli requisiti citati. La tabella riporta letteralmente due riferimenti con probabile "
            "errata di redazione del documento ETSI stesso (\"GEN-A.3-03\" al posto di \"OVR-A.3-03\"; \"SIG-A.7-01\" "
            "al posto di \"LNK-A.7-01\"), riportati verbatim come scritti nell'originale. Le relazioni verso gli "
            "articoli del Regolamento (EU) 2024/1183/eIDAS2 citati non sono create in questo import: sono deferite "
            "alla pipeline di collegamento cross-fonte a posteriori (ADR-0009)."
        ),
        "testo_integrale": (
            "B.2 Regulation (EU) 2024/1183: Table B.3 identifies how the security controls objectives and other "
            "parts of the EU SSAS policy (EUSPv2) defined in the present document address the requirement of TSP "
            "managing remote QSCD as defined in Regulation (EU) 2024/1183 [i.11] in the context of electronic "
            "signatures or seals. Table B.3: Electronic signature context. "
            "Article 29 Requirements for qualified electronic signature creation devices | EUv2 SSAS policy "
            'reference "1a. Generating or managing electronic signature creation data or duplicating such '
            "signature creation data for back-up purposes shall be carried out only on behalf of the signatory, "
            "at the request of the signatory, and by a qualified trust service provider providing a qualified "
            'trust service for the management of a remote qualified electronic signature creation device." | '
            "SIG-A.6-01: signature activation data format. SIG-A.6-02: signature activation data collection and "
            "generation. SIG-A.6-03: signature activation data parameters. SIG-A.6-04: signature activation data "
            "usage. SIG-A.6-05: signature activation data destination. SIG-A.6-06A: signature activation data "
            "collection and protection. SIG-A.6-07: signature activation data submission under sole control. "
            "SIG-A.6-08: signature activation data protection after activation. SIG-A.7-01: eID means linking. "
            "Article 29a Requirements for a qualified service for the management of remote qualified electronic "
            "signature creation devices | EUv2 SSAS policy reference "
            '"1. The management of remote qualified electronic signature creation devices as a qualified service '
            "shall be carried out only by a qualified trust service provider that: (a) generates or manages "
            'electronic signature creation data on behalf of the signatory;" | GEN-A.4-01, GEN-A.4-02, SIG-A.5-01 '
            "to SIG-A.5-08, SIG-A.6-01 to SIG-A.6-08. "
            '"(b) notwithstanding point (1)(d) of Annex II, duplicates the electronic signature creation data for '
            "back-up purposes only, provided that the following requirements are met: (i) the security of the "
            "duplicated datasets must be at the same level as for the original datasets; (ii) the number of "
            'duplicated datasets must not exceed the minimum needed to ensure continuity of the service;" | '
            "GEN-6.3.3-02: backup protection. GEN-6.3.3-04: backup minimum datasets. "
            '"(c) complies with any requirements identified in the certification report of the specific remote '
            'qualified electronic signature creation device issued pursuant to Article 30." | GEN-A.3-03, '
            "GEN-A.4-02, SIG-A.5-02. "
            "Article 39 | EUv2 SSAS policy reference. Article 29 shall apply mutatis mutandis to requirements for "
            "qualified electronic seal creation devices. | SIG-A.6-01: signature activation data format. "
            "SIG-A.6-02: signature activation data collection and generation. SIG-A.6-03: signature activation "
            "data parameters. SIG-A.6-04: signature activation data usage. SIG-A.6-05: signature activation data "
            "destination. SIG-A.6-06A: signature activation data collection and protection. SIG-A.6-07A: signature "
            "activation data submission under sole control. SIG-A.6-08: signature activation data protection "
            "after activation. SIG-A.7-01: eID means linking. "
            "Article 39a Requirements for a qualified service for the management of remote qualified electronic "
            "seal creation devices | EUv2 SSAS policy reference "
            '"Article 29a shall apply mutatis mutandis to a qualified service for the management of remote '
            'qualified electronic seal creation devices." | GEN-A.4-01, GEN-A.4-02, SIG-A.5-01 to SIG-A.5-08, '
            "SIG-A.6-01 to SIG-A.6-08. GEN-6.3.3-02: backup protection. GEN-6.3.3-04: backup minimum datasets. "
            "GEN-A.3-03, GEN-A.4-02, SIG-A.5-02. "
            "ANNEX II Requirements for qualified electronic signature creation devices | EUv2 SSAS policy "
            'reference "1. Qualified electronic signature creation devices shall ensure, by appropriate technical '
            "and procedural means, that at least: (a) the confidentiality of the electronic signature creation "
            "data used for electronic signature creation is reasonably assured; (b) the electronic signature "
            "creation data used for electronic signature creation can practically occur only once; (c) the "
            "electronic signature creation data used for electronic signature creation cannot, with reasonable "
            "assurance, be derived and the electronic signature is reliably protected against forgery using "
            "currently available technology; (d) the electronic signature creation data used for electronic "
            'signature creation can be reliably protected by the legitimate signatory against use by others." | '
            "GEN-A.4-01: signing keys generated in a QSCD. GEN-A.4-02: QSCD configuration and operation. "
            '"2. Qualified electronic signature creation devices shall not alter the data to be signed or prevent '
            'such data from being presented to the signatory prior to signing." | SIG-A.5-01: signing keys used '
            "in a QSCD. SIG-A.5-02: QSCD configuration and operation."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": [
            "dispositivo qualificato di creazione di firma elettronica",
            "dispositivo qualificato di creazione di sigillo elettronico",
        ],
    },
    {
        "riferimento": "Parte 1: C.1",
        "testo": (
            "Una figura (Figura C.1) illustra i diversi standard applicabili ai differenti componenti di un "
            "servizio di creazione di firma da remoto. L'annesso non contiene, nel testo estratto, ulteriore "
            "contenuto descrittivo oltre al rinvio alla figura; il contenuto grafico della figura non è "
            "riproducibile in forma testuale."
        ),
        "testo_integrale": (
            "C.1 Scope of remote signing standards: Figure C.1 illustrates the different standards applicable "
            "for a remote signature creation service. Figure C.1: Scope of standards on the different remote "
            "signing components."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Parte 1: OVR-7-01", "Parte 1: OVR-7-02", "Parte 1: OVR-7-03", "Parte 1: OVR-7-04", "Parte 1: OVR-7-05",
    "Parte 1: OVR-7-06", "Parte 1: OVR-7-07", "Parte 1: OVR-7-08", "Parte 1: OVR-7-09", "Parte 1: OVR-7-10",
    "Parte 1: A.1", "Parte 1: A.2",
    "Parte 1: OVR-A.3-01", "Parte 1: OVR-A.3-02", "Parte 1: OVR-A.3-03",
    "Parte 1: GEN-A.4-01", "Parte 1: GEN-A.4-02",
    "Parte 1: SIG-A.5-01", "Parte 1: SIG-A.5-02", "Parte 1: SIG-A.5-03", "Parte 1: SIG-A.5-04", "Parte 1: SIG-A.5-05",
    "Parte 1: SIG-A.5-06", "Parte 1: SIG-A.5-07", "Parte 1: SIG-A.5-08", "Parte 1: SIG-A.5-09",
    "Parte 1: SIG-A.6-01", "Parte 1: SIG-A.6-02", "Parte 1: SIG-A.6-03", "Parte 1: SIG-A.6-04", "Parte 1: SIG-A.6-05",
    "Parte 1: SIG-A.6-06A", "Parte 1: SIG-A.6-07", "Parte 1: SIG-A.6-07A", "Parte 1: SIG-A.6-08",
    "Parte 1: LNK-A.7-01",
    "Parte 1: B.2",
    "Parte 1: C.1",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

_REQUISITI_NSP_CAP01 = [
    "Parte 1: GEN-6.2.1-02", "Parte 1: GEN-6.2.1-02A",
    "Parte 1: LNK-6.2.2-02A", "Parte 1: LNK-6.2.2-02B", "Parte 1: LNK-6.2.2-02C", "Parte 1: LNK-6.2.2-02D", "Parte 1: LNK-6.2.2-02E",
    "Parte 1: LNK-6.2.2-08", "Parte 1: LNK-6.2.2-08A", "Parte 1: LNK-6.2.2-09",
    "Parte 1: SIG-6.3.1-05", "Parte 1: SIG-6.3.1-06", "Parte 1: SIG-6.3.1-07", "Parte 1: SIG-6.3.1-15", "Parte 1: SIG-6.3.1-16",
]

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "Parte 1: OVR-A.3-01"),
        "nodo_a": ("obbligo", None, rif_nsp),
        "tipo_relazione": "richiede come precondizione",
        "evidence_type": "textual",
        "confidence": None,
    }
    for rif_nsp in _REQUISITI_NSP_CAP01
] + [
    {
        "nodo_da": ("obbligo", None, "Parte 1: SIG-A.5-09"),
        "nodo_a": ("obbligo", None, "Parte 1: SIG-6.3.1-14"),
        "tipo_relazione": "specifica",
        "evidence_type": "inferred",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("principio", None, "Parte 1: B.2"),
        "nodo_a": ("obbligo", None, "Parte 1: GEN-6.3.3-02"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "Parte 1: B.2"),
        "nodo_a": ("obbligo", None, "Parte 1: GEN-6.3.3-04"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
