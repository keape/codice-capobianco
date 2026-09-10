"""Popola censimento.db con l'estrazione reale degli obblighi QTSP dal
Regolamento eIDAS (UE) 910/2014 e dal Regolamento (UE) 2024/1183 ("eIDAS2")
che lo modifica, trattati qui come due Fonti distinte (su richiesta esplicita
dell'utente, per poter confrontare cosa e' definito nell'uno e cosa
nell'altro) anziche' come un'unica Fonte evolutiva. Sostituisce i dati di
fantasia del mockup iniziale (ticket 07) con la prima estrazione di produzione.

Fonti primarie consultate in sessione (EUR-Lex, 9/9/2026):
- Testo originale 2014: CELEX 32014R0910 (https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014R0910)
- Regolamento emendante: CELEX 32024R1183 (https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1183)
- Versione consolidata vigente: CELEX 02014R0910-20241018 (https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02014R0910-20241018)

Perimetro: Capitolo III (Trust Services), limitato alle disposizioni che
impongono un obbligo a un soggetto tra le 4 categorie del censimento
(QTSP/gestore, Utente/titolare, Terza parte, Terzi affidanti/pubblico).
Escluse le disposizioni il cui unico soggetto obbligato e' uno Stato
membro, la Commissione o un organismo di vigilanza (fuori schema: nessuna
categoria di soggetto li rappresenta) e le disposizioni puramente
definitorie/dichiarative (es. "una firma elettronica non e' priva di
effetti legali...") prive di un soggetto individuabile.

Testo parafrasato in italiano a partire dal testo inglese ufficiale
(non riproduzione letterale). Tutte le righe restano `stato_validazione='bozza'`:
l'estrazione LLM richiede validazione umana esplicita (ADR-0003, CONTEXT.md).

    .venv\\Scripts\\python.exe seed.py

Ricrea sempre il file da zero.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "censimento.db"
SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def seed():
    if DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))

    def many(table, cols, rows):
        placeholders = ",".join("?" * len(cols))
        conn.executemany(f"INSERT INTO {table} ({','.join(cols)}) VALUES ({placeholders})", rows)

    # --- lookup ---------------------------------------------------------
    many("stati_fonte", ["id", "nome"], [
        (1, "vigente"), (2, "abrogata"), (3, "in transizione"),
    ])
    # Condivisa tra Obbligo e Principio (ticket 08).
    many("stati_norma", ["id", "nome"], [
        (1, "vigente"), (2, "abrogato"), (3, "in transizione eIDAS->eIDAS2"),
    ])
    many("tipi_obbligo", ["id", "nome"], [
        (1, "organizzativo"), (2, "tecnico/sicurezza"), (3, "informativo/trasparenza"),
        (4, "procedurale"), (5, "di conservazione"), (6, "sanzionatorio"),
    ])
    many("tipi_principio", ["id", "nome"], [
        (1, "non discriminazione"), (2, "equivalenza giuridica"),
        (3, "valore probatorio"), (4, "presunzione legale"), (5, "altro"),
    ])
    many("oggetti_giuridici", ["id", "nome"], [
        (1, "firma elettronica"), (2, "firma elettronica avanzata"), (3, "firma elettronica qualificata"),
        (4, "sigillo elettronico"), (5, "sigillo elettronico avanzato"), (6, "sigillo elettronico qualificato"),
        (7, "marca temporale elettronica qualificata"), (8, "documento elettronico"),
        (9, "servizio di recapito elettronico certificato"), (10, "identificazione elettronica"), (11, "altro"),
    ])
    many("categorie_soggetto", ["id", "nome"], [
        (1, "QTSP/gestore"), (2, "Utente/titolare"),
        (3, "Terza parte"), (4, "Terzi affidanti/pubblico"),
    ])
    many("tipi_relazione", ["id", "nome", "nome_inverso"], [
        (1, "sostituisce", "è sostituito da"),
        (2, "specifica", "è specificato da"),
        (3, "si sovrappone a", "si sovrappone a"),
        (4, "richiede come precondizione", "è precondizione di"),
        (5, "è condizionato da", "condiziona"),
    ])

    # --- fonti ------------------------------------------------------------
    # Due Fonti distinte, non una sola: su richiesta esplicita dell'utente,
    # per poter vedere la differenza tra i due regolamenti (ogni obbligo e'
    # assegnato alla Fonte il cui testo lo definisce attualmente). Nota: questo
    # diverge dalla decisione registrata in CONTEXT.md ("una Fonte esiste una
    # volta sola nel censimento") — da riconciliare esplicitamente con l'utente
    # prima di considerarla definitiva.
    many("fonti", ["id", "nome", "url_sorgente", "versione", "data_entrata_vigore", "stato_id"], [
        (1, "Regolamento eIDAS (UE) 910/2014",
         "https://eur-lex.europa.eu/legal-content/IT/TXT/HTML/?uri=CELEX:32014R0910",
         "testo originario (atto come adottato nel 2014)", "2014-09-17", 3),
        (2, "Regolamento (UE) 2024/1183 (\"eIDAS2\")",
         "https://eur-lex.europa.eu/legal-content/IT/TXT/HTML/?uri=CELEX:32024R1183",
         "testo originario (atto come adottato nel 2024, modifica il Reg. 910/2014)", "2024-05-20", 1),
    ])

    # --- obblighi -----------------------------------------------------
    # id, fonte_id, riferimento, testo, tipo, stato, severita, sanzioni, condizione, stato_validazione, validato_da, data_validazione
    # fonte_id: 1 = Regolamento eIDAS 910/2014 (testo originario, che l'obbligo sia
    # ancora vigente o abrogato), 2 = Regolamento (UE) 2024/1183 "eIDAS2" (testo
    # nuovo o sostituito introdotto dall'atto emendante).
    obblighi = [
        # --- Art. 13 - Responsabilita' -----------------------------------
        (1, 1, "art. 13 §1 (testo originario 2014)",
         "Il prestatore di servizi fiduciari è responsabile dei danni causati intenzionalmente o per negligenza a qualsiasi persona fisica o giuridica per la violazione degli obblighi previsti dal regolamento; per il prestatore qualificato l'intenzionalità o la negligenza si presumono, salvo prova contraria a suo carico.",
         6, 2, "alta", "responsabilità civile per danni, con onere della prova invertito per i prestatori qualificati", None, "bozza", None, None),
        (2, 2, "art. 13 §1 (testo vigente, eIDAS2)",
         "Il prestatore di servizi fiduciari è responsabile dei danni causati intenzionalmente o per negligenza a qualsiasi persona fisica o giuridica per la violazione degli obblighi previsti dal regolamento, fermo restando il Regolamento (UE) 2016/679 (GDPR); chi ha subito un danno materiale o immateriale per tale violazione ha diritto al risarcimento secondo il diritto UE e nazionale. Per il prestatore qualificato l'intenzionalità o la negligenza si presumono, salvo prova contraria a suo carico.",
         6, 1, "alta", "responsabilità civile per danni, con onere della prova invertito per i prestatori qualificati; diritto al risarcimento esplicitato", None, "bozza", None, None),
        (3, 1, "art. 13 §2",
         "Se il prestatore di servizi fiduciari informa preventivamente e chiaramente i propri clienti dei limiti d'uso del servizio, e tali limiti sono riconoscibili dai terzi, il prestatore non risponde dei danni derivanti da un uso del servizio che ecceda tali limiti.",
         3, 1, "media", None, "il limite di responsabilità opera solo se i limiti d'uso sono comunicati preventivamente e riconoscibili dai terzi", "bozza", None, None),

        # --- Art. 15 - Accessibilita' -------------------------------------
        (4, 1, "art. 15 (testo originario 2014)",
         "Ove possibile, i servizi fiduciari erogati e i prodotti per l'utente finale impiegati nell'erogazione di tali servizi sono resi accessibili alle persone con disabilità.",
         1, 2, "bassa", None, "obbligo di mezzi ('ove possibile'), non di risultato", "bozza", None, None),
        (5, 2, "art. 15 (testo vigente, eIDAS2)",
         "I mezzi di identificazione elettronica, i servizi fiduciari e i prodotti per l'utente finale impiegati nell'erogazione di tali servizi sono resi disponibili in linguaggio chiaro e comprensibile, in conformità alla Convenzione ONU sui diritti delle persone con disabilità e ai requisiti di accessibilità della direttiva (UE) 2019/882 (European Accessibility Act), a beneficio anche di chi ha limitazioni funzionali (es. anziani) o accesso limitato alle tecnologie digitali.",
         1, 1, "media", None, "rafforzato rispetto al testo 2014: da obbligo di mezzi a rinvio a uno standard di accessibilità vincolante (dir. 2019/882)", "bozza", None, None),

        # --- Art. 19 (abrogato, confluito in art. 24§2) ---------------------
        (6, 1, "art. 19 §1 (abrogato, testo originario 2014)",
         "Il prestatore di servizi fiduciari, qualificato o non qualificato, adotta misure tecniche e organizzative adeguate a gestire i rischi per la sicurezza dei servizi fiduciari erogati, commisurate al livello di rischio secondo lo stato dell'arte tecnologico, in particolare per prevenire e minimizzare l'impatto di incidenti di sicurezza.",
         2, 2, "alta", None, None, "bozza", None, None),
        (7, 1, "art. 19 §2 (abrogato, testo originario 2014)",
         "Il prestatore di servizi fiduciari, qualificato o non qualificato, notifica senza ritardo ingiustificato e comunque entro 24 ore dalla conoscenza del fatto all'organismo di vigilanza (e, se rilevante, all'autorità di protezione dei dati) qualunque violazione della sicurezza o perdita di integrità con impatto significativo sul servizio fornito o sui dati personali ivi conservati; se la violazione può pregiudicare una persona fisica o giuridica destinataria del servizio, ne dà notizia senza ritardo ingiustificato anche a quest'ultima.",
         4, 2, "alta", "sanzione amministrativa (rif. autorità di vigilanza nazionale)", "solo se la violazione ha un impatto significativo sul servizio o sui dati", "bozza", None, None),

        # --- Art. 23§2 - marchio di fiducia UE ------------------------------
        (8, 1, "art. 23 §2",
         "Quando utilizza il marchio di fiducia UE per i servizi fiduciari qualificati che eroga, il prestatore qualificato garantisce che sul proprio sito web sia reso disponibile un link alla lista di fiducia (trusted list) pertinente.",
         3, 1, "bassa", None, "si applica solo ai prestatori che scelgono di usare il marchio di fiducia UE", "bozza", None, None),

        # --- Art. 20§1 - Audit --------------------------------------------
        (9, 1, "art. 20 §1 (abrogato, testo originario 2014)",
         "Il prestatore qualificato di servizi fiduciari è sottoposto, a proprie spese, ad audit almeno ogni 24 mesi da parte di un organismo di valutazione della conformità, allo scopo di confermare che esso e i servizi qualificati erogati soddisfano i requisiti del regolamento; il prestatore trasmette all'organismo di vigilanza la relazione di valutazione della conformità entro 3 giorni lavorativi dal ricevimento.",
         4, 2, "media", "sospensione/revoca della qualifica in caso di esito negativo non sanato", None, "bozza", None, None),
        (10, 2, "art. 20 §1 (vigente, eIDAS2)",
         "Il prestatore qualificato di servizi fiduciari è sottoposto, a proprie spese, ad audit almeno ogni 24 mesi da parte di un organismo di valutazione della conformità, per confermare la conformità propria e dei servizi qualificati erogati al regolamento e all'art. 21 della direttiva NIS2 (UE) 2022/2555; trasmette la relazione di valutazione della conformità all'organismo di vigilanza entro 3 giorni lavorativi dal ricevimento.",
         4, 1, "media", "sospensione/revoca della qualifica in caso di esito negativo non sanato", None, "bozza", None, None),
        (11, 2, "art. 20 §1-bis (nuovo, eIDAS2)",
         "Il prestatore qualificato di servizi fiduciari informa l'organismo di vigilanza almeno un mese prima di ogni audit programmato e consente all'organismo di vigilanza di parteciparvi come osservatore su richiesta.",
         4, 1, "bassa", None, None, "bozza", None, None),

        # --- Art. 21§1 - Avvio di un servizio fiduciario qualificato ---------
        (12, 1, "art. 21 §1 (abrogato, testo originario 2014)",
         "Il prestatore di servizi fiduciari non ancora qualificato che intende iniziare a erogare un servizio fiduciario qualificato presenta all'organismo di vigilanza una notifica della propria intenzione, corredata da una relazione di valutazione della conformità rilasciata da un organismo di valutazione della conformità.",
         4, 2, "media", None, None, "bozza", None, None),
        (13, 2, "art. 21 §1 (vigente, eIDAS2)",
         "Il prestatore di servizi fiduciari che intende iniziare a erogare un servizio fiduciario qualificato notifica all'organismo di vigilanza la propria intenzione, corredata da una relazione di valutazione della conformità rilasciata da un organismo di valutazione della conformità che attesti il rispetto del regolamento e dell'art. 21 della direttiva NIS2.",
         4, 1, "media", None, None, "bozza", None, None),

        # --- Art. 24 - Requisiti dei prestatori qualificati -------------------
        (14, 1, "art. 24 §1 (abrogato, testo originario 2014)",
         "Quando rilascia un certificato qualificato, il prestatore qualificato verifica, con mezzi adeguati e conformemente al diritto nazionale, l'identità e, se applicabile, gli attributi specifici della persona fisica o giuridica cui il certificato è rilasciato, direttamente o tramite terza parte delegata, mediante presenza fisica, identificazione elettronica di livello sostanziale/elevato, certificato di firma/sigillo qualificato equivalente, o altro metodo nazionale di assicurazione equivalente confermato da un organismo di valutazione della conformità.",
         4, 2, "alta", None, None, "bozza", None, None),
        (15, 2, "art. 24 §1 (vigente, eIDAS2)",
         "Quando rilascia un certificato qualificato o un'attestazione elettronica qualificata di attributi (QEAA), il prestatore qualificato verifica l'identità e, se applicabile, gli attributi specifici della persona fisica o giuridica cui il certificato o l'attestazione sono rilasciati, secondo i metodi di cui ai §1-bis e 1-ter.",
         4, 1, "alta", None, None, "bozza", None, None),
        (16, 2, "art. 24 §1-bis (nuovo, eIDAS2 — metodi di verifica dell'identità)",
         "Il prestatore qualificato verifica l'identità, direttamente o tramite terza parte, mediante: il Wallet europeo di identità digitale o un mezzo di identificazione elettronica notificato di livello 'elevato'; un certificato di firma o sigillo elettronico qualificato; altri metodi di identificazione con livello di affidabilità elevato confermati da un organismo di valutazione della conformità; oppure la presenza fisica della persona secondo il diritto nazionale.",
         4, 1, "alta", None, None, "bozza", None, None),
        (17, 2, "art. 24 §1-ter (nuovo, eIDAS2 — metodi di verifica degli attributi)",
         "Il prestatore qualificato verifica gli attributi specifici, direttamente o tramite terza parte, mediante: il Wallet europeo di identità digitale o un mezzo di identificazione elettronica notificato di livello 'elevato'; un certificato di firma o sigillo qualificato; un'attestazione elettronica qualificata di attributi; altri metodi con livello di affidabilità elevato confermati da un organismo di valutazione della conformità; oppure la presenza fisica della persona.",
         4, 1, "alta", None, "si applica solo quando il certificato/l'attestazione include attributi specifici oltre all'identità", "bozza", None, None),

        (18, 1, "art. 24 §2(a) (abrogato, testo originario 2014)",
         "Il prestatore qualificato che eroga servizi fiduciari qualificati informa l'organismo di vigilanza di ogni cambiamento nell'erogazione dei propri servizi fiduciari qualificati e dell'intenzione di cessare tali attività.",
         3, 2, "media", None, None, "bozza", None, None),
        (19, 2, "art. 24 §2(a) (vigente, eIDAS2)",
         "Il prestatore qualificato informa l'organismo di vigilanza almeno un mese prima di attuare qualsiasi cambiamento nell'erogazione dei propri servizi fiduciari qualificati, o almeno tre mesi prima in caso di intenzione di cessare tali attività; l'organismo di vigilanza può chiedere informazioni aggiuntive o l'esito di una valutazione di conformità e condizionare l'autorizzazione al cambiamento.",
         3, 1, "media", None, None, "bozza", None, None),

        (20, 1, "art. 24 §2(d) (abrogato, testo originario 2014)",
         "Prima di stipulare un rapporto contrattuale, il prestatore qualificato informa in modo chiaro e completo chiunque intenda utilizzare un servizio fiduciario qualificato sulle condizioni precise d'uso del servizio, incluse eventuali limitazioni.",
         3, 2, "media", None, None, "bozza", None, None),
        (21, 2, "art. 24 §2(d) (vigente, eIDAS2)",
         "Prima di stipulare un rapporto contrattuale, il prestatore qualificato informa in modo chiaro, completo e facilmente accessibile — sia in uno spazio pubblicamente accessibile sia individualmente — chiunque intenda utilizzare un servizio fiduciario qualificato sulle condizioni precise d'uso del servizio, incluse eventuali limitazioni.",
         3, 1, "media", None, None, "bozza", None, None),

        (22, 1, "art. 24 §2(e) (abrogato, testo originario 2014)",
         "Il prestatore qualificato utilizza sistemi e prodotti affidabili, protetti da modifiche, che garantiscano la sicurezza tecnica e l'affidabilità dei processi da essi supportati.",
         2, 2, "alta", None, None, "bozza", None, None),
        (23, 2, "art. 24 §2(e) (vigente, eIDAS2)",
         "Il prestatore qualificato utilizza sistemi e prodotti affidabili, protetti da modifiche, che garantiscano la sicurezza tecnica e l'affidabilità dei processi da essi supportati, incluso il ricorso a tecniche crittografiche adeguate.",
         2, 1, "alta", None, None, "bozza", None, None),

        (24, 2, "art. 24 §2(fa) (nuovo, eIDAS2 — successore dell'art. 19§1)",
         "Il prestatore qualificato adotta politiche adeguate e misure corrispondenti per gestire i rischi legali, commerciali, operativi e altri rischi diretti o indiretti per l'erogazione del servizio fiduciario qualificato, includendo almeno misure su: procedure di registrazione e onboarding del servizio; controlli procedurali o amministrativi necessari; gestione e implementazione dei servizi. Ciò fermo restando l'art. 21 della direttiva NIS2.",
         2, 1, "alta", None, None, "bozza", None, None),
        (25, 2, "art. 24 §2(fb) (nuovo, eIDAS2 — successore dell'art. 19§2)",
         "Il prestatore qualificato notifica all'organismo di vigilanza, alle persone fisiche identificabili colpite, ad altri organismi competenti pertinenti e, su richiesta dell'organismo di vigilanza, al pubblico se di interesse pubblico, qualunque violazione di sicurezza o interruzione del servizio (o delle misure di cui al punto fa) con impatto significativo sul servizio fiduciario erogato o sui dati personali ivi conservati, senza ritardo ingiustificato e in ogni caso entro 24 ore dall'incidente.",
         4, 1, "alta", "sanzione amministrativa (rif. autorità di vigilanza nazionale)", "solo se la violazione ha un impatto significativo sul servizio o sui dati", "bozza", None, None),

        (26, 1, "art. 24 §2(g) (abrogato, testo originario 2014)",
         "Il prestatore qualificato adotta misure adeguate contro la contraffazione e il furto dei dati.",
         2, 2, "media", None, None, "bozza", None, None),
        (27, 2, "art. 24 §2(g) (vigente, eIDAS2)",
         "Il prestatore qualificato adotta misure adeguate contro la contraffazione, il furto o l'appropriazione indebita dei dati, o contro la loro cancellazione, alterazione o inaccessibilità non autorizzata.",
         2, 1, "media", None, None, "bozza", None, None),

        (28, 1, "art. 24 §2(h) (abrogato, testo originario 2014)",
         "Il prestatore qualificato registra e mantiene accessibili, per un periodo di tempo adeguato anche dopo la cessazione dell'attività, tutte le informazioni pertinenti sui dati emessi e ricevuti, in particolare a fini probatori in giudizio e di continuità del servizio; la registrazione può avvenire elettronicamente.",
         5, 2, "media", None, None, "bozza", None, None),
        (29, 2, "art. 24 §2(h) (vigente, eIDAS2)",
         "Il prestatore qualificato registra e mantiene accessibili, per tutto il tempo necessario anche dopo la cessazione dell'attività, tutte le informazioni pertinenti sui dati emessi e ricevuti, in particolare a fini probatori in giudizio e di continuità del servizio; la registrazione può avvenire elettronicamente.",
         5, 1, "media", None, None, "bozza", None, None),

        (30, 1, "art. 24 §2(i) (abrogato, testo originario 2014)",
         "Il prestatore qualificato dispone di un piano di cessazione aggiornato che garantisca la continuità del servizio, secondo le modalità verificate dall'organismo di vigilanza ai sensi dell'art. 17§4(i).",
         1, 2, "media", None, None, "bozza", None, None),
        (31, 2, "art. 24 §2(i) (vigente, eIDAS2)",
         "Il prestatore qualificato dispone di un piano di cessazione aggiornato che garantisca la continuità del servizio, secondo le modalità verificate dall'organismo di vigilanza ai sensi del nuovo art. 46-ter §4(i) (che sostituisce il precedente art. 17§4(i)).",
         1, 1, "media", None, None, "bozza", None, None),

        (32, 1, "art. 24 §2(j) (abrogato senza successore, testo originario 2014)",
         "Il prestatore qualificato garantisce il trattamento lecito dei dati personali ai sensi della direttiva 95/46/CE.",
         1, 2, "media", None, "punto soppresso da eIDAS2 senza sostituzione diretta in art. 24: l'obbligo di trattamento lecito dei dati personali resta comunque applicabile per effetto diretto del GDPR (Reg. (UE) 2016/679), che ha abrogato la direttiva 95/46/CE indipendentemente da eIDAS — non tracciato come Fonte in questo censimento pilota", "bozza", None, None),

        (33, 2, "art. 24 §4-bis (nuovo, eIDAS2)",
         "Le regole sulla revoca dei certificati qualificati (registrazione nel database dei certificati, pubblicazione tempestiva ed entro 24 ore, effetto immediato dalla pubblicazione) si applicano allo stesso modo alla revoca delle attestazioni elettroniche qualificate di attributi (QEAA).",
         4, 1, "media", None, None, "bozza", None, None),

        # --- Firme elettroniche qualificate: dispositivi, servizi di validazione/conservazione ---
        (34, 1, "art. 28 §1",
         "Il prestatore qualificato che rilascia certificati qualificati per firme elettroniche garantisce che tali certificati soddisfino i requisiti dell'allegato I del regolamento.",
         2, 1, "alta", None, None, "bozza", None, None),
        (35, 1, "art. 29 §1",
         "Il prestatore qualificato garantisce che i dispositivi per la creazione di firme elettroniche qualificate che utilizza o rende disponibili soddisfino i requisiti dell'allegato II del regolamento.",
         2, 1, "alta", None, None, "bozza", None, None),
        (36, 2, "art. 29 §1-bis (nuovo, eIDAS2)",
         "La generazione o gestione dei dati di creazione della firma elettronica da remoto, o la loro duplicazione a fini di backup, sono effettuate solo per conto del firmatario, su sua richiesta, e da un prestatore qualificato che eroga il servizio qualificato di gestione di un dispositivo remoto di creazione di firma elettronica qualificata.",
         2, 1, "alta", None, None, "bozza", None, None),
        (37, 2, "art. 29-bis (nuovo, eIDAS2 — servizio qualificato di gestione remota di QSCD)",
         "Il prestatore qualificato che eroga il servizio di gestione remota di dispositivi di creazione di firma qualificata: genera o gestisce i dati di creazione della firma per conto del firmatario; può duplicarli solo a fini di backup, garantendo per i dataset duplicati lo stesso livello di sicurezza degli originali e limitandone il numero al minimo necessario per la continuità del servizio; rispetta i requisiti identificati nel rapporto di certificazione del dispositivo remoto specifico rilasciato ai sensi dell'art. 30.",
         2, 1, "alta", None, None, "bozza", None, None),
        (38, 1, "art. 32 §1-§2",
         "Il prestatore qualificato che eroga un servizio di validazione di firme elettroniche qualificate garantisce che il processo di validazione confermi la validità della firma solo se sono soddisfatte le condizioni previste (certificato qualificato valido al momento della firma, dati di validazione corrispondenti, integrità dei dati firmati non compromessa, dispositivo di creazione qualificato, requisiti dell'art. 26 rispettati, ecc.), e che il sistema fornisca al soggetto affidante il risultato corretto della validazione permettendogli di rilevare eventuali problemi di sicurezza.",
         2, 1, "alta", None, None, "bozza", None, None),
        (39, 2, "art. 32-bis (nuovo, eIDAS2)",
         "Il prestatore che eroga un servizio di validazione di firme elettroniche avanzate basate su certificato qualificato garantisce che il processo di validazione confermi la validità della firma solo se sono soddisfatte condizioni equivalenti a quelle previste per le firme qualificate (validità del certificato al momento della firma, corrispondenza dei dati di validazione, integrità dei dati, rispetto dei requisiti dell'art. 26), fornendo al soggetto affidante il risultato corretto della validazione.",
         2, 1, "media", None, "si applica alle firme avanzate basate su certificato qualificato, categoria di servizio non regolata prima di eIDAS2", "bozza", None, None),
        (40, 1, "art. 33 §1",
         "Il servizio di validazione qualificato per firme elettroniche qualificate può essere erogato solo da un prestatore qualificato che validi ai sensi dell'art. 32§1 e che consenta ai soggetti affidanti di ricevere il risultato della validazione in modo automatico, affidabile ed efficiente, munito della firma o sigillo elettronico avanzato del prestatore del servizio di validazione.",
         2, 1, "media", None, None, "bozza", None, None),
        (41, 1, "art. 34 §1",
         "Il servizio di conservazione qualificato per firme elettroniche qualificate può essere erogato solo da un prestatore qualificato che utilizzi procedure e tecnologie in grado di estendere l'affidabilità della firma elettronica qualificata oltre il periodo di validità tecnologica.",
         5, 1, "alta", None, None, "bozza", None, None),
        (42, 1, "art. 38 §1",
         "Il prestatore qualificato che rilascia certificati qualificati per sigilli elettronici garantisce che tali certificati soddisfino i requisiti dell'allegato III del regolamento.",
         2, 1, "alta", None, None, "bozza", None, None),
        (43, 1, "art. 42 §1",
         "Il prestatore qualificato che eroga marche temporali elettroniche qualificate garantisce che la marca vincoli data e ora ai dati in modo da precludere ragionevolmente modifiche non rilevabili, si basi su una fonte di tempo accurata collegata al Tempo Universale Coordinato, e sia firmata o sigillata elettronicamente in modo avanzato dal prestatore (o con metodo equivalente).",
         2, 1, "alta", None, None, "bozza", None, None),
        (44, 1, "art. 44 §1",
         "Il servizio di recapito elettronico certificato qualificato è erogato da uno o più prestatori qualificati che garantiscono con un livello di sicurezza elevato l'identificazione del mittente e, prima della consegna, del destinatario; assicurano che invio e ricezione siano protetti da firma o sigillo elettronico avanzato del prestatore in modo da precludere modifiche non rilevabili; indicano chiaramente al mittente e al destinatario ogni modifica dei dati necessaria per l'invio/ricezione; e indicano data e ora di invio, ricezione ed eventuale modifica tramite marca temporale elettronica qualificata.",
         2, 1, "alta", None, None, "bozza", None, None),

        # --- Art. 45 - Autenticazione di siti web (QWAC) ----------------------
        (45, 1, "art. 45 §1 (abrogato, testo originario 2014)",
         "Il prestatore qualificato che rilascia certificati qualificati per l'autenticazione di siti web garantisce che tali certificati soddisfino i requisiti dell'allegato IV del regolamento.",
         2, 2, "media", None, None, "bozza", None, None),
        (46, 2, "art. 45 §1 (vigente, eIDAS2)",
         "Il prestatore qualificato che rilascia certificati qualificati per l'autenticazione di siti web (QWAC) garantisce che tali certificati soddisfino i requisiti dell'allegato IV; la valutazione di conformità a tali requisiti è condotta secondo gli standard, le specifiche e le procedure individuati dalla Commissione.",
         2, 1, "media", None, None, "bozza", None, None),
        (47, 2, "art. 45 §1-bis (nuovo, eIDAS2 — obbligo dei fornitori di browser)",
         "Il fornitore di browser web riconosce i certificati qualificati per l'autenticazione di siti web (QWAC) rilasciati ai sensi dell'art. 45§1, garantendo che i dati identificativi attestati nel certificato e gli eventuali attributi aggiuntivi siano visualizzati in modo facilmente comprensibile per l'utente, e assicura il supporto e l'interoperabilità con tali certificati (esenzione per le micro e piccole imprese durante i primi 5 anni di attività come fornitori di servizi di navigazione).",
         2, 1, "alta", None, "esenzione temporanea (5 anni) per micro/piccole imprese fornitrici di browser", "bozza", None, None),
        (48, 2, "art. 45-bis (nuovo, eIDAS2 — misure cautelari di cybersicurezza)",
         "Il fornitore di browser web non adotta misure contrarie all'obbligo di riconoscere i QWAC e di visualizzarne i dati identificativi in modo comprensibile (art. 45-bis §1); in deroga, solo in presenza di fondati timori relativi a violazioni di sicurezza o perdita di integrità di uno specifico certificato o insieme di certificati, può adottare misure cautelari verso quel certificato, notificandone senza ritardo per iscritto le motivazioni e le misure adottate alla Commissione, all'organismo di vigilanza competente, al soggetto titolare del certificato e al prestatore qualificato che lo ha rilasciato; se l'indagine dell'organismo di vigilanza non porta alla revoca della qualifica del certificato, il fornitore di browser deve porre fine alle misure cautelari su richiesta dell'organismo.",
         2, 1, "alta", None, "si applica solo in presenza di fondati timori di violazione di sicurezza; le misure cautelari sono provvisorie e revocabili su richiesta dell'organismo di vigilanza", "bozza", None, None),

        # --- Sezione 9 (nuova) - Attestazione elettronica qualificata di attributi (QEAA) ---
        (49, 2, "art. 45-quater §1, §3, §4 (nuovo, eIDAS2)",
         "Il prestatore qualificato che rilascia attestazioni elettroniche qualificate di attributi (QEAA) garantisce che soddisfino i requisiti dell'allegato V, senza sottoporle a requisiti obbligatori ulteriori; se un'attestazione qualificata è revocata dopo l'emissione iniziale, perde validità dal momento della revoca e il suo stato non può in alcun caso essere ripristinato.",
         2, 1, "alta", None, "categoria di servizio non regolata prima di eIDAS2", "bozza", None, None),
        (50, 2, "art. 45-septies §2 (nuovo, eIDAS2)",
         "Il prestatore di attestazioni elettroniche qualificate di attributi (QEAA) fornisce un'interfaccia con i Wallet europei di identità digitale erogati ai sensi dell'art. 5-bis.",
         2, 1, "media", None, "categoria di servizio non regolata prima di eIDAS2", "bozza", None, None),
        (51, 2, "art. 45-octies (nuovo, eIDAS2)",
         "Il prestatore di servizi di attestazione elettronica di attributi, qualificati o non qualificati, non combina i dati personali relativi all'erogazione di tali servizi con dati personali provenienti da altri servizi propri o di partner commerciali; mantiene tali dati logicamente separati dagli altri dati detenuti; e implementa il servizio qualificato in modo funzionalmente separato dagli altri servizi che eroga.",
         1, 1, "alta", None, "categoria di servizio non regolata prima di eIDAS2", "bozza", None, None),

        # --- Sezione 10 (nuova) - Servizio di conservazione elettronica qualificato ---
        (52, 2, "art. 45-undecies §1 (nuovo, eIDAS2)",
         "Il servizio di archiviazione elettronica qualificato è erogato da un prestatore qualificato che utilizza procedure e tecnologie in grado di garantire la durabilità e la leggibilità dei dati/documenti elettronici oltre il periodo di validità tecnologica e per l'intero periodo di conservazione legale o contrattuale, mantenendone integrità e origine; ne garantisce la salvaguardia da perdita e alterazione (salvo cambi di supporto/formato); e consente ai soggetti affidanti autorizzati di ricevere, in modo automatico, un rapporto — munito di firma o sigillo elettronico qualificato del prestatore — che confermi la presunzione di integrità dei dati dall'inizio della conservazione al momento del recupero.",
         5, 1, "alta", None, "categoria di servizio non regolata prima di eIDAS2", "bozza", None, None),

        # --- Sezione 11 (nuova) - Registro elettronico qualificato (ledger) ---
        (53, 2, "art. 45-terdecies §1 (nuovo, eIDAS2)",
         "Il registro elettronico qualificato è creato e gestito da uno o più prestatori qualificati che ne stabiliscono l'origine dei dati registrati, ne garantiscono l'ordinamento cronologico sequenziale univoco e accurato, e registrano i dati in modo tale che ogni successiva modifica sia immediatamente rilevabile, assicurandone l'integrità nel tempo.",
         2, 1, "alta", None, "categoria di servizio non regolata prima di eIDAS2", "bozza", None, None),
    ]
    many("obblighi", ["id", "fonte_id", "riferimento", "testo", "tipo_obbligo_id", "stato_id",
                       "severita", "sanzioni", "condizione_applicabilita",
                       "stato_validazione", "validato_da", "data_validazione"], obblighi)

    # --- soggetti (ruolo: obbligato / destinatario) ------------------------
    # Categorie: 1 QTSP/gestore, 2 Utente/titolare, 3 Terza parte, 4 Terzi affidanti/pubblico
    obbligo_soggetti = [
        (1, 1, "obbligato"), (1, 2, "destinatario"), (1, 4, "destinatario"),
        (2, 1, "obbligato"), (2, 2, "destinatario"), (2, 4, "destinatario"),
        (3, 1, "obbligato"), (3, 2, "destinatario"), (3, 4, "destinatario"),
        (4, 1, "obbligato"), (4, 2, "destinatario"),
        (5, 1, "obbligato"), (5, 2, "destinatario"),
        (6, 1, "obbligato"),
        (7, 1, "obbligato"), (7, 2, "destinatario"), (7, 4, "destinatario"),
        (8, 1, "obbligato"), (8, 4, "destinatario"),
        (9, 1, "obbligato"),
        (10, 1, "obbligato"),
        (11, 1, "obbligato"),
        (12, 1, "obbligato"),
        (13, 1, "obbligato"),
        (14, 1, "obbligato"), (14, 2, "destinatario"),
        (15, 1, "obbligato"), (15, 2, "destinatario"),
        (16, 1, "obbligato"), (16, 2, "destinatario"),
        (17, 1, "obbligato"), (17, 2, "destinatario"),
        (18, 1, "obbligato"),
        (19, 1, "obbligato"),
        (20, 1, "obbligato"), (20, 2, "destinatario"),
        (21, 1, "obbligato"), (21, 2, "destinatario"),
        (22, 1, "obbligato"),
        (23, 1, "obbligato"),
        (24, 1, "obbligato"),
        (25, 1, "obbligato"), (25, 2, "destinatario"), (25, 4, "destinatario"),
        (26, 1, "obbligato"),
        (27, 1, "obbligato"),
        (28, 1, "obbligato"),
        (29, 1, "obbligato"),
        (30, 1, "obbligato"), (30, 2, "destinatario"),
        (31, 1, "obbligato"), (31, 2, "destinatario"),
        (32, 1, "obbligato"), (32, 2, "destinatario"),
        (33, 1, "obbligato"),
        (34, 1, "obbligato"), (34, 2, "destinatario"),
        (35, 1, "obbligato"), (35, 2, "destinatario"),
        (36, 1, "obbligato"), (36, 2, "destinatario"),
        (37, 1, "obbligato"), (37, 2, "destinatario"),
        (38, 1, "obbligato"), (38, 4, "destinatario"),
        (39, 1, "obbligato"), (39, 4, "destinatario"),
        (40, 1, "obbligato"), (40, 4, "destinatario"),
        (41, 1, "obbligato"), (41, 2, "destinatario"),
        (42, 1, "obbligato"), (42, 2, "destinatario"),
        (43, 1, "obbligato"), (43, 4, "destinatario"),
        (44, 1, "obbligato"), (44, 2, "destinatario"),
        (45, 1, "obbligato"), (45, 4, "destinatario"),
        (46, 1, "obbligato"), (46, 4, "destinatario"),
        (47, 3, "obbligato"), (47, 4, "destinatario"), (47, 1, "destinatario"),
        (48, 3, "obbligato"), (48, 1, "destinatario"),
        (49, 1, "obbligato"), (49, 2, "destinatario"),
        (50, 1, "obbligato"), (50, 2, "destinatario"),
        (51, 1, "obbligato"), (51, 2, "destinatario"),
        (52, 1, "obbligato"), (52, 2, "destinatario"), (52, 4, "destinatario"),
        (53, 1, "obbligato"), (53, 4, "destinatario"),
    ]
    many("obbligo_soggetti", ["obbligo_id", "categoria_soggetto_id", "ruolo"], obbligo_soggetti)

    # --- principi (ticket 08 / ADR-0004) -------------------------------
    # Norme dichiarative che non impongono un comportamento a un soggetto:
    # effetto giuridico, non discriminazione, presunzione. Esempio guida:
    # art. 25 e art. 46 eIDAS rispondono al quesito "può un giudice non
    # considerare un documento firmato con firma elettronica?".
    # id, fonte_id, riferimento, testo, tipo_principio, stato, condizione, stato_validazione, validato_da, data_validazione
    principi = [
        (1, 1, "art. 25 §1",
         "A una firma elettronica non sono negati gli effetti giuridici né l'ammissibilità come prova in giudizio per il solo motivo della sua forma elettronica o del fatto che non soddisfi i requisiti della firma elettronica qualificata.",
         1, 1, None, "bozza", None, None),
        (2, 1, "art. 25 §2",
         "Una firma elettronica qualificata ha effetto giuridico equivalente a quello di una firma autografa.",
         2, 1, None, "bozza", None, None),
        (3, 1, "art. 25 §3",
         "Una firma elettronica qualificata basata su un certificato qualificato rilasciato in uno Stato membro è riconosciuta come firma elettronica qualificata in tutti gli altri Stati membri.",
         2, 1, None, "bozza", None, None),
        (4, 1, "art. 35 §1",
         "A un sigillo elettronico non sono negati gli effetti giuridici né l'ammissibilità come prova in giudizio per il solo motivo della sua forma elettronica o del fatto che non soddisfi i requisiti del sigillo elettronico qualificato.",
         1, 1, None, "bozza", None, None),
        (5, 1, "art. 35 §2",
         "Un sigillo elettronico qualificato gode della presunzione di integrità dei dati e di correttezza dell'origine dei dati cui è associato.",
         4, 1, None, "bozza", None, None),
        (6, 1, "art. 41 §1",
         "A una marca temporale elettronica non sono negati gli effetti giuridici né l'ammissibilità come prova in giudizio per il solo motivo della sua forma elettronica o del fatto che non soddisfi i requisiti della marca temporale elettronica qualificata.",
         1, 1, None, "bozza", None, None),
        (7, 1, "art. 41 §2",
         "Una marca temporale elettronica qualificata gode della presunzione di accuratezza della data e dell'ora che indica e di integrità dei dati a cui la data e l'ora sono associate.",
         4, 1, None, "bozza", None, None),
        (8, 1, "art. 43 §1",
         "Ai dati inviati e ricevuti tramite un servizio di recapito elettronico certificato non sono negati gli effetti giuridici né l'ammissibilità come prova in giudizio per il solo motivo della loro forma elettronica o del fatto che il servizio non soddisfi i requisiti del servizio qualificato.",
         1, 1, None, "bozza", None, None),
        (9, 1, "art. 43 §2",
         "I dati inviati e ricevuti mediante un servizio di recapito elettronico certificato qualificato godono della presunzione di integrità dei dati, di invio di tali dati da parte del mittente identificato, di ricezione da parte del destinatario identificato, e di accuratezza della data e dell'ora di invio e ricezione indicate dal servizio qualificato.",
         4, 1, None, "bozza", None, None),
        (10, 1, "art. 46",
         "A un documento elettronico non sono negati gli effetti giuridici e l'ammissibilità come prova in giudizio per il solo motivo della sua forma elettronica.",
         1, 1, None, "bozza", None, None),
    ]
    many("principi", ["id", "fonte_id", "riferimento", "testo", "tipo_principio_id", "stato_id",
                       "condizione_applicabilita", "stato_validazione", "validato_da", "data_validazione"], principi)

    # oggetto giuridico a cui si applica ciascun principio
    principio_oggetti = [
        (1, 1),          # art.25§1 -> firma elettronica
        (2, 3),          # art.25§2 -> firma elettronica qualificata
        (3, 3),          # art.25§3 -> firma elettronica qualificata
        (4, 4),          # art.35§1 -> sigillo elettronico
        (5, 6),          # art.35§2 -> sigillo elettronico qualificato
        (6, 7),          # art.41§1 -> marca temporale elettronica qualificata (unica categoria tracciata per marche)
        (7, 7),          # art.41§2 -> marca temporale elettronica qualificata
        (8, 9),          # art.43§1 -> servizio di recapito elettronico certificato
        (9, 9),          # art.43§2 -> servizio di recapito elettronico certificato
        (10, 8),         # art.46 -> documento elettronico
    ]
    many("principio_oggetti", ["principio_id", "oggetto_giuridico_id"], principio_oggetti)

    # --- relazioni tipizzate ------------------------------------------------
    # Tipo 1 = "sostituisce" (da: nuovo -> a: vecchio); tipo 2 = "specifica"
    # nodo_da_tipo/nodo_a_tipo: 'obbligo' o 'principio' (ticket 08 / ADR-0004)
    relazioni = [
        (1, "obbligo", 2, "obbligo", 1, 1),      # art.13§1 vigente sostituisce art.13§1 originario
        (2, "obbligo", 5, "obbligo", 4, 1),      # art.15 vigente sostituisce art.15 originario
        (3, "obbligo", 10, "obbligo", 9, 1),     # art.20§1 vigente sostituisce art.20§1 originario
        (4, "obbligo", 11, "obbligo", 10, 2),    # art.20§1-bis specifica l'audit dell'art.20§1 vigente
        (5, "obbligo", 13, "obbligo", 12, 1),    # art.21§1 vigente sostituisce art.21§1 originario
        (6, "obbligo", 15, "obbligo", 14, 1),    # art.24§1 vigente sostituisce art.24§1 originario
        (7, "obbligo", 16, "obbligo", 14, 1),    # art.24§1-bis (metodi) sostituisce anch'esso art.24§1 originario
        (8, "obbligo", 19, "obbligo", 18, 1),    # art.24§2(a) vigente sostituisce art.24§2(a) originario
        (9, "obbligo", 21, "obbligo", 20, 1),    # art.24§2(d) vigente sostituisce art.24§2(d) originario
        (10, "obbligo", 23, "obbligo", 22, 1),   # art.24§2(e) vigente sostituisce art.24§2(e) originario
        (11, "obbligo", 24, "obbligo", 6, 1),    # art.24§2(fa) sostituisce art.19§1 (misure di sicurezza)
        (12, "obbligo", 25, "obbligo", 7, 1),    # art.24§2(fb) sostituisce art.19§2 (notifica violazioni)
        (13, "obbligo", 27, "obbligo", 26, 1),   # art.24§2(g) vigente sostituisce art.24§2(g) originario
        (14, "obbligo", 29, "obbligo", 28, 1),   # art.24§2(h) vigente sostituisce art.24§2(h) originario
        (15, "obbligo", 31, "obbligo", 30, 1),   # art.24§2(i) vigente sostituisce art.24§2(i) originario
        (16, "obbligo", 46, "obbligo", 45, 1),   # art.45§1 vigente sostituisce art.45§1 originario
        (17, "obbligo", 37, "obbligo", 36, 2),   # art.29-bis specifica l'art.29§1-bis (generazione/duplicazione dati di firma da remoto)
        (18, "obbligo", 38, "principio", 2, 2),  # art.32 (validazione firme qualificate) specifica il principio di equivalenza giuridica (art.25§2)
        (19, "obbligo", 41, "principio", 3, 2),  # art.34 (conservazione qualificata) specifica il principio di equivalenza giuridica (art.25§3, riconoscimento transfrontaliero)
        (20, "principio", 2, "principio", 1, 2), # art.25§2 (equivalenza) specifica il principio generale di non discriminazione (art.25§1)
    ]
    many("relazioni", ["id", "nodo_da_tipo", "nodo_da_id", "nodo_a_tipo", "nodo_a_id", "tipo_relazione_id"], relazioni)

    # --- monitoraggio: modifiche rilevate (rilevanti ai fini eIDAS2) --------
    modifiche = [
        (1, 1, "art. 24 §2(j)", "2026-09-09",
         "Il prestatore qualificato garantisce il trattamento lecito dei dati personali ai sensi della direttiva 95/46/CE.",
         "[punto soppresso da eIDAS2 - Reg. (UE) 2024/1183, art. 1(19)(b)(iii)]",
         0),
        (2, 1, "art. 24 §2(i)", "2026-09-09",
         "Il prestatore qualificato dispone di un piano di cessazione aggiornato che garantisca la continuità del servizio, secondo le modalità verificate dall'organismo di vigilanza ai sensi dell'art. 17§4(i).",
         "Il prestatore qualificato dispone di un piano di cessazione aggiornato che garantisca la continuità del servizio, secondo le modalità verificate dall'organismo di vigilanza ai sensi del nuovo art. 46-ter §4(i) [rif. incrociato aggiornato da eIDAS2 - Reg. (UE) 2024/1183, poiché l'art. 17 è stato abrogato].",
         0),
    ]
    many("modifiche_rilevate", ["id", "fonte_id", "riferimento", "data_rilevamento",
                                  "testo_precedente", "testo_nuovo", "esaminata"], modifiche)

    conn.commit()
    conn.close()
    print(f"Creato {DB_PATH} con {len(obblighi)} obblighi e {len(principi)} principi reali (eIDAS + eIDAS2, Cap. III Trust Services).")


if __name__ == "__main__":
    seed()
