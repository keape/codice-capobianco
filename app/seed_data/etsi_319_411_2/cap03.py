"""Estrazione granulare ETSI EN 319 411-2 V2.6.1 (2025-06) — Capitolo 3:
clausola 7 (Framework for the definition of other certificate policies built
on the present document: 7.1 Certificate policy management, 7.2 Additional
requirements), Annex A informativo (Regulation and EU qualified certificate
policy mapping — Table A.1) e Annex B informativo (Conformity Assessment
Checklist).

Fonte 18 (numerazione definitiva cablata dalla sessione principale in
app/seed.py — questo modulo NON tocca seed.py). Testo ufficiale in
app/.source_cache/etsi_319_411_2/cap03.txt.

## Clausola 7

Struttura del testo — clausola 7 e le sue sottoclausole 7.1/7.2 hanno solo
intestazioni di sezione seguite immediatamente dal primo requisito numerato
(nessun paragrafo introduttivo privo di REQ proprio da assorbire come
Principio autonomo, stesso schema già osservato per clausola 6 di ETSI EN
319 401, vedi app/seed_data/etsi_319_401/cap02.py): "## 7 Framework for the
definition..." non ha testo proprio, seguito direttamente da "#### 7.1
Certificate policy management" e OVR-7.1-01. Di conseguenza nessun nodo
Principio "altro"/"scopo di applicazione" per "clausola 7"/"clausola 7.1"/
"clausola 7.2" in sé: ogni item di indice corrisponde 1:1 a un requisito
OVR-7.x-nn -> 1 Obbligo. tipo_obbligo "organizzativo" per tutti e tre (sono
requisiti di governance sulla costruzione di una certificate policy che
incorpora/vincola le clausole 5-6 del presente documento e i requisiti di
EN 319 411-1, non controlli tecnici in senso stretto). OVR-7.1-01 e
OVR-7.2-01 richiamano testualmente le clausole 7.1/7.2 di ETSI EN 319 411-1
[2] (fonte 17, già assegnata ma la cui numerazione REQ di quelle clausole è
prodotta da un capitolo pari di quella fonte, non consultato da questo
modulo); per vincolo di fase (RELAZIONI vuoto, vedi sotto) nessuna relazione
di rinvio viene creata qui.

## Annex A (informative): Regulation and EU qualified certificate policy
mapping — Table A.1

Un solo nodo Principio "altro", riferimento "Parte 2: Annex A (Table A.1)", con
l'intera Table A.1 riportata in `testo_integrale` in formato Markdown,
verbatim e senza troncare righe (ADR-0010). La tabella mappa gli obiettivi
di controllo di sicurezza e le altre disposizioni delle EU Qualified
Certificate Policy (QCP) definite nel presente documento sui requisiti del
TSP che emette certificati qualificati ex articoli 5.1, 13.2, 15, 19, 24, 28
(38), 30 e Allegati I/II/III/IV del Regolamento (UE) n. 910/2014.

Nota di fedeltà dell'estrazione (non un'elisione, va letta insieme al testo
del nodo): il testo ufficiale disponibile in cap03.txt ha una struttura
tabellare Markdown pulita (`|cella|cella|` con separatore `|---|---|`) per
le righe relative agli articoli 5.1, 13.2, 15 e 19 (fine pagina 27) e di
nuovo per le righe relative all'art. 24 §§2(g)-(k)/§§3-4, art. 28(38) e
Allegati I/III/IV (pagine 29-30). Nel mezzo — le righe relative all'art. 24
§1 e §2(b)-(f), a cavallo del cambio pagina 27→28 — l'estrazione ufficiale
perde la sintassi a pipe (verosimilmente perché la cella "regulation text"
per l'art. 24 è un paragrafo multi-riga che il convertitore PDF→testo non
è riuscito a mantenere dentro una tabella Markdown a cavallo di pagina) e il
contenuto compare come paragrafi in chiaro, con l'ordine di lettura colonna
riferimento/colonna testo normativo non sempre lineare rispetto alle altre
righe della tabella. Non essendo disponibile il PDF originale per
ricostruire con certezza la topologia esatta delle celle in quel tratto,
questo modulo riporta OGNI porzione di testo trovata, nello stesso ordine di
lettura del file sorgente, usando sintassi di tabella Markdown dove il
sorgente la usa e paragrafi semplici dove il sorgente la perde — zero
parole omesse, zero parole aggiunte, nessun marcatore di elisione. I
marcatori di paginazione PDF puramente redazionali ("***ETSI***",
"<!-- Page NN -->") sono stati rimossi in quanto paratesto non normativo,
non contenuto della tabella.

## Annex B (informative): Conformity Assessment Checklist

Un solo nodo Principio "altro", riferimento "Parte 2: Annex B": il testo è un breve
paragrafo introduttivo che rimanda integralmente a ETSI TR 119 411-4 [i.10]
per la checklist di conformità vera e propria (non riprodotta nel presente
documento) — nessun contenuto normativo proprio oltre il rinvio, riportato
verbatim.

## RELAZIONI

Vuoto per vincolo di fase — nessuna relazione, né interna al capitolo né
cross-capitolo/cross-fonte (incluse le citazioni a ETSI EN 319 411-1 in
OVR-7.1-01/OVR-7.2-01 e nella Table A.1). Verrà eventualmente popolato dalla
pipeline dedicata (ADR-0009) o da una cura editoriale successiva.

## Conteggio

3 Obblighi (OVR-7.1-01, OVR-7.1-02, OVR-7.2-01) + 2 Principi (Annex A Table
A.1, Annex B) = 5 righe, 5 item di indice.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "Parte 2: OVR-7.1-01",
        "testo": "Si applicano i requisiti identificati nella clausola 7.1 di ETSI EN 319 411-1.",
        "testo_integrale": (
            "The requirements identified in ETSI EN 319 411-1 [2], clause 7.1 shall apply. "
            "In addition the following particular requirements apply:"
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.1-02",
        "testo": (
            "La certificate policy deve incorporare, o vincolare ulteriormente, tutti i requisiti "
            "delle clausole 5 e 6 del presente documento, come appropriato all'uso, costruendo sui "
            "requisiti della certificate policy pertinente definita nel documento."
        ),
        "testo_integrale": (
            "The certificate policy shall incorporate, or further constrain, all the requirements "
            "identified in clauses 5 and 6 of the present document, as appropriate to the usage, "
            "building on the requirements of the appropriate certificate policy as defined in the "
            "present document."
        ),
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Parte 2: OVR-7.2-01",
        "testo": "Si applicano i requisiti identificati nella clausola 7.2 di ETSI EN 319 411-1.",
        "testo_integrale": "The requirements identified in ETSI EN 319 411-1 [2], clause 7.2 shall apply.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

_TABELLA_A1 = """Annex A (informative): Regulation and EU qualified certificate policy mapping

Table A.1 identifies how the security controls objectives and other parts of the EU Qualified Certificate Policies (QCP) defined in the present document address the requirements of TSP issuing qualified certificates as defined in articles 19 and 24 and annexes of Regulation (EU) No 910/2014 [i.1]. This annex should not be taken as definitive statement of conformance to the Regulation (EU) No 910/2014 [i.1]. There are requirements in the Regulation (EU) No 910/2014 [i.1] which are not technical and are then out of scope of the present document, and the present document has not been subject to any legal review.

| Table A.1 | |
|---|---|
| Regulation article 5.1 Data protection | EU qualified certificate policy reference |
| "5 1. Processing of personal data shall be carried out in accordance with Directive 95/46/EC." | ETSI EN 319 401 [1], REQ-7.13-05 and note |
| Regulation article 13.2 Liability and burden of proof | EU qualified certificate policy reference |
| "13 2. Where trust service providers duly inform their customers in advance of the limitations on the use of the services they provide and where those limitations are recognisable to third parties, trust service providers shall not be liable for damages arising from the use of services exceeding the indicated limitations." | ETSI EN 319 401 [1], REQ-6.2-02 items f) and g) |
| Regulation article 15 Accessibility for persons with disabilities | EU qualified certificate policy reference |
| "Where feasible, trust services provided and end-user products used in the provision of those services shall be made accessible for persons with disabilities." | ETSI EN 319 401 [1], REQ-7.13-03 and REQ-7.13-04 |
| Regulation article 19 Security requirements applicable to trust service providers | EU qualified certificate policy reference |
| "19 1. Qualified and non-qualified trust service providers shall take appropriate technical and organisational measures to manage the risks posed to the security of the trust services they provide. Having regard to the latest technological developments, those measures shall ensure that the level of security is commensurate to the degree of risk." "In particular, measures shall be taken to prevent and minimise the impact of security incidents and inform stakeholders of the adverse effects of any such incidents." | Clause 6.4 ETSI EN 319 411-1 [2], clause 6.4 ETSI EN 319 401 [1], clauses 5, 6.3 and 7.3 ETSI EN 319 401 [1], clause 7.6 ETSI EN 319 401 [1], REQ-7.4-04A to REQ-7.4-09 ETSI EN 319 401 [1], clause 7.2 ETSI EN 319 401 [1], clause 7.10 ETSI EN 319 401 [1], clauses 7.9 and 7.11 ETSI EN 319 401 [1], clause 7.12 (termination) Clause 6.5 ETSI EN 319 411-1 [2], clause 6.5 ETSI EN 319 401 [1], clause 7.5 ETSI EN 319 401 [1], REQ-7.4-10, REQ-7.8-16 and REQ-7.8-17 ETSI EN 319 401 [1], clause 7.7 ETSI EN 319 401 [1], clause 7.8 ETSI EN 319 411-1 [2], clause 6.4.8 ETSI EN 319 411-1 [2], clause 6.4.8 ETSI EN 319 401 [1], clauses 7.9 and 7.11 |
| "19. 2. Qualified and non-qualified trust service providers shall, without undue delay but in any event within 24 hours after having become aware of it, notify the supervisory body and, where applicable, other relevant bodies, such as the competent national body for information security or the data protection authority, of any breach of security or loss of integrity that has a significant impact on the trust service provided or on the personal data maintained therein. Where the breach of security or loss of integrity is likely to adversely affect a natural or legal person to whom the trusted service has been provided, the trust service provider shall also notify the natural or legal person of the breach of security or loss of integrity without undue delay." | Clause 6.4.8 ETSI EN 319 411-1 [2], clause 6.4.8 ETSI EN 319 401 [1], clauses 7.9 and 7.11 |

**EU qualified certificate policy reference** ETSI EN 319 401 [1], clause 7.2 Clause 6.2.2 ETSI EN 319 411-1 [2], clause 6.2.2 Clause 6.2.3 *The information referred to in the first subparagraph shall be verified by* ETSI EN 319 411-1 [2], clause 6.2.3

Clause 6.4.4 ETSI EN 319 411-1 [2], clause 6.4.4 *who have received appropriate training regarding security and personal* ETSI EN 319 401 [1], clause 7.2

**Regulation article 24** **Requirements for qualified trust service providers** *"24.1. Verify, by appropriate means and in accordance with national law, the identity and, if applicable, any specific attributes of the natural or legal person to whom the qualified certificate is issued.*

*the qualified trust service provider either directly or by relying on a third party in accordance with national law:*

*(a) by the physical presence of the natural person or of an authorised representative of the legal person; or*
*(b) remotely, using electronic identification means, for which prior to the issuance of the qualified certificate, a physical presence of the natural person or of an authorised representative of the legal person was ensured and which meets the requirements set out in Article 8 with regard to the assurance levels 'substantial' or 'high'; or*
*(c) by means of a certificate of a qualified electronic signature or of a qualified electronic seal issued in compliance with point (a) or*
*(b); or*
*(d) by using other identification methods recognised at national level which provide equivalent assurance in terms of reliability to physical presence. The equivalent assurance shall be confirmed by a conformity assessment body."*

*"24.2 (b) employ staff and, if applicable, subcontractors who possess the necessary expertise, reliability, experience, and qualifications and data protection rules and shall apply administrative and management procedures which correspond to European or international standards."* *"24.2 (c) with regard to the risk of liability for damages in accordance with Article 13, maintain sufficient financial resources and/or obtain appropriate liability insurance, in accordance with national law;"* *"24.2 (d) before entering into a contractual relationship, inform, in a clear and comprehensive manner, any person seeking to use a use of that service, including any limitations on its use;"*

Clause 6.8.2 ETSI EN 319 411-1 [2], clause 6.8.2 ETSI EN 319 401 [1], REQ-7.1.1-04 ETSI EN 319 411-1 [2], DIS-6.1-04 to DIS-6.1-09 ETSI EN 319 411-1 [2], REG-6.3.4-02 to Clause 6.9.4 ETSI EN 319 411-1 [2], clause 6.9.4 ETSI EN 319 401 [1] clause 6.2 Clause 6.5 ETSI EN 319 411-1 [2], clause 6.5 ETSI EN 319 401 [1], clause 7.5 ETSI EN 319 401 [1], clause 7.6 ETSI EN 319 401 [1], REQ-7.4-10, REQ-7.8-16 and REQ-7.8-17 ETSI EN 319 401 [1], clause 7.7 ETSI EN 319 401 [1], clause 7.8

*"24.2 (e) use trustworthy systems and products that are protected against modification and ensure the technical security and reliability of the processes supported by them;"*

| "24.2 (f) use trustworthy systems to store data provided to them, in a | | Clause 6.4.3 |
|---|---|---|
| verifiable form so that: | | ETSI EN 319 411-1 [2], clause 6.4.3 |
| (i) | they are publicly available for retrieval only where the consent of the person to whom the data relates has been obtained, | Clause 6.4.6 |
| (ii) | only authorised persons can make entries and changes to the stored data, | ETSI EN 319 411-1 [2], clause 6.4.6 |
| (iii) | the data can be checked for authenticity;" | Clause 6.5 |

ETSI EN 319 411-1 [2], clause 6.5 ETSI EN 319 401 [1], clause 7.5 ETSI EN 319 401 [1], clause 7.6 ETSI EN 319 401 [1], REQ-7.4-10, REQ-7.8-16 and REQ-7.8-17 ETSI EN 319 401 [1], clause 7.7 <u>ETSI EN 319 401 [1], clause 7.8</u>

*qualified trust service of the precise terms and conditions regarding the* REG-6.3.4-03 and OVR-6.3.4-04 to OVR-6.3.4-06

| Regulation article 24 Requirements for qualified trust service providers | EU qualified certificate policy reference |
|---|---|
| "24.2 (g) take appropriate measures against forgery and theft of data;" | Clause 6.4 ETSI EN 319 411-1 [2], clause 6.4 ETSI EN 319 401 [1], clauses 5, 6.3 and 7.3 ETSI EN 319 401 [1], clause 7.6 ETSI EN 319 401 [1], REQ-7.4-04A to REQ-7.4-09 ETSI EN 319 401 [1], clause 7.2 ETSI EN 319 401 [1], clause 7.10 ETSI EN 319 401 [1], clauses 7.9 and 7.11 ETSI EN 319 401 [1], clause 7.12 (termination) Clause 6.5 ETSI EN 319 411-1 [2], clause 6.5 ETSI EN 319 401 [1], clause 7.5 ETSI EN 319 401 [1], REQ-7.4-10, REQ-7.8-16 and REQ-7.8-17 ETSI EN 319 401 [1], clause 7.7 ETSI EN 319 401 [1], clause 7.8 |
| "24.2 (h) record and keep accessible for an appropriate period of time, including after the activities of the qualified trust service provider have ceased, all relevant information concerning data issued and received by the qualified trust service provider, in particular, for the purpose of providing evidence in legal proceedings and for the purpose of ensuring continuity of the service. Such recording may be done electronically;" | ETSI EN 319 411-1 [2], REG-6.2.2-18 ETSI EN 319 411-1 [2], REG-6.3.4-07, REG-6.3.4-08, and REG-6.3.4-17 ETSI EN 319 411-1 [2], REG-6.3.8-02 ETSI EN 319 411-1 [2], REG-6.4.5-04 Clause 6.4.6 ETSI EN 319 411-1 [2], clause 6.4.6 Clause 6.4.9 in ETSI EN 319 411-1 [2], clause 6.4.9 ETSI EN 319 401 [1], clause 7.12 ETSI EN 319 401 [1], REQ-7.3.2-02 |
| "24.2 (i) have an up-to-date termination plan to ensure continuity of service in accordance with provisions verified by the supervisory body." | Clause 6.4.9 ETSI EN 319 411-1 [2], clause 6.4.9 ETSI EN 319 401 [1], clause 7.12 |
| "24.2 (j) ensure lawful processing of personal data in accordance with Directive 95/46/EC." | Clause 6.8.4 ETSI EN 319 411-1 [2], clause 6.8.4 ETSI EN 319 401 [1], REQ-7.13-05 |
| "24.2 (k) in case of qualified trust service providers issuing qualified certificates, establish and keep updated a certificate database." | Clause 6.1 ETSI EN 319 411-1 [2], clause 6.1 |
| "24.3. If a qualified trust service provider issuing qualified certificates decides to revoke a certificate, it shall register such revocation in its certificate database and publish the revocation status of the certificate in a timely manner, and in any event within 24 hours after the receipt of the request. The revocation shall become effective immediately upon its publication." | Clause 6.2.4 ETSI EN 319 411-1 [2], clause 6.2.4 Clause 6.3.9 ETSI EN 319 411-1 [2], clause 6.3.9 |
| "24.4. With regard to paragraph 3, qualified trust service providers issuing qualified certificates shall provide to any relying party information on the validity or revocation status of qualified certificates issued by them. This information shall be made available at least on a per certificate basis at any time and beyond the validity period of the certificate in an automated manner that is reliable, free of charge and efficient." | Clause 6.3.10 ETSI EN 319 411-1 [2], clause 6.3.10 "free of charge" is out of scope |
| Regulation article 28 (38) Qualified certificates for electronic signatures (Qualified certificates for electronic seal) | EU qualified certificate policy reference |
| "28, (38) 3. Qualified certificates for electronic signatures (seals) may include non-mandatory additional specific attributes. Those attributes shall not affect the interoperability and recognition of qualified electronic signatures (seals)." | ETSI EN 319 411-1 [2], clause 6.6.1 |
| "28, (38) 4. If a qualified certificate for electronic signatures (seal) has been revoked after initial activation, it shall lose its validity from the moment of its revocation, and its status shall not in any circumstances be reverted." | ETSI EN 319 411-1 [2], REV-6.3.9-04 |

| Regulation article 28 (38) Qualified certificates for electronic signatures (Qualified certificates for electronic seal) | EU qualified certificate policy reference |
|---|---|
| "28, (38) 5. Subject to the following conditions, Member States may lay down national rules on temporary suspension of qualified certificates for electronic signatures (seals): (a) if a qualified certificate for electronic signature (seal) has been temporarily suspended that certificate shall lose its validity for the period of suspension; (b) the period of suspension shall be clearly indicated in the certificate database and the suspension status shall be visible, during the period of suspension, from the service providing information on the status of the certificate." | The present document places no restrictions on use of suspension. |
| Regulation articles 28 1, 38 1 and 45 1; conformity to Annexes I, III and IV specifying requirement for qualified certificates | EU qualified certificate policy reference |
| Annexes I and III (a) to (i), Annex IV (a) to (j), Annexes I and III (j) | GEN-6.6.1-02 ETSI EN 319 411-1 [2], clause 6.6.1 GEN-6.6.1-03 |
| Regulation requirement on other TSP than TSP issuing certificates but to be verified by TSP issuing EU qualified certificates | EU qualified certificate policy reference |
| Article 30 certification of qualified electronic signature creation devices | SDP-6.5.1-02 |
| "Annex II 3: Generating or managing electronic signature creation data on behalf of the signatory may only be done by a qualified trust service provider." | SDP-6.5.1-03 |
| "Annex II 4 qualified trust service providers managing electronic signature creation data on behalf of the signatory may duplicate the electronic signature creation data only for back-up purposes provided the following requirements are met: (a) the security of the duplicated datasets must be at the same level as for the original datasets; (b) the number of duplicated datasets shall not exceed the minimum needed to ensure continuity of the service." | Clause 6.3.12 ETSI EN 319 411-1 [2], clause 6.3.12 |"""

RIGHE_PRINCIPI = [
    {
        "riferimento": "Parte 2: Annex A (Table A.1)",
        "testo": (
            "Tabella informativa che mappa gli obiettivi di controllo di sicurezza e le altre "
            "disposizioni delle EU Qualified Certificate Policy (QCP) definite nel presente "
            "documento sui requisiti del TSP che emette certificati qualificati ai sensi degli "
            "articoli 5.1, 13.2, 15, 19, 24, 28/38/45 e degli Allegati I/II/III/IV del Regolamento "
            "(UE) n. 910/2014, con rinvio incrociato alle clausole/REQ pertinenti di ETSI EN 319 "
            "401, ETSI EN 319 411-1 e del presente documento; espressamente non costituisce "
            "dichiarazione definitiva di conformità al Regolamento, che contiene anche requisiti "
            "non tecnici fuori dall'ambito del documento."
        ),
        "testo_integrale": _TABELLA_A1,
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Parte 2: Annex B",
        "testo": (
            "Rimanda integralmente a ETSI TR 119 411-4 per la checklist di conformità ai requisiti "
            "del presente documento, ai requisiti generici indipendenti dal TSP (ETSI EN 319 401) e "
            "a quelli indipendenti dal tipo di certificato emesso (ETSI EN 319 411-1); utilizzabile "
            "sia dal TSP per l'autovalutazione sia dall'organismo di valutazione della conformità."
        ),
        "testo_integrale": (
            "Annex B (informative): Conformity Assessment Checklist\n\n"
            "A checklist for the policy requirements specified in the present document as well as "
            "the generic requirements which are independent of the TSP (as expressed in ETSI EN 319 "
            "401 [1]) and independent of the type of certificate issued (as expressed in ETSI EN 319 "
            "411-1 [2]) is contained in ETSI TR 119 411-4 [i.10]. The checklist lists the conformity "
            "criteria in such a way that it can be used by the TSP itself to prepare for an "
            "assessment of its practices against the present document (i.e. serve as a basis for a "
            "self-declaration) and/or by the assessor when conducting the assessment, for the sake "
            "of facility for both the assessor and the TSP to be assessed."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Parte 2: OVR-7.1-01", "Parte 2: OVR-7.1-02", "Parte 2: OVR-7.2-01",
    "Parte 2: Annex A (Table A.1)", "Parte 2: Annex B",
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
