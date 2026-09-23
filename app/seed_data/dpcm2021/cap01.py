"""DPCM 19 ottobre 2021 - Modifiche al DPCM 24 ottobre 2014 (SPID). Fonte 6,
un unico capitolo (decreto di sole 5 disposizioni di modifica, non richiede
suddivisione per subagent). Testo ufficiale in
app/.source_cache/dpcm2021/raw.txt (GU n.296 del 14-12-2021).

Modellazione (ADR-0007): il decreto e' interamente novellistico (ogni
articolo modifica una disposizione del DPCM 24/10/2014, Fonte 5, senza
introdurre un precetto autonomo separato da tracciare come Obbligo).
Ciascuno dei 5 articoli e' quindi censito come Principio, tipo "altro" (non
esiste in tassonomia un tipo dedicato alla novella legislativa in senso
stretto - "scopo/ambito" e "definitorio" non si applicano), con relazione
tipizzata "modifica"/"abroga" verso il nodo Fonte 5 realmente inciso (ADR-0009,
collegamento cross-fonte nativo in fase di creazione, non differito: la Fonte
6 esiste per definizione solo in funzione della Fonte 5 che modifica).

L'art. 1 modifica le premesse (i "Visto") del DPCM 2014, non un articolo del
suo articolato: non esiste un nodo Fonte 5 corrispondente da collegare (le
premesse non sono censite, ADR-0007 si applica ad articoli/commi
dell'articolato). Nessuna relazione per questo nodo, riportato comunque per
coprire l'intero decreto (nessun discrimine di rilevanza).

Correzione dati 2026-09-21: i nodi Fonte 5 realmente modificati (art. 7 c.9,
art. 10 c.3/c.4, art. 12) sono stati aggiornati direttamente nei moduli
app/seed_data/spid/cap02.py e cap03.py per riportare il testo vigente
post-2021 (in precedenza riportavano per errore il testo previgente 2014,
nonostante l'etichetta della Fonte 5 dichiarasse gia' "comprensivo delle
modifiche del DPCM 19 ottobre 2021").

Fase 6 (ADR-0009) verso le altre fonti censite: il decreto non contiene
alcuna citazione testuale diretta a eIDAS/eIDAS2, CAD o DPCM 22/2/2013 nel
proprio articolato (solo riferimenti, nelle premesse, al regolamento eIDAS
910/2014 e, nell'art. 2, al regolamento (UE) 2016/679 - GDPR, non una fonte
censita in questo grafo); grep sul testo ufficiale conferma zero occorrenze
di "eIDAS", "910/2014", "82/2005" (CAD) e "22 febbraio 2013" (DPCM firme)
fuori dalle premesse generali. Nessuna relazione aggiuntiva verso quelle
fonti: esito verificato, non fase saltata.
"""

RIGHE_OBBLIGHI: list[dict] = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 1",
        "testo": "Nelle premesse del DPCM 24 ottobre 2014 è inserito il richiamo al "
                 "regolamento di esecuzione (UE) 2015/1502 della Commissione dell'8 "
                 "settembre 2015, relativo alle specifiche e procedure tecniche minime "
                 "sui livelli di garanzia per i mezzi di identificazione elettronica "
                 "(art. 1 comma 2 e punto 2.4.1 dell'allegato).",
        "testo_integrale": "Nelle premesse del decreto del Presidente del Consiglio dei "
                            "ministri del 24 ottobre 2014, dopo il capoverso relativo al "
                            "regolamento (UE) n. 910/2014, è inserito il seguente: «Visto "
                            "il regolamento di esecuzione (UE) 2015/1502 della Commissione "
                            "dell'8 settembre 2015 relativo alla definizione delle "
                            "specifiche e procedure tecniche minime riguardanti i livelli "
                            "di garanzia per i mezzi di identificazione elettronica ai "
                            "sensi dell'art. 8, paragrafo 3, del regolamento (UE) "
                            "n. 910/2014 del Parlamento europeo e del Consiglio in materia "
                            "di identificazione elettronica e servizi fiduciari per le "
                            "transazioni elettroniche nel mercato interno e, in "
                            "particolare, l'art. 1, comma 2 e il numero 2.4.1 "
                            "(Disposizioni generali) del relativo allegato;».",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 2",
        "testo": "Modifica l'art. 7 comma 9 del DPCM 24 ottobre 2014: il trattamento dei "
                 "dati personali raccolti ai fini SPID deve avvenire anche nel rispetto "
                 "del regolamento (UE) 2016/679 (GDPR), oltre che del d.lgs. 196/2003.",
        "testo_integrale": "All'art. 7, comma 9, del decreto del Presidente del Consiglio "
                            "dei ministri 24 ottobre 2014, dopo le parole «di cui» sono "
                            "inserite le seguenti: «al regolamento (UE) 2016/679 e».",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 3",
        "testo": "Modifica l'art. 10 comma 3 del DPCM 24 ottobre 2014: introduce il "
                 "requisito di personalità giuridica riconosciuta con patrimonio/capitale "
                 "minimo di 300.000 euro (nuova lettera 0-b), introduce l'obbligo di "
                 "copertura assicurativa minima di 1,5 milioni di euro annui/150.000 euro "
                 "per sinistro (nuova lettera c-bis), estende il trattamento dei dati "
                 "personali (lettera g) al regolamento (UE) 2016/679, e aggiorna di "
                 "conseguenza il rinvio dell'art. 10 comma 4 (esenzione PA) includendo la "
                 "nuova lettera c-bis).",
        "testo_integrale": "All'art. 10, comma 3, del decreto del Presidente del Consiglio "
                            "dei ministri 24 ottobre 2014, sono apportate le seguenti "
                            "modificazioni: a) prima della lettera b) è inserita la "
                            "seguente: «0 b) essere una persona giuridica riconosciuta, con "
                            "un patrimonio o un capitale sociale non inferiore a "
                            "trecentomila euro e con un'organizzazione consolidata e "
                            "pienamente operativa sotto tutti gli aspetti pertinenti per la "
                            "fornitura dei servizi»; b) dopo la lettera c) è inserita la "
                            "seguente: «c-bis) disporre, per il risarcimento dei danni "
                            "causati, con dolo o colpa, a qualsiasi persona fisica o "
                            "giuridica a causa del mancato adempimento degli obblighi "
                            "connessi alla gestione del sistema SPID, di una adeguata "
                            "copertura assicurativa di almeno 1,5 milioni di euro annui e "
                            "centocinquantamila euro per singolo sinistro;» b) alla lettera "
                            "g) dopo le parole «nel rispetto del» sono inserite le "
                            "seguenti: «regolamento (UE) 2016/679 e del»; c) al comma 4, le "
                            "parole: «lettere a) e b)» sono sostituite dalle seguenti: "
                            "«lettere a), b) e c-bis)».",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 4",
        "testo": "Modifica l'art. 12 del DPCM 24 ottobre 2014: estende da trenta a "
                 "sessanta giorni il preavviso di cessazione attività del gestore e ne "
                 "ridefinisce il contenuto (comma 1); integra la procedura di subentro con "
                 "il recepimento di eventuali prescrizioni dell'Agenzia (comma 2); "
                 "sopprime il comma 3 (revoca automatica delle identità in assenza di "
                 "subentro); introduce il nuovo comma 5-bis, che attribuisce all'Agenzia il "
                 "potere di ridistribuire le identità digitali del gestore cessato o "
                 "revocato tra gli altri gestori quando nessuno è disponibile a subentrare "
                 "volontariamente.",
        "testo_integrale": "All'art. 12 del decreto del Presidente del Consiglio dei "
                            "ministri 24 ottobre 2014 sono apportate le seguenti "
                            "modificazioni: a) al comma 1, le parole «trenta giorni» sono "
                            "sostituite dalle parole «sessanta giorni» e le parole da «gli "
                            "eventuali» fino alla fine del comma sono sostituite dalle "
                            "seguenti: «i gestori sostitutivi e le modalità tecniche e "
                            "operative per il trasferimento delle identità digitali, nel "
                            "rispetto delle indicazioni fornite dall'Agenzia ai sensi "
                            "dell'art. 4.»; b) al comma 2, dopo le parole «dichiarazione di "
                            "accettazione» sono aggiunte le seguenti: «, recepimento di "
                            "eventuali prescrizioni dell'Agenzia in ordine alle modalità del "
                            "trasferimento»; c) il comma 3 è soppresso; d) dopo il comma 5 è "
                            "inserito il seguente: «5-bis. Nel caso in cui, a seguito della "
                            "cessazione dell'attività da parte di un gestore dell'identità "
                            "digitale o della revoca del suo accreditamento, nessun altro "
                            "gestore è disponibile a subentrare con le modalità del comma 2, "
                            "l'Agenzia, con determinazione del direttore generale recante "
                            "anche prescrizioni in ordine alle modalità del trasferimento, "
                            "provvede a ridistribuire le identità digitali rilasciate dal "
                            "gestore cessato o revocato tra tutti gli altri gestori che "
                            "subentreranno nella relativa gestione in misura proporzionale "
                            "alla ripartizione percentuale, tra gli stessi, di tutte le "
                            "identità SPID rilasciate alla data della cessazione o della "
                            "revoca.».",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 5",
        "testo": "Modifica l'art. 16 comma 3 lettera d) del DPCM 24 ottobre 2014: "
                 "aggiorna il riferimento da «indice degli indirizzi della pubblica "
                 "amministrazione [...] di cui all'art. 57-bis» (articolo del CAD abrogato "
                 "dal d.lgs. 179/2016) a «indice dei domicili digitali [...] di cui "
                 "all'art. 6-ter», l'indice CAD effettivamente vigente e funzionalmente "
                 "successore del precedente.",
        "testo_integrale": "All'art. 16, comma 3, lettera d), del decreto del Presidente "
                            "del Consiglio dei ministri 24 ottobre 2014, le parole «degli "
                            "indirizzi della pubblica amministrazione e dei gestori dei "
                            "pubblici servizi di cui all'art. 57-bis» sono sostituite dalle "
                            "seguenti: «dei domicili digitali delle pubbliche "
                            "amministrazioni e dei gestori di pubblici servizi di cui "
                            "all'art. 6-ter».",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 1",
    "art. 2",
    "art. 3",
    "art. 4",
    "art. 5",
]

MAPPATURA_LOCALE = {
    "art. 1": ["art. 1"],
    "art. 2": ["art. 2"],
    "art. 3": ["art. 3"],
    "art. 4": ["art. 4"],
    "art. 5": ["art. 5"],
}

RELAZIONI = [
    {
        "nodo_da": ("principio", None, "art. 2"),
        "nodo_a": ("obbligo", 5, "art. 7 c.9"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
    {
        "nodo_da": ("principio", None, "art. 3"),
        "nodo_a": ("obbligo", 5, "art. 10 c.3 lett.0-b)"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
    {
        "nodo_da": ("principio", None, "art. 3"),
        "nodo_a": ("obbligo", 5, "art. 10 c.3 lett.c-bis)"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
    {
        "nodo_da": ("principio", None, "art. 3"),
        "nodo_a": ("obbligo", 5, "art. 10 c.3 lett.g)"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
    {
        "nodo_da": ("principio", None, "art. 3"),
        "nodo_a": ("principio", 5, "art. 10 c.4"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
    {
        "nodo_da": ("principio", None, "art. 4"),
        "nodo_a": ("obbligo", 5, "art. 12 c.1"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
    {
        "nodo_da": ("principio", None, "art. 4"),
        "nodo_a": ("obbligo", 5, "art. 12 c.2"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
    {
        "nodo_da": ("principio", None, "art. 4"),
        "nodo_a": ("obbligo", 5, "art. 12 c.3"),
        "tipo_relazione": "abroga",
        "evidence_type": "textual",
        "confidence": 0.9,
    },
    {
        "nodo_da": ("principio", None, "art. 4"),
        "nodo_a": ("principio", 5, "art. 12 c.5-bis"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
    {
        "nodo_da": ("principio", None, "art. 5"),
        "nodo_a": ("principio", 5, "art. 16 c.3 lett.d)"),
        "tipo_relazione": "modifica",
        "evidence_type": "textual",
        "confidence": 0.95,
    },
]
