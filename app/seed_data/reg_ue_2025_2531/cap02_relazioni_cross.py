"""Fase 6 (ADR-0009) di Fonte 23 - Regolamento di esecuzione (UE) 2025/2531
(norme di riferimento e specifiche applicabili ai registri elettronici
qualificati, art. 45 terdecies §3 eIDAS2). Capitolo virtuale: solo RELAZIONI,
nessun nodo proprio.

Le 15 relazioni *native* dell'atto (base giuridica, specifica dell'art. 45
terdecies §1, rinvio a ETSI EN 319 401 e 12 adeguamenti di requisiti della
stessa norma) stanno in cap01.py: sono citazioni e adeguamenti letterali, non
il prodotto di questa pipeline. Qui ci sono le sole proposte emerse dal KNN
sullo shortlist.

## Pipeline eseguita (2026-09-28, sessione principale)

Stadio 1 con app/tools/fase6_candidati_knn.py (embedding dei nodi nuovi
calcolato al volo, quindi Fase 6 prima del seed): 26 nodi, 118 coppie
candidate (k=6, soglia 0.85), shortlist in
app/.source_cache/reg_ue_2025_2531/fase6_candidati.json.

Il KNN ha confermato da solo, a 0.91-0.995, dieci delle relazioni native
previste (REQ-7.9.1-02X -> REQ-7.9.1-02 a 0.995; REQ-7.5-01X -> REQ-7.5-01 a
0.987; REQ-6.2-03 -> REQ-6.2-03 a 0.977; REQ-7.8-14X -> REQ-7.8-14 a 0.965;
REQ-7.8-21X -> REQ-7.8-22 a 0.946, con REQ-7.8-21 a 0.917 come alternativo
scartato; REQ-6.3-04X -> REQ-6.3-04 a 0.940; REQ-7.2-04X -> REQ-7.2-04 a
0.913). Il grep delle citazioni esplicite non aggiungeva nulla: l'atto cita
solo ETSI EN 319 401 v3.1.1, l'art. 45 terdecies §3 eIDAS2, l'art. 24 §5, le
norme ISO 23257/23635 e i documenti ENISA/RFC/FIPS/ISO dell'allegato 2.1.

Stadio 2 - classificazione sullo shortlist nella sessione principale.
Stadio 3 - validazione dei `riferimento` controparte su Neo4j.

## Esito: 3 relazioni cross-fonte validate

1. "allegato, punto 3(a), 7.12 REQ-7.12-02 A" -> Fonte 8 "allegato, punto 6
   (OVR-7.12-02)" (si sovrappone a, textual, 0.9): stesso obbligo - il piano di
   cessazione e' conforme agli atti di esecuzione adottati a norma dell'art. 24
   §5 - formulato nel Reg. 2025/1566 per ETSI EN 319 401 e qui per i registri
   elettronici. Il KNN lo porta a 0.988, il punteggio piu' alto dello shortlist.
2. "allegato, punto 3(a), 7.12 REQ-7.12-02 A" -> Fonte 12 "allegato, punto 4
   (OVR-6.4.9-02)" (si sovrappone a, textual, 0.85): stesso obbligo, terzo atto
   di esecuzione del lotto. Le due relazioni atto-atto sono ammesse qui e non
   altrove perche' questa regola non ripete un requisito di una norma tecnica:
   e' una regola *sugli atti di esecuzione* dell'art. 24 §5, quindi il termine
   di confronto utile e' l'altro atto, non la norma. Con queste due relazioni i
   tre atti del lotto che contengono la clausola sono fra loro collegati a
   triangolo.
3. "allegato, punto 3(a), 7.5 REQ-7.5-06" -> Fonte 4 "art. 11 c.1" (si
   sovrappone a, inferred, 0.75): entrambi impongono che le chiavi private di
   firma siano detenute e usate dentro un dispositivo sicuro (il DPCM 22/2/2013
   parla di "dispositivo sicuro di firma" per la generazione di firme
   qualificate e digitali; l'atto aggiunge la certificazione a EAL 4 o
   superiore, EUCC o FIPS 140-3 fino al 2030). Stessa regola, soglia di
   garanzia diversa: `inferred` perche' la corrispondenza e' nel contenuto, non
   in un rinvio.

## Proposte valutate e scartate

- Boilerplate "entrata in vigore" (0.985-0.926): Fonte 1 art. 52 §1, Fonti 8,
  12 e 22 art. 2/art. 11 "entrata in vigore", Fonte 14 art. 2. Formule di
  chiusura identiche senza relazione giuridica: stesso falso positivo scartato
  nei tre giri precedenti del lotto.
- Boilerplate "art. 1 designa l'allegato" (0.938-0.913): Fonte 22 art. 1, Fonte
  12 art. 1, Fonte 7 "Parte 5: Annex A.1/A.2" (tabelle di mapping verso gli
  allegati eIDAS). Tutti gli atti di esecuzione hanno un art. 1 di rinvio.
- Paralleli nella norma dei certificati (0.94-0.916): Fonte 17 "Parte 1:
  OVR-6.5.2-12", "OVR-6.5.2-02", "SDP-6.5.1-24" verso REQ-7.5-01X, e Fonte 18
  "OVR-7.8-02": requisiti crittografici analoghi ma di un servizio diverso
  (certificati/ marche temporali), gia' coperti dal collegamento al requisito
  di origine in Fonte 10. Scartati per non duplicare lo stesso fatto su tre
  archi.
- 6.3 REQ-6.3-04X verso Fonte 2 "art. 24 §2(a)" (0.949) e "art. 20 §1-bis"
  (0.920): l'art. 24 §2(a) riguarda gli obblighi del prestatore qualificato su
  correttezza dei dati, l'art. 20 §1-bis l'accesso dei prestatori all'elenco di
  fiducia; nessuna corrispondenza con la notifica di modifiche all'organismo di
  vigilanza.
- 7.2 REQ-7.2-05X verso Fonte 12 "allegato, punto 3 (OVR-6.4.4-03)" (0.930) e
  7.2 REQ-7.2-04X verso Fonte 12 "allegato, punto 3 (OVR-6.4.4-02)" (0.898):
  entrambi sono la stessa regola del Reg. 2025/1567, che a sua volta e' gia'
  collegata al requisito di origine in Fonte 10. L'arco atto-atto sarebbe
  ridondante (stessa origine), a differenza del caso 7.12 sopra.
- 7.5 REQ-7.5-03 verso Fonte 22 "allegato II, punto 1" (0.879) e verso Fonte 2
  "art. 45 terdecies §1" (0.872), 7.5 REQ-7.5-04/-05 verso lo stesso §1:
  i requisiti della clausola 7.5 dettagliano i singoli elementi dell'art. 45
  terdecies §1 (origine, ordine cronologico, integrita'), ma la relazione
  articolo-livello e' gia' portata dal chapeau del punto 3 di questo stesso
  atto: quattro archi in piu' verso lo stesso nodo non aggiungerebbero
  informazione.
- 6.1 REQ-6.1-12 verso Fonte 22 "art. 3 §2" (0.863) e "art. 4 §1" (0.852):
  sotto la fascia utile, nessuna corrispondenza di contenuto.
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = []

MAPPATURA_LOCALE = {}

RELAZIONI = [
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 7.12 REQ-7.12-02 A'),
        'nodo_a': ('obbligo', 8, 'allegato, punto 6 (OVR-7.12-02)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'textual',
        'confidence': 0.9,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 7.12 REQ-7.12-02 A'),
        'nodo_a': ('obbligo', 12, 'allegato, punto 4 (OVR-6.4.9-02)'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'textual',
        'confidence': 0.85,
    },
    {
        'nodo_da': ('obbligo', None, 'allegato, punto 3(a), 7.5 REQ-7.5-06'),
        'nodo_a': ('obbligo', 4, 'art. 11 c.1'),
        'tipo_relazione': 'si sovrappone a',
        'evidence_type': 'inferred',
        'confidence': 0.75,
    },
]
