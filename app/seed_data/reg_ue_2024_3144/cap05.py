"""Regolamento di esecuzione (UE) 2024/3144 della Commissione, del 18 dicembre
2024, che modifica il regolamento di esecuzione (UE) 2024/482 per quanto
riguarda le norme internazionali applicabili e che rettifica tale regolamento
di esecuzione. Fonte 30 (slug `reg_ue_2024_3144`), capitolo 5 di 5 (vedi
app/.source_cache/reg_ue_2024_3144/manifest.json): Allegato II - modifiche
all'allegato IV del regolamento di esecuzione (UE) 2024/482 (Fonte 29, slug
`reg_ue_2024_482`). L'art. 1 punti 1-8, gli artt. 2-3 e l'allegato I sono nei
capitoli 1-4, assegnati ad altri moduli: nessuno di quei file e' toccato qui.

Provenienza del testo: app/.source_cache/reg_ue_2024_3144/cap05.txt, estratto
dal raw.txt integrale acquisito per content negotiation CELLAR
(http://publications.europa.eu/resource/celex/32024R3144, lingua italiana; URL
risolto
http://publications.europa.eu/resource/cellar/12c401d0-bdaa-11ef-91ed-01aa75ed71a1.0014.03/DOC_1,
XHTML della Gazzetta ufficiale; fetch 2026-09-29T10:29:08+00:00, 74.420 byte
scaricati, 22.217 caratteri di testo, sha256 del raw.txt
7ced6d4bfe633cf367b3c72ec593ebd5e49c369c7f86f4386984fe81cb81493a - dettagli
completi in app/.source_cache/reg_ue_2024_3144/provenance.json). La porzione
assegnata e' l'allegato II per intero: dall'intestazione "ALLEGATO II" alla riga
che precede "ELI: http://data.europa.eu/eli/reg_impl/2024/3144/oj". Il preambolo
e' a monte degli allegati e non e' in questa porzione; qui non compaiono
epigrafe, firma, formula di chiusura ne' note a pie' di pagina.

Natura del capitolo (atto modificativo). L'allegato II non enuncia un precetto
di per se': e' una disposizione di novella che sostituisce, nell'allegato IV del
regolamento di esecuzione (UE) 2024/482 (Fonte 29), i punti 5 e 6 della sezione
IV.3 con il testo riportato tra virgolette («...»). Le righe di questo modulo
sono quindi i due punti del testo sostitutivo, con il loro contenuto verbatim,
che e' cio' che l'atto modificativo dispone. Le disposizioni del regolamento
modificato richiamate dal testo sostitutivo (l'organismo di certificazione, il
prodotto TIC, la relazione sull'analisi dell'impatto) NON sono censite qui:
vivono nella Fonte 29 e sarebbero duplicate.

Convenzione dei riferimenti (nota di capitolo: allegato la cui unica
numerazione e' quella del testo sostitutivo): i punti numerati sono "allegato
II, punto 5" e "allegato II, punto 6"; le loro lettere seguono la convenzione
del censimento ("allegato II, punto 5(a)", "allegato II, punto 5(b)", "allegato
II, punto 5(c)"). I numeri 5 e 6 sono quelli della sezione IV.3 dell'allegato IV
della Fonte 29 (il testo sostitutivo non ne introduce di nuovi): il riferimento
interno del modulo resta pero' quello dell'allegato II, perche' e' la
disposizione dell'atto modificativo che questi nodi censiscono - le relazioni
verso i nodi corrispondenti della Fonte 29 ("allegato IV, sezione IV.3, punto
5" e "allegato IV, sezione IV.3, punto 6", censiti nel cap11 di quella Fonte)
sono di Fase 6. Nessun item a livello di allegato ("allegato II"): i punti sono
numerati e il livello-allegato non aggiungerebbe un precetto (stessa scelta del
cap04 di questa Fonte per l'allegato I e del cap11 di Fonte 29 per l'allegato
IV). Gli stessi riferimenti sono usati da INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE
e RELAZIONI.

Modellazione (ADR-0007, nessun item di indice scoperto, nessuno coperto due
volte; item di copertura: 5):
- Chapeau ("Nell'allegato IV del regolamento di esecuzione (UE) 2024/482, alla
  sezione IV.3 i punti 5 e 6 sono sostituiti dai seguenti:") -> nessun nodo e
  nessun item di indice proprio: e' la frase che introduce il testo sostitutivo
  e non ha precetto autonomo, il suo contenuto sono i due punti che seguono.
  Resta verbatim in testa al `testo_integrale` della prima riga del capitolo
  ("allegato II, punto 5"), dove il testo ufficiale lo precede immediatamente -
  stessa convenzione con cui il cap01 di questa Fonte tiene il chapeau "Il
  regolamento di esecuzione (UE) 2024/482 è così modificato:" all'inizio della
  riga "art. 1, punto 1", e con cui il cap04 di questa Fonte tiene l'intestazione
  quotata e il titolo dell'allegato I in testa alla riga "allegato I, punto 1".
  Il chapeau e' l'unico enunciato del capitolo che nomina il regolamento
  modificato, la sezione e i punti incisi: dovendo per forza stare dentro una
  riga, sta in quella (l'informazione e' cosi' disponibile alla Fase 6 anche
  senza un nodo dedicato). Scartata l'alternativa di un nodo Principio "altro"
  dedicato alla clausola di novella (pure sostenibile: il dpcm2021/cap01.py
  censisce cosi' gli articoli novellistici del DPCM 19 ottobre 2021) perche'
  qui il chapeau non designa da solo alcun oggetto che le altre righe non
  designino gia' - a differenza del chapeau dell'allegato del Reg. 2025/2532
  (cap01 di quella Fonte), che nomina la norma di riferimento designata e per
  questo ha un nodo proprio - e perche' la convenzione omogenea dei capitoli di
  questa Fonte e' di non dare item alle frasi introduttive del testo sostitutivo.
- Punto 5 -> UNA SOLA riga Obbligo "procedurale", con i quattro item (punto 5 e
  lettere a)-c)). Il punto consta di due capoversi - nessun nuovo certificato
  per il prodotto TIC modificato e redazione della relazione di manutenzione; la
  relazione di manutenzione e' inclusa come sottoinsieme della relazione
  sull'analisi dell'impatto e contiene le sezioni a)-c) - che concorrono allo
  stesso precetto di documentazione del processo di certificazione: un solo
  nodo, entrambi i capoversi integralmente nel `testo_integrale`. Le tre lettere
  ("introduzione;", "descrizione delle modifiche;", "developer evidence
  interessata;") sono voci dell'elenco retto dal secondo capoverso, senza
  predicato proprio ne' precetto autonomo: restano nel `testo_integrale` della
  riga del punto, con item di indice separati (stessa soluzione del cap11 di
  Fonte 29 per i punti 2 e 5 della sezione IV.3 e del cap09 di quella Fonte per
  l'allegato I). tipo_obbligo "procedurale" e non "tecnico/sicurezza", come per
  il punto 5 sostituito nel cap11 di Fonte 29: disciplina il procedimento di
  certificazione, non una proprieta' tecnica del prodotto.
- Punto 6 -> UNA riga Obbligo "informativo/trasparenza": la relazione di
  manutenzione e' fornita all'ENISA per la pubblicazione sul sito web relativo
  alla certificazione della cibersicurezza (stesso tipo della riga gemella del
  punto 6 sostituito, cap11 di Fonte 29).
- Soggetti. Il punto 5 e' impersonale (non e' rilasciato alcun nuovo certificato
  per il prodotto TIC modificato ed e' redatta una relazione di manutenzione in
  riferimento alla relazione di certificazione iniziale) e non nomina ne'
  l'obbligato ne' un destinatario; l'obbligato dichiarato e' "Terza parte"
  (l'organismo di certificazione, che rilascia i certificati EUCC e redige le
  relazioni di certificazione: e' il soggetto che il cap11 di Fonte 29
  attribuisce alla versione sostituita dello stesso punto), senza destinatario,
  perche' il testo non ne nomina alcuno. Il punto 6 nomina espressamente
  l'ENISA: obbligato "Terza parte" (l'obbligo di fornire e' posto in capo
  all'organismo di certificazione, soggetto di tutto il processo di
  certificazione, come nel punto 5 della sezione IV.2 censito nel cap11 di
  Fonte 29) e destinatario "Terza parte" (l'ENISA), come nel punto 6 sostituito.
- `condizione_applicabilita` valorizzata dove il precetto e' subordinato a un
  fatto: punto 5 e punto 6 (modifiche confermate di minore entita').
- `severita` e `sanzioni` non valorizzati: nessuno dei due commi le prevede
  (stesso trattamento del cap11 di Fonte 29 per la medesima sezione).

Cosa e' escluso e perche':
- intestazione "ALLEGATO II" -> nessun nodo e nessun item: e' paratesto
  dell'atto, non un punto dell'allegato (stesso trattamento dell'intestazione
  non quotata "ALLEGATO I" nel cap04 di questa Fonte e delle intestazioni degli
  allegati I e II della Fonte 29, cap09/cap11 di quella Fonte);
- riga "ELI: http://data.europa.eu/eli/reg_impl/2024/3144/oj" e riga "ISSN
  1977-0707 (electronic edition)" -> nessun nodo: corredo editoriale della
  Gazzetta ufficiale;
- virgoletta di apertura « davanti al punto 5 e, dopo il punto 6, il punto fermo
  che chiude il periodo del testo sostitutivo, la virgoletta di chiusura » e il
  punto fermo che chiude la frase del chapeau (il testo ufficiale pubblica
  "cibersicurezza.». "): riportati verbatim ciascuno nella riga in cui il testo
  ufficiale li colloca, perche' il testo sostitutivo e' un unico blocco citato
  che comprende i due punti; nessuna riga a se';
- disposizioni della Fonte 29 incise o richiamate dal testo sostitutivo
  (allegato IV, sezione IV.3, punti 5 e 6 sostituiti; relazione sull'analisi
  dell'impatto di cui al punto 1 della stessa sezione; definizioni dell'art. 2):
  nessun nodo, appartengono alla Fonte 29 e sarebbero duplicati qui.

Rinvii e passaggi alla Fase 6 (nessuna relazione verso la Fonte 29 dichiarata in
questo modulo, come da perimetro):
- "allegato II, punto 5" -> Fonte 29 "allegato IV, sezione IV.3, punto 5":
  intervento "sostituisce" (sostituzione integrale del punto; la nuova versione
  elimina il rilascio del nuovo certificato previsto dalla versione sostituita).
  Il chapeau che ordina la sostituzione di entrambi i punti e' in testa al
  `testo_integrale` di questa riga: e' qui l'evidenza testuale di entrambi gli
  interventi;
- "allegato II, punto 6" -> Fonte 29 "allegato IV, sezione IV.3, punto 6":
  intervento "sostituisce" (la versione sostituita forniva all'ENISA il nuovo
  certificato comprensivo della relazione di manutenzione, non la sola
  relazione);
- "allegato II, punto 5" e "allegato II, punto 6" -> entrata in vigore dell'atto
  modificativo (art. 3, cap03 di questa Fonte): la sostituzione produce effetto
  dalla data di applicazione dell'atto;
- l'allegato II non cita alcun articolo o allegato con numero: nessun altro
  rinvio da costruire.

Copertura: 5 item di indice, 2 righe (2 Obblighi + 0 Principi), 1 relazione
interna ("allegato II, punto 6" richiama "allegato II, punto 5",
`evidence_type` "textual": "di cui al punto 5" e' citazione letterale verificata
nel `testo_integrale` del nodo citante).

Dubbi di classificazione rimasti aperti (dichiarati, non risolti in modo
univoco dal testo):
(1) Soggetto obbligato del punto 5: il capoverso e' impersonale e non nomina chi
redige la relazione di manutenzione. Qui "Terza parte" (l'organismo di
certificazione), per coerenza con la riga sostituita del cap11 di Fonte 29; la
lettura alternativa e' "Utente/titolare", perche' la relazione di manutenzione
e' un sottoinsieme della relazione sull'analisi dell'impatto, che il punto 1
della sezione IV.3 di Fonte 29 attribuisce al titolare del certificato. Nessuna
delle due letture e' esclusa dal testo.
(2) Gli stessi due punti potrebbero essere letti come norme del regolamento
modificato (Fonte 29) anziche' dell'atto modificativo: qui sono censiti nella
Fonte dell'atto che li dispone, come richiesto dal perimetro (e' lo stesso
dubbio dichiarato dal cap02 di questa Fonte per i paragrafi inseriti negli
artt. 48 e 49).
(3) Il punto 5 non e' scomposto nei suoi due capoversi (un solo nodo): se si
volesse l'unita' di copertura al comma, il primo capoverso (soppressione del
nuovo certificato + redazione della relazione) e il secondo (contenuto della
relazione) diventerebbero due righe. Qui e' stato mantenuto il punto come unita'
- come per il punto 5 della sezione IV.3 nel cap11 di Fonte 29, che accorpa
chapeau e lettere in una riga.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "allegato II, punto 5",
        "testo": "Qualora l'organismo di certificazione abbia confermato che le modifiche sono di minore entità, non è rilasciato alcun nuovo certificato per il prodotto TIC modificato ed è redatta una relazione di manutenzione in riferimento alla relazione di certificazione iniziale; la relazione di manutenzione è inclusa come sottoinsieme della relazione sull'analisi dell'impatto e contiene le sezioni seguenti: introduzione (a), descrizione delle modifiche (b), developer evidence interessata (c). Sostituisce il punto 5 della sezione IV.3 dell'allegato IV del regolamento di esecuzione (UE) 2024/482: nella versione sostituita era previsto il rilascio di un nuovo certificato.",
        "testo_integrale": "Nell'allegato IV del regolamento di esecuzione (UE) 2024/482, alla sezione IV.3 i punti 5 e 6 sono sostituiti dai seguenti:\n\n«5. Qualora l'organismo di certificazione abbia confermato che le modifiche sono di minore entità, non è rilasciato alcun nuovo certificato per il prodotto TIC modificato ed è redatta una relazione di manutenzione in riferimento alla relazione di certificazione iniziale.\n\nLa relazione di manutenzione è inclusa come sottoinsieme della relazione sull'analisi dell'impatto e contiene le sezioni seguenti:\n\na) introduzione;\n\nb) descrizione delle modifiche;\n\nc) developer evidence interessata;",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica qualora l'organismo di certificazione abbia confermato che le modifiche sono di minore entità.",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "allegato II, punto 6",
        "testo": "La relazione di manutenzione di cui al punto 5 è fornita all'ENISA per la pubblicazione sul sito web relativo alla certificazione della cibersicurezza. Sostituisce il punto 6 della sezione IV.3 dell'allegato IV del regolamento di esecuzione (UE) 2024/482: nella versione sostituita era fornito all'ENISA il nuovo certificato, comprensivo della relazione di manutenzione.",
        "testo_integrale": "6. La relazione di manutenzione di cui al punto 5 è fornita all'ENISA per la pubblicazione sul sito web relativo alla certificazione della cibersicurezza.».",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Si applica alla relazione di manutenzione di cui al punto 5 (modifiche confermate di minore entità dall'organismo di certificazione).",
        "soggetti": [
            {"categoria": "Terza parte", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "destinatario"},
        ],
    },
]

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = [
    "allegato II, punto 5",
    "allegato II, punto 5(a)",
    "allegato II, punto 5(b)",
    "allegato II, punto 5(c)",
    "allegato II, punto 6",
]

MAPPATURA_LOCALE = {
    "allegato II, punto 5": [
        "allegato II, punto 5",
        "allegato II, punto 5(a)",
        "allegato II, punto 5(b)",
        "allegato II, punto 5(c)",
    ],
    "allegato II, punto 6": [
        "allegato II, punto 6",
    ],
}

RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "allegato II, punto 6"),
        "nodo_a": ("obbligo", None, "allegato II, punto 5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
