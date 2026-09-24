"""ETSI EN 319 421 V1.3.1 (2025-07) - Electronic Signatures and Trust
Infrastructures (ESI); Policy and Security Requirements for Trust Service
Providers issuing Time-Stamps. Fonte 18 (numerazione definitiva cablata dalla
sessione principale in app/seed.py - questo modulo NON tocca seed.py).
Capitolo 6: annex informative A-H - Annex A (responsabilita' nell'erogazione
dei servizi di marca temporale), Annex B (modello di TSA disclosure
statement), Annex C (Coordinated Universal Time), Annex D (verifica a lungo
termine delle marche temporali), Annex E (cross-reference con il Regolamento
(UE) n. 910/2014), Annex F.1 (servizio gestito) e F.2 (qualita' alternativa
selettiva), Annex G (modifiche principali rispetto a ETSI TS 102 023), Annex
H (check list di valutazione della conformita'). Testo ufficiale in
app/.source_cache/etsi_319_421/cap06.txt, letto SEMPRE con il selettore
":raw" del tool di lettura: diverse righe di questo capitolo superano i 1000
caratteri e senza ":raw" verrebbero troncate a 768 caratteri con l'aggiunta
di un marcatore di ellissi, facendo scattare (correttamente) la guardia
`verifica_completezza_testo_integrale` di app/seed_data/lib.py. Manifest di
split: app/.source_cache/etsi_319_421/manifest.json.

Modellazione (adattamento ETSI di ADR-0007, stesso criterio delle altre fonti
ETSI gia' censite): gli annex A-H sono informativi e non contengono alcun
requisito numerato (nel testo non compare nessun identificatore OVR-/TIS-),
quindi non generano Obblighi: ogni unita' di contenuto e' modellata come un
singolo nodo Principio, tutti con stato "vigente". Il tipo_principio e'
scelto tra "altro" (contenuto esplicativo/illustrativo/descrittivo, scelta di
default) e "definitorio" (contenuto che definisce un concetto o una grandezza
usata dal documento), voce per voce:

- "Annex A (Potential liability in the provision of time-stamping services)"
  -> "altro". Inquadramento giuridico informativo della responsabilita' del
  TSA (fonti: contratto o legge nazionale; tutele statutarie a favore dei
  consumatori, in particolare Direttiva 93/13/EEC [i.5] sulle clausole
  abusive e relative attuazioni nazionali, che possono persino aumentare il
  livello di protezione e limitare la capacita' del TSA di escludere la
  responsabilita'; possibilita' residua di escludere garanzie e limitare la
  responsabilita' fuori da tali eccezioni). Non definisce un termine del
  documento e non e' una clausola di scopo/ambito: "altro".
- "Annex B (Model TSA disclosure statement)" -> "altro". UN SOLO nodo che
  copre B.1 (Introduction), B.2 (TSA disclosure statement structure) e
  l'intera tabella B.1 (tipi di statement, descrizioni, requisiti specifici):
  e' un modello/esempio di strumento supplementare di disclosure, non la
  definizione di un concetto ne' l'illustrazione di una architettura.
- "Annex C (Coordinated Universal Time (UTC))" -> "definitorio". Definisce la
  scala temporale UTC (mantenuta dal BIPM con l'assistenza dell'IERS, base
  della diffusione coordinata di frequenze e segnali orari, corrispondente
  esattamente in frequenza al TAI ma differenziata da un numero intero di
  secondi) su cui si fonda la sincronizzazione dell'orologio della TSU
  richiesta dalla clausola 7.7.2 e dalla clausola 8: e' l'unico annex di
  questo capitolo che fissa il significato di un concetto usato dal corpo
  principale, quindi "definitorio" e' piu' preciso di "altro".
- "Annex D (Long term verification of time-stamps)" -> "altro". Spiega quando
  e a quali condizioni una marca temporale resta verificabile oltre la fine
  del periodo di validita' del certificato della TSU (chiave privata della
  TSU non compromessa, nessuna collisione degli algoritmi di hash usati,
  algoritmo e lunghezza della chiave di firma fuori dalla portata degli
  attacchi crittografici) e quali meccanismi possono mantenere la validita'
  (marca temporale aggiuntiva a protezione dell'integrita' della precedente,
  ovvero collocazione dei dati marcati in archivio sicuro), dichiarando
  esplicitamente che i dettagli non sono specificati dal documento. E'
  spiegazione informativa, non definizione: "altro".
- "Annex E (Regulation (EU) No 910/2014 and qualified electronic time-stamp
  policy cross-reference)" -> "altro". Tabella E.1 di raccordo
  (cross-reference) tra i requisiti del Regolamento (UE) n. 910/2014 (articolo
  3 e clausola 33 per la definizione di marca temporale elettronica, articolo
  24 §2 per i requisiti sui prestatori di servizi fiduciari qualificati,
  articolo 42 §1 lettere a), b) e c)) e le clausole della Best practices
  Time-Stamp Policy (BTSP) definita nel presente documento. E' l'UNICO nodo
  di questo capitolo con oggetti_giuridici = ["marca temporale elettronica
  qualificata"], perche' l'intero annex riguarda esclusivamente le marche
  temporali elettroniche qualificate ai sensi dell'articolo 42 eIDAS; per
  tutti gli altri annex la chiave e' omessa non essendo legati a un oggetto
  giuridico specifico (A riguarda la responsabilita', C una scala temporale,
  D la verifica a lungo termine, B/F strumenti e architetture, G una
  cronologia di modifiche, H una check list di conformita').
- "Annex F.1 (Managed time-stamping service)" e "Annex F.2 (Selective
  alternative quality)" -> DUE nodi distinti, entrambi "altro": sono due
  architetture/opzioni di implementazione autonome (F.1: servizio gestito, con
  una o piu' Time-Stamping Unit installate nei locali dell'organizzazione
  ospitante e gestite da remoto da una TSA che assume la responsabilita'
  complessiva della qualita' del servizio; F.2: qualita' alternativa
  selettiva, per algoritmo di firma e/o lunghezza della chiave e accuratezza
  del tempo contenuto nella marca). Il titolo dell'annex F ("Annex F
  (informative): Possible implementation architectures-time-stamping
  service", che nella conversione e' spezzato su due righe) e' riportato in
  testa al solo nodo F.1 - primo nodo dell'annex - e non ripetuto in F.2, per
  non duplicare contenuto fra i due nodi dello stesso annex.
- "Annex G (Major changes from ETSI TS 102 023)" -> "altro". Elenco
  informativo delle modifiche rispetto all'edizione ETSI TS 102 023 (rinvio
  alla general TSP policy di ETSI EN 319 401 [4]; modifiche alle clausole
  3.1, 6.2, 7.6.2, 7.6.3, 7.6.4, 7.6.5, 7.6.7, 7.7.2). Cronologia di
  modifiche, non definizione: "altro".
- "Annex H (Conformity Assessment Check list)" -> "altro". Rinvia alla check
  list contenuta nel file foglio di calcolo EN319421-checklist.xlsx reso
  disponibile dal repository Forge ETSI indicato nel testo, ne descrive l'uso
  da parte del TSP (preparazione alla valutazione delle proprie prassi, base
  per un'autodichiarazione) e dell'assessore, e riporta la concessione ETSI di
  riprodurre liberamente il file della check list e pubblicarlo compilato.
  Contenuto procedurale/illustrativo: "altro".

Clausole senza requisito, paratesto e perimetro:
- Nessuno degli annex A-H porta requisiti numerati, quindi RIGHE_OBBLIGHI e'
  vuota (0 obblighi) e i 9 nodi Principio esauriscono il perimetro assegnato
  (dal marker "## Annex A (informative)" fino alla fine di "## Annex H
  (informative): Conformity Assessment Check list"): non esistono clausole di
  cornice ulteriori da censire dentro il perimetro, perche' ogni unita' di
  contenuto coincide con uno dei 9 annex/sottoannex elencati.
- "Annex I (informative): Change history" (tabella delle modifiche V1.2.0 /
  V1.2.7 / V1.3.1, resa dalla conversione come tabella "Change history") e'
  paratesto editoriale: ESCLUSO dall'estrazione (assegnato a cap07_escluso),
  nessun nodo e nessun item di indice.
- Paratesto di conversione PDF->markdown escluso da `testo_integrale`: i
  marcatori di pagina "***ETSI***", i commenti "<!-- Page NN -->" e la riga
  "|||25|" (numero di pagina finito dentro la tabella) non sono contenuto del
  documento. Le etichette "<u>...</u>" (sottolineatura dell'originale) sono
  invece conservate verbatim, come gia' fatto per ETSI EN 319 411-2 Parte 2
  Annex A. I titoli di annex spezzati su due righe dalla conversione
  ("## Annex E ... qualified electronic" + "## time-stamp policy
  cross-reference"; "## Annex F ... architectures-time-stamping" +
  "service") sono ricomposti in un unico titolo separato da uno spazio, senza
  modificare ne' aggiungere parole.
- NOTE ed EXAMPLE: nessuno degli annex di questo capitolo contiene NOTE o
  EXAMPLE del testo ufficiale (verificato sul testo di split), quindi non si
  pone il problema di distinguere NOTE interpretative da NOTE meramente
  bibliografiche.

Difetto di resa di Annex B (segnalato, NON corretto): la conversione
PDF->markdown rende la pagina dell'annex B come una tabella in cui il titolo
dell'annex, il testo di B.1 (Introduction) e quello di B.2 (TSA disclosure
statement structure) finiscono dentro le celle, mescolati: la riga che apre
la tabella e' "|Annex B (informative): B.1 Introduction practice statement.|
Model TSA disclosure statement The proposed model ... contained in a deployed
time-stamping service.||", con la frase di B.1 spezzata a meta' ("... is not
intended to replace a security policy or" + "This annex provides an example of
the structure ..."). La tabella B.1 vera e propria (riga "|Statement
types|Statement descriptions|Specific requirements|") non ha riga di
delimitazione markdown sotto l'intestazione; la continuazione a pagina 25 e'
una seconda tabella introdotta dalla riga "|||25|" e alcune righe sono
disallineate (es. "Applicable law, complaints" / "and dispute resolution" su
due righe con il testo della terza colonna spostato, e "TSA and repository" /
"licenses, trust marks, and" / "audit" su tre righe, con "**Specific
requirements**" e "<u>and if applicable the audit firm.</u>" emessi come
paragrafi separati a fine pagina). Il testo e' riportato verbatim cosi' come
arriva dalla conversione, senza ricostruire le celle ne' inserire righe di
delimitazione mancanti: la resa si corregge solo confrontando l'originale PDF,
il che non e' compito di questo censimento. Segnalata in Annex G anche la
forma "requirement b) updated to ISO a CEN/TS references" (verosimilmente
"and"), riportata verbatim senza correzione.

Relazioni: RELAZIONI e' vuota. In questo capitolo non compare alcuna citazione
letterale di un requirement id (pattern OVR-.../TIS-...): Annex G cita solo
numeri di clausola con lettere di requisito ("Clause 7.6.2 ... requirement
b)", "Clause 7.7.2 ... requirement d)") e Annex E rinvia ad articoli eIDAS e a
clausole di policy, non a id di requisito; i rinvii di clausola ("see clause
6.6", "see annex A") non costituiscono relazione ai sensi del criterio
adottato (solo citazione letterale dell'id). NESSUNA relazione verso fonti
diverse dalla 18, anche dove il testo cita Regolamento (UE) n. 910/2014, ETSI
EN 319 401, ETSI EN 319 411-1 o ETSI EN 319 422: il collegamento cross-fonte
e' demandato alla Fase 6 della sessione principale (ADR-0009).

Copertura: INDICE_ARTICOLI_LOCALE contiene 9 item (uno per annex/sottoannex),
MAPPATURA_LOCALE mappa ciascun item sul proprio riferimento (nessun
accorpamento reale, nessun item doppio) e nessun item collide con gli altri
capitoli della fonte (i capitoli 1-5 coprono clausole 1-8, questo capitolo
solo gli annex A-H).
"""

RIGHE_OBBLIGHI: list[dict] = []
# Nessun Obbligo in questo capitolo: gli annex A-H sono informativi e non
# contengono requisiti numerati (nessun identificatore OVR-/TIS-).

RIGHE_PRINCIPI = [
    {
        "riferimento": (
            "Annex A (Potential liability in the provision of time-stamping services)"
        ),
        "testo": (
            "Annesso informativo sulla responsabilita' del TSA nell'erogazione dei servizi di marca "
            "temporale: la responsabilita' deriva da contratto o da legge (diritto nazionale); quando "
            "sono coinvolti consumatori si applicano anche tutele statutarie - in particolare la "
            "Direttiva 93/13/EEC sulle clausole abusive e le relative attuazioni nazionali, che possono "
            "persino aumentare il livello di protezione - che possono limitare la capacita' del TSA di "
            "escludere la propria responsabilita', perche' la Direttiva 93/13/EEC vieta le clausole non "
            "negoziate individualmente che determinano un significativo squilibrio dei diritti e degli "
            "obblighi delle parti a danno del consumatore; anche il diritto nazionale puo' stabilire "
            "ulteriori restrizioni alla limitazione di responsabilita'. Fuori da queste eccezioni il TSA "
            "puo' escludere qualsiasi garanzia e limitare la propria responsabilita'."
        ),
        "testo_integrale": (
            "Annex A (informative): Potential liability in the provision of time-stamping services\n\nLiability"
            " derives from one of two sources: contract or statutory law (i.e. national law). Where consumers"
            " are involved, statutory protections can also apply-especially the Unfair Contract Terms "
            "Directive (Directive 93/13/EEC [i.5]) and the corresponding national implementations, which can "
            "even increase the level of protection. These rules can constrain the TSA's capability to limit "
            "its liability, because the Directive 93/13/EEC [i.5] prohibits terms that have not been "
            "individually negotiated which cause a significant imbalance in the parties' rights and "
            "obligations to the detriment of the consumer. A national law can also establish additional "
            "restrictions on liability limitation. Where these exceptions do not apply, a TSA may disclaim "
            "any or all warranties and limit its liability."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex B (Model TSA disclosure statement)",
        "testo": (
            "Annesso informativo con il modello di TSA disclosure statement (Tabella B.1), strumento "
            "supplementare e semplificato di disclosure e notice rispetto alla security policy e alla "
            "practice statement: B.1 (Introduction) ne spiega la finalita' - rispondere ai requisiti e "
            "alle preoccupazioni regolatorie, specie per il dispiegamento verso i consumatori, e "
            "favorire l'autoregolamentazione di settore costruendo consenso sugli elementi della "
            "security policy e/o practice statement che richiedono enfasi e disclosure - e chiarisce "
            "che, poiche' tali documenti sono di difficile comprensione per molti utenti e soprattutto "
            "per i consumatori, serve uno strumento supplementare e semplificato che li aiuti a "
            "prendere decisioni di affidamento informate, senza sostituire la security policy o la "
            "practice statement. B.2 (TSA disclosure statement structure) stabilisce che la "
            "dichiarazione contiene una sezione per ciascun tipo di statement definito, con una "
            "descrizione che puo' includere hyperlink alla certificate policy o certification practice "
            "statement pertinente. La Tabella B.1 elenca i tipi di statement (entire agreement; "
            "contatti del TSA; tipi e uso delle marche temporali elettroniche; limiti di affidamento; "
            "obblighi dei sottoscrittori; obblighi delle relying party di verifica dello stato del "
            "certificato a chiave pubblica della TSU; garanzia limitata ed esclusione o limitazione di "
            "responsabilita'; accordi e practice statement applicabili; privacy policy; refund policy; "
            "legge applicabile, reclami e risoluzione delle controversie; licenze, trust mark e audit "
            "del TSA e del repository), con la relativa descrizione e, dove previsti, i requisiti "
            "specifici (fra cui: indicazione della policy applicata, dei contesti d'uso, degli "
            "algoritmi di hash, della vita attesa della firma della marca temporale e delle modalita' "
            "di verifica; accuratezza del tempo e periodo di conservazione dei log del TSA; modalita' "
            "di verifica dello stato del certificato della TSU e revoca, cosi' che la relying party sia "
            "considerata affidarsi ragionevolmente alla marca temporale; limiti di responsabilita' "
            "come in Annex A; procedure di reclamo e risoluzione delle controversie e sistema legale "
            "applicabile; eventuale valutazione di conformita' alla policy identificata e soggetto "
            "indipendente che l'ha eseguita)."
        ),
        "testo_integrale": (
            "|Annex B (informative): B.1 Introduction practice statement.|Model TSA disclosure statement The "
            "proposed model TSA disclosure statement in table B.1 is designed for use by a TSP issuing "
            "time-stamps as a supplemental instrument of disclosure and notice. A TSA disclosure statement "
            "can assist a TSA to respond to regulatory requirements and concerns, particularly those related "
            "to consumer deployment. Further, the aim of the model TSA disclosure statement is to foster "
            "industry \"self-regulation\" and build consensus on those elements of a security policy and/or "
            "practice statement that require emphasis and disclosure. Although security policy and practice "
            "statement documents are essential for describing and governing time-stamp policies and "
            "practices, many TSA users, especially consumers, can find these documents difficult to "
            "understand. Consequently, there is a need for a supplemental and simplified instrument that can "
            "assist TSA users in making informed trust decisions. Consequently, a TSA disclosure statement is"
            " not intended to replace a security policy or This annex provides an example of the structure "
            "for a TSA disclosure statement, illustrating the harmonized set of statement types (categories) "
            "that would be contained in a deployed time-stamping service.||\n|---|---|---|\n|B.2 practice "
            "statement sections.|TSA disclosure statement structure The TSA disclosure statement contains a "
            "section for each defined statement type. Each section of a TSA disclosure statement contains a "
            "descriptive statement, which may include hyperlinks to the relevant certificate "
            "policy/certification Table B.1: Model of TSA disclosure statement structure||\n\n|Statement "
            "types|Statement descriptions|Specific requirements|\n|Entire agreement|A statement indicating "
            "that the TSA disclosure statement is not the entire agreement, but only a part of it.||\n|TSA "
            "contact info|The name, location and relevant contact information for the TSA.||\n|Electronic "
            "time-stamp types and usage|A description of each class/type of electronic time-stamps issued by "
            "the TSA (in accordance with each time-stamp policy) and any restrictions on time-stamp "
            "usage.|Indication of the policy being applied (i.e. BTSP), including the contexts for which the "
            "time-stamp can be used (e.g. only for use with electronic signatures), the hashing algorithms, "
            "the expected life time of the time-stamp signature, any limitations on the use of the time-stamp"
            " and information on how to verify the time-stamp.|\n|Reliance limits|The reliance limits, if "
            "any.|Indication of the accuracy of the time in the time-stamp, and the period of time for which "
            "TSA event logs are maintained (and hence are available to provide supporting evidence).|\n"
            "|Obligations of subscribers|The description of, or reference to, the critical subscriber "
            "obligations.|No specific requirements identified in the present document. Where applicable the "
            "TSA may specify additional obligations.|\n|TSU public key certificate status checking obligations"
            " of relying parties|The extent to which relying parties are obligated to check the TSU public "
            "key certificate status, and references to further explanation.|Information on how to validate "
            "the TSU public key certificate status, including requirements to check the revocation status of "
            "TSU public key certificate, such that the relying party is considered to \"reasonably rely\" on "
            "the time-stamp (see clause 6.6).|\n|Limited warranty and disclaimer/Limitation of "
            "liability|Summary of the warranty, disclaimers, limitations of liability and any applicable "
            "warranty or insurance programs.|Limitations of liability (see annex A).|\n\n|||25|\n|Statement "
            "types|Statement descriptions||\n|Applicable agreements|Identification and references to||\n|and "
            "practice statement|applicable agreements, practice statement, time-stamp policy and other "
            "relevant documents.||\n|Privacy policy|A description of and reference to the applicable privacy "
            "policy.||\n|Refund policy|A description of and reference to the applicable refund policy.||\n"
            "|Applicable law, complaints|Statement of the choice of law,|The procedures for complaints and "
            "dispute|\n|and dispute resolution|complaints procedure and dispute resolution "
            "mechanisms.|settlements. The applicable legal system.|\n|TSA and repository|Summary of any "
            "governmental|If the TSA has been assessed to be conformant with|\n|licenses, trust marks, "
            "and|licenses, seal programs; and a|the identified time-stamp policy, and if so through|\n"
            "|audit|description of the audit process|which independent party.|\n\n**Specific requirements**\n\n"
            "<u>and if applicable the audit firm.</u>"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex C (Coordinated Universal Time (UTC))",
        "testo": (
            "Annesso informativo che definisce la scala temporale UTC: e' mantenuta dal BIPM con "
            "l'assistenza dell'IERS e costituisce la base di una diffusione coordinata delle frequenze "
            "e dei segnali orari standard; corrisponde esattamente in frequenza al TAI ma ne differisce "
            "per un numero intero di secondi; la definizione completa di UTC e' contenuta nella "
            "Raccomandazione ITU-R TF.460-6."
        ),
        "testo_integrale": (
            "Annex C (informative): Coordinated Universal Time (UTC)\n\nUTC is the time-scale maintained by the"
            " BIPM, with assistance from the IERS, which forms the basis of a coordinated dissemination of "
            "standard frequencies and time signals. It corresponds exactly in rate with TAI but differs from "
            "it by an integer number of seconds. The full definition of UTC is contained in Recommendation "
            "ITU-R TF.460-6 [1]."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex D (Long term verification of time-stamps)",
        "testo": (
            "Annesso informativo sulla verifica a lungo termine delle marche temporali: di regola una "
            "marca temporale diventa non verificabile oltre la fine del periodo di validita' del "
            "certificato della TSU, perche' la CA che ha emesso il certificato di norma non fornisce "
            "piu' informazioni sullo stato di revoca dei certificati scaduti. Se al momento della "
            "verifica la chiave privata della TSU non e' stata compromessa, gli algoritmi di hash usati "
            "nella marca non presentano collisioni e l'algoritmo di firma e la lunghezza della chiave "
            "di firma restano fuori dalla portata degli attacchi crittografici, la verifica della marca "
            "temporale resta possibile anche oltre la fine di tale periodo di validita'. La validita' "
            "puo' essere mantenuta applicando una marca temporale aggiuntiva a protezione "
            "dell'integrita' della precedente, oppure collocando i dati marcati in archivio sicuro; il "
            "presente documento non specifica i dettagli di tali protezioni e, in attesa che siano "
            "definiti miglioramenti a supporto di queste funzionalita', le informazioni possono essere "
            "ottenute con mezzi out-of-band (ad esempio, la garanzia di una CA di rendere disponibili "
            "le informazioni di revoca dopo la fine del periodo di validita' dei certificati delle TSU "
            "soddisferebbe la verifica che la chiave privata della TSU non e' stata compromessa)."
        ),
        "testo_integrale": (
            "Annex D (informative): Long term verification of time-stamps\n\nUsually, a time-stamp becomes "
            "unverifiable beyond the end of the TSU certificate validity period, because the CA that has "
            "issued the certificate does not usually warrant any more providing revocation status information"
            " for expired certificates. If at the time of verification:\n\n- the TSU private key has not been "
            "compromised at any time up to the time that a relying part verifies a time-stamp;\n- the hash "
            "algorithms used in the time-stamp exhibits no collisions at the time of verification; and\n- the "
            "signature algorithm and signature key size under which the time-stamp has been signed is still "
            "beyond the reach of cryptographic attacks at the time of verification;\nthen verification of a "
            "time-stamp can still be performed beyond the end of the TSU certificate validity period. The "
            "validity may be maintained by applying an additional time-stamp to protect the integrity of the "
            "previous one. Alternatively the time-stamped data may be placed in secure storage. The present "
            "document does not specify the details of how such protection can be obtained. For the time "
            "being, and until some enhancements are defined to support these features, the information may be"
            " obtained using out-of-bands means. As an example, should a CA guarantee to make the revocation "
            "status information after the end of TSU certificates validity period, this would fulfil "
            "verification that the TSU private key has not been compromised."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": (
            "Annex E (Regulation (EU) No 910/2014 and qualified electronic time-stamp policy "
            "cross-reference)"
        ),
        "testo": (
            "Annesso informativo che, con la Tabella E.1, identifica come gli obiettivi di controllo di "
            "sicurezza e le altre parti della Best practices Time-Stamp Policy (BTSP) definita nel "
            "presente documento rispondano ai requisiti dei TSA che emettono marche temporali "
            "elettroniche qualificate ai sensi dell'articolo 42 del Regolamento (UE) n. 910/2014: per "
            "ogni riferimento eIDAS (articolo 3 e clausola 33 per la definizione di marca temporale "
            "elettronica; articolo 24 §2 per i requisiti sui prestatori di servizi fiduciari "
            "qualificati; articolo 42 §1 lettere a), b) e c)) e' indicata la clausola di policy "
            "corrispondente (clausola 7.7.1 Time-stamp issuance; marche temporali profilate in ETSI EN "
            "319 422; requisiti generici di ETSI EN 319 401; voci d) ed e) della clausola 7.7.1 per il "
            "divieto di modifiche non rilevabili; voci a), b) e c) per la sorgente di tempo accurata "
            "collegata a UTC)."
        ),
        "testo_integrale": (
            "Annex E (informative): Regulation (EU) No 910/2014 and qualified electronic time-stamp policy "
            "cross-reference\n\nTable E.1 identifies how the security controls objectives and other parts of "
            "the Best practices Time-Stamp Policy (BTSP) defined in the present document address the "
            "requirements of TSAs issuing qualified electronic time-stamps as defined in article 42 of the "
            "Regulation (EU) No 910/2014 [i.4]. **Table E.1: Regulation (EU) No 910/2014 and qualified "
            "electronic time-stamp policy cross-reference**\n\n|Reference|Regulation (EU) No 910/2014 "
            "requirement|Time-stamp policy reference|\n|---|---|---|\n|Article 3|'electronic time stamp' means "
            "data in electronic|Clause 7.7.1 Time-stamp issuance|\n|Clause 33|form which binds other "
            "electronic data to a particular time establishing evidence that these data existed at that "
            "time|Time-stamp profiled in ETSI EN 319 422 [5]|\n|Article 24|Requirements on qualified trust "
            "service provider|met, as relevant to time-stamping, through|\n|Clause 2|providing qualified trust"
            " services|use of ETSI EN 319 401 [4]|\n|Article 42|it binds the date and time to data in such a "
            "manner|Clause 7.7.1 Time-stamp issuance|\n|Clause 1 (a)|as to reasonably preclude the possibility"
            " of the data being changed undetectably|Items d) & e)|\n|Article 42|it is based on an accurate "
            "time source linked to|Clause 7.7.1 Time-stamp issuance|\n|Clause 1 (b)|Coordinated Universal Time"
            " (UTC)|items a), b) & c)|\n|Article 42|it is signed using an advanced electronic signature|Clause"
            " 7.7.1 Time-stamp issuance|\n|Clause 1 (c)|or sealed with an advanced electronic seal of the "
            "qualified trust service provider, or by some|Time-stamp profiled in ETSI EN 319 422 [5] requires"
            " a digital signature|\n<u>equivalent method</u>"
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["marca temporale elettronica qualificata"],
    },
    {
        "riferimento": "Annex F.1 (Managed time-stamping service)",
        "testo": (
            "Annesso informativo sulle possibili architetture di implementazione di un servizio di "
            "marca temporale. F.1 (servizio gestito): alcune organizzazioni sono disposte a ospitare "
            "una o piu' Time-Stamping Unit per sfruttare prossimita' e qualita' del servizio senza "
            "essere responsabili dell'installazione, dell'esercizio e della gestione di tali unita'; "
            "cio' si realizza con unita' installate nei locali dell'organizzazione ospitante e gestite "
            "da remoto da una Time-Stamping Authority che assume la responsabilita' complessiva della "
            "qualita' del servizio reso all'organizzazione ospitante. I requisiti del presente "
            "documento coprono sia il time-stamping management sia l'esercizio dell'unita' che emette "
            "le marche temporali, e la TSA identificata nella marca ha la responsabilita' di "
            "garantirne il rispetto (ad esempio tramite obblighi contrattuali); l'organizzazione "
            "ospitante vorra' in genere poter monitorare l'uso del servizio - come minimo sapere se "
            "funziona e poterne misurare le prestazioni, ad esempio il numero di marche generate in un "
            "certo periodo - e tale monitoraggio puo' essere considerato esterno al servizio di marca "
            "temporale della TSA, per cui la descrizione delle operazioni di gestione nel corpo "
            "principale del documento non e' limitativa e le operazioni di monitoraggio, se eseguite "
            "direttamente sull'unita', possono essere consentite dalla Time-Stamping Authority. Il "
            "diagramma (Figure F.1) rappresenta la Time-Stamping Authority, il time-stamping "
            "management, l'unita' di marca temporale e l'installazione e il monitoraggio da parte "
            "dell'organizzazione ospitante."
        ),
        "testo_integrale": (
            "Annex F (informative): Possible implementation architectures-time-stamping service\n\nF.1 Managed "
            "time-stamping service\n\nSome organizations will be willing to host one or more Time-Stamping "
            "Units in order to take advantage of both the proximity and the quality of the time-stamping "
            "service, without being responsible for the installation, operation and management of these "
            "Time-Stamping Units. This can be achieved by using units that are installed in the premises from"
            " the hosting organization and then remotely managed by a Time-Stamping Authority that takes the "
            "overall responsibility of the quality of the service delivered to the hosting organization.\n\n"
            "##### Time-stamping Authority\n|Time- Stamping Unit Monitoring Hosting "
            "Organization||Time-Stamping Management||\n|---|---|---|---|\n||Installation "
            "Management||Installation Management|\nTime-Stamping Unit\nHosting Organization\n##### Figure F.1: "
            "Managed time-stamping service\n\nThe requirements for time-stamping services described in the "
            "present document include requirements on both the time-stamping management and for the operation"
            " of the unit which issues the time-stamps. The TSA, as identified in the time-stamp, has the "
            "responsibility to ensure that these requirements are met (for example through contractual "
            "obligations). The hosting organization will generally want to be able to monitor the use of the "
            "service and, at a minimum, know whether the service is working or not and even be able to "
            "measure the performances of the service, e.g. the number of time-stamps generated during some "
            "period of time. Such monitoring can be considered to be outside of TSA's time-stamping service. "
            "Therefore the description of the management operation described in the main body of the present "
            "document is not limitative. Monitoring operations, if performed directly on the unit, can be "
            "permitted by the Time-Stamping Authority."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex F.2 (Selective alternative quality)",
        "testo": (
            "F.2 (qualita' alternativa selettiva): alcune relying party sono disposte a sfruttare "
            "caratteristiche particolari di una marca temporale, come uno specifico algoritmo di firma "
            "e/o una specifica lunghezza della chiave oppure una specifica accuratezza del tempo "
            "contenuto nella marca; questi parametri possono essere considerati come la qualita' della "
            "marca temporale, e marche temporali di qualita' diverse possono essere emesse da unita' "
            "diverse operate dalla stessa TSA o da TSA diverse. Una particolare unita' di marca "
            "temporale fornisce una sola combinazione di algoritmo e lunghezza della chiave, essendo "
            "un insieme di hardware e software gestito come unita' con un'unica chiave di firma delle "
            "marche temporali; per ottenere combinazioni diverse occorre quindi usare unita' diverse. "
            "Una particolare unita' puo' fornire un'accuratezza fissa del tempo contenuto nella marca "
            "temporale, oppure accuratezze diverse se istruita in tal senso usando uno specifico modo "
            "di accesso (ad esempio e-mail o http) oppure parametri specifici nella richiesta."
        ),
        "testo_integrale": (
            "F.2 Selective alternative quality\n\nSome relying parties will be willing to take advantage of "
            "particular characteristics from a time-stamp such as a specific signature algorithm and/or key "
            "length or a specific accuracy for the time contained in the time-stamp. These parameters can be "
            "considered as specifying a \"quality\" for the time-stamp. Time-stamps with various qualities can "
            "be issued by different time-stamping units operated by the same or different TSAs.\n\nA particular"
            " time-stamping unit will only provide one combination of algorithm and key length (since a "
            "time-stamping unit is a set of hardware and software which is managed as a unit and has a single"
            " time-stamp signing key). In order to obtain different combinations of algorithm and key length,"
            " different time-stamping units need to be used. A particular time-stamping unit can provide a "
            "fixed accuracy for the time contained in the time-stamp or different accuracy if instructed to "
            "do so either by using a specific mode of access (e.g. e-mail or http) or by using specific "
            "parameters in the request."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex G (Major changes from ETSI TS 102 023)",
        "testo": (
            "Annesso informativo che elenca le modifiche principali rispetto a ETSI TS 102 023: "
            "richiama i requisiti della general TSP policy (ETSI EN 319 401); modifica la definizione "
            "di subscriber nella clausola 3.1; aggiorna la TSA disclosure statement nella clausola 6.2 "
            "(Trust Service Practice Statement); nella clausola 7.6.2 (TSU key generation) aggiorna ai "
            "riferimenti ISO e CEN/TS i requisiti b) ed e), aggiunge al requisito d) la "
            "raccomandazione di non importare la stessa chiave in piu' moduli e prevede al requisito "
            "e) una sola chiave di firma delle marche temporali attiva alla volta; nella clausola "
            "7.6.3 (TSU private key protection) aggiorna ai riferimenti ISO e CEN/TS il requisito a); "
            "nella clausola 7.6.4 (TSU public key certificate) aggiunge il requisito c) per vietare "
            "l'emissione di marche temporali prima del caricamento del certificato della TSA; nella "
            "clausola 7.6.5 (Rekeying TSU's key) riformula la nota 1; nella clausola 7.6.7 (End of "
            "TSU key life cycle) aggiunge le voci 1, 2 e 3; nella clausola 7.7.2 (Clock "
            "Synchronization with UTC) inserisce il requisito d) su derive o salti fuori "
            "sincronizzazione."
        ),
        "testo_integrale": (
            "Annex G (informative): Major changes from ETSI TS 102 023\n\nGeneral TSP policy (ETSI EN 319 401 "
            "[4]) requirements referenced. Clause 3.1 Definitions, subscriber's definition. Clause 6.2 Trust "
            "Service Practice Statement, updated TSA disclosure statement. Clause 7.6.2 TSU key generation, "
            "requirement b) updated to ISO a CEN/TS references. Clause 7.6.2 TSU key generation, requirement "
            "d) recommending that same key should not be imported to multiple modules. Clause 7.6.2 TSU key "
            "generation, requirement e) single time-stamp signing key active at a time. Clause 7.6.3 TSU "
            "private key protection, requirement a) updated to ISO a CEN/TS references. Clause 7.6.4 TSU "
            "public key certificate, requirement c) added to disallow time-stamp issuance before a TSA "
            "certificate is loaded. Clause 7.6.5 Rekeying TSU's key, note 1 reworded. Clause 7.6.7 End of TSU"
            " key life cycle, added items 1, 2 & 3. Clause 7.7.2 Clock Synchronization with UTC, inserted "
            "requirement d) about drifts or jumps out of synchronization."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "Annex H (Conformity Assessment Check list)",
        "testo": (
            "Annesso informativo che rinvia alla check list di valutazione della conformita' contenuta "
            "nel file foglio di calcolo EN319421-checklist.xlsx, reso disponibile dal repository Forge "
            "ETSI indicato nel testo: la check list raccoglie i requisiti di policy specificati nel "
            "presente documento nonche' i requisiti generici indipendenti dal TSP espressi in ETSI EN "
            "319 401, ed e' utilizzabile sia dal TSP per prepararsi a una valutazione delle proprie "
            "prassi rispetto al presente documento (ossia come base per un'autodichiarazione) sia "
            "dall'assessore che conduce la valutazione, a beneficio di entrambi. Nonostante le "
            "disposizioni sulla clausola di copyright relativa al testo del presente documento, ETSI "
            "concede che gli utenti possano riprodurre liberamente il file della check list "
            "identificato in questo annex per gli scopi previsti e pubblicare la check list compilata."
        ),
        "testo_integrale": (
            "Annex H (informative): Conformity Assessment Check list\n\nA check list for the policy "
            "requirements specified in the present document as well as the generic requirements which are "
            "independent of the TSP (as expressed in ETSI EN 319 401 [4]) is contained in the spreadsheet "
            "file EN319421-checklist.xlsx available from "
            "<u>[https://forge.etsi.org/rep/esi/x19_421_time-stamping_services/](https://forge.etsi.org/rep/esi/x19_421_time-stamping_services/)</u>."
            " The check list summarizes the requirements in such a way that it can be used by the TSP itself "
            "to prepare for an assessment of its practices against the present document (i.e. serve as a "
            "basis for a self-declaration) and/or by the assessor when conducting the assessment, for the "
            "sake of facility for both the assessor and the TSP to be assessed. Notwithstanding the "
            "provisions of the copyright clause related to the text of the present document, ETSI grants that"
            " users of the present document may freely reproduce the check list file identified in this annex"
            " so that it can be used for its intended purposes and may further publish the completed check "
            "list."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "Annex A (Potential liability in the provision of time-stamping services)",
    "Annex B (Model TSA disclosure statement)",
    "Annex C (Coordinated Universal Time (UTC))",
    "Annex D (Long term verification of time-stamps)",
    "Annex E (Regulation (EU) No 910/2014 and qualified electronic time-stamp policy cross-reference)",
    "Annex F.1 (Managed time-stamping service)",
    "Annex F.2 (Selective alternative quality)",
    "Annex G (Major changes from ETSI TS 102 023)",
    "Annex H (Conformity Assessment Check list)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_copertura
    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, {len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
