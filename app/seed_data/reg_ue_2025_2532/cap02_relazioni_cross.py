"""Fase 6 (ADR-0009) di Fonte 24 - Regolamento di esecuzione (UE) 2025/2532
(norme di riferimento e specifiche per i servizi di archiviazione elettronica
qualificati, art. 45 undecies §2 eIDAS2). Capitolo virtuale: solo RELAZIONI.

Le 9 relazioni *native* dell'atto stanno in cap01.py (art. 45 undecies §1 e §2,
art. 24 §5, le citazioni per id dei requisiti di ETSI EN 319 401 nella lettera
f) e le quattro clausole sul piano di cessazione). Qui le sole proposte emerse
dal KNN.

## Pipeline eseguita (2026-09-28, sessione principale)

Stadio 1 con app/tools/fase6_candidati_knn.py (embedding dei nodi nuovi
calcolato al volo, Fase 6 prima del seed): 14 nodi, 79 coppie candidate (k=6,
soglia 0.83), shortlist in
app/.source_cache/reg_ue_2025_2532/fase6_candidati.json.

Stadio 2 - classificazione sullo shortlist. Stadio 3 - verifica dei
`riferimento` controparte su Neo4j.

## Esito: 3 relazioni cross-fonte validate

1. "allegato, adeguamento d) risorse umane" -> Fonte 10 "REQ-7.2-04" (si
   sovrappone a, inferred, 0.75): la lettera ripete il requisito sul personale
   in ruoli di fiducia, identico a quello gia' censito in ETSI EN 319 401 e
   gia' riprodotto dagli atti Fonti 12 e 23 per i rispettivi servizi.
2. "allegato, adeguamento d) risorse umane" -> Fonte 10 "REQ-7.2-05" (si
   sovrappone a, inferred, 0.75): la seconda parte della stessa lettera,
   aggiornamenti almeno ogni 12 mesi sulle nuove minacce.
3. "allegato, adeguamento e) controlli e monitoraggio crittografici" -> Fonte 4
   "art. 11 c.1" (si sovrappone a, inferred, 0.75): stesso oggetto (chiavi
   private di firma detenute e usate dentro un dispositivo sicuro), con soglia
   di garanzia diversa - il DPCM 22/2/2013 chiede un "dispositivo sicuro di
   firma", l'atto una certificazione a EAL 4 o superiore, EUCC, o FIPS 140-3
   livello 3 fino al 31.12.2030.

## Proposte valutate e scartate

- Boilerplate "entrata in vigore" (0.987-0.919): Fonte 23 "art. 2, entrata in
  vigore", Fonte 1 art. 52 §1, Fonti 8, 12 e 22, Fonte 14 art. 2. Formule di
  chiusura identiche senza relazione giuridica: stesso falso positivo scartato
  in tutti i giri precedenti del lotto.
- Boilerplate "riferimenti normativi" (0.938-0.897): Fonte 23 "allegato, punto
  3(a), 2.1 riferimenti normativi", Fonte 12 "allegato, punto 1", Fonte 17
  "Parte 1: clausola 2.1 (Normative references)" e "Parte 2: clausola 3.1
  (Terms)", Fonte 7 "Parte 5: Annex A.2", Fonte 1 "art. 37 §4 (abrogato)".
  Tutte le lettere a) degli atti di esecuzione sono liste di riferimenti
  bibliografici: la somiglianza e' nel fatto di essere elenchi di norme, non
  nel contenuto.
- Cluster "sicurezza di rete e raccolta di prove" (0.920-0.899): Fonte 9
  "OVR-7.8-01", Fonte 17 "Parte 2: OVR-6.5.7-01" e "Parte 1: OVR-6.5.5-01A",
  Fonte 18 "OVR-7.10-01", "OVR-7.11-01", "OVR-7.15-01", Fonte 11 "Parte 1:
  OVR-6.4.8-01", "OVR-6.4.9-01", "Parte 2: OVR-7.10-01", Fonte 12 "allegato,
  punto 5 (OVR-6.5.5-02)". Le lettere f) e g) dell'atto non riformulano quei
  requisiti: rinviano a clausole di ETSI EN 319 401 o di CEN/TS 18170, e
  citano per id solo REQ-7.8-13 e REQ-7.8-17X (relazioni native). Le
  somiglianze verso altri standard sono quindi requisiti *di altre norme* sullo
  stesso tema, non la stessa prescrizione.
- "art. 2" (rinvio all'allegato) verso Fonte 23 "art. 1" (0.897): entrambi
  designano un allegato, nessuna corrispondenza di contenuto.

## Limite noto

I rinvii di clausola di questo atto ("si applicano i requisiti di ETSI EN 319
401, punto 5 / sottopunto 7.5 / 7.8 / 7.10", "i requisiti di CEN/TS 18170,
punto 6.1 / 6.2 / 7.3 / 7.13 / 13.3.1") non producono relazioni: la Fonte 10
ha nodi per id di requisito e non per clausola, e CEN/TS 18170 non e' censita
(vedi backlog in docs/plan-import-lotto-eidas2-standard.md § 7). Un rinvio di
clausola non ha quindi un nodo controparte esatto, e non ne e' stato scelto uno
arbitrario. E' il motivo per cui questo atto, pur essendo il piu' dipendente da
norme tecniche, ha meno relazioni dei tre atti precedenti del lotto.
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = []

MAPPATURA_LOCALE = {}

RELAZIONI = [
    {
        'nodo_da': ('obbligo', None, 'allegato, adeguamento d) risorse umane'),
        'nodo_a': ('obbligo', 10, 'REQ-7.2-04'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, adeguamento d) risorse umane'),
        'nodo_a': ('obbligo', 10, 'REQ-7.2-05'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.75,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, adeguamento e) controlli e monitoraggio crittografici'),
        'nodo_a': ('obbligo', 4, 'art. 11 c.1'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.75,
    },
]
