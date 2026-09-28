"""ETSI TS 119 101 V1.1.1 (2016-03) - Electronic Signatures and
Infrastructures (ESI); Policy and security requirements for applications for
signature creation and signature validation.

Fonte: requisiti di politica e sicurezza per le APPLICAZIONI di creazione,
convalida e augmentation della firma (il software con cui l'utente firma,
verifica e mantiene valida la firma), non per il prestatore di servizi
fiduciari. Capitolo 3: clausola 8 (Signature creation, validation and
augmentation processing requirements), sottoclavole 8.1.1-8.1.13 (creazione),
8.2.1-8.2.6 (convalida), 8.3.1-8.3.6 (augmentation). Le sottoclavole 8, 8.1,
8.1.8, 8.2, 8.3 e 8.3.2 sono pure intestazioni di raggruppamento (solo
titolo, il contenuto vive interamente nelle sottoclavole): non generano nodo
ne' item di indice, come da criterio di copertura.

Testo ufficiale in app/.source_cache/etsi_119_101/cap03.txt (md5
d862d068c88be781bdb5e4f03f8957bb), estratto dal PDF con
pdftotext -layout. Manifest di split:
app/.source_cache/etsi_119_101/manifest.json. La numerazione degli id e'
risolta per riferimento dalla sessione principale in app/seed.py: questo
modulo non tocca seed.py.

Copertura (ADR-0007), criterio applicato voce per voce - GRANULARITA' AL
CONTROLLO, decisa dalla sessione principale (contatto 2026-09-28): la
clausola 8 e' strutturata in sottoclavole numerate (8.1.1, 8.1.2, ... 8.3.6)
che contengono ciascuna uno o piu' blocchi "Control objective" (dichiarativi)
e uno o piu' controlli dotati di id proprio. Come per ogni altra fonte ETSI
gia' censita in cui il documento assegna ai requisiti un'identita' propria
(EN 319 401 "REQ-...", EN 319 421 "OVR-/TIS-...", TS 119 431-1
"GEN-/LNK-/SIG-...", TS 119 431-2 "ASI-/OVR-..."), l'unita' di censimento e'
l'id del requisito e non la clausola contenitrice: gli id di questa fonte
(SCP 1-SCP 94 nella creazione, SVP 1-SVP 23 nella convalida, SAP 1-SAP 9
nell'augmentation) sono citati per id da nodi di altre fonti gia' nel grafo
(es. TS 119 431-2 ASI-8.1-09 richiama "SCP 13 and SCP 47", EN 319 411-2
OVR-8.2-04 richiama "SCP 14, SCP 31, SCP 37 and SCP 61"), quindi un nodo
puntuale per id e' l'unico che consente di agganciare la relazione alla
prescrizione citata. Il caso opposto (TS 119 312), dove la clausola era
l'unita' di censimento, non contraddice la regola: quel testo non assegna
alcun id ai propri requisiti, quindi l'identita' del nodo puo' essere solo il
numero di clausola.

- 126 controlli con id proprio (SCP 1-SCP 94, SVP 1-SVP 23, SAP 1-SAP 9) ->
  126 Obblighi, uno per id, `riferimento` = id esatto come appare nel testo
  (es. "SCP 13"). Sono inclusi i controlli espressi come facolta' ("may":
  es. SCP 36 sull'accesso in linea alle informazioni di revoca, SCP 41 sulla
  politica predefinita, SCP 70 sul contatore di ritentativi, SVP 11 sugli
  input ulteriori dell'utente; clausole subordinate con "may" compaiono anche
  in SCP 31, SCP 84 e SAP 7): il documento li elenca comunque fra i propri
  "Controls" numerati, quindi seguono lo stesso trattamento, come gia' fatto
  per i requisiti permissivi di TS 119 431-1 (LNK-6.2.2-04/-06).
- 43 blocchi "Control objective" -> 43 Principi "altro", riferimento
  "clausola X.Y (Titolo) - control objective N" con N progressivo
  nell'ordine del documento all'interno della sottoclavola. Non sono fusi nei
  controlli che introducono: sono enunciati dichiarativi con contenuto proprio
  (a 8.1.3, 8.1.4, 8.1.6, 8.1.8.1 e 8.1.8.2 ce ne sono rispettivamente 8, 6,
  3, 3 e 4, uno per ciascun gruppo di controlli) e ADR-0007 non ammette
  discriminanti di rilevanza. In `testo_integrale` il blocco e' preceduto
  dalla riga di intestazione "X.Y Titolo", per mantenere il contesto verbatim.
- 7 sottoclavole prive di controlli con contenuto proprio -> 7 Principi,
  riferimento "clausola X.Y (Titolo)": 8.1.1 (General) "scopo/ambito di
  applicazione"; 8.1.12 (SCDev/SCA interface (SSI) requirements) "altro" per
  il solo testo introduttivo (i quattro controlli SSI sono nodi Obbligo
  separati); 8.2.1 (Introduction) "altro"; 8.3.1 (Introduction) "altro";
  8.3.2.1, 8.3.2.2 e 8.3.2.3 (i tre casi d'uso dell'augmentation) "altro".

Totale: 176 item di indice (126 Obblighi + 50 Principi), mappatura 1:1.

Scelte di modellazione non ovvie:

- Intestazioni "Controls (Signature Creation Process)" / "Controls (Signature
  Validation Process)" / "Controls (Signature Augmentation Process)" e le due
  intestazioni "1. Inputs" / "2. Outputs" interne alla clausola 8.2.6: sono
  intestazioni di elenco prive di contenuto normativo proprio. Sono riportate
  in testa a `testo_integrale` del primo controllo del rispettivo gruppo (SCP
  1, SCP 3, SCP 5, SCP 10, SCP 15, SCP 18, SCP 19, SCP 23, SCP 27, SCP 31,
  SCP 37, SCP 38, SCP 43, SCP 46, SCP 49, SCP 54, SCP 55, SCP 57, SCP 60,
  SCP 67, SCP 71, SCP 74, SCP 75, SCP 77, SCP 78, SCP 79, SCP 82, SCP 86,
  SCP 87, SCP 88, SCP 92; SVP 1, SVP 3, SVP 8, SVP 10, SVP 12, SVP 14 - che
  porta anche "1. Inputs" - e SVP 20 con "2. Outputs"; SAP 1, SAP 3, SAP 6,
  SAP 8), senza creare nodi ne' item di indice separati - stessa convenzione
  gia' adottata per le frasi introduttive non numerate di EN 319 421.
  Attribuzione verificata meccanicamente sul testo: 42 controlli ricevono una
  o due intestazioni (43 segmenti di intestazione in totale). SCP 25 e SCP 40
  non ne ricevono alcuna perche' nel testo ufficiale i loro gruppi iniziano
  direttamente con il controllo, senza intestazione "Controls (...)".
- NOTE ed EXAMPLE: ogni NOTE/EXAMPLE e' riportata integralmente nel
  `testo_integrale` del blocco a cui il testo ufficiale la annette. Regola
  applicata: una NOTE/EXAMPLE che segue il testo di un obiettivo di controllo
  e precede l'intestazione "Controls (...)" appartiene al blocco obiettivo
  (8.1.3 obiettivo 6 con NOTE 4, 8.1.4 obiettivo 6 con NOTE 4, 8.1.11
  obiettivo 1 con la NOTE, 8.2.6 obiettivo 1 con NOTE 1); una NOTE/EXAMPLE che
  segue un controllo appartiene a quel controllo (SCP 1 con EXAMPLE, SCP 7 con
  NOTE 1, SCP 8 con NOTE 2, SCP 10 con NOTE 3, SCP 24 con NOTE 5, SCP 27 con
  NOTE 1, SCP 35 con NOTE 2, SCP 37 con NOTE 3, SCP 44 con NOTE 5, SCP 47 con
  la NOTE, SCP 51 con EXAMPLE 1, SCP 55 con EXAMPLE 2, SCP 59 con la NOTE, SCP
  64 con la NOTE, SCP 86 con l'EXAMPLE, SVP 1 con l'EXAMPLE, SVP 23 con NOTE
  2, SAP 1 con l'EXAMPLE). Le NOTE/EXAMPLE delle sottoclavole senza controlli
  restano nel nodo della sottoclavola (8.1.1 con NOTE 1-3; 8.3.1 con
  l'EXAMPLE dell'esito "augmentation unnecessary"; 8.3.2.1 con EXAMPLE 1 ed
  EXAMPLE 2). Conteggio verificato meccanicamente: 19 NOTE e 9 EXAMPLE nella
  clausola 8, tutte presenti nel modulo, nessuna omessa e nessuna duplicata.
- `condizione_applicabilita` non valorizzato in nessuna riga: diversamente dai
  requisiti marcati "[CONDITIONAL]" di TS 119 431-1/-2 ed EN 319 421, questo
  documento non usa marcature di condizionalita'; molte righe sono formulate in
  modo condizionale nel testo ("If biometric devices are used", "When bulk
  signing is supported", "If a signature creation policy is used"), ma la
  condizione resta dove il testo ufficiale la pone, cioe' nella prescrizione
  stessa - stesso criterio gia' adottato per TIS-7.6.3-04 di EN 319 421.
- `tipo_obbligo`, criterio di classificazione: "informativo/trasparenza" per i
  controlli che impongono contenuto di documentazione o informazione/avviso a
  una persona (firmatario, utente, verificatore, DA); "tecnico/sicurezza" per i
  controlli su proprieta' crittografiche e tecniche dell'applicazione (chiavi,
  certificati, percorsi fidati, integrita' di DTBS/DTBSR, algoritmi, hash e
  suite); "procedurale" per i controlli su passi, sequenze e regole di processo
  (convalida dell'input, ordine degli eventi, regole di convalida e di
  augmentation, verifica di conformita' fra documentazione e implementazione -
  es. SCP 2/SCP 4/SVP 2/SAP 2); "organizzativo" per la sola riga che demanda
  una scelta di assetto (SCP 41, politica di creazione della firma
  predefinita). Nessuna riga "di conservazione" ne' "sanzionatorio": la
  clausola 8 non impone obblighi di conservazione documentale ne' sanzioni (le
  prescrizioni di longevita' di SAP 6/SAP 7 sono requisiti tecnici di
  augmentation, non obblighi di conservazione di documenti o registrazioni).
- `soggetti`: la clausola 8 non disciplina il prestatore ma le applicazioni di
  firma; il ruolo di obbligato e' quindi assegnato a "QTSP/gestore" (il
  soggetto che implementa, fornisce o gestisce SCA/DA/SVA/SAA, il componente
  SSI, lo SCDev e l'interfaccia utente - figura indicata dal brief per i
  controlli tecnici di questa clausola). "Utente/titolare" compare come
  destinatario quando il controllo informa o avverte il firmatario, e come
  obbligato nelle due righe in cui il testo impone un comportamento al
  firmatario stesso (SCP 51, interazione non banale di invocazione, e SCP 54,
  nuova autenticazione presso lo SCDev dopo il tempo di inattivita'). Nella
  clausola 8.2 (convalida) il destinatario delle informazioni e' il soggetto
  che convalida, cioe' "Terzi affidanti/pubblico" (terzo affidante), mentre
  "Utente/titolare" resta riservato al firmatario nella creazione. "Terza
  parte" non ricorre: la clausola non attribuisce compiti a organismi di
  valutazione o autorita' esterne.
- Refusi del testo ufficiale riprodotti senza correzione: SCP 40 e' intestato
  alla "SVA o DA" pur trattando di politica di creazione della firma (contesto
  di creazione, dove gli attori sono SCA e DA); l'obiettivo di controllo della
  clausola 8.3.3 nomina la SVA pur trattando della SAA. In entrambi i casi il
  verbatim e' conservato e il refuso e' annotato in `testo`.
- Riferimenti esterni (ETSI TS 119 102, ETSI TS 119 312, ETSI EN 319 412-5,
  ETSI TS 119 172, CAdES/XAdES/PAdES/ASiC, RFC/ISO citati nelle NOTE) NON sono
  trasformati in relazioni: `RELAZIONI` e' vuota per mandato esplicito del
  task di capitolo, il cross-collegamento e' demandato alla sessione
  principale (ADR-0009, Fase 6).

Self-check: eseguito con `app/.venv/bin/python -c "import sys;
sys.path.insert(0,'app'); from seed_data.etsi_119_101 import cap03 as m; from
seed_data import lib; lib.verifica_copertura(m.INDICE_ARTICOLI_LOCALE,
m.MAPPATURA_LOCALE); lib.verifica_completezza_testo_integrale([m])"` -
176 item coperti, 126 obblighi, 50 principi.
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "SCP 1",
        "testo": "La documentazione della SCA deve indicare: a) tutti i formati di firma supportati (CAdES, XAdES, PAdES, ASiC) e i livelli di firma supportati; b) gli elementi e le funzionalita' opzionali supportati e come possono essere selezionati e controllati. Esempi di opzioni: firme detached/enveloped/enveloping, firme parallele o controfirme.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 1: The SCA documentation shall indicate:\n\na) All the signature formats (CAdES [i.10], XAdES [i.11], PAdES [i.12], ASiC [i.13]) and signature levels that are supported.\n\nb) Optional elements and features that are supported and how they can be selected and controlled.\n\nEXAMPLE: Examples for such optional elements and features are whether signatures can be detached/enveloped/enveloping signatures, parallel signatures or counter signatures.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 2",
        "testo": "La SCA deve essere controllata (verificata) in modo da supportare effettivamente le funzionalita' documentate in SCP 1.",
        "testo_integrale": "SCP 2: The SCA shall be controlled to support the functionalities, as documented in SCP 1.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 3",
        "testo": "La documentazione della SCA deve specificare i tipi di contenuto dei dati che la SCA supporta e che e' in grado di presentare correttamente.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 3: The SCA documentation shall specify the data content types the SCA supports and can present correctly.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 4",
        "testo": "La SCA deve essere controllata in modo da supportare i tipi di contenuto dei dati come documentato in SCP 3.",
        "testo_integrale": "SCP 4: The SCA shall be controlled to support the data content types as documented in SCP 3.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 5",
        "testo": "La SCA deve consentire l'inclusione del tipo di contenuto dei dati della SD (signer's document) o implicitamente nel documento o esplicitamente come attributo di firma esplicito.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 5: The SCA shall allow the inclusion of the SD data content type either implicitly in the document or explicitly as an explicit signature attribute.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 6",
        "testo": "Se nella firma e' incluso un tipo di contenuto della SD, la SCA deve essere in grado di fornirlo al firmatario.",
        "testo_integrale": "SCP 6: If a SD content type is included in the signature, the SCA shall be able to provide it to the signer.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 7",
        "testo": "L'interfaccia utente dovrebbe avvertire il firmatario se la SD non e' conforme alla sintassi specificata dal tipo di contenuto dichiarato e dovrebbe consentirgli di interrompere il processo di firma. Non e' definito un obbligo di interruzione automatica: la decisione dipende dal processo di business (NOTE 1).",
        "testo_integrale": "SCP 7: The user interface should warn the signer if the SD does not conform to the syntax specified by the data content type of the SD and should allow the signer to abort the signature process.\n\nNOTE 1: No requirement is defined to abort the signature process when the SD does not conform to the syntax as it depends on the business process who makes the decision of abortion.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 8",
        "testo": "L'interfaccia utente dovrebbe avvertire il firmatario contro la creazione di una firma su una SD che dichiari un tipo di contenuto che l'interfaccia stessa non e' in grado di presentare all'utente (NOTE 2: esistono processi di business in cui il firmatario non esamina la SD prima della firma, es. firma massiva di fatture).",
        "testo_integrale": "SCP 8: The user interface should warn the signer against creating a signature of any SD that indicates that it is of a data content type which cannot be presented to the user by the user interface.\n\nNOTE 2: There can be business processes in which the signer will not view the SD in details before the signature, e.g. in case of mass signing of invoices.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 9",
        "testo": "L'interfaccia utente dovrebbe avvertire il firmatario se non e' in grado di presentare accuratamente tutte le parti della SD secondo il tipo di contenuto dei dati.",
        "testo_integrale": "SCP 9: The user interface should warn the signer if it cannot accurately present all parts of the SD according to the data content type.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 10",
        "testo": "La SCA deve consentire al firmatario di identificare esattamente cio' che la firma coprira'. Rilevante soprattutto quando la firma copre solo una parte di un documento (NOTE 3).",
        "testo_integrale": "Controls\n\nSCP 10: The SCA shall allow the signer to identify exactly what the signature will cover.\n\nNOTE 3: This is especially relevant when the signature covers only part of a given document.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 11",
        "testo": "La DA (driving application) deve consentire al firmatario di selezionare la SD tra i documenti disponibili.",
        "testo_integrale": "SCP 11: The DA shall allow the signer to select the SD among available documents.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 12",
        "testo": "Se il processo prevede interazione umana, l'interfaccia utente dovrebbe presentare la SD al firmatario.",
        "testo_integrale": "SCP 12: In the case the process includes human interaction, the user interface should present the SD to the signer.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 13",
        "testo": "Quando la SD e' stata presentata al firmatario, la SCA deve garantire che la SD presentata sia la stessa che sara' firmata nel processo di firma.",
        "testo_integrale": "SCP 13: When the SD was presented to the signer, the SCA shall ensure that the SD presented to the signer is the same as the one that will be signed in the signature process.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 14",
        "testo": "La DA deve garantire che la SD selezionata dal firmatario per la firma sia la stessa fornita alla SCA per la firma.",
        "testo_integrale": "SCP 14: The DA shall ensure that the SD selected by the signer for signing is the same as the one provided to the SCA for the signature.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 15",
        "testo": "Se la SD da firmare contiene oggetti di dati firmati e se e' disponibile un'applicazione di convalida della firma (SVA), prima di creare la firma la DA o la SCA dovrebbe convalidare gli oggetti di dati firmati usando una SVA.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 15: If the SD to sign contains signed data objects and if a signature validation application is available, before creating the signature:\n\ni) the DA or the SCA should validate the signed data objects using a SVA.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 16",
        "testo": "Se la convalida degli oggetti di dati firmati e' stata effettuata: i) la DA o la SCA dovrebbe informare il firmatario di ogni politica di convalida usata dalla SVA; ii) la DA o la SCA deve informare l'utente dei risultati di convalida; iii) la DA o la SCA deve informare l'utente di quali firme sono state convalidate o lasciate non convalidate.",
        "testo_integrale": "SCP 16: If validation of the signed data objects was done:\n\ni) the DA or the SCA should inform the signer about each signature validation policy that has been used by the SVA to perform the validation;\n\nii) the DA or the SCA shall inform the user about validation results; and\n\niii) the DA or the SCA shall inform the user about which signatures have been validated or left invalidated.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 17",
        "testo": "Se la SD da firmare contiene oggetti di dati firmati e non e' disponibile o non viene usata alcuna SVA, la SCA dovrebbe informare il firmatario che nella SD sono incorporati altri oggetti di dati firmati e che dovrebbe convalidare esternamente la firma incorporata prima di firmare il documento.",
        "testo_integrale": "SCP 17: If the SD to sign contains signed data objects and if no SVA is available or used, the SCA should inform the signer that other signed data objects are embedded in the SD. and that he should validate the embedded signature externally before signing the document.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 18",
        "testo": "La SCA deve impedire al firmatario di modificare qualsiasi parte della SD durante il processo di presentazione.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 18: The SCA shall prevent the signer from changing any part of the SD during the presentation process.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 19",
        "testo": "La DA dovrebbe includere l'attributo del tipo di contenuto dei dati nella selezione degli attributi da firmare.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 19: The DA should include the data content type attribute in the selection of the attributes to be signed.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 20",
        "testo": "La SCA deve consentire l'inclusione di un attributo di tipo di contenuto dei dati nei DTBS, per rendere non ambiguo il tipo di dato della SD.",
        "testo_integrale": "SCP 20: The SCA shall allow inclusion of a data content type attribute in the DTBS to ensure that the data type of the SD is unambiguous.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 21",
        "testo": "Se la SD puo' essere ambigua per informazioni insufficienti a descriverne struttura e interpretazione della semantica, la DA dovrebbe includere l'attributo del tipo di contenuto dei dati nella selezione degli attributi da firmare, per garantire che sia possibile una sola interpretazione della semantica della SD.",
        "testo_integrale": "SCP 21: If the SD can be ambiguous due to insufficient information describing the structure and interpretation of its semantics, the DA should include the data content type attribute in the selection of attributes to be signed to ensure that only a single interpretation of the SD's semantics can be made.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 22",
        "testo": "Se la DA richiede l'inclusione del tipo di contenuto dei dati, la SCA deve codificare il tipo di dato del documento e deve proteggerlo con la firma.",
        "testo_integrale": "SCP 22: If the DA requests the inclusion of the data content type, the SCA shall encode the data type of the document and shall protect it by the signature.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 23",
        "testo": "Se il tipo di dato della SD e' suscettibile di ospitare malware o codice nascosto capace di alterare la presentazione della SD senza intaccare la firma, la DA o la SCA dovrebbero informare il firmatario di questa debolezza del tipo di dato.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 23: If the SD data type is susceptible to host malware or hidden code capable to alter the SD presentation without affecting the signature, the DA or the SCA should inform the signer of this data type weakness.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 24",
        "testo": "La DA o la SCA dovrebbero segnalare chiaramente al firmatario se i dati da firmare non possono essere presentati affatto o non possono esserlo in modo affidabile (NOTE 5: una via per evitare problemi di codice nascosto o malware e' la trasformazione del documento in un tipo che non presenta il problema).",
        "testo_integrale": "SCP 24: The DA or the SCA should clearly report to the signer if the data to be signed cannot be presented to the signer at all or cannot be presented in a reliable manner.\n\nNOTE 5: A possible way of avoiding any problems with hidden code or malware is the transformation of the document to a type not having this problem.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 25",
        "testo": "La SCA deve consentire al firmatario di essere informato sul contenuto che viene firmato.",
        "testo_integrale": "SCP 25: The SCA shall allow the signer to be informed about the content being signed.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 26",
        "testo": "La SCA deve consentire al firmatario di essere informato su qualsiasi tipo di impegno (commitment type) da usare nella firma.",
        "testo_integrale": "SCP 26: The SCA shall allow the signer to be informed about any commitment type to be used in the signature.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 27",
        "testo": "L'interfaccia utente deve consentire al firmatario di visualizzare gli attributi di firma; in particolare il firmatario deve poter controllare: a) il certificato del firmatario, con il distinguished name (DN) del soggetto e il DN dell'emittente; b) il tipo di contenuto dei dati della SD (se presente); c) la politica di firma (se presente); d) il tipo di impegno (se presente). NOTE 1: la politica di firma e' generalmente rappresentata negli attributi di firma tramite un identificatore di politica e il valore di hash della politica.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 27: The user interface shall allow the signer to view the signature attributes. In particular, the signer shall be able to check the content of the following:\n\na) the signer's certificate, in particular the distinguished name (DN) of the subject and the DN of the issuer;\n\nb) the SD data content type (if present);\n\nc) the signature policy (if present); and\n\nNOTE 1: The signature policy is generally represented in the signature attributes by means of a signature policy identifier and the hash value of the signature policy.\n\nd) the commitment type (if present).",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 28",
        "testo": "La SCA deve garantire che gli attributi di firma presentati al firmatario siano gli stessi che saranno firmati nel processo di firma.",
        "testo_integrale": "SCP 28: The SCA shall ensure that the signature attributes presented to the signer are the same as those that will be signed in the signature process.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 29",
        "testo": "La DA deve garantire che gli attributi di firma (se presenti) selezionati dal firmatario per la firma siano gli stessi che saranno dati alla SCA.",
        "testo_integrale": "SCP 29: The DA shall ensure that the signature attributes (if any) selected by the signer for signing are the same as those that will be given to the SCA.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 30",
        "testo": "L'interfaccia utente dovrebbe avvertire il firmatario se il tipo di attributo consente la presenza di testo nascosto, macro o codice attivo nell'attributo, o di elementi nascosti rilevati.",
        "testo_integrale": "SCP 30: The user interface should warn the signer if the attribute type allows the presence of any hidden text, macros or active code in the attribute, or of any detected hidden elements.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 31",
        "testo": "Quando al firmatario sono disponibili piu' certificati di firma, la DA deve consentirgli di selezionare il certificato da usare. La DA puo' fornire una selezione predefinita. Se c'e' una sola scelta possibile, questo passo puo' essere omesso.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 31: When more than one signing certificate is available to be used by the signer, the DA shall allow the signer to select the certificate to be used for creating the signature. The DA may provide a default selection for the user. If there is only a single choice possible, this step may be omitted.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 32",
        "testo": "La SCA deve ottenere dalla DA l'identificatore necessario per usare i dati di creazione della firma (SCD) associati al certificato selezionato per la firma.",
        "testo_integrale": "SCP 32: The SCA shall obtain the identifier from the DA needed to use the signature creation data associated with the selected certificate for signing.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 33",
        "testo": "L'interfaccia utente deve consentire al firmatario di ispezionare almeno i seguenti componenti dei certificati selezionati per l'inclusione nei DTBS: a) il distinguished name (DN) del soggetto; b) il numero seriale; c) il DN dell'emittente.",
        "testo_integrale": "SCP 33: The user interface shall allow the signer to inspect at least the following components of the certificates selected for inclusion in the DTBS:\n\na) the distinguished name (DN) of the subject;\n\nb) the serial number; and\n\nc) the DN of the issuer.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 34",
        "testo": "La SCA deve verificare il periodo di validita' del certificato di firma e, se l'ora corrente cade fuori da quel periodo, deve impedire al firmatario di usare i corrispondenti dati di creazione della firma (SCD).",
        "testo_integrale": "SCP 34: The SCA shall verify the signing certificate validity period, and if the current time is found outside that period, the SCA shall prevent the signer from using the corresponding signature creation data (SCD).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 35",
        "testo": "La SCA dovrebbe verificare il periodo di validita' dei certificati della catena dal certificato di firma fino alla trust anchor esclusa e, se il momento della firma cade fuori da quel periodo, dovrebbe impedire al firmatario di usare i dati di creazione della firma corrispondenti a quella catena (NOTE 2: per la fiducia diretta nella trust anchor non serve verificarne lo stato).",
        "testo_integrale": "SCP 35: The SCA should verify for the certificates in the certificate chain from the signing certificate up to, but not including, the trust anchor, the validity period, and if the time of signature is found outside that period, the SCA should prevent the signer from using the signature creation data corresponding to this chain.\n\nNOTE 2: Due to the direct trust in the trust anchor it is not needed to verify its status.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 36",
        "testo": "Se la SCA ha accesso (in linea) alle informazioni di revoca del certificato, puo' verificare lo stato di revoca dei certificati della catena dal certificato di firma fino alla trust anchor esclusa. Se il certificato di firma risulta revocato, deve impedire al firmatario di usare i corrispondenti dati di creazione della firma. Se risulta revocato un altro certificato della catena, deve avvertire l'utente e la SCA dovrebbe impedire al firmatario di usare gli SCD corrispondenti a quella catena.",
        "testo_integrale": "SCP 36: If the SCA has (on-line) access to the revocation information of the certificate, it may verify the revocation status information of the certificates in the certificate chain from the signing certificate up to, but not including, the trust anchor. If the signing certificate is found revoked, it shall prevent the signer from using the corresponding signature creation data. If another certificate of the chain is found revoked, it shall warn the user and the SCA should prevent the signer from using the SCD corresponding to this chain.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 37",
        "testo": "La SCA deve proteggere il riferimento al certificato di firma (o la sua copia) all'interno della firma da sostituzioni non rilevate dopo la creazione della firma (NOTE 3: tipicamente firmando questi dati insieme al documento e collocandoli, ad esempio, nella sezione degli attributi autenticati del formato di firma).",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 37: The SCA shall protect the reference to or copy of the signing certificate within the signature from undetected replacement after the signature has been created.\n\nNOTE 3: This typically is realized by signing this data along with the document and by putting it in e.g. the authenticated attributes section of the signature format.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 38",
        "testo": "La SCA deve garantire che l'impegno sia codificato in modo appropriato nella firma, se un impegno specifico e' stato selezionato dalla DA, dalla SCA o dall'utente.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 38: The SCA shall ensure that the commitment is appropriately encoded in the signature, if a specific commitment was selected by the DA, the SCA or the user.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 39",
        "testo": "Se un tipo di impegno (commitment type) sara' incluso nella firma, l'interfaccia utente deve presentarlo all'utente.",
        "testo_integrale": "SCP 39: If a commitment type will be included into the signature, the user interface shall present the commitment type to the user.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 40",
        "testo": "Quando sono disponibili piu' politiche di creazione della firma il firmatario puo' selezionare la politica tra quelle disponibili. In questo caso la SVA o la DA deve: a) fornire all'utente l'elenco delle possibili politiche di creazione della firma; b) informare l'utente del contenuto delle politiche; c) chiedere all'utente di sceglierne una.",
        "testo_integrale": "SCP 40: When more than one signature creation policy is available the signer may select the policy among available ones. In this case the SVA or DA shall:\n\na) provide to the user the list of possible signatures creation policies;\n\nb) inform the user of the content of the signatures creation policies; and\n\nc) request the user to select one.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 41",
        "testo": "Se l'utente non seleziona una politica specifica, o se non esiste una politica esplicita di creazione della firma, puo' essere applicata una politica di creazione della firma predefinita.",
        "testo_integrale": "SCP 41: If the user does not select a specific policy or if there is no explicit signature creation policy a default signature creation policy may be applied.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 42",
        "testo": "Il firmatario dovrebbe poter richiedere quale politica di firma e' stata applicata.",
        "testo_integrale": "SCP 42: The signer should be able to request the applied signature policy used.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 43",
        "testo": "Se una politica di firma esplicita e' necessaria per requisiti di business, legali o di policy, la DA deve fornire tale politica alla SCA.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 43: If an explicit signature policy is needed by business, legal or policy requirements, the DA shall provide such a signature policy to the SCA.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 44",
        "testo": "Se una politica di firma esplicita e' fornita dalla DA, la SCA deve includere nella firma un'identificazione non ambigua della politica esattamente fornita (NOTE 5: puo' essere fatto usando un hash della politica).",
        "testo_integrale": "SCP 44: If an explicit signature policy is provided by the DA, the SCA shall include an unambiguous identification of the exact provided policy within the signature.\n\nNOTE 5: This can be done using a hash of the policy.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 45",
        "testo": "Se il firmatario ha selezionato una politica di creazione della firma, la DA deve fornirla alla SCA senza alcuna modifica.",
        "testo_integrale": "SCP 45: If the signer selected a signature creation policy, the DA shall provide it to the SCA with no change.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 46",
        "testo": "La SCA deve calcolare la firma solo dopo che il firmatario ha dato il proprio consenso al calcolo della firma.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 46: The SCA shall compute the signature only after the signer has given its consent on calculating the signature.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 47",
        "testo": "Se il processo di business prevede la presentazione dei DTBS o della SD al firmatario, la SCA deve calcolare la firma solo dopo che i DTBS o la SD sono stati presentati (NOTE: nella firma massiva il firmatario puo' non ricevere la presentazione di tutti i DTBS/SD).",
        "testo_integrale": "SCP 47: If the business process contains the presentation of the DTBS or the SD to the signer, the SCA shall compute the signature only after the DTBS or SD was presented to the signer.\n\nNOTE: In the case of bulk signing the signer may not get all the DTBS/SD presented.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 48",
        "testo": "Se la politica di creazione della firma richiede una o piu' marche temporali, la SCA deve richiedere un token di marca temporale dopo la creazione della firma. Se il token non puo' essere acquisito entro il limite di tempo specificato dalla politica, il processo di creazione della firma deve essere interrotto.",
        "testo_integrale": "SCP 48: If the signature creation policy requires the use of one or more signature time-stamps, the SCA shall request a time-stamp token after the signature has been created. If a time-stamp token cannot be acquired within a time-limit specified by the policy the signature creation process shall be aborted.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 49",
        "testo": "L'interfaccia utente deve limitare l'invocazione accidentale del processo di firma da parte del firmatario.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 49: The user interface shall limit accidental invocation of the signature process by the signer.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 50",
        "testo": "La SCA deve garantire che la firma sia applicata con l'intenzione del firmatario.",
        "testo_integrale": "SCP 50: The SCA shall ensure that the signature is applied with the intent of the signer.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 51",
        "testo": "Se l'espressione di volonta' e' uno scopo della firma, prima di avviare il processo di firma l'interfaccia utente deve chiedere al firmatario di compiere un'interazione di invocazione della firma non banale, improbabile che avvenga accidentalmente (EXAMPLE 1: scorrere fino alla fine del documento da firmare prima di accettare la firma, non solo selezionare \"avanti\").",
        "testo_integrale": "SCP 51: If the expression of will is a goal of the signature, prior to initiation of the signature process, the user interface shall request the signer to perform a non-trivial signature invocation interaction with the SCA that is unlikely to occur accidentally.\n\nEXAMPLE 1: An example for a non-trivial action is scrolling down to the end of the document to be signed before accepting the signature, and not just selecting \"next\".",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 52",
        "testo": "L'interfaccia utente deve comunicare in modo chiaro che sta per essere creata una firma.",
        "testo_integrale": "SCP 52: The user interface shall convey clear information that a signature is going to be created.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 53",
        "testo": "L'interfaccia utente dovrebbe essere in grado di fornire consigli e informazioni su tutti gli aspetti della firma, ad esempio su processo e stato legale, se tali informazioni sono disponibili.",
        "testo_integrale": "SCP 53: The user interface should be able to provide advice and information on all aspects of the signature, e.g. on process and legal status, if such information is available.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 54",
        "testo": "Nella SCA deve essere definito un limite al tempo di inattivita' in cui la SCA non interagisce con il firmatario ne' sta elaborando. Se il limite decorre, il firmatario deve autenticarsi di nuovo presso lo SCDev.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 54: In the SCA, a limit shall be defined on the idle time the SCA neither interacts with the signer, nor is processing. If this time limit elapses, then the signer shall authenticate again to the SCDev.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 55",
        "testo": "L'interfaccia utente deve essere tanto lineare quanto l'applicazione puo' implementare, per evitare che il firmatario crei falle di sicurezza (EXAMPLE 2: se il dialogo non e' chiaro l'utente puo' inserire dati riservati in campi non protetti).",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 55: The user interface shall be as straightforward as the application can implement, to prevent the signer from creating security loopholes.\n\nEXAMPLE 2: If the dialog is not clear, the user can enter confidential data into fields which are not secured.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 56",
        "testo": "L'interfaccia utente deve essere ripulita dai dati riservati del firmatario dopo un limite di tempo sufficiente a compiere le operazioni normali. I campi in cui erano presentati i dati riservati devono essere sovrascritti con altri dati \"neutrali\", per evitare immagini residue.",
        "testo_integrale": "SCP 56: The user interface shall be cleared of signer's confidential data after a time limit sufficient to perform normal operations. The fields where the confidential data were presented shall be overridden by other \"neutral\" data, to prevent latent images.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 57",
        "testo": "Se la politica (implicita o esplicita) di creazione della firma richiede una specifica suite di creazione della firma, inclusa la lunghezza della chiave, la SCA deve usare l'algoritmo specificato.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 57: If the implicit or explicit signature creation policy requires a specific signature creation suite, including the key length, the SCA shall use the specified algorithm.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 58",
        "testo": "Se si usa una politica di creazione della firma, la SCA deve verificare che la politica indichi quali algoritmi crittografici possono essere usati. Se la politica non contiene tali informazioni, la SCA dovrebbe avvertire l'utente di questo fatto e di quale algoritmo viene usato.",
        "testo_integrale": "SCP 58: If a signature creation policy is used, the SCA shall check that the policy indicates which cryptographic algorithms can be used. If the policy does not contain such information, the SCA should warn the user of this fact and which algorithm is used.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 59",
        "testo": "Se non si usa alcuna politica di creazione della firma, o la politica non contiene requisiti sugli algoritmi crittografici, dovrebbero essere usati algoritmi e lunghezze di chiave corrispondenti a ETSI TS 119 312 (NOTE: informazioni sugli algoritmi idonei e sul tempo per cui sono considerati sicuri si trovano in ETSI TS 119 312).",
        "testo_integrale": "SCP 59: If no signature creation policy is used or the policy does not contain any requirements on the cryptographic algorithms, algorithms and key length corresponding to ETSI TS 119 312 [i.25] should be used.\n\nNOTE: Information on suitable algorithms and the time for which they are considered being secure can be found in ETSI TS 119 312 [i.25].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 60",
        "testo": "Per l'autenticazione del firmatario basata sulla conoscenza, i dati di autenticazione (es. PIN o password) dovrebbero resistere ad attacchi pratici di indovinamento e di forza bruta.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 60: For knowledge based signer authentication, the authentication data (e.g. PIN or password) should withstand practical guessing and brute force attacks.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 61",
        "testo": "Quando i dati di autenticazione del firmatario transitano attraverso la SCA, la SCA deve mantenerne riservatezza e integrita' e deve cancellarli in modo sicuro non appena non sono piu' necessari (es. quando vengono sostituiti o l'enrolment del firmatario e' rimosso).",
        "testo_integrale": "SCP 61: When the signer's authentication data transits through the SCA, the SCA shall maintain the confidentiality and integrity of the authentication data and shall securely erase it as soon as it is no longer needed (e.g. they are substituted or the signer's enrolment is removed).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 62",
        "testo": "Se i dati di autenticazione (come PIN o PW) sono inviati da un dispositivo di input esterno (come un PIN pad o una tastiera), la trasmissione tra il dispositivo di input e lo SCDev deve avvenire su un percorso fidato (trusted path).",
        "testo_integrale": "SCP 62: Where authentication data (like a PIN or a PW) is sent from an external input device (like a PIN pad or a keyboard), then the data transmission between the input device and the SCDev shall be done over a trusted path.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 63",
        "testo": "Se lo SCDev lo consente, dovrebbe essere fornita una funzione per cambiare in modo sicuro i dati di autenticazione del firmatario basati sulla conoscenza.",
        "testo_integrale": "SCP 63: If allowed by the SCDev, a function for securely changing knowledge based signer authentication data should be provided.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 64",
        "testo": "Nell'inserimento di dati di autenticazione basati sulla conoscenza (PW o PIN) il riscontro (feedback) non deve rivelarne il valore. Puo' essere dato il riscontro di una cifra o carattere digitato tramite un simbolo appropriato che non riveli piu' di una cifra o carattere alla volta e solo per un breve periodo; il riscontro dovrebbe non rivelare affatto cifra o carattere (NOTE: la mascheratura non serve per l'inserimento di un OTP, usato una sola volta).",
        "testo_integrale": "SCP 64: When entering knowledge based authentication data, like a PW or a PIN, the feedback shall not reveal its value. This may be done by providing the feedback of a typed digit or character to the signer by an appropriate symbol or method that does not reveal more than one digit or character at a time and only during a short period of time. This should be done by a feedback that does not reveal the digit or character at all.\n\nNOTE: This masking is not needed for entering an OTP, since it is used only once.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 65",
        "testo": "Ne' la SCA ne' il componente di autenticazione del firmatario devono impedire la gestione del PIN/PW da parte dello SCDev; devono quindi: a) gestire PIN/PW della lunghezza massima consentita dallo SCDev; b) non impedire ai firmatari di modificare a piacimento il proprio PIN/PW.",
        "testo_integrale": "SCP 65: Neither the SCA nor the signer's authentication component shall prevent the management of PIN/PW by the SCDev. Therefore they shall:\n\na) handle PIN/PW of the maximum length allowed for by the SCDev; and\n\nb) not prevent signers to modify their own PIN/PW at will.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 66",
        "testo": "Nel cambio del PIN/PW la SCA deve richiedere la presentazione due volte del nuovo PIN/PW e verificare che le due presentazioni siano identiche prima di consegnare il nuovo PIN/PW allo SCDev. Quando possibile la SCA dovrebbe evitare che l'utente riutilizzi gli ultimi PW o PIN usati.",
        "testo_integrale": "SCP 66: When changing the PIN/PW, the SCA shall require the presentation of a new PIN/PW twice and check whether both presentations are identical before delivering the new PIN/PW to the SCDev. When possible, the SCA should avoid that the user reuses the last used PWs or PINs.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 67",
        "testo": "Lo SCDev deve essere configurato con un numero massimo di dati di autenticazione errati consecutivi consentiti.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 67: The SCDev shall be configured with a maximum number of allowed consecutive wrong signer's authentication data.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 68",
        "testo": "Quando il firmatario fornisce dati di autenticazione errati e il massimo definito in SCP 67 non e' raggiunto, deve essere fornita una risposta di errore al firmatario e gli si dovrebbe consentire un nuovo tentativo. Non deve essere fornita all'utente alcuna informazione sul tipo di errore.",
        "testo_integrale": "SCP 68: When the signer provides the wrong signer's authentication data and the maximum as defined in SCP 67 is not reached, an error response shall be provided to the signer and the signer should be allowed to make a new try. No information on the type of mistake shall be provided to the user.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 69",
        "testo": "Quando il firmatario fornisce dati di autenticazione errati e si raggiunge il numero massimo di dati errati consecutivi definito in SCP 67, lo SCDev deve bloccare il metodo di autenticazione del firmatario e deve informarlo.",
        "testo_integrale": "SCP 69: When the signer provides the wrong signer's authentication data and the maximal number of consecutive wrong signer's authentication data, as defined in SCP 67, is reached, the SCDev shall block the signer's authentication method and shall inform the signer.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 70",
        "testo": "Il numero di confronti non riusciti con i dati di autenticazione del firmatario deve essere registrato con un contatore di ritentativi. Lo SCDev puo' anche fornire un mezzo per riportare il contatore al valore iniziale (es. presentando un codice di reset, detto anche Personal Unblocking Key, PUK).",
        "testo_integrale": "SCP 70: The number of unsuccessful comparisons with the signer's authentication data shall be recorded with a retry counter. The SCDev may also provide a means for resetting the retry counter to its initial value (e.g. by presenting a reset code, also referred as Personal Unblocking Key (PUK)).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 71",
        "testo": "L'utente dovrebbe essere informato dalla documentazione dei passi da compiere per mantenere sicuri i dati di autenticazione del firmatario, garantendo tra l'altro che l'utente non sia osservabile da persone o telecamere.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 71: The user should be informed by the documentation of steps to be taken to keep the signer's authentication data secure, including ensuring that the user is not overlooked by persons or cameras.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 72",
        "testo": "Non deve essere possibile copiare i dati di autenticazione del firmatario dall'input della SCA.",
        "testo_integrale": "SCP 72: It shall not be possible to copy the signer's authentication data from the input of the SCA.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 73",
        "testo": "Se l'applicazione e' usata in un'area pubblica, la tastiera usata per inserire le informazioni nella SCA deve: a) essere protetta da spionaggio e da sguardi indiscreti (over the shoulder peering); b) non emettere suoni di digitazione diversi per ciascun tasto.",
        "testo_integrale": "SCP 73: In the case where the application is used in a public area, the keyboard used to key in the information into the SCA, shall:\n\na) be protected from spying and over the shoulder peering, and\n\nb) not emit keying sounds different for each key.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 74",
        "testo": "Se si usano dispositivi biometrici, devono essere predisposti requisiti ambientali idonei a prevenire attacchi ai dispositivi biometrici, come la presentazione di elementi biometrici \"falsi\" (dita di silicone, uso di immagini residue, ecc.).",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 74: Environment requirements suitable to prevent attacks to biometric devices, such as submission of \"fake\" biometric elements (silicon fingers, usage of latent images, etc.) shall be in place, if biometric devices are used.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 75",
        "testo": "Se si usano dispositivi biometrici, deve essere fornito un percorso fidato che assicuri integrita', autenticita' e riservatezza per la trasmissione dei dati biometrici tra l'unita' sensore biometrica e lo SCDev.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 75: If biometric devices are used, a trusted path, providing integrity, authenticity and confidentiality, shall be provided for the transmission of biometric data between the biometric sensor unit and the SCDev.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 76",
        "testo": "Se si usano dispositivi biometrici, i sensori biometrici devono proteggere i dati di identificazione biometrica dell'utente dall'essere usati in attacchi di replay.",
        "testo_integrale": "SCP 76: If biometric devices are used, biometric sensors shall protect the user's biometric identification data from being used in replay attacks.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 77",
        "testo": "Se si usano dispositivi biometrici, l'associazione dei dati biometrici all'utente non dovrebbe avvenire al di fuori di un percorso fidato o dello SCDev.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 77: If biometric devices are used, biometric data association to the user should not occur outside a trusted path or the SCDev.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 78",
        "testo": "Se si usano dispositivi biometrici, la comparazione (matching) dei dati biometrici non dovrebbe avvenire all'interno della SCA.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 78: If biometric devices are used, matching of biometric data should not occur inside the SCA.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 79",
        "testo": "La SCA deve verificare validita', autenticita' e completezza di tutti i componenti ottenuti per produrre il corretto formato DTBS selezionato dal firmatario.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 79: The SCA shall verify the validity, authenticity and completeness of all the components obtained in order to produce the correct DTBS format selected by the signer.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 80",
        "testo": "La SCA dovrebbe usare solo funzioni di hash specificate in ETSI TS 119 312.",
        "testo_integrale": "SCP 80: The SCA should use only hash algorithms specified in ETSI TS 119 312 [i.25].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 81",
        "testo": "La SCA dovrebbe usare solo suite di firma specificate in ETSI TS 119 312.",
        "testo_integrale": "SCP 81: The SCA should use only signature suites specified in ETSI TS 119 312 [i.25].",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 82",
        "testo": "La SCA deve selezionare gli attributi di firma secondo le regole applicabili o la politica di creazione della firma implicita o esplicita selezionata.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 82: The SCA shall select the signature attributes according to the applicable rules or selected implicit or explicit signature creation policy.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 83",
        "testo": "La SCA deve produrre la corretta rappresentazione dei dati da firmare (DTBSR) per una firma.",
        "testo_integrale": "SCP 83: The SCA shall produce the correct data to be signed representation (DTBSR) for a signature.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 84",
        "testo": "La SCA deve calcolare la DTBSR secondo le regole applicabili o la politica di creazione della firma selezionata, tramite formattazione, codifica e hashing dei DTBS. L'hashing puo' essere eseguito nello SCDev; la formattazione e la codifica devono essere sempre eseguite dalla SCA.",
        "testo_integrale": "SCP 84: The SCA shall compute the DTBSR according to the applicable rules or selected implicit or explicit signature creation policy, by formatting, encoding and hashing of the DTBS. The hashing may be done in the SCDev, the formatting and encoding shall always done by the SCA.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 85",
        "testo": "La SCA deve mantenere l'integrita' dei DTBS nel calcolo della DTBSR.",
        "testo_integrale": "SCP 85: The SCA shall maintain the integrity of the DTBS when computing the DTBSR.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 86",
        "testo": "Se la politica (implicita o esplicita) di creazione della firma richiede un tipo specifico di dispositivo di creazione della firma e questo tipo puo' essere verificato automaticamente, la SCA deve verificare che il dispositivo corrisponda ai requisiti dati (EXAMPLE: se la politica richiede un dispositivo qualificato di creazione della firma, la SCA puo' verificare il relativo QCStatement (ETSI EN 319 412-5) nel certificato del firmatario).",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 86: If the implicit or explicit signature creation policy requires a specific type of signature creation device, and this type can be checked automatically, the SCA shall check that the signature creation device corresponds to the given requirements.\n\nEXAMPLE: If a qualified signature creation device is required by the signature creation policy, the SCA can check the related QCStatement (ETSI EN 319 412-5 [i.26]) within the signer certificate.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 87",
        "testo": "Se la documentazione dello SCDev contiene una guida operativa o informazioni equivalenti sull'uso del dispositivo, l'utilizzo dello SCDev deve tenere conto di ogni indicazione applicabile.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 87: If the documentation of the SCDev contains an operational guide or equivalent information on how to use the device, the usage of the SCDev shall take into account any applicable guidance.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 88",
        "testo": "Il componente SSI (interfaccia SCDev/SCA) deve impedire che i dati comunicati sull'interfaccia siano osservati o modificati.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 88: The SSI component shall prevent data communicated over the interface to be observed or changed.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 89",
        "testo": "Per i tipi di SCDev che il componente SSI dichiara di supportare, il componente SSI deve supportare tutti gli elementi rilevanti dell'interfaccia fisica nel campo specificato o con le caratteristiche specificate, per garantire il corretto funzionamento.",
        "testo_integrale": "SCP 89: For the types of SCDev that the SSI component claims to support, the SSI component shall support all items relevant to the physical interface in the specified range or with its specified characteristics to ensure proper operation.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 90",
        "testo": "Il componente SSI deve selezionare la corretta funzionalita' dello SCDev, se la piattaforma su cui e' implementata la funzionalita' dello SCDev richiede una selezione.",
        "testo_integrale": "SCP 90: The SSI component shall select the correct SCDev functionality, if the platform, on which the SCDev functionality is implemented requires a selection.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 91",
        "testo": "Il componente SSI deve selezionare il certificato di firma e poi i relativi dati di creazione della firma.",
        "testo_integrale": "SCP 91: The SSI component shall select the signing certificate and then the related signature creation data.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 92",
        "testo": "Quando la firma massiva e' supportata, la SCA deve consentire al firmatario di visualizzare individualmente ogni SD che fa parte del processo di firma massiva.",
        "testo_integrale": "Controls (Signature Creation Process)\n\nSCP 92: When bulk signing is supported, the SCA shall allow the signer to individually display any SD that is part of the bulk signature process.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Utente/titolare",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SCP 93",
        "testo": "Quando la firma massiva e' supportata, la SCA deve garantire che un documento non selezionato dal firmatario non possa entrare a far parte del processo di firma massiva.",
        "testo_integrale": "SCP 93: When bulk signing is supported, the SCA shall ensure that a document that was not selected by the signer cannot be part of the bulk signature process.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SCP 94",
        "testo": "Quando la firma massiva e' supportata, la SCA dovrebbe fornire un rapporto del processo di firma massiva che includa l'elenco di ogni SD inclusa nella firma massiva.",
        "testo_integrale": "SCP 94: When bulk signing is supported, the SCA should provide a report of a bulk signature process including a list of every SD included in the bulk signing.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 1",
        "testo": "La documentazione della SVA deve contenere una descrizione: a) dei formati di firma/contenitore supportati (es. CAdES, XAdES, PAdES, ASiC, ecc.); b) dei livelli di firma/contenitore supportati per la convalida come specificato in CAdES, XAdES, PAdES e ASiC; c) di ogni restrizione specifica sulle firme/contenitori supportati (EXAMPLE: sono supportate solo firme attached, oppure non sono supportate firme contenenti elementi di versioni precedenti di uno standard).",
        "testo_integrale": "Controls (Signature Validation Process)\n\nSVP 1: The SVA documentation shall contain a description of:\n\na) the supported signature/container formats (e.g. CAdES [i.10], XAdES [i.11], PAdES [i.12], ASiC [i.13], etc.);\n\nb) the supported signature/container levels for validation as specified in CAdES [i.10], XAdES [i.11], PAdES [i.12], and ASiC [i.13]); and\n\nc) any specific restrictions on the supported signatures/containers.\n\nEXAMPLE: Examples for such restrictions might be that only attached signatures are supported, or that signatures containing elements from older version of a standard are not supported.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 2",
        "testo": "La SVA deve essere controllata in modo da supportare le funzionalita' come documentato in SVP 1.",
        "testo_integrale": "SVP 2: The SVA shall be controlled to support the functionalities, as documented in SVP 1.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 3",
        "testo": "Le regole di processo devono essere descritte nella documentazione della SVA (almeno per riferimento a un documento pertinente); devono definire una procedura per convalidare le firme. Tale procedura di convalida dovrebbe considerare la convalida delle firme \"vecchie\", in cui i certificati possono essere scaduti o revocati o in cui il periodo di uso degli algoritmi crittografici puo' essere stato superato.",
        "testo_integrale": "Controls (Signature Validation Process)\n\nSVP 3: Process rules shall be described in the SVA documentation (at least by reference to a relevant document). They shall define a procedure to validate signatures. This validation procedure should consider the validation of \"old\" signatures, where certificates may have expired or may have been revoked or even where the usage period of cryptographic algorithms may have been exceeded.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 4",
        "testo": "Dovrebbe essere usata la procedura di convalida descritta in ETSI TS 119 102, o procedure che forniscono gli stessi risultati.",
        "testo_integrale": "SVP 4: The validation procedure described in ETSI TS 119 102 [i.8] or procedures providing the same results should be used.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 5",
        "testo": "L'implementazione della SVA deve essere controllata rispetto alle procedure di convalida della firma definite secondo SVP 3.",
        "testo_integrale": "SVP 5: SVA implementation shall be controlled against the signature validation procedures defined as per SVP 3.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 6",
        "testo": "Quando la politica di convalida della firma e/o alcuni vincoli aggiuntivi della DA impongono che specifici elementi all'interno della firma siano presenti e firmati (es. un tipo di impegno), la SVA deve verificare che tali elementi siano effettivamente presenti e firmati.",
        "testo_integrale": "SVP 6: When the signature validation policy and/or some additional constraints of the DA mandate that some specific elements within the signature need to be present and signed, e.g. a commitment type, then the SVA shall verify that these elements are indeed present and signed.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 7",
        "testo": "La documentazione della SVA deve contenere quale politica di convalida della firma e' usata per impostazione predefinita, se ve n'e' una, e quali costanti di convalida possono essere configurate e come.",
        "testo_integrale": "SVP 7: The SVA documentation shall contain which signature validation policy is used by default, if there is any, and which validation constants can be configured and how.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 8",
        "testo": "Se la firma contiene un OID di politica diverso dalla politica usata dalla convalida, la SVA deve fornire questa informazione alla DA.",
        "testo_integrale": "Controls (Signature Validation Process)\n\nSVP 8: If the signature contains a policy OID which is different from the policy used by the validation, then the SVA shall provide this information to the DA.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 9",
        "testo": "Se la firma contiene un OID di politica diverso dalla politica usata dalla convalida, l'utente dovrebbe essere informato.",
        "testo_integrale": "SVP 9: If the signature contains a policy OID which is different from the policy used by the validation, then the user should be informed.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Terzi affidanti/pubblico",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SVP 10",
        "testo": "Secondo i requisiti legali e di business, la SVA deve consentire alla DA o all'utente di selezionare: a) l'SDO da verificare e la SD da verificare se non e' inclusa nell'SDO; b) se gli attributi dell'SDO non contengono i certificati necessari, i certificati da usare per la convalida; c) se l'SDO contiene piu' firme, la specifica firma da verificare; d) la politica di convalida implicita o esplicita da usare tra quelle disponibili.",
        "testo_integrale": "Controls (Signature Validation Process)\n\nSVP 10: According to the legal and business requirements, the SVA shall allow the DA or the user to select\n\na) the SDO to verify and the SD to verify if it is not included in the SDO;\n\nb) if the attributes of the SDO do not contain the certificate(s) needed, the certificate(s) to be used for the validation;\n\nc) if the SDO contains multiple signatures, the specific signature to be verified; and\n\nd) the implicit or explicit signature validation policy to be used amongst the available ones.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Terzi affidanti/pubblico",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SVP 11",
        "testo": "La SVA puo' consentire all'utente di fornire ulteriori input per il processo di convalida (elementi per parametrizzare la politica di convalida, come il termine di conservazione o una trust anchor). Questa opzione dovrebbe essere proposta solo in contesti di business in cui l'utente ha qualche nozione delle politiche di convalida.",
        "testo_integrale": "SVP 11: The SVA may allow the user to provide further inputs for the validation process (i.e. elements to parameterize the validation policy such as the term of preservation, a trust anchor, etc.). This latter option should only be proposed in business contexts where the user has some notions of validation policies.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Terzi affidanti/pubblico",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SVP 12",
        "testo": "L'interfaccia utente deve essere in grado di presentare, su richiesta dell'utente, una sintesi del risultato di convalida in forma leggibile e deve poter fornire un rapporto di convalida come da SVP 22.",
        "testo_integrale": "Controls (Signature Validation Process)\n\nSVP 12: The user interface shall be able to present, upon request from the user, a summary of the validation result to the user in a human readable form and shall be able to provide a validation report as per SVP 22.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Terzi affidanti/pubblico",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SVP 13",
        "testo": "L'interfaccia utente deve poter presentare l'identita' presunta del firmatario, incluse: a) il distinguished name del soggetto del certificato del firmatario; b) il distinguished name della CA emittente; c) il distinguished name delle CA gerarchicamente superiori fino a una radice accettabile per la politica di convalida della firma.",
        "testo_integrale": "SVP 13: The user interface shall be able to present the purported signer's identity, including:\n\na) the signer's certificate subject's distinguished name;\n\nb) the distinguished name of the issuing CA; and\n\nc) the distinguished name of the hierarchically superior CAs up to a root that is acceptable for the signature validation policy.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Terzi affidanti/pubblico",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SVP 14",
        "testo": "La DA deve fornire la firma alla SVA.",
        "testo_integrale": "Controls (Signature Validation Process)\n\n1. Inputs\n\nSVP 14: The DA shall provide the signature to the SVA.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 15",
        "testo": "Se la firma non contiene il documento firmato, la DA deve fornire il documento firmato alla SVA.",
        "testo_integrale": "SVP 15: If the signature does not contain the signed document, the DA shall provide the signed document to the SVA.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 16",
        "testo": "La DA deve fornire alla SVA la politica di convalida della firma da usare nel processo di convalida.",
        "testo_integrale": "SVP 16: The DA shall provide to the SVA the signature validation policy to be used in the validation process.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 17",
        "testo": "La SVA deve usare nel processo di convalida ogni regola applicabile definita nella politica di convalida della firma.",
        "testo_integrale": "SVP 17: The SVA shall use in the signature validation process any applicable rules defined in the signature validation policy.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 18",
        "testo": "La DA o la SVA devono recuperare i dati di convalida necessari usando sia le regole definite nella politica di convalida sia i puntatori presenti nei dati di convalida gia' recuperati.",
        "testo_integrale": "SVP 18: The DA or the SVA shall fetch the validation data as necessary using both the rules defined in the signature validation policy in the validation process and the pointers present in already fetched validation data.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 19",
        "testo": "La SVA deve avere a disposizione una sorgente temporale di riferimento.",
        "testo_integrale": "SVP 19: The SVA shall have a reference time-source available.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 20",
        "testo": "La SVA deve fornire alla DA: il risultato principale di convalida (valido, invalido, indeterminato), il momento della convalida e, se richiesto, un rapporto di convalida.",
        "testo_integrale": "2. Outputs\n\nSVP 20: The SVA shall provide to the DA: the main validation result (valid, invalid, indeterminate), the time of validation and if requested a validation report.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 21",
        "testo": "La SVA deve fornire ulteriori informazioni sugli elementi della convalida che superano o non superano i controlli e informazioni aggiuntive relative alla convalida della firma (certificati, informazioni di revoca e marche temporali).",
        "testo_integrale": "SVP 21: The SVA shall provide further information about the elements of signature validation that pass or fail and additional information relating to the signature validation (certificates, revocation information, and time- stamps).",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SVP 22",
        "testo": "L'interfaccia utente deve poter presentare al verificatore i risultati principali di convalida.",
        "testo_integrale": "SVP 22: The user interface shall be able to present to the verifier the main validation results.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Terzi affidanti/pubblico",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SVP 23",
        "testo": "L'interfaccia utente deve consentire all'utente di apprendere: a) la politica di firma usata nella convalida; b) quando si usa una politica esplicita, il contenuto o il riferimento a tale politica; c) il nome del firmatario; d) ogni impegno noto implicato dalla firma. NOTE 2: la convalida usa sempre una politica di firma, anche se non e' specificata esplicitamente da un identificatore; esempio di politica implicita e' la legge applicabile.",
        "testo_integrale": "SVP 23: The user interface shall allow the user to learn:\n\na) the signature policy used in the signature validation;\n\nNOTE 2: The validation always uses a signature policy, even if it is not explicitly specified by a signature policy identifier. An example of implicit signature policy is the applicable law.\n\nb) when an explicit signature policy is used, the content or reference to this signature policy;\n\nc) the name of the signer; and\n\nd) any known commitment implied by the signature.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            },
            {
                "categoria": "Terzi affidanti/pubblico",
                "ruolo": "destinatario"
            }
        ]
    },
    {
        "riferimento": "SAP 1",
        "testo": "La documentazione della SAA deve indicare: a) tutti i livelli di firma/contenitore supportati ai quali puo' portare in augmentation la firma/contenitore; b) ogni restrizione che si applica all'augmentation (EXAMPLE: restrizioni su algoritmi di hash supportati, o se e' supportata l'augmentation di firme detached o parallele).",
        "testo_integrale": "Controls (Signature Augmentation Process)\n\nSAP 1: The SAA documentation shall indicate:\n\na) all supported signature/container levels to which it can augment the signature/container; and\n\nb) any restrictions that apply on the augmentation.\n\nEXAMPLE: Examples for such restrictions are supported hash algorithms, or if augmentation of detached, or parallel signatures are supported.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SAP 2",
        "testo": "La SAA deve essere controllata in modo da supportare le funzionalita' come documentato in SAP 1.",
        "testo_integrale": "SAP 2: The SAA shall be controlled to support the functionalities, as documented in SAP 1.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SAP 3",
        "testo": "Le procedure di augmentation della firma implementate devono essere descritte nella documentazione della SAA (almeno per riferimento a un documento pertinente).",
        "testo_integrale": "Controls (Signature Augmentation Process)\n\nSAP 3: The implemented signature augmentation procedures shall be described in the SAA documentation (at least by reference to a relevant document).",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SAP 4",
        "testo": "Dovrebbero essere usate le procedure di augmentation descritte in ETSI TS 119 102.",
        "testo_integrale": "SAP 4: The augmentation procedures described in ETSI TS 119 102 [i.8] should be used.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SAP 5",
        "testo": "L'implementazione della SAA deve essere controllata rispetto alle procedure di augmentation della firma definite secondo SAP 3.",
        "testo_integrale": "SAP 5: SAA implementation shall be controlled against the signature augmentation procedures defined as per SAP 3.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SAP 6",
        "testo": "Se il momento di creazione della firma e' richiesto dal livello scelto per l'augmentation, la SAA deve acquisire un'asserzione temporale (es. marca temporale, time mark o evidence record) il prima possibile dopo l'avvio del processo di augmentation, per fornire un punto nel tempo utilizzabile per confrontare le date di possibili eventi (es. compromissione della chiave, revoca, scadenza).",
        "testo_integrale": "Controls (Signature Augmentation Process)\n\nSAP 6: If the signature creation time is required by the chosen level to which the signature is augmented, then the SAA shall capture a time assertion (e.g. time-stamp, time mark or evidence record) as soon as possible after starting the augmentation process to provide a point of time that can be used to compare with the dates of possible events (e.g. key compromise, revocation, expiry).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SAP 7",
        "testo": "Se richiesto dal livello di firma scelto per l'augmentation, le informazioni sui certificati e sul loro stato di revoca per l'intero percorso di certificazione, dal certificato del firmatario fino al certificato di una CA fidata, devono essere incluse dalla SAA nella firma e, quando rilevante, protette da un tempo fidato. Quando la verifica del percorso di certificazione non e' possibile, la SAA puo' proseguire con la verifica crittografica della firma e includere questa informazione nel risultato consegnato alla DA.",
        "testo_integrale": "SAP 7: If required by the chosen signature level to which the signature is augmented, information on certificates and their revocation status for the whole certificate path from the signer's certificate up to a trusted CA's certificate, shall be included by the SAA in the signature and, when relevant, protected by a trusted time. When the verification of the certificate path is not possible, the SAA may continue with the cryptographic signature verification and include this information in the result delivered to the DA.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SAP 8",
        "testo": "Se richiesto dalla politica di augmentation della firma, la firma di input deve essere convalidata.",
        "testo_integrale": "Controls (Signature Augmentation Process)\n\nSAP 8: If required by the signature augmentation policy, the input signature shall be validated.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    },
    {
        "riferimento": "SAP 9",
        "testo": "Se la firma e' stata convalidata, il rapporto di augmentation deve includere il risultato della convalida.",
        "testo_integrale": "SAP 9: If the signatures was validated, the augmentation report shall include the validation result.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {
                "categoria": "QTSP/gestore",
                "ruolo": "obbligato"
            }
        ]
    }
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "clausola 8.1.1 (General)",
        "testo": "Introduzione della clausola 8.1: specifica requisiti e raccomandazioni di sicurezza propri della creazione della firma e contiene requisiti per la SCA, la DA e l'interfaccia utente; si basa su definizioni, modelli e introduzione tecnica di ETSI TS 119 102. NOTE 1: a differenza del modello di ETSI TS 119 102, la SVA descritta in questa clausola copre solo la fornitura dei dati minimi necessari alla SVA per convalidare la firma; il processo di augmentation e' trattato nella clausola 8.3. NOTE 2: una politica di creazione della firma puo' specificare requisiti sul processo di firma (applicazione delle firme a documenti e dati in un particolare contesto, dominio di business o applicazione, comunita'), perche' tali firme siano considerate valide; la specificazione di una politica di creazione della firma e' fuori perimetro di questo documento (vedi ETSI TS 119 172). NOTE 3: il controllo esclusivo (sole control) sulla chiave di firma non e' coperto da uno specifico obiettivo di controllo ma da una combinazione di controlli individuali all'interno della clausola 8.1.",
        "testo_integrale": "8.1.1 General\n\nThis clause specifies security requirements and recommendations specific to the signature creation. It contains\n\nrequirements for the SCA, the DA and the user interface. It builds on the definitions, models and technical introduction\n\nof ETSI TS 119 102 [i.8].\n\nNOTE 1: Contrary to the model in ETSI TS 119 102, the SVA described in this clause only covers to provide the minimum data that will be needed by the SVA to validate the signature. The process of augmenting the signature is covered in clause 8.3.\n\nNOTE 2: A signature creation policy can be used to specify requirements on the signature process, with respect to the application of signatures to documents and data to be signed in a particular context, business or application domain, community in order for these signatures to be considered as valid signatures. The specification of a signature creation policy is out of the scope of the present document, see ETSI TS 119 172 [i.14] for more details.\n\nNOTE 3: Sole control on the signing key is not covered by a specific control objective but by a combination of individual controls within clause 8.1.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.2 (Main functionalities requirements) — control objective 1",
        "testo": "Garantire che le funzionalita' principali della SCA siano ben documentate.",
        "testo_integrale": "8.1.2 Main functionalities requirements\n\nControl objective\n\nEnsure that the main functionalities of the SCA are well documented.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.3 (Data content type requirements) — control objective 1",
        "testo": "Garantire che il formato di firma sia appropriato al tipo di dato del documento da firmare e conforme a ogni requisito legale o di business applicabile.",
        "testo_integrale": "8.1.3 Data content type requirements\n\nControl objective\n\nEnsure that the signature format is appropriate for the document data type that is to be signed and conforms to any legal\n\nor business requirements applicable.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.3 (Data content type requirements) — control objective 2",
        "testo": "Garantire che il verificatore non possa interpretare male la SD a causa, ad esempio, della mancanza di informazioni sul tipo di dato, di sintassi errata o di presentazione inaccurata, o perche' l'interfaccia utente non e' in grado di presentare correttamente la SD.",
        "testo_integrale": "8.1.3 Data content type requirements\n\nControl objective\n\nEnsure that the verifier cannot misinterpret the SD because of e.g. lack of information on the type of data, wrong syntax\n\nor inaccurate presentation or because the user interface is unable to present the SD correctly.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.3 (Data content type requirements) — control objective 3",
        "testo": "Garantire che la firma sia applicata alla SD corretta (obiettivo di controllo del processo di creazione della firma).",
        "testo_integrale": "8.1.3 Data content type requirements\n\nControl objective (Signature Creation Process)\n\nEnsure that the signature is applied to the right SD.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.3 (Data content type requirements) — control objective 4",
        "testo": "Garantire che il firmatario non firmi inconsapevolmente altri oggetti di dati firmati, con firme non valide create da altri, e che sia in grado di sapere quali firme sono state convalidate o lasciate non verificate.",
        "testo_integrale": "8.1.3 Data content type requirements\n\nControl objective\n\nEnsure that the signer does not un-knowingly sign other embedded signed data objects with non-valid signatures created\n\nby others and that the signer is able to know which signatures have been validated or left unverified.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.3 (Data content type requirements) — control objective 5",
        "testo": "Garantire che il firmatario non alteri accidentalmente la SD.",
        "testo_integrale": "8.1.3 Data content type requirements\n\nControl objective\n\nEnsure that the signer does not accidentally alter the SD.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.3 (Data content type requirements) — control objective 6",
        "testo": "Garantire che la SCA disponga di informazioni sufficienti per presentare accuratamente la SD al firmatario tramite un'interfaccia utente. Dove la presentazione e' importante (cioe' e' uno dei mezzi che veicolano la semantica), la SD puo' essere ambigua se cio' non e' garantito, e il firmatario puo' dedurne un significato non voluto. NOTE 4: includere il tipo di contenuto dei dati (es. .doc, .xlsx, jpg) come attributo firmato puo' prevenire, ad esempio, attacchi basati sull'inserimento di istruzioni html nei DTBS che, sostituendo il tipo di dato con \"html\", portano a una presentazione completamente diversa.",
        "testo_integrale": "8.1.3 Data content type requirements\n\nControl objective\n\nEnsure that the SCA is provided with enough information to be able to accurately present the SD to the signer over a\n\nuser interface. Where presentation of the SD is important (i.e. presentation is one of the means of conveying the\n\nsemantics), the SD can be ambiguous if not ensured, and the signer can infer a meaning from the SD that is not intended\n\nby the signer.\n\nNOTE 4: The inclusion of the data content type, (e.g. .doc, .xlsx, jpg, etc.) as a signed attribute can prevent for example attacks based on inserting html instructions in the DTBS that, when the data type is replaced with \"html\" lead to a completely different presentation.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.3 (Data content type requirements) — control objective 7",
        "testo": "Garantire che una SD contenente codice nascosto capace di modificare la presentazione del documento firmato senza intaccarne la validita' crittografica non inganni il verificatore e/o il firmatario.",
        "testo_integrale": "8.1.3 Data content type requirements\n\nControl objective\n\nEnsure that an SD holding hidden code capable of modifying the signed document presentation without affecting its\n\ncryptographic validity does not deceive the verifier and/or the signer.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.3 (Data content type requirements) — control objective 8",
        "testo": "Garantire che il firmatario non firmi contro la propria volonta' un contenuto o un impegno.",
        "testo_integrale": "8.1.3 Data content type requirements\n\nControl objective\n\nEnsure that the signer does not unwillingly sign a content or a commitment.\n\nControl (Signature Creation Process)",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.4 (Signature attribute requirements) — control objective 1",
        "testo": "Garantire che la firma sia applicata agli attributi di firma corretti e che gli attributi non siano alterati accidentalmente o dolosamente.",
        "testo_integrale": "8.1.4 Signature attribute requirements\n\nControl objective\n\nEnsure that the signature is applied to the right signature attributes and that the attributes are not altered accidentally or\n\nmaliciously.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.4 (Signature attribute requirements) — control objective 2",
        "testo": "Garantire che per creare la firma sia usato il certificato corretto e che nessuna firma sia creata con un certificato scaduto; se possibile, garantire che il certificato non sia revocato al momento della firma.",
        "testo_integrale": "8.1.4 Signature attribute requirements\n\nControl objective\n\nEnsure that the right certificate is used for creating the signature and no signature is created using an expired certificate.\n\nIf possible, ensure that the certificate is not revoked at the moment of the signature.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.4 (Signature attribute requirements) — control objective 3",
        "testo": "Garantire che il riferimento al certificato di firma (o il certificato di firma) e gli altri attributi siano indicati nella firma e che tale informazione sia protetta da attacchi di sostituzione.",
        "testo_integrale": "8.1.4 Signature attribute requirements\n\nControl objective\n\nEnsure that the correct (reference to) or signing certificate and other attributes are indicated in the signature and that this\n\ninformation is protected against substitution attacks.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.4 (Signature attribute requirements) — control objective 4",
        "testo": "Garantire che la firma contenga tutti gli attributi necessari allo scopo della firma secondo i requisiti di business, se cio' non e' gia' chiaro dal contesto e dal contenuto della SD; garantire che il firmatario sia consapevole dello scopo della propria firma.",
        "testo_integrale": "8.1.4 Signature attribute requirements\n\nControl objective\n\nEnsure that the signature contains all attributes necessary to the purpose of the signature according to the business\n\nrequirements, if this is not already clear from the context and content of the SD. Ensure that the signer is aware of the\n\npurpose of its signature.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.4 (Signature attribute requirements) — control objective 5",
        "testo": "L'utente dovrebbe poter sapere quale politica di creazione della firma e' usata nel processo di firma; nel caso in cui il processo di business preveda policy di creazione della firma diverse selezionabili dal firmatario, garantire che il firmatario sappia quali policy sono supportate.",
        "testo_integrale": "8.1.4 Signature attribute requirements\n\nControl objective\n\nThe user should be able to know which signature creation policy is used in the signature process. In the case that the\n\nbusiness process foresees different signature creation policies to be selected by the signer, ensure that the signer knows\n\nwhich signature creation policies are supported.\n\nControl (Signature Creation Process)",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.4 (Signature attribute requirements) — control objective 6",
        "testo": "Garantire che la politica esplicita di creazione della firma usata per creare la firma e/o la politica di firma raccomandata per la convalida sia comunicata ai terzi affidanti, se cio' e' richiesto da requisiti di business, legali o di policy. NOTE 4: una politica di firma esplicita inclusa nella firma puo' essere piu' ampia di una politica di sola creazione della firma, ad esempio puo' includere una politica di convalida o una politica di augmentation.",
        "testo_integrale": "8.1.4 Signature attribute requirements\n\nControl objective\n\nEnsure that the explicit signature creation policy used for creating the signature and/or signature policy recommended to\n\nbe used for validation of the signature is conveyed to the relying parties, if this is needed by the business, legal or policy\n\nrequirements.\n\nNOTE 4: An explicit signature policy included into the signature, can be wider than just a signature creation policy, e.g. it can include a signature validation policy or a signature augmentation policy.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.5 (Time and sequence) — control objective 1",
        "testo": "Garantire che il processo di creazione della firma segua la sequenza di eventi prevista.",
        "testo_integrale": "8.1.5 Time and sequence\n\nControl objective\n\nEnsure that the signature creation process follows the foreseen sequence of events.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.6 (Signature invocation requirements) — control objective 1",
        "testo": "Garantire che ogni firma generata sia il risultato di un'invocazione esplicita della firma. L'interfaccia utente puo' far parte della SCA e/o della DA.",
        "testo_integrale": "8.1.6 Signature invocation requirements\n\nControl objective\n\nEnsure that each signature generated is the result of an explicit signature invocation. The user interface can be part of\n\nthe SCA and/or of the DA.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.6 (Signature invocation requirements) — control objective 2",
        "testo": "Prevenire situazioni in cui la SCA e lo SCDev restano nello stato in cui i dati di autenticazione del firmatario sono stati forniti e il firmatario resta inattivo per lunghi periodi (es. perche' distratto dal processo di firma), con il rischio che un'altra persona non autorizzata possa completare il processo di firma su SD e firme modificate o sostituite.",
        "testo_integrale": "8.1.6 Signature invocation requirements\n\nControl objective\n\nPrevent situations where the SCA and SCDev are in the state where the signer's authentication data has been provided\n\nand the signer remains inactive for long periods of time, e.g. where the signer has been distracted from signature\n\nprocessing and another unauthorized person might possibly be able to complete the signature process on a modified or\n\nsubstituted SDs and signature.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.6 (Signature invocation requirements) — control objective 3",
        "testo": "Prevenire situazioni in cui un firmatario disorientato possa compiere operazioni in modo errato, cosi' che un attaccante possa captare dati riservati (es. un PIN o una password che porterebbero all'impersonificazione del firmatario).",
        "testo_integrale": "8.1.6 Signature invocation requirements\n\nControl objective\n\nPrevent situations where a misguided signer can perform operations in a wrong way so that an attacker can capture\n\nconfidential data (e.g. a PIN or a password that would lead to signer's impersonation).",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.7 (Cryptographic algorithm choice) — control objective 1",
        "testo": "Garantire che tutti gli algoritmi coinvolti nel calcolo di qualunque elemento della firma si basino su algoritmi e lunghezze di chiave appropriati ai requisiti di business.",
        "testo_integrale": "8.1.7 Cryptographic algorithm choice\n\nControl objective\n\nEnsure that all algorithms involved in calculating any element of the signature are based on algorithms and key lengths\n\nthat are appropriate for the business requirements.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.8.1 (General requirements) — control objective 1",
        "testo": "Garantire che solo il legittimo utente dello SCDev possa richiedere la creazione di un valore di firma digitale.",
        "testo_integrale": "8.1.8.1 General requirements\n\nControl objective\n\nEnsure that only the legitimate SCDev user can request creation of a digital signature value.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.8.1 (General requirements) — control objective 2",
        "testo": "Garantire che gli attacchi di forza bruta siano contrastati, ad esempio con un numero di tentativi protetto da un contatore di ritentativi.",
        "testo_integrale": "8.1.8.1 General requirements\n\nControl objective\n\nEnsure that brute force attacks are countered, e.g. the number of retries is protected by a retry counter.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.8.1 (General requirements) — control objective 3",
        "testo": "Assicurare che non sia possibile osservare i dati di autenticazione del firmatario (ad esempio PIN/PW o dati biometrici).",
        "testo_integrale": "8.1.8.1 General requirements\n\nControl objective\n\nMake sure that it is not possible to observe the signer's authentication data (for example, PIN/PW or biometric data).",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.8.2 (Requirements for biometric authentication methods) — control objective 1",
        "testo": "Rendere difficile o praticamente impossibile un attacco di impersonificazione tramite falsi dei tratti biometrici.",
        "testo_integrale": "8.1.8.2 Requirements for biometric authentication methods\n\nControl objective\n\nEnsure that it is made difficult or practically impossible to make an impersonation attack with fakes of the biometric\n\nfeatures.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.8.2 (Requirements for biometric authentication methods) — control objective 2",
        "testo": "Contrastare gli attacchi di replay: se si usano metodi biometrici basati su dati potenzialmente pubblici (volto, forma dell'orecchio o impronta digitale), i dati di autenticazione del firmatario sono protetti per garantirne l'autenticita', poiche' un attaccante puo' ottenere dati biometrici pubblici come immagini del volto e impronte digitali e da essi derivare i dati di autenticazione per abusare dello SCDev.",
        "testo_integrale": "8.1.8.2 Requirements for biometric authentication methods\n\nControl objective\n\nEnsure that replay attacks are countered: if biometric methods based on potentially publicly known data (face, ear\n\nshape, or fingerprint) are used, then the signer's authentication data is protected to ensure authenticity, e.g. an attacker\n\ncan get public biometric features such as face and fingerprint images and derive the signer's authentication data from it\n\nin order to misuse the SCDev.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.8.2 (Requirements for biometric authentication methods) — control objective 3",
        "testo": "Rendere praticamente impossibile, al momento dell'enrolment, collegare una persona al template biometrico di un'altra. Ad esempio, codice malevolo potrebbe intercettare i dati della persona da enrolare e collegarli a dati biometrici di una persona diversa, per esportare poi tale associazione usata dall'impostore per impersonare l'utente autentico.",
        "testo_integrale": "8.1.8.2 Requirements for biometric authentication methods\n\nControl objective\n\nEnsure that it is made practically impossible at enrolment time to link a person to someone else's biometric template.\n\nE.g. malicious code could intercept the data of the person to be enrolled and link it to a biometric data belonging to a\n\ndifferent person, to later on export this association that will be used by the impostor to impersonate the authentic user.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.8.2 (Requirements for biometric authentication methods) — control objective 4",
        "testo": "Rendere praticamente impossibile, al momento dell'autenticazione, alterare l'esito della verifica dei dati di autenticazione del firmatario. Ad esempio un attaccante potrebbe intercettare la risposta del processo di autenticazione per dare una falsa risposta positiva (autenticando una persona non autorizzata) o una risposta negativa (per attuare un attacco di negazione del servizio).",
        "testo_integrale": "8.1.8.2 Requirements for biometric authentication methods\n\nControl objective\n\nEnsure that it is made practically impossible at authentication time to alter the result of the signer's authentication data\n\nverification. E.g. an attacker could intercept the reply of the authentication process, in order to either give a false\n\npositive response (to authenticate an unauthorized person) or to give negative response (to enact a denial of service\n\nattack).",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.9 (DTBS preparation requirements) — control objective 1",
        "testo": "Garantire che un attaccante non possa fornire alla SCA componenti di firma contraffatti e impedire alla SCA di applicare l'intero insieme di componenti di firma specifici del formato scelto per raggiungere un dato scopo.",
        "testo_integrale": "8.1.9 DTBS preparation requirements\n\nControl objective\n\nEnsure that an attacker cannot provide the SCA with forged signature components and prevent the SCA from applying\n\nthe entire signature components specific to the format chosen to achieve a given purpose.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.10 (DTBSR preparation) — control objective 1",
        "testo": "Garantire che la rappresentazione dei dati da firmare (DTBSR) sia composta correttamente.",
        "testo_integrale": "8.1.10 DTBSR preparation\n\nControl objective\n\nEnsure that the data to be signed representation (DTBSR) is correctly composed.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.11 (Signature creation device) — control objective 1",
        "testo": "Garantire che il dispositivo di creazione della firma usato per creare una firma abbia il corretto livello legale e tecnico secondo i requisiti di business. NOTE: un modo possibile per comunicare questa informazione alla SCA e' la politica di creazione della firma.",
        "testo_integrale": "8.1.11 Signature creation device\n\nControl objective\n\nEnsure that the signature creation device used for creating a signature has the right legal and technical level according to\n\nthe business requirements.\n\nNOTE: A possible way to convey this information to the SCA is the signature creation policy.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.11 (Signature creation device) — control objective 2",
        "testo": "Garantire che lo SCDev sia usato come previsto.",
        "testo_integrale": "8.1.11 Signature creation device\n\nControl objective\n\nEnsure that the SCDev is used as intended.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.12 (SCDev/SCA interface (SSI) requirements)",
        "testo": "Testo introduttivo della clausola 8.1.12: l'interfaccia tra dispositivo di creazione della firma (SCDev) e SCA (SSI) e' responsabile della connessione tra SCDev e SCA. E' una dichiarazione di ruolo del componente, non un requisito: i quattro controlli della sottoclavola (SCP 88-SCP 91) sono censiti separatamente.",
        "testo_integrale": "8.1.12 SCDev/SCA interface (SSI) requirements\n\nThe signature creation device (SCDev)/SCA Interface is responsible for the connection between the SCDev and the\n\nSCA.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.12 (SCDev/SCA interface (SSI) requirements) — control objective 1",
        "testo": "Garantire che la comunicazione tra SCA e SCDev sia protetta.",
        "testo_integrale": "8.1.12 SCDev/SCA interface (SSI) requirements\n\nControl objective\n\nEnsure that the communication between SCA and SCDev is protected.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.1.13 (Bulk signing requirements) — control objective 1",
        "testo": "Garantire che un processo di firma massiva non sia meno sicuro di un processo in cui ogni documento sarebbe firmato separatamente; garantire che non vengano firmati documenti che il firmatario non intende firmare.",
        "testo_integrale": "8.1.13 Bulk signing requirements\n\nControl objective\n\nEnsure that a bulk signature process is not less secure than a process where each document would be signed separately.\n\nEnsure that no documents are signed that are not intended to be signed by the signer.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.2.1 (Introduction)",
        "testo": "Introduzione della clausola 8.2: il processo di convalida della firma convalida una firma rispetto a un insieme di vincoli di convalida, espressi in una politica di convalida (implicita o esplicita) che riflette requisiti di business, legali e di sicurezza; possono essere definite piu' politiche adattate ai requisiti di business. La convalida si basa sempre su una politica implicita o esplicita, definibile mediante una descrizione in una sintassi (testo, XML o ASN.1) oppure un insieme di parametri di configurazione. Quando la firma ricevuta contiene un identificatore di politica, la DA puo' usarlo per determinare la politica di convalida appropriata, ma puo' anche decidere che un'altra sia piu' appropriata; se la firma non contiene l'identificatore, la politica e' fornita dalla DA. La SVA riceve dati firmati e altri input dalla DA, convalida la firma rispetto ai vincoli e produce un rapporto di convalida composto da un risultato principale e da voci di dati aggiuntive con i dettagli della convalida tecnica di ciascun vincolo testato, in particolare per esiti invalidi o indeterminati. Esiti possibili: TOTAL-PASSED (la firma e' considerata tecnicamente valida), TOTAL-FAILED (la firma non deve essere considerata tecnicamente valida), INDETERMINATE (le informazioni disponibili non bastano a stabilire se la firma e' valida o invalida). Il rapporto puo' includere informazioni aggiuntive (es. momento della convalida, spiegazioni) ritenute rilevanti dalla SVA e utili alla DA nell'interpretazione dei risultati (vedi ETSI TS 119 102). All'interno del processo di convalida la verifica della firma consiste nel controllo del valore crittografico della firma digitale tramite i dati di verifica della firma. Il modello concettuale della convalida della firma e' descritto in ETSI TS 119 102.",
        "testo_integrale": "8.2.1 Introduction\n\nThe signature validation process validates a signature against a set of validation constraints. These constraints are\n\nexpressed in a signature validation policy, be it implicit or explicit, which reflects business, legal and security policy\n\nrequirements.\n\nOne or more signature validation policies that are adapted to the business requirements can be defined.\n\nA signature validation is always based on an implicit or explicit signature validation policy. It can be defined using:\n\n• a description of that policy using a syntax like text, XML or ASN.1; or\n\n• a set of configuration parameters.\n\nWhen the signature that is received contains a signature policy identifier the driving application (DA) can use the\n\nsignature policy to determine which signature validation policy is appropriate, but can also decide that another signature\n\nvalidation policy is more appropriate.\n\nWhen the signature that is received does not contain a signature policy identifier, then the DA provides the signature\n\npolicy.\n\nA signature validation application (SVA) receives signed data and other input from the DA, validates the signature\n\nagainst a set of validation constraints and outputs a validation report. This report consists of a main validation result\n\naccompanied by additional data items, providing the details of the technical validation of each of the tested constraints,\n\nin particular when an invalid or an indeterminate result is being returned.\n\nThe validation can have one of the following results:\n\n• TOTAL-PASSED: The signature is considered technically valid;\n\n• TOTAL-FAILED: The signature is not to be considered technically valid;\n\n• INDETERMINATE: The available information is insufficient to ascertain the signature to be valid or invalid.\n\nThe report can include additional information (e.g. time of validation, explanations and other information to be\n\ndisplayed) that has been found relevant by the SVA and can be relevant for the driving application (DA) in interpreting\n\nthe results (see ETSI TS 119 102 [i.8]).\n\nWithin a validation process, the signature verification consists of checking the cryptographic value of the digital\n\nsignature value using signature verification data.\n\nThe conceptual model of signature validation is described in ETSI TS 119 102 [i.8].",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.2.2 (Main functionalities requirements) — control objective 1",
        "testo": "Garantire che le funzionalita' principali della SVA siano ben documentate.",
        "testo_integrale": "8.2.2 Main functionalities requirements\n\nControl objective\n\nEnsure that the main functionalities of the SVA are well documented.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.2.3 (Validation process rules) — control objective 1",
        "testo": "Sia definito e seguito un processo di convalida della firma solido; tale processo stabilisce se una firma e' tecnicamente valida rispetto a una politica di convalida della firma.",
        "testo_integrale": "8.2.3 Validation process rules\n\nControl objective\n\nA sound process for signature validation is defined and followed. Such a process establishes whether a signature is\n\ntechnically valid against a signature validation policy.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.2.4 (Validation policy) — control objective 1",
        "testo": "Se la firma ricevuta contiene un identificatore di politica di firma, la DA puo' usarlo per determinare quale politica di convalida usare, ma puo' anche decidere che un'altra politica di convalida sia piu' appropriata. La selezione della politica di firma implicita o esplicita usata per la convalida spetta alla DA e dipende dal processo di business e dallo scopo della convalida. Per il verificatore e' un'informazione utile il fatto che sia stata usata una politica di convalida diversa da quella contenuta nella firma.",
        "testo_integrale": "8.2.4 Validation policy\n\nControl objective\n\nIf the signature that is received contains a signature policy identifier, then the DA can use the signature policy identifier\n\nto determine which signature validation policy to use, but can also decide that another signature policy is more\n\nappropriate. The selection of the implicit or explicit signature policy used for the validation is up to the DA and depends\n\non the business process and the purpose of the validation. For the verifier, the fact that a signature validation policy\n\ndifferent from the one contained in the signature is a useful information.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.2.5 (Validation user interface) — control objective 1",
        "testo": "A seconda del modello di business, i vincoli e gli input del processo di convalida possono essere forniti dalla DA (es. una politica predefinita o una politica scelta fra un insieme di politiche supportate, secondo il contesto; in questo caso la DA e' in grado di selezionare la politica di convalida da usare e puo' essere autorizzata a sovrascrivere alcuni parametri predefiniti) oppure in tutto o in parte dall'utente. Nel secondo caso l'interfaccia utente consente all'utente di selezionare una politica di convalida; in alcuni casi la politica puo' anche essere parametrizzata dall'utente, e l'interfaccia gli consente di parametrizzare la politica selezionata.",
        "testo_integrale": "8.2.5 Validation user interface\n\nControl objective\n\nDepending on the business model, the constraints and inputs to the validation process can either be provided by the DA\n\n(e.g. a default policy or a policy selected amongst a set of supported policies, according to the context; in this case, the\n\ndriving application is able to select the signature validation policy to be used and can be allowed to override some of the\n\ndefault parameters) or fully or partly by the user.\n\nIn the second case, the user interface allows the selection of a signature validation policy by the user. In some cases a\n\nvalidation policy can even be parameterized by the user, in this case the interface allows the user to parameterize the\n\nselected validation policy.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.2.5 (Validation user interface) — control objective 2",
        "testo": "Garantire che l'interfaccia utente presenti il risultato della verifica in modo chiaro all'utente, se un'interfaccia utente fa parte dell'applicazione.",
        "testo_integrale": "8.2.5 Validation user interface\n\nControl objective\n\nEnsure that the user interface provides the result of the verification in a clear way to the user, if a user interface is part\n\nof the application.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.2.6 (Validation inputs and outputs) — control objective 1",
        "testo": "Garantire che: durante la convalida di una firma siano presenti gli input richiesti dalle regole di processo, la politica di convalida applicabile, i dati di convalida (es. certificati, CRL e risposte OCSP) e una sorgente temporale, e che tutti i controlli richiesti dalla politica di convalida del verificatore siano implementati; il processo di convalida implementato fornisca lo stato e i dati di output richiesti dalla DA che presenta il rapporto di convalida. NOTE 1: lo stato e i dati di output possono essere presentati o dalla DA o dalla SVA.",
        "testo_integrale": "8.2.6 Validation inputs and outputs\n\nControl objective\n\nEnsure that:\n\n• During the validation of a signature, the inputs required by the processing rules, the applicable signature validation policy, validation data (e.g. certificates, CRLs and OCSP responses) and a time-source are present and that all checks required by the verifier's signature validation policy are implemented.\n\n• The validation process implemented provides the output status and output data as requested by the DA which presents the validation report.\n\nNOTE 1: The output status and the output data can be presented either by the DA or by the SVA.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.3.1 (Introduction)",
        "testo": "Introduzione della clausola 8.3: l'augmentation della firma e' il processo con cui certo materiale (es. marche temporali, dati di convalida e materiale correlato all'archiviazione) viene incorporato nella firma per renderla piu' resiliente ai cambiamenti o per allungarne la longevita'. Una SAA (Signature Augmentation Application) riceve firme e altri input da una driving application (DA), esegue l'augmentation secondo un insieme di vincoli e produce un rapporto di augmentation, opzionalmente con la firma aumentata. Il rapporto di augmentation deve indicare, in base alla politica di augmentation, uno dei tre esiti: successful (firma aumentata con successo); augmentation unnecessary (la firma non e' stata aumentata perche' l'input e' gia' conforme ai requisiti della politica di augmentation; EXAMPLE: la politica richiede una firma con tempo e la firma contiene gia' una marca temporale di firma); unsuccessful (la firma non ha potuto essere aumentata con successo). Il rapporto di augmentation e' composto da un risultato principale e da voci di dati aggiuntive, in particolare quando l'esito e' unsuccessful; il formato del rapporto e' fuori perimetro di questo documento. Il processo di augmentation puo' essere usato in aggiunta a un processo di creazione della firma, in aggiunta a un processo di convalida o indipendentemente da entrambi; i tre casi sono trattati nella sottoclavola successiva.",
        "testo_integrale": "8.3.1 Introduction\n\nAugmenting signatures is the process by which certain material (e.g. time stamps, validation data and even\n\narchival-related material) is incorporated to the signatures for making them more resilient to change or for enlarging\n\ntheir longevity.\n\nA Signature Augmentation Application (SAA) receives signatures as well as other inputs from a driving application\n\n(DA) and augments a received signatures according to a set of constraints and outputs an augmentation report,\n\noptionally with an augmented signature.\n\nThe augmentation report shall indicate one of the three following results based on the signature augmentation policy:\n\nsuccessful: the signature has been successfully augmented.\n\naugmentation unnecessary: the signature has not been augmented since the input signature is already compliant with\n\nthe requirements of the signature augmentation policy.\n\nEXAMPLE: Implicit or explicit augmentation policy requires signature with time and the signature already contains a signature time-stamp.\n\nunsuccessful: the signature could not be successfully augmented.\n\nThe augmentation report consists of a main augmentation result accompanied by additional data items, in particular\n\nwhen an unsuccessful result is being returned. The format of the augmentation report is out of scope of the present\n\ndocument.\n\nA signature augmentation process can be used in addition to a signature creation process, in addition to a signature\n\nvalidation process or independently of any signature creation process or signature validation process. The three cases\n\nare further addressed in the next clause.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.3.2.1 (Signature augmentation process used by a SCA)",
        "testo": "Primo dei tre casi d'uso: il processo di augmentation della firma usato da una SCA. Una SCA fornisce ai verificatori almeno una Basic Signature come definita in ETSI TS 119 102, cosi' che possa essere convalidata rispetto a una politica di convalida; se pero' la SCA ha accesso in linea, puo' fornire piu' di questo formato minimo. La SCA puo' quindi applicare, oltre a una politica di creazione della firma, una politica di augmentation della firma. EXAMPLE 1: puo' fornire, in accordo con una politica di augmentation, un token di marca temporale applicato alla firma, che consente di mantenere la validita' della firma se il certificato di firma viene revocato dopo il tempo UTC indicato nel token. EXAMPLE 2: puo' includere dati di convalida (es. certificati, CRL o risposte OCSP), secondo una politica di convalida, evitando al verificatore di doverli recuperare.",
        "testo_integrale": "8.3.2.1 Signature augmentation process used by a SCA\n\nA SCA provides to verifiers at least a Basic Signature as defined in ETSI TS 119 102 [i.8], so that it can be validated\n\nagainst a signature validation policy.\n\nHowever, if the SCA has an on-line access, it can provide more than this minimum format.\n\nThe SCA can thus apply, in addition to a signature creation policy, a signature augmentation policy.\n\nEXAMPLE 1: It can provide, in accordance with a signature augmentation policy, a time-stamp token that will be applied to the signature. This allows to maintain the validity of a signature in case the signing certificate is revoked after the UTC time that is indicated within that time-stamp token.\n\nEXAMPLE 2: It can include validation data (e.g. certificates, CRLs or OCSP responses), according to a validation policy, that can avoid a verifier to fetch this data.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.3.2.2 (Signature augmentation process used by a SVA)",
        "testo": "Secondo dei tre casi d'uso: il processo di augmentation della firma usato da una SVA. Una SVA convalida le firme rispetto a una politica di convalida e indica ai verificatori se una firma e' valida, invalida o se il suo stato non puo' essere determinato. Generalmente la SVA ha accesso in linea e puo' quindi aumentare la firma ricevuta con dati di convalida, se richiesto dal verificatore e se la firma e' stata verificata con successo come valida; se ha una connessione a una TSA puo' anche includere un nuovo token di marca temporale nella firma. La SVA puo' quindi applicare, oltre a una politica di convalida, una politica di augmentation della firma.",
        "testo_integrale": "8.3.2.2 Signature augmentation process used by a SVA\n\nA SVA validates signatures against a signature validation policy and indicates to verifiers whether a signature is valid,\n\ninvalid or whether its status cannot be determined.\n\nHowever, generally the SVA has an on-line access and thus can augment the received signature with validation data, if\n\nthis is requested by the verifier and if the signature has been successfully checked as being valid. If it has a connection\n\nto a TSA, it can also include a new time-stamp token within the signature.\n\nThe SVA can thus apply, in addition to a signature validation policy, a signature augmentation policy.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.3.2.3 (Independent signature augmentation process)",
        "testo": "Terzo dei tre casi d'uso: processo di augmentation della firma indipendente. In questo caso una SAA (Signature Augmentation Application) e' usata indipendentemente da una SCA o da una SVA e aggiunge alla firma gli elementi di dati richiesti dalla politica di augmentation. Questo processo indipendente puo' essere utile per firme gia' verificate con successo e archiviate, quindi una SAA indipendente non ha bisogno di convalidare le firme; puo' comunque controllare quali algoritmi crittografici e funzioni di hash sono usati in una firma candidata all'augmentation, cosi' come la validita' dell'ultimo token di marca temporale applicato, per determinare quando la firma deve essere aumentata.",
        "testo_integrale": "8.3.2.3 Independent signature augmentation process\n\nIn this case, a Signature Augmentation Application (SAA) is used independently of a SCA or of a SVA and adds to the\n\nsignature the data elements required by the signature augmentation policy.\n\nThis independent process can be useful for signatures that have already been successfully verified and that have been\n\narchived. This means that an independent SAA does not need to validate signatures. However, it can check which\n\ncryptographic algorithms and hash functions are being used in a signature that is eligible to be augmented as well as the\n\nvalidity of the last applied time-stamp token to determine when the signature needs to be augmented.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.3.3 (Main functionalities requirements) — control objective 1",
        "testo": "Garantire che le funzionalita' principali della SVA siano ben documentate (il testo ufficiale della clausola 8.3.3 nomina la SVA, pur trattando dell'applicazione di augmentation: refuso editoriale riprodotto verbatim).",
        "testo_integrale": "8.3.3 Main functionalities requirements\n\nControl objective\n\nEnsure that the main functionalities of the SVA are well documented.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.3.4 (Augmentation procedures) — control objective 1",
        "testo": "Garantire che siano definite e seguite procedure solide per l'augmentation della firma.",
        "testo_integrale": "8.3.4 Augmentation procedures\n\nControl objective\n\nEnsure that sound procedures for signature augmentation are defined and followed.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.3.5 (Data inclusion) — control objective 1",
        "testo": "Garantire che la firma contenga tutti i dati necessari dopo l'augmentation della firma.",
        "testo_integrale": "8.3.5 Data inclusion\n\nControl objective\n\nEnsure that the signature contains all the necessary data after the augmentation of the signature.",
        "tipo_principio": "altro",
        "stato": "vigente"
    },
    {
        "riferimento": "clausola 8.3.6 (Validation of the input signature to the augmentation process) — control objective 1",
        "testo": "Garantire che la firma di input sia convalidata prima dell'augmentation, se richiesto dalla politica di augmentation della firma.",
        "testo_integrale": "8.3.6 Validation of the input signature to the augmentation process\n\nControl objective\n\nEnsure that the input signature is validated before augmentation if required by the signature augmentation policy.",
        "tipo_principio": "altro",
        "stato": "vigente"
    }
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "clausola 8.1.1 (General)",
    "clausola 8.1.2 (Main functionalities requirements) — control objective 1",
    "SCP 1",
    "SCP 2",
    "clausola 8.1.3 (Data content type requirements) — control objective 1",
    "SCP 3",
    "SCP 4",
    "clausola 8.1.3 (Data content type requirements) — control objective 2",
    "SCP 5",
    "SCP 6",
    "SCP 7",
    "SCP 8",
    "SCP 9",
    "clausola 8.1.3 (Data content type requirements) — control objective 3",
    "SCP 10",
    "SCP 11",
    "SCP 12",
    "SCP 13",
    "SCP 14",
    "clausola 8.1.3 (Data content type requirements) — control objective 4",
    "SCP 15",
    "SCP 16",
    "SCP 17",
    "clausola 8.1.3 (Data content type requirements) — control objective 5",
    "SCP 18",
    "clausola 8.1.3 (Data content type requirements) — control objective 6",
    "SCP 19",
    "SCP 20",
    "SCP 21",
    "SCP 22",
    "clausola 8.1.3 (Data content type requirements) — control objective 7",
    "SCP 23",
    "SCP 24",
    "clausola 8.1.3 (Data content type requirements) — control objective 8",
    "SCP 25",
    "SCP 26",
    "clausola 8.1.4 (Signature attribute requirements) — control objective 1",
    "SCP 27",
    "SCP 28",
    "SCP 29",
    "SCP 30",
    "clausola 8.1.4 (Signature attribute requirements) — control objective 2",
    "SCP 31",
    "SCP 32",
    "SCP 33",
    "SCP 34",
    "SCP 35",
    "SCP 36",
    "clausola 8.1.4 (Signature attribute requirements) — control objective 3",
    "SCP 37",
    "clausola 8.1.4 (Signature attribute requirements) — control objective 4",
    "SCP 38",
    "SCP 39",
    "clausola 8.1.4 (Signature attribute requirements) — control objective 5",
    "SCP 40",
    "SCP 41",
    "SCP 42",
    "clausola 8.1.4 (Signature attribute requirements) — control objective 6",
    "SCP 43",
    "SCP 44",
    "SCP 45",
    "clausola 8.1.5 (Time and sequence) — control objective 1",
    "SCP 46",
    "SCP 47",
    "SCP 48",
    "clausola 8.1.6 (Signature invocation requirements) — control objective 1",
    "SCP 49",
    "SCP 50",
    "SCP 51",
    "SCP 52",
    "SCP 53",
    "clausola 8.1.6 (Signature invocation requirements) — control objective 2",
    "SCP 54",
    "clausola 8.1.6 (Signature invocation requirements) — control objective 3",
    "SCP 55",
    "SCP 56",
    "clausola 8.1.7 (Cryptographic algorithm choice) — control objective 1",
    "SCP 57",
    "SCP 58",
    "SCP 59",
    "clausola 8.1.8.1 (General requirements) — control objective 1",
    "SCP 60",
    "SCP 61",
    "SCP 62",
    "SCP 63",
    "SCP 64",
    "SCP 65",
    "SCP 66",
    "clausola 8.1.8.1 (General requirements) — control objective 2",
    "SCP 67",
    "SCP 68",
    "SCP 69",
    "SCP 70",
    "clausola 8.1.8.1 (General requirements) — control objective 3",
    "SCP 71",
    "SCP 72",
    "SCP 73",
    "clausola 8.1.8.2 (Requirements for biometric authentication methods) — control objective 1",
    "SCP 74",
    "clausola 8.1.8.2 (Requirements for biometric authentication methods) — control objective 2",
    "SCP 75",
    "SCP 76",
    "clausola 8.1.8.2 (Requirements for biometric authentication methods) — control objective 3",
    "SCP 77",
    "clausola 8.1.8.2 (Requirements for biometric authentication methods) — control objective 4",
    "SCP 78",
    "clausola 8.1.9 (DTBS preparation requirements) — control objective 1",
    "SCP 79",
    "SCP 80",
    "SCP 81",
    "clausola 8.1.10 (DTBSR preparation) — control objective 1",
    "SCP 82",
    "SCP 83",
    "SCP 84",
    "SCP 85",
    "clausola 8.1.11 (Signature creation device) — control objective 1",
    "SCP 86",
    "clausola 8.1.11 (Signature creation device) — control objective 2",
    "SCP 87",
    "clausola 8.1.12 (SCDev/SCA interface (SSI) requirements)",
    "clausola 8.1.12 (SCDev/SCA interface (SSI) requirements) — control objective 1",
    "SCP 88",
    "SCP 89",
    "SCP 90",
    "SCP 91",
    "clausola 8.1.13 (Bulk signing requirements) — control objective 1",
    "SCP 92",
    "SCP 93",
    "SCP 94",
    "clausola 8.2.1 (Introduction)",
    "clausola 8.2.2 (Main functionalities requirements) — control objective 1",
    "SVP 1",
    "SVP 2",
    "clausola 8.2.3 (Validation process rules) — control objective 1",
    "SVP 3",
    "SVP 4",
    "SVP 5",
    "SVP 6",
    "SVP 7",
    "clausola 8.2.4 (Validation policy) — control objective 1",
    "SVP 8",
    "SVP 9",
    "clausola 8.2.5 (Validation user interface) — control objective 1",
    "SVP 10",
    "SVP 11",
    "clausola 8.2.5 (Validation user interface) — control objective 2",
    "SVP 12",
    "SVP 13",
    "clausola 8.2.6 (Validation inputs and outputs) — control objective 1",
    "SVP 14",
    "SVP 15",
    "SVP 16",
    "SVP 17",
    "SVP 18",
    "SVP 19",
    "SVP 20",
    "SVP 21",
    "SVP 22",
    "SVP 23",
    "clausola 8.3.1 (Introduction)",
    "clausola 8.3.2.1 (Signature augmentation process used by a SCA)",
    "clausola 8.3.2.2 (Signature augmentation process used by a SVA)",
    "clausola 8.3.2.3 (Independent signature augmentation process)",
    "clausola 8.3.3 (Main functionalities requirements) — control objective 1",
    "SAP 1",
    "SAP 2",
    "clausola 8.3.4 (Augmentation procedures) — control objective 1",
    "SAP 3",
    "SAP 4",
    "SAP 5",
    "clausola 8.3.5 (Data inclusion) — control objective 1",
    "SAP 6",
    "SAP 7",
    "clausola 8.3.6 (Validation of the input signature to the augmentation process) — control objective 1",
    "SAP 8",
    "SAP 9",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

# Nessuna relazione: il collegamento con le altre fonti (ETSI TS 119 102,
# ETSI TS 119 312, ETSI EN 319 412-5, CAdES/XAdES/PAdES/ASiC, e le fonti
# che citano per id i controlli di questa fonte) e' demandato alla sessione
# principale (ADR-0009, Fase 6) - mandato esplicito del task di capitolo.
RELAZIONI: list[dict] = []
