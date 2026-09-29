"""Regolamento di esecuzione (UE) 2024/2979 della Commissione, del 28 novembre
2024 - modalita' di applicazione del regolamento (UE) n. 910/2014 per quanto
riguarda l'integrita' e le funzionalita' di base dei portafogli europei di
identita' digitale (articolo 5 bis, paragrafo 23, eIDAS). Fonte
`reg_ue_2024_2979`, capitolo 1 di 5 (vedi
app/.source_cache/reg_ue_2024_2979/manifest.json): Capo I - Disposizioni
generali (articoli 1-2). Gli articoli 3-7 (integrita'), 8-14 (funzionalita' e
caratteristiche di base), 15 (disposizioni finali) e gli allegati I-V sono nei
capitoli 2-5, assegnati ad altri moduli. Testo ufficiale italiano in
app/.source_cache/reg_ue_2024_2979/cap01.txt, acquisito per content
negotiation CELLAR (CELEX 32024R2979, lingua italiana; URL risolto
http://publications.europa.eu/resource/cellar/a7576de1-b1e0-11ef-acb1-01aa75ed71a1.0014.03/DOC_1,
XHTML in Gazzetta ufficiale; provenienza completa e sha256 in provenance.json).

Modellazione (ADR-0007, nessun discrimine di rilevanza):
- Il preambolo (considerando), l'epigrafe "Fatto a Bruxelles", la firma, le
  note a pie' di pagina bibliografiche, la riga ELI, l'atto di adozione ("HA
  ADOTTATO IL PRESENTE REGOLAMENTO") e la formula di chiusura non producono
  nodi, come in tutte le Fonti gia' censite: non sono articoli, commi o
  lettere. Nella porzione assegnata non ne compare nessuno (il preambolo e' a
  monte del Capo I; la formula di chiusura e' nell'art. 15, capitolo 4).
- Art. 1 (oggetto e ambito di applicazione: norme relative all'integrita' e
  alle funzionalita' di base dei portafogli, da aggiornare periodicamente per
  tenere conto degli sviluppi tecnologici, della normazione e del lavoro
  svolto sulla base della raccomandazione (UE) 2021/946) -> un solo
  Principio, tipo "scopo/ambito di applicazione". L'articolo non ha commi ne'
  punti: una sola disposizione di cornice. La subordinata "da aggiornare
  periodicamente" e' una qualita' delle norme stabilite, non un comportamento
  imposto a un soggetto nominato: nessun obbligato identificabile, quindi non
  e' un Obbligo ma un Principio, con la stessa formula dell'art. 1 del Reg.
  2025/1569 e del Reg. 2025/2531 (entrambi censiti come Principio). Non e'
  tipo "altro" come quelli perche' qui l'articolo e' espressamente rubricato
  "Oggetto e ambito di applicazione".
- Art. 2 (definizioni) -> UNA SOLA riga Principio, tipo "definitorio": un
  elenco definitorio non ha autonomia prescrittiva voce per voce (stesso
  criterio dell'art. 3 eIDAS, dell'art. 2 del Reg. 2025/1569 e del punto 1
  dell'allegato del Reg. 2025/2531). Il chapeau ("Ai fini del presente
  regolamento si applicano le definizioni seguenti:") introduce 15 definizioni
  numerate da (1) a (15), che restano integralmente nel `testo_integrale`
  verbatim; le 15 voci sono pero' indicizzate separatamente ("art. 2, punto
  1" ... "art. 2, punto 15") e mappate tutte a questa riga, come da istruzione
  del task. Convenzione di item "art. 2, punto N" (e non "art. 2 par. 1 punto
  N"): il testo ufficiale non numera il chapeau come paragrafo - l'articolo e'
  composto da un chapeau non numerato piu' 15 punti numerati -, ed e' la
  stessa convenzione adottata per l'art. 2 del Reg. 2025/1569 (elenco
  definitorio non numerato a paragrafi).
- Granularita' delle righe: un comma = una riga. In questo capitolo non
  esistono lettere interne con precetto autonomo e distinto (l'art. 2 non
  contiene lettere: le voci sono punti definitori, non precetti), quindi non
  e' stata necessaria alcuna eccezione alla regola "le lettere restano dentro
  il comma".
- `testo_integrale`: verbatim e integrale, ricucito dalle righe spezzate
  dalla conversione XHTML -> testo. Per entrambi gli articoli include
  l'intestazione dell'articolo e il titolo ("Articolo N" + rubrica), che nel
  testo ufficiale precedono immediatamente il corpo: il testo resta cosi'
  contiguo alla fonte (stessa convenzione del Reg. 2025/1569 e del Reg.
  2025/2532). Nell'art. 2 i marcatori di voce "(1)" ... "(15)", che la
  conversione ha isolato su righe separate, sono riuniti al testo della
  rispettiva definizione ("(N) «termine»: definizione;") e le voci sono
  separate da riga vuota; le virgolette caporali «» del testo ufficiale
  italiano sono mantenute. Nessun marcatore di elisione (vincolo
  `verifica_completezza_testo_integrale`, ADR-0010): il testo e' completo.
- `testo` e' la sintesi compressa: per l'art. 1 coincide con l'unica
  proposizione normativa; per l'art. 2 elenca i 15 termini definiti con una
  glossa breve ciascuno, per rendere l'elenco cercabile senza aprire il
  `testo_integrale`.
- Nessun `soggetti` (le due righe sono Principi, che non hanno soggetto
  obbligato) e nessun `oggetti_giuridici` valorizzato: art. 1 e art. 2 sono
  disposizioni di cornice non legate a un singolo strumento giuridico;
  CONTEXT.md ammette che l'attributo resti vuoto per le disposizioni di
  cornice, e i moduli gemelli (Reg. 2025/1569, 2025/2531, 2025/2532) non lo
  valorizzano per le rispettive righe di cornice.
- `stato` = vigente per entrambe le righe (il regolamento e' in vigore).
- RELAZIONI = []: nella porzione assegnata non esiste alcuna citazione
  letterale interna (ne' l'art. 1 ne' l'art. 2 rinviano ad altri articoli di
  questo regolamento; le definizioni dell'art. 2 richiamano istituti definiti
  nell'art. 3 eIDAS e in eIDAS2, cioe' altre Fonti). I collegamenti
  cross-fonte (art. 5 bis §23 eIDAS2, art. 3 eIDAS) li costruisce la sessione
  principale dopo il merge. Una relazione interna art. 1 -> artt. 3-14 di
  questa stessa Fonte sarebbe possibile in linea di principio, ma imporrebbe
  di indovinare il `riferimento` adottato dai moduli paralleli dei capitoli
  2-5 (es. "art. 3" o "art. 3 §1"): un riferimento sbagliato farebbe fallire
  il merge con KeyError e buttare l'intero import, a fronte di un beneficio
  nullo (l'appartenenza del capitolo all'oggetto e' gia' data dalla Fonte).

Copertura: 17 item di indice (art. 1; art. 2; art. 2, punti 1-15), 2 righe
(0 Obblighi + 2 Principi).
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 1",
        "testo": "Il presente regolamento stabilisce le norme relative all'integrità e alle funzionalità di base dei portafogli, da aggiornare periodicamente per tenere conto degli sviluppi tecnologici, della normazione e del lavoro svolto sulla base della raccomandazione (UE) 2021/946 della Commissione, in particolare dell'architettura e del quadro di riferimento.",
        "testo_integrale": "Articolo 1\n\nOggetto e ambito di applicazione\n\nIl presente regolamento stabilisce le norme relative all'integrità e alle funzionalità di base dei portafogli, da aggiornare periodicamente per tenere conto degli sviluppi tecnologici, della normazione e del lavoro svolto sulla base della raccomandazione (UE) 2021/946 della Commissione, in particolare dell'architettura e del quadro di riferimento.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2",
        "testo": "Ai fini del presente regolamento si applicano 15 definizioni: «applicazione crittografica sicura per il portafoglio» (applicazione che gestisce risorse critiche tramite un collegamento alle funzioni crittografiche e non crittografiche fornite dal dispositivo crittografico sicuro per il portafoglio); «unità di portafoglio» (configurazione unica di una soluzione di portafoglio, che comprende istanze di portafoglio, applicazioni crittografiche sicure e dispositivi crittografici sicuri per il portafoglio forniti da un fornitore del portafoglio a un singolo utente del portafoglio); «risorse critiche» (risorse all'interno di un'unità di portafoglio o ad essa relative, la cui compromissione avrebbe un effetto estremamente grave e debilitante sulla possibilità di fare affidamento sull'unità di portafoglio); «fornitore di dati di identificazione personale» (persona fisica o giuridica responsabile del rilascio e della revoca dei dati di identificazione personale, che garantisce l'associazione crittografica di tali dati a un'unità di portafoglio); «utente del portafoglio» (utente che ha il controllo dell'unità di portafoglio); «parte facente affidamento sul portafoglio» (parte facente affidamento che intende fare affidamento sulle unità di portafoglio per la prestazione di servizi pubblici o privati mediante interazione digitale); «fornitore del portafoglio» (persona fisica o giuridica che fornisce soluzioni di portafoglio); «attestato di unità di portafoglio» (oggetto di dati che descrive i componenti dell'unità di portafoglio o ne consente l'autenticazione e la convalida); «politica di divulgazione incorporata» (insieme di norme, incorporato in un attestato elettronico di attributi dal suo fornitore, che indica le condizioni che una parte facente affidamento sul portafoglio deve soddisfare per accedere a tale attestato); «istanza di portafoglio» (applicazione installata e configurata su un dispositivo o su un ambiente di un utente del portafoglio, che fa parte di un'unità di portafoglio e che l'utente utilizza per interagire con essa); «soluzione di portafoglio» (combinazione di software, hardware, servizi, impostazioni e configurazioni, comprese le istanze di portafoglio, una o più applicazioni crittografiche sicure e uno o più dispositivi crittografici sicuri per il portafoglio); «dispositivo crittografico sicuro per il portafoglio» (dispositivo resistente alle manomissioni che fornisce un ambiente collegato all'applicazione crittografica sicura per il portafoglio e da essa utilizzato per proteggere le risorse critiche e fornire funzioni crittografiche per l'esecuzione sicura di operazioni critiche); «operazione crittografica del portafoglio» (meccanismo crittografico necessario nel contesto dell'autenticazione dell'utente del portafoglio e del rilascio o della presentazione di dati di identificazione personale o di attestati elettronici di attributi); «certificato di accesso della parte facente affidamento sul portafoglio» (certificato per sigilli elettronici o firme elettroniche che autenticano e convalidano la parte facente affidamento sul portafoglio, rilasciato da un fornitore di certificati di accesso della parte facente affidamento sul portafoglio); «fornitore di certificati di accesso della parte facente affidamento sul portafoglio» (persona fisica o giuridica incaricata da uno Stato membro di rilasciare certificati di accesso delle parti facenti affidamento alle parti facenti affidamento sul portafoglio registrate in tale Stato membro).",
        "testo_integrale": "Articolo 2\n\nDefinizioni\n\nAi fini del presente regolamento si applicano le definizioni seguenti:\n\n(1) «applicazione crittografica sicura per il portafoglio»: un'applicazione che gestisce risorse critiche tramite un collegamento alle funzioni crittografiche e non crittografiche fornite dal dispositivo crittografico sicuro per il portafoglio e l'uso di tali funzioni;\n\n(2) «unità di portafoglio»: una configurazione unica di una soluzione di portafoglio che comprende istanze di portafoglio, applicazioni crittografiche sicure per il portafoglio e dispositivi crittografici sicuri per il portafoglio forniti da un fornitore del portafoglio a un singolo utente del portafoglio;\n\n(3) «risorse critiche»: risorse all'interno di un'unità di portafoglio o ad essa relative, di importanza tale che un'eventuale compromissione della loro disponibilità, riservatezza o integrità avrebbe un effetto estremamente grave e debilitante sulla possibilità di fare affidamento sull'unità di portafoglio;\n\n(4) «fornitore di dati di identificazione personale»: la persona fisica o giuridica responsabile del rilascio e della revoca dei dati di identificazione personale e che garantisce che i dati di identificazione personale di un utente siano associati crittograficamente a un'unità di portafoglio;\n\n(5) «utente del portafoglio»: un utente che ha il controllo dell'unità di portafoglio;\n\n(6) «parte facente affidamento sul portafoglio»: una parte facente affidamento che intende fare affidamento sulle unità di portafoglio per la prestazione di servizi pubblici o privati mediante interazione digitale;\n\n(7) «fornitore del portafoglio»: una persona fisica o giuridica che fornisce soluzioni di portafoglio;\n\n(8) «attestato di unità di portafoglio»: un oggetto di dati che descrive i componenti dell'unità di portafoglio o consente la loro autenticazione e convalida;\n\n(9) «politica di divulgazione incorporata»: un insieme di norme, incorporato in un attestato elettronico di attributi dal suo fornitore, che indica le condizioni che una parte facente affidamento sul portafoglio deve soddisfare per accedere all'attestato elettronico di attributi;\n\n(10) «istanza di portafoglio»: l'applicazione installata e configurata su un dispositivo o su un ambiente di un utente del portafoglio, che fa parte di un'unità di portafoglio, e che l'utente del portafoglio utilizza per interagire con l'unità di portafoglio;\n\n(11) «soluzione di portafoglio»: una combinazione di software, hardware, servizi, impostazioni e configurazioni, comprese le istanze di portafoglio, una o più applicazioni crittografiche sicure per il portafoglio e uno o più dispositivi crittografici sicuri per il portafoglio;\n\n(12) «dispositivo crittografico sicuro per il portafoglio»: un dispositivo resistente alle manomissioni che fornisce un ambiente collegato all'applicazione crittografica sicura per il portafoglio e da essa utilizzato per proteggere le risorse critiche e fornire funzioni crittografiche per l'esecuzione sicura di operazioni critiche;\n\n(13) «operazione crittografica del portafoglio»: un meccanismo crittografico necessario nel contesto dell'autenticazione dell'utente del portafoglio e del rilascio o della presentazione di dati di identificazione personale o di attestati elettronici di attributi;\n\n(14) «certificato di accesso della parte facente affidamento sul portafoglio»: un certificato per sigilli elettronici o firme elettroniche che autenticano e convalidano la parte facente affidamento sul portafoglio, rilasciato da un fornitore di certificati di accesso della parte facente affidamento sul portafoglio;\n\n(15) «fornitore di certificati di accesso della parte facente affidamento sul portafoglio»: una persona fisica o giuridica incaricata da uno Stato membro di rilasciare certificati di accesso delle parti facenti affidamento alle parti facenti affidamento sul portafoglio registrate in tale Stato membro.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 1",
    "art. 2",
    "art. 2, punto 1",
    "art. 2, punto 2",
    "art. 2, punto 3",
    "art. 2, punto 4",
    "art. 2, punto 5",
    "art. 2, punto 6",
    "art. 2, punto 7",
    "art. 2, punto 8",
    "art. 2, punto 9",
    "art. 2, punto 10",
    "art. 2, punto 11",
    "art. 2, punto 12",
    "art. 2, punto 13",
    "art. 2, punto 14",
    "art. 2, punto 15",
]

MAPPATURA_LOCALE = {
    "art. 1": ["art. 1"],
    "art. 2": [
        "art. 2",
        "art. 2, punto 1",
        "art. 2, punto 2",
        "art. 2, punto 3",
        "art. 2, punto 4",
        "art. 2, punto 5",
        "art. 2, punto 6",
        "art. 2, punto 7",
        "art. 2, punto 8",
        "art. 2, punto 9",
        "art. 2, punto 10",
        "art. 2, punto 11",
        "art. 2, punto 12",
        "art. 2, punto 13",
        "art. 2, punto 14",
        "art. 2, punto 15",
    ],
}

RELAZIONI = []
