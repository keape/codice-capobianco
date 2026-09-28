"""Fase 6 (ADR-0009) di Fonte 22 - Regolamento di esecuzione (UE) 2025/1569
(attestati elettronici qualificati di attributi - QEAA - e attestati
elettronici di attributi rilasciati da un organismo del settore pubblico
responsabile di una fonte autentica o per suo conto). Capitolo virtuale: solo
RELAZIONI cross-fonte, nessun nodo proprio.

Le relazioni *native* dell'atto (4 basi giuridiche "attua" portate dall'art. 1,
i richiami testuali all'art. 45 septies §3 e all'art. 45 sexies §1 eIDAS2, il
rinvio di allegato I a ETSI EN 319 401) stanno nei moduli cap01/cap02/cap03,
non qui: sono citazioni letterali del testo, non il prodotto di questa
pipeline.

## Pipeline eseguita (2026-09-28, sessione principale)

Questo e' il primo giro di Fase 6 del progetto eseguito **senza seedare prima
la Fonte nuova**: i candidati si generano con app/tools/fase6_candidati_knn.py,
che calcola l'embedding dei `testo` dei nodi nuovi al volo con lo stesso
modello e lo stesso campo usati da app/embed_neo4j.py e li interroga contro
l'indice HNSW gia' popolato. Effetto: un solo `app/seed.py` per import invece
di due (i moduli fase6_candidati_431/432/612.py precedenti lavoravano sugli
embedding in Neo4j e richiedevano quindi la Fonte gia' seedata).

Stadio 1 - 53 nodi nuovi, 191 coppie candidate (k=6, soglia 0.85), shortlist
completa in app/.source_cache/reg_ue_2025_1569/fase6_candidati.json.
Il grep delle citazioni esplicite sul testo ufficiale aveva gia' esaurito i
rinvii ai nodi esistenti (tutti modellati come relazioni native): articoli
eIDAS2 45 quinquies §5, 45 sexies §1 e §2, 45 septies §3, §6, §7 e allegato
VI; ETSI EN 319 401 v3.1.1; regolamento di esecuzione (UE) 2024/2979 (non
censito). Zero citazioni di CAD, DPCM 22/2/2013, SPID, DPCM 19/10/2021,
Regolamento AgID SPID, Regole Tecniche AgID, Reg. (UE) 2015/1502, Codice
Civile o di altri standard ETSI.

Stadio 2 - classificazione dello shortlist nella sessione principale
(classificazione inline, non via subagent: stessa ratio dell'ADR-0009), con
lettura del testo reale delle controparti in Neo4j prima di decidere.

Stadio 3 - validazione: esistenza dei `riferimento` proposti verificata con
query mirata su Neo4j prima della scrittura.

## Esito: 4 relazioni cross-fonte validate (tutte "inferred")

Un numero basso, e non per pigrizia: gli istituti di questo atto (catalogo
degli attributi, catalogo dei regimi, attestati per il portafoglio EUDI,
notifica degli organismi del settore pubblico) sono in larga parte **nuovi**
rispetto al corpus gia' censito, che e' massicciamente orientato a
certificati, formati AdES, marche temporali e identity proofing. Il KNN lo
conferma: sotto la soglia 0.86 le coppie diventano rumore da linguaggio
normativo generico (SPID, DPCM, PEC), non corrispondenze.

1. art. 3 §1 -> Fonte 2 "art. 45 quinquies §1" (specifica, inferred, 0.75):
   l'atto rende operativo l'obbligo di conformita' dei QEAA (allegato V
   eIDAS2) nominando le norme di riferimento e le specifiche tecniche.
2. art. 4 §3 -> Fonte 2 "art. 24 §4-bis (nuovo, eIDAS2)" (specifica,
   inferred, 0.8): l'atto fissa le circostanze minime di revoca degli
   attestati con validita' superiore a 24 ore, completando la regola eIDAS2
   che estende agli attestati qualificati la disciplina di revoca dei
   certificati qualificati.
3. art. 7 §6 -> Fonte 9 "QTS-C.2.3-03" (si sovrappone a, inferred, 0.7):
   entrambe impongono come deve essere firmata/qualificata la richiesta del
   soggetto, ma con soglia diversa - la norma ETSI richiede una firma o un
   sigillo *qualificato*, l'atto ammette anche una firma/sigillo *avanzato*
   basato su certificato qualificato. Le due disposizioni vanno lette
   insieme: chi si conforma a ETSI TS 119 461 soddisfa l'atto, non viceversa.
4. allegato II, punto 2(a) -> Fonte 17 "Parte 1: REG-6.3.1-00F" (si
   sovrappone a, inferred, 0.7): stesso oggetto (rilascio a un soggetto
   diverso dal richiedente, con necessita' di titolo per agire per suo
   conto), uno come autorizzazione del sottoscrittore, l'altro come obbligo
   del fornitore di verificare quel titolo.

## Proposte valutate e scartate (non silenziose, come da ADR-0009)

- Cluster del portafoglio EUDI (il piu' numeroso: 6 candidati per ciascuno dei
  punti 3(a)/3(b) dell'allegato II, a 0.90-0.95): Fonte 2 "art. 5 bis §4(c)",
  "§4(e)", "§5(c)", "§5(d)", "§5(e)", "§11", "art. 5 ter §8". I punti 3(a)/3(b)
  impongono al *fornitore dell'attestato* di autenticarsi nell'unita' di
  portafoglio e di verificarne la revoca; i nodi eIDAS2 citati sono requisiti
  *del portafoglio* (funzionalita', livello di garanzia, autenticazione dei
  soggetti affidanti). Somiglianza lessicale ("portafoglio", "attestato"),
  soggetto e contenuto prescrittivo diversi.
- Cluster "stessa formula, oggetto diverso" su art. 3 §1 (0.897-0.919): Fonte 1
  "art. 28 §1", "art. 29 §1", "art. 30 §1", "art. 38 §1", Fonte 3 "art. 35
  c.1-bis" e "c.5", Fonte 2 "art. 45 quinquies §1" (quest'ultimo invece
  accettato, perche' l'oggetto e' lo stesso: conformita' degli *attestati*
  alle norme di riferimento, non di certificati o dispositivi).
- Cluster "elenco pubblico" (0.86-0.89): Fonte 4 "art. 43 c.2" (elenco AgID
  dei certificatori), Fonte 3 "art. 47 c.3" (Indice dei domicili digitali),
  Fonte 5 "art. 16 c.2" (registro SPID delle tipologie di attributi), Fonte 3
  "art. 6-ter c.1-bis" (Indice per la fatturazione elettronica) verso artt. 5,
  6 e 7 dell'atto. Tutti sono "elenchi/registri pubblici" ma di oggetti e
  sistemi diversi (SPID, PEC, fatturazione) e di autorita' diverse.
- Cluster sull'identita' dei soggetti e delle fonti (0.90-0.91): Fonte 9
  "COL-8.2.5-04X", "VAL-8.3.1-01X", "VAL-8.3.7-03", "COL-8.2.6-03X",
  "COL-8.2.1-05", "USE-9.2.4-01" e Fonte 8 "allegato, punto 2 (QTS-C3-01)".
  L'atto impone di verificare l'*identita' della fonte autentica* e di
  indicare nella richiesta gli attributi e i dati identificativi del soggetto;
  la norma ETSI impone di *validare gli attributi* presso una fonte autorevole
  e di qualificare la firma del richiedente. Prescrizioni adiacenti, non la
  stessa.
- Cluster "entrata in vigore / applicazione" (score fino a 1.000): Fonte 1
  "art. 52 §1" e "§2", Fonte 8 "art. 2, entrata in vigore"/"applicazione",
  Fonte 12 "art. 2, entrata in vigore"/"applicazione", Fonte 14 "art. 2".
  Formule di chiusura identiche senza relazione giuridica: stesso falso
  positivo scartato nei giri Fase 6 del Reg. 2025/1566 e del Reg. 2025/1567.
- Isolati: Fonte 1 "art. 44 §1" (recapito elettronico certificato) verso
  art. 4 §5; Fonte 2 "art. 5 quinquies §5", "art. 44 §2-bis", "art. 45 ter
  §2", "art. 12 §5" verso artt. 4 §2, 5 §4, 7 §7, 8 §2, 10 §1 (nessuna
  corrispondenza di contenuto, solo vicinanza di vocabolario); Fonte 5
  "art. 5 c.3", "art. 7 c.7", "art. 16 c.1" verso artt. 3 §2, 4 §1, 7 §1,
  7 §9, 9 §1, 8 §1 (norme SPID su oggetti diversi); Fonte 4 "art. 4 c.2"
  verso art. 8 §7; Fonte 3 "art. 32 c.3 lett.m", "art. 73 c.3-quater",
  Fonte 2 "art. 24 §1-ter" verso artt. 4 §4, 9 §3, 10 §2.

## Nodi senza alcun candidato sopra soglia (10 su 53)

"art. 2" (definizioni), "art. 5 §3", "art. 7 §5", "§8", "§10", "art. 8 §3",
"§6", "§8", "art. 9 §4", "allegato II, punto 2(c)". Coerente con la natura
dell'atto: sono prescrizioni di dettaglio su procedimenti e contenuti interni
al nuovo sistema degli attestati di attributi, senza corrispondente nel
corpus censito.
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = []

MAPPATURA_LOCALE = {}

RELAZIONI = [
    {
        'nodo_da': ('obbligo', None, 'art. 3 §1'),
        'nodo_a': ('obbligo', 2, 'art. 45 quinquies §1'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('obbligo', None, 'art. 4 §3'),
        'nodo_a': ('obbligo', 2, 'art. 24 §4-bis (nuovo, eIDAS2)'),
        'tipo_relazione': 'specifica',
        'evidence_type': 'inferred',
        'confidence': 0.8,
    },
    {
        'nodo_da': ('obbligo', None, 'art. 7 §6'),
        'nodo_a': ('obbligo', 9, 'QTS-C.2.3-03'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.7,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato II, punto 2(a)'),
        'nodo_a': ('obbligo', 17, 'Parte 1: REG-6.3.1-00F'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.7,
    },
]
