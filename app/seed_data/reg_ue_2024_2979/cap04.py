"""Regolamento di esecuzione (UE) 2024/2979 della Commissione, del 28 novembre
2024 - modalita' di applicazione del regolamento (UE) n. 910/2014 per quanto
riguarda l'integrita' e le funzionalita' di base dei portafogli europei di
identita' digitale (articolo 5 bis, paragrafo 23, eIDAS). Fonte 28 (id
assegnato dal wiring della sessione principale: questo modulo NON tocca
`app/seed.py`, gli id sono risolti per riferimento dal registro di
`app/seed_data/lib.py`).

Porzione di questo modulo (cap04 di 5, come da manifest di
`app/tools/split_source.py`): Capo IV - Disposizioni finali (art. 15) piu' il
paratesto finale e le note a pie' di pagina. Testo ufficiale italiano in
app/.source_cache/reg_ue_2024_2979/cap04.txt, acquisito con content
negotiation CELLAR (publications.europa.eu/resource/celex/32024R2979,
Accept-Language: ita): url risolto .../cellar/a7576de1-b1e0-11ef-acb1-
01aa75ed71a1.0014.03/DOC_1 (XHTML della Gazzetta ufficiale), fetch
2026-09-28, 38.236 caratteri di testo, sha256 del raw.txt
c0bebf5c6707ddb9c70999245e38999f63f154afee2afc6009aad72d1d09cad0 (integrale in
provenance.json). Il preambolo (considerando 1-48) e la parte dispositiva
degli artt. 1-14 e degli allegati I-V appartengono ad altri capitoli di questa
Fonte e non sono toccati qui.

Modellazione (ADR-0007, nessun discrimine di rilevanza):
- Art. 15, comma sull'entrata in vigore -> UN nodo Principio tipo "altro": e'
  una disposizione sulla vigenza dell'atto (dies a quo al ventesimo giorno
  successivo alla pubblicazione in GUUE), che non impone alcun comportamento
  a un soggetto e non e' ne' definitoria ne' di scopo/ambito. Stesso
  trattamento dell'art. 2 del Reg. 2025/1566, dell'art. 2 del Reg. 2025/1567 e
  dell'art. 3 del Reg. 2025/2532 (tutti atti di esecuzione eIDAS2).
- Applicazione differita: NON esiste in questo regolamento e non e' stata
  inventata. Verificato riga per riga su cap04.txt, l'art. 15 si compone di
  due soli paragrafi (entrata in vigore; formula di chiusura) e non contiene
  alcun secondo termine di applicazione, a differenza dell'art. 2 del Reg.
  2025/1566/2025/1567 e dell'art. 11 §2 del Reg. 2025/1569 (che differiscono
  l'applicazione al 19 agosto 2027/2026). Nessuna riga e nessuna
  `condizione_applicabilita` per una data differita che il testo non prevede;
  l'assenza e' dichiarata nel campo `testo` del nodo.
- Art. 15, comma della formula di chiusura ("Il presente regolamento e'
  obbligatorio in tutti i suoi elementi e direttamente applicabile in
  ciascuno degli Stati membri") -> nessun nodo: e' la formula standard di ogni
  regolamento UE self-executing, elemento di formattazione dell'atto senza
  contenuto normativo distinto dalla forma giuridica "regolamento" gia'
  presupposta dal censimento (stesso criterio di tutte le Fonti gia' censite,
  da ultimo l'art. 3 del Reg. 2025/2532). Per lo stesso motivo non compare in
  INDICE_ARTICOLI_LOCALE: un item di indice privo di riga farebbe fallire
  `verifica_copertura`.
- Granularita' dell'articolo finale: i due paragrafi del testo ufficiale NON
  sono numerati (nessun "1."/"2."), quindi una numerazione per comma
  ("art. 15 §1") sarebbe inventata. L'unico item di indice e' "art. 15,
  entrata in vigore", nominato per contenuto come negli articoli finali degli
  altri atti di esecuzione eIDAS2 ("art. 2, entrata in vigore" nel Reg.
  2025/1566, "art. 3, entrata in vigore" nel Reg. 2025/2532). L'art. 15 non ha
  lettere: nessuna lettera da indicizzare.
- `testo_integrale`: verbatim e integrale, ricucendo le righe spezzate dalla
  conversione, con l'intestazione "Articolo 15" e il titolo "Entrata in
  vigore" come il testo ufficiale li premette immediatamente al comma. Il
  comma della formula di chiusura resta fuori dal `testo_integrale` perche'
  non ha una riga propria: non e' un'elisione (nessun testo del comma censito
  e' abbreviato), e' semplicemente un paragrafo che il censimento non mappa.
  Nessun campo valorizza severita' o sanzioni: l'atto non prevede sanzioni
  proprie.
- Paratesto amministrativo -> nessun nodo: "Fatto a Bruxelles, il 28 novembre
  2024" (epigrafe), "Per la Commissione / La presidente / Ursula VON DER
  LEYEN" (firma) non sono articoli, commi o lettere, ma la chiusura formale
  dell'atto. La riga "ELI:
  http://data.europa.eu/eli/reg_impl/2024/2979/oj" e "ISSN 1977-0707
  (electronic edition)" chiudono il documento in coda all'allegato V (quindi
  cadono fuori da questa porzione, che termina con le note a pie' di pagina) e
  restano paratesto di pubblicazione in ogni caso: nessun nodo. Per completezza
  di questa porzione: l'art. 15, comma 2 (formula di chiusura) e le undici
  note a pie' di pagina sono le uniche altre righe di cap04.txt.
- Note a pie' di pagina (1)-(11) -> nessun nodo proprio. Sono i riferimenti
  bibliografici alle citazioni degli atti: (1) GU L 257 del 28.8.2014,
  pag. 73 (regolamento (UE) n. 910/2014); (2) regolamento (UE) 2016/679
  (GDPR); (3) direttiva 2002/58/CE; (4) regolamento di esecuzione (UE)
  2024/2982; (5) lo stesso regolamento di esecuzione (UE) 2024/2979; (6)
  regolamento di esecuzione (UE) 2024/2977; (7) regolamento di esecuzione (UE)
  2024/2980; (8) GU L 210 del 14.6.2021, pag. 51 (raccomandazione (UE)
  2021/946); (9) regolamento (UE) 2024/1183 (eIDAS2); (10) regolamento (UE)
  2018/1725; (11) regolamento di esecuzione (UE) 2015/1502. Descrivono atti
  citati e il loro recapito in GUUE, non disposizioni di questo regolamento:
  nessun comportamento imposto, nessun effetto giuridico proprio. Il segnaposto
  "(N)" che le richiama e' un rinvio bibliografico, non un precetto; e il
  collegamento verso le Fonti esterne a cui rinviano (eIDAS/eIDAS2, GDPR,
  Reg. 2015/1502, gli altri tre regolamenti di esecuzione 2024/2977-2980-2982)
  e' materia della fase ADR-0009 della sessione principale, non di questo
  modulo.
- RELAZIONI = []: questa porzione non contiene nessun rinvio a un altro
  articolo o allegato di questa Fonte (l'art. 15 non cita alcun nodo interno),
  quindi non c'e' alcuna relazione interna da dichiarare. Nessuna relazione
  cross-fonte tentata in fase di import parallelo per capitolo (sarebbe
  KeyError sul registro, che non contiene ancora le altre Fonti).

Copertura: 1 item di indice, 1 riga (0 Obblighi + 1 Principio).
"""

RIGHE_OBBLIGHI = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 15, entrata in vigore",
        "testo": "Il presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea; il testo non prevede alcuna disposizione di applicazione differita separata.",
        "testo_integrale": "Articolo 15\n\nEntrata in vigore\n\nIl presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell'Unione europea.",
        "tipo_principio": "altro",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 15, entrata in vigore",
]

MAPPATURA_LOCALE = {
    "art. 15, entrata in vigore": ["art. 15, entrata in vigore"],
}

RELAZIONI = []
