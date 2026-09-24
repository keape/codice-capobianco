"""Estrazione granulare ETSI EN 319 411-1 V1.5.1 (2025-04) — Capitolo 5:
clausola 7 (Framework for the definition of other certificate policies: 7.1
Certificate policy management, 7.2 Additional requirements), Annex A
informativo (Model PKI disclosure statement: A.1 Introduction, A.2 The PDS
structure, A.3 The PDS format), Annex B informativo (Conformity assessment
checklist).

Fonte 17 (numerazione definitiva cablata dalla sessione principale in
app/seed.py — questo modulo NON tocca seed.py). Testo ufficiale in
app/.source_cache/etsi_319_411_1/cap05.txt. Manifest di split:
app/.source_cache/etsi_319_411_1/manifest.json.

Modellazione (ADR-0007), stesso criterio già applicato a ETSI EN 319 401
(fonte 10, app/seed_data/etsi_319_401/cap02.py) e ETSI TS 119 461 (fonte 9,
app/seed_data/etsi_119_461/) per un capitolo tecnico ETSI a clausole/
requisiti numerati:

Clausola 7 — "## 7 Framework for the definition of other certificate
policies" non ha testo proprio (nessun paragrafo introduttivo privo di REQ
proprio da assorbire come Principio autonomo): il titolo di clausola 7 è
seguito immediatamente da "#### 7.1 Certificate policy management" e dal
primo requisito OVR-7.1-01, quindi nessun nodo per "clausola 7" in sé
(stesso schema di "## 6 Policies and practices" senza testo proprio in
ETSI EN 319 401 cap02.py).

OVR-7.1-01 introduce con proprio contenuto prescrittivo ("The authority
issuing a CP... shall demonstrate that the CP is effective. In particular,
when the TSP issues other CPs:") un elenco puntato dove OGNI voce ha un
proprio identificatore di requisito (OVR-7.1-02 .. OVR-7.1-12): per
l'istruzione generale, il paragrafo introduttivo resta un nodo a sé (ha un
proprio REQ e un proprio obbligo — dimostrare l'efficacia della CP,
distinto dal contenuto delle singole voci elencate) e ciascuna voce
dell'elenco resta un nodo separato con il proprio riferimento letterale.

tipo_obbligo per clausola 7.1/7.2 — nessun controllo tecnico in senso
stretto, sono requisiti di governance/gestione della CP salvo tre eccezioni
tecniche esplicite:
- "organizzativo": OVR-7.1-01..06, OVR-7.1-09 (identificazione della base
  CP, organo di approvazione, valutazione del rischio, processo di
  revisione, incorporazione/vincolo dei requisiti delle clausole 5-6 —
  tutti requisiti di governance del documento CP, non controlli operativi).
- "tecnico/sicurezza": OVR-7.1-10, OVR-7.1-11, OVR-7.1-12 (specifica dei
  requisiti di profilo di certificato ISO/IEC 9594-8/ITU-T X.509, uso dei
  profili ETSI EN 319 412 parti 2/3/4, ottenimento di un OID univoco per
  la CP — contenuto tecnico del certificato/della sua identificazione, non
  governance documentale).
- "informativo/trasparenza": OVR-7.1-07, OVR-7.1-08, OVR-7.2-01 (messa a
  disposizione delle CP e delle loro revisioni alla comunità di utenti/a
  subscriber e relying party; informativa su come la policy specifica
  aggiunge o vincola i requisiti della CP) — questi tre hanno `soggetti`
  con `categoria`/`ruolo` "destinatario" per "Utente/titolare" (subscriber/
  subject) e "Terzi affidanti/pubblico" (relying party), oltre al TSP
  obbligato, in coerenza con il testo che nomina esplicitamente entrambe le
  categorie come beneficiarie dell'informativa (OVR-7.1-07 NOTE per la
  composizione della "user community").

NOTE informative: la NOTE di OVR-7.1-07 ("The TSP's user community
includes the subscribers/subjects eligible to hold certificates issued
under the policy and any parties which rely on those certificates.") è
mantenuta in `testo_integrale` perché definisce il perimetro soggettivo
dell'obbligo (base per i due `soggetti` "destinatario" del nodo), non è un
mero rimando bibliografico.

Annex A (informativo, Model PKI disclosure statement) — A.1/A.3 sono
paragrafi discorsivi senza identificatore di requisito -> 1 Principio
"altro" ciascuno, riferimento "Parte 1: A.1 (Introduction)"/"Parte 1: A.3 (The PDS format)".
Il testo di A.1 nel file sorgente presenta un connettore duplicato/
spurio ("...informed trust decisions. Consequently, a" seguito a riga
successiva da "This annex provides an example...") — artefatto di
estrazione PDF->markdown analogo a quelli già documentati in
app/seed_data/etsi_119_461/cap01.py e cap02.py: la frase tronca
"Consequently, a" non introduce alcun contenuto normativo proprio
verificabile (non risulta seguita da testo coerente nella stessa
posizione) ed è omessa da `testo_integrale`, che riporta le frasi
integrali nell'ordine logico del paragrafo (non un troncamento di
contenuto normativo, cfr. ADR-0010) — verificabile contro il raw in
app/.source_cache/etsi_319_411_1/cap05.txt righe 30-40 (`:raw`).

A.2 (The PDS structure) contiene la tabella dei tipi di dichiarazione del
PDS (statement types/descriptions/specific requirements of certificate
policy), su 2 pagine del PDF originale, la cui conversione PDF->markdown è
fortemente frammentata (celle spezzate su più righe, contenuto di colonne
diverse interlacciato, intestazione di colonna 3 anticipata prima della
tabella) — stesso fenomeno già documentato per le tabelle di
app/seed_data/etsi_119_461/cap01.py (tabella abbreviazioni) e cap02.py
(tabella minacce/contromisure). Per istruzione del task, censita come UN
solo nodo Principio "altro" con la tabella ricostruita in formato Markdown
in `testo_integrale` (non frammentata voce per voce). Ricostruzione fatta
riassemblando i frammenti di cella nell'ordine di lettura the-through del
raw text (app/.source_cache/etsi_319_411_1/cap05.txt righe 40-83, verbatim
`:raw`) sotto le 11 etichette di riga ("Statement types") esplicite nel
testo. Unica cella la cui ricomposizione ha richiesto un ponte editoriale
minimo (non un'invenzione di contenuto normativo, ma una ricongiunzione di
due frammenti di frase visibilmente spezzati dall'estrazione): la
descrizione della riga "Obligations of subscribers", ricostruita come "The
description of, or reference to, the critical elements of the subscriber
obligations." unendo il frammento iniziale "The description of, or
reference to, the critical" (riga 1336 del raw) con il frammento finale
"subscriber obligations." (riga 1317 del raw, isolato tra le colonne della
riga "Reliance limits"); la connessione "elements of the" non è
recuperabile dal testo estratto e non è attestata verbatim — segnalata qui
per trasparenza. Due celle "Specific requirements" (righe "TSP contact
info" e "Refund policy") risultano vuote nel testo originale (nessun
rimando a una clausola specifica per quelle due voci) e sono riportate
come celle Markdown vuote, non come omissioni di contenuto.

Annex B (informativo, Conformity assessment checklist) — non è una tabella
in questo capitolo (rimanda per intero a un documento esterno, ETSI TR 119
411-4): 1 solo Principio "altro", riferimento "Annex B (Conformity
assessment checklist)", testo_integrale = paragrafo introduttivo completo.

RELAZIONI: vuoto per vincolo di fase — nessuna relazione, né interna al
capitolo né cross-capitolo/cross-fonte (incluso il rimando esplicito ad
ETSI TR 119 411-4 in Annex B e i richiami a ETSI EN 319 412 parti 2/3/4 in
OVR-7.1-11: nessuna di queste due fonti tecniche è oggi presente nel
censimento, quindi nessuna relazione sarebbe comunque risolvibile).
Eventuale collegamento demandato alla pipeline dedicata (ADR-0009) o a una
cura editoriale successiva quando quelle fonti saranno importate.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "Parte 1: OVR-7.1-01",
        "testo": (
            "L'autorità che emette una CP diversa da quelle definite alla "
            "clausola 5 deve dimostrarne l'efficacia; in particolare, quando il "
            "TSP emette altre CP, si applicano i requisiti seguenti."
        ),
        "testo_integrale": (
            "OVR-7.1-01: The authority issuing a CP other than the ones defined "
            "in clause 5 shall demonstrate that the CP is effective. In "
            "particular, when the TSP issues other CPs:"
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: OVR-7.1-02",
        "testo": (
            "La CP deve identificare quale delle certificate policy definite "
            "nel presente documento adotta come base, e le eventuali varianti "
            "che sceglie di applicare."
        ),
        "testo_integrale": (
            "OVR-7.1-02: The CP shall identify which of the certificate "
            "policies defined in the present document it adopts as the basis, "
            "plus any variances it chooses to apply."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: OVR-7.1-03",
        "testo": (
            "Deve esistere un organismo (es. una policy management authority) "
            "con autorità finale e responsabilità per specificare e approvare "
            "la CP."
        ),
        "testo_integrale": (
            "OVR-7.1-03: There shall be a body (e.g. a policy management "
            "authority) with final authority and responsibility for specifying "
            "and approving the CP."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: OVR-7.1-04",
        "testo": (
            "Dovrebbe essere condotta una valutazione del rischio per valutare "
            "i requisiti di business e determinare i requisiti di sicurezza da "
            "includere nella CP per la comunità e l'ambito di applicabilità "
            "dichiarati."
        ),
        "testo_integrale": (
            "OVR-7.1-04: A risk assessment should be carried out to evaluate "
            "business requirements and determine the security requirements to "
            "be included in the CP for the stated community and applicability."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: OVR-7.1-05",
        "testo": (
            "Le CP dovrebbero essere approvate e modificate secondo un "
            "processo di revisione definito, incluse le responsabilità di "
            "mantenimento della CP."
        ),
        "testo_integrale": (
            "OVR-7.1-05: CPs should be approved and modified in accordance "
            "with a defined review process, including responsibilities for "
            "maintaining the CP."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: OVR-7.1-06",
        "testo": (
            "Dovrebbe esistere un processo di revisione definito per garantire "
            "che la CP sia supportata dalla CPS della CA."
        ),
        "testo_integrale": (
            "OVR-7.1-06: A defined review process should exist to ensure that "
            "the CP is supported by the CA's CPS."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: OVR-7.1-07",
        "testo": (
            "Il TSP dovrebbe rendere disponibili alla propria comunità di "
            "utenti le CP che supporta; tale comunità comprende subscriber/"
            "subject titolari di certificati emessi sotto la policy e le parti "
            "che fanno affidamento su tali certificati."
        ),
        "testo_integrale": (
            "OVR-7.1-07: The TSP should make available the CPs supported by "
            "the TSP to its user community. NOTE: The TSP's user community "
            "includes the subscribers/subjects eligible to hold certificates "
            "issued under the policy and any parties which rely on those "
            "certificates."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "Parte 1: OVR-7.1-08",
        "testo": (
            "Le revisioni delle CP supportate dal TSP dovrebbero essere rese "
            "disponibili a subscriber e relying party."
        ),
        "testo_integrale": (
            "OVR-7.1-08: Revisions to CPs supported by the TSP should be made "
            "available to subscribers and relying parties."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "Parte 1: OVR-7.1-09",
        "testo": (
            "La CP deve incorporare, o vincolare ulteriormente, tutti i "
            "requisiti identificati alle clausole 5 e 6 che sono privi di una "
            "specifica marcatura relativa alla CP come previsto dalla "
            "clausola 5.3."
        ),
        "testo_integrale": (
            "OVR-7.1-09: The CP shall incorporate, or further constrain, all "
            "the requirements identified in clauses 5 and 6 where they are "
            "without a specific marking relating CP as specified in clause "
            "5.3."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: OVR-7.1-10",
        "testo": (
            "La CP deve specificare i requisiti di profilo di certificato "
            "secondo ISO/IEC 9594-8/Raccomandazione ITU-T X.509."
        ),
        "testo_integrale": (
            "OVR-7.1-10: The CP shall specify the ISO/IEC 9594-8/"
            "Recommendation ITU-T X.509 [7] certificate profile requirements."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: OVR-7.1-11",
        "testo": (
            "I profili di certificato definiti da ETSI EN 319 412 parti 2, 3 "
            "e 4 dovrebbero essere usati ove appropriato."
        ),
        "testo_integrale": (
            "OVR-7.1-11: Certificate profiles as defined by ETSI EN 319 412 "
            "parts 2 [10], 3 [11] and 4 [2] should be used where appropriate."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: OVR-7.1-12",
        "testo": (
            "Per la CP deve essere ottenuto un object identifier univoco nella "
            "forma richiesta da ISO/IEC 9594-8/Raccomandazione ITU-T X.509."
        ),
        "testo_integrale": (
            "OVR-7.1-12: A unique object identifier shall be obtained for the "
            "CP of the form required in ISO/IEC 9594-8/Recommendation ITU-T "
            "X.509 [7]."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 1: OVR-7.2-01",
        "testo": (
            "Subscriber e relying party devono essere informati, nell'ambito "
            "dell'attuazione dei requisiti della clausola 6.9.4, del modo in "
            "cui la specifica policy aggiunge o vincola ulteriormente i "
            "requisiti della CP definita nel presente documento."
        ),
        "testo_integrale": (
            "OVR-7.2-01: Subscribers and relying parties shall be informed, as "
            "part of implementing the requirements defined in clause 6.9.4, of "
            "the ways in which the specific policy adds to or further "
            "constrains the requirements of the CP as defined in the present "
            "document."
        ),
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
            {"categoria": "Terzi affidanti/pubblico", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "Parte 1: A.1 (Introduction)",
        "testo": (
            "Introduzione informativa al modello di PKI disclosure statement "
            "(PDS): strumento supplementare di disclosure e notice del TSP, "
            "pensato per rispondere a esigenze regolamentari, favorire "
            "l'autoregolamentazione del settore e rendere comprensibili ai "
            "consumatori elementi di CP/CPS altrimenti tecnici; non sostituisce "
            "CP o CPS."
        ),
        "testo_integrale": (
            "A.1 Introduction: The proposed model PKI disclosure statement is "
            "for use as a supplemental instrument of disclosure and notice by "
            "a TSP. A PKI disclosure statement may assist a TSP to respond to "
            "regulatory requirements and concerns, particularly those related "
            "to consumer deployment. Further, the aim of the model PKI "
            "disclosure statement is to foster industry \"self-regulation\" and "
            "build consensus on those elements of a CP and/or CPS that "
            "require emphasis and disclosure. Although CP and CPS documents "
            "are essential for describing and governing certificate policies "
            "and practices, many PKI users, especially consumers, find these "
            "documents difficult to understand. Consequently, there is a need "
            "for a supplemental and simplified instrument that can assist PKI "
            "users in making informed trust decisions. This annex provides an "
            "example of the structure for a PKI disclosure statement. The PDS "
            "contains a clause for each defined statement type. Each clause "
            "of a PDS contains a descriptive statement, which may include "
            "hyperlinks to the relevant CP/CPS clauses. PKI disclosure "
            "statement is not intended to replace a CP or CPS."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: A.2 (The PDS structure)",
        "testo": (
            "Struttura del PDS: tabella degli 11 tipi di dichiarazione "
            "previsti (contatti del TSP, tipo di certificato e procedure di "
            "validazione, limiti di affidamento, obblighi del subscriber, "
            "verifica dello stato del certificato, garanzie/limitazioni di "
            "responsabilità, accordi/CPS/CP applicabili, privacy, rimborsi, "
            "legge applicabile e reclami/dispute, licenze/marchi di fiducia e "
            "audit), ciascuno con una descrizione discorsiva e il rimando ai "
            "requisiti specifici di CP del presente documento."
        ),
        "testo_integrale": (
            "A.2 The PDS structure: Each clause of a PDS contains a "
            "descriptive statement, which may include hyperlinks to the "
            "relevant CP/CPS clauses.\n\n"
            "| Statement type | Statement description | Specific requirements "
            "of certificate policy |\n"
            "|---|---|---|\n"
            "| TSP contact info | The name, location and relevant contact "
            "information for the CA/PKI (name of responsible person, address, "
            "website, info mail, FAQ, etc.), including clear information on "
            "how to contact the TSP to request a revocation. | |\n"
            "| Certificate type, validation procedures and usage | A "
            "description of each class/type of certificate issued by the CA, "
            "corresponding validation procedures, and any restrictions on "
            "certificate usage. | Any limitations on its use. Whether the "
            "policy is for certificate issued to the public. CP being applied "
            "(including OID and short summary). |\n"
            "| Reliance limits | The reliance limits, if any. | Indication "
            "that the certificate is only for use with electronic signatures "
            "or seals. The period of time which registration information and "
            "TSP's event logs (see clauses 6.4.5 and 6.4.6) are maintained "
            "(and hence are available to provide supporting evidence). |\n"
            "| Obligations of subscribers | The description of, or reference "
            "to, the critical elements of the subscriber obligations. | The "
            "subscriber's obligations as defined in clause 6.3.5, "
            "OVR-6.3.5-02 items a) to j), including whether the policy "
            "requires use of a secure cryptographic device. |\n"
            "| Certificate status checking obligations of relying parties | "
            "The extent to which relying parties are obligated to check "
            "certificate status, and references to further explanation. | "
            "Information on how to validate the certificate, including "
            "requirements to check the revocation status of the certificate, "
            "such that the relying party is considered to \"reasonably rely\" "
            "on the certificate (see clause 6.3.5, OVR-6.3.5-03 items a) to "
            "c)). |\n"
            "| Limited warranty and disclaimer/Limitation of liability | "
            "Summary of the warranty, disclaimers, limitations of liability "
            "and any applicable warranty or insurance programs. | Limitations "
            "of liability (see clause 6.8.8). |\n"
            "| Applicable agreements, CPS, CP | Identification and references "
            "to applicable agreements, CPS, CP and other relevant documents. "
            "| CP being applied. |\n"
            "| Privacy policy | A description of and reference to the "
            "applicable privacy policy. | See clause 6.8.4 for issues "
            "relating to Data Protection. The period of time during which "
            "registration information (see clause 6.3.4, REG-6.3.4-17) is "
            "retained. |\n"
            "| Refund policy | A description of and reference to the "
            "applicable refund policy. | |\n"
            "| Applicable law, complaints and dispute resolution | Statement "
            "of the choice of law, complaints procedure and dispute "
            "resolution mechanisms (anticipated to often include a reference "
            "to the International Chambers of Commerce's arbitration "
            "services). | The procedures for complaints and dispute "
            "settlements. The applicable legal system. |\n"
            "| TSP and repository licenses, trust marks, and audit | Summary "
            "of any governmental licenses, seal programs; and a description "
            "of the audit process and if applicable the audit firm. | If the "
            "TSP has been certified to be conformant with a CP, and if so "
            "through which scheme. The link toward the Trusted List of the "
            "country within which the TSP is operated. |"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: A.3 (The PDS format)",
        "testo": (
            "Il PDS dovrebbe essere reso disponibile in formato PDF/A come "
            "specificato in ISO 19005 parti 1-3."
        ),
        "testo_integrale": (
            "A.3 The PDS format: The PDS should be available under PDF/A "
            "format as specified in ISO 19005 parts 1 to 3 [i.4]."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 1: Annex B (Conformity assessment checklist)",
        "testo": (
            "Una checklist dei requisiti di policy del presente documento e "
            "dei requisiti generici indipendenti dal TSP (ETSI EN 319 401) è "
            "contenuta in ETSI TR 119 411-4, utilizzabile dal TSP per "
            "l'autovalutazione (autodichiarazione) e dall'assessor in sede di "
            "verifica di conformità, con identificativi di requisito allineati "
            "a quelli del presente documento."
        ),
        "testo_integrale": (
            "Annex B (informative): Conformity assessment checklist: A "
            "checklist for the policy requirements specified in the present "
            "document as well as the generic requirements which are "
            "independent of the TSP (as expressed in ETSI EN 319 401 [9]) is "
            "contained in ETSI TR 119 411-4 [i.20]. The checklist provides "
            "all requirements identifiers in such a way that it can be used "
            "by the TSP itself to prepare for an assessment of its practices "
            "against the present document (i.e. serve as a basis for a "
            "self-declaration) and/or by the assessor when conducting the "
            "assessment, for the sake of facility for both the assessor and "
            "the TSP to be assessed."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Parte 1: OVR-7.1-01", "Parte 1: OVR-7.1-02", "Parte 1: OVR-7.1-03", "Parte 1: OVR-7.1-04", "Parte 1: OVR-7.1-05",
    "Parte 1: OVR-7.1-06", "Parte 1: OVR-7.1-07", "Parte 1: OVR-7.1-08", "Parte 1: OVR-7.1-09", "Parte 1: OVR-7.1-10",
    "Parte 1: OVR-7.1-11", "Parte 1: OVR-7.1-12",
    "Parte 1: OVR-7.2-01",
    "Parte 1: A.1 (Introduction)", "Parte 1: A.2 (The PDS structure)", "Parte 1: A.3 (The PDS format)",
    "Parte 1: Annex B (Conformity assessment checklist)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from seed_data.lib import verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    print(
        f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
        f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti."
    )
