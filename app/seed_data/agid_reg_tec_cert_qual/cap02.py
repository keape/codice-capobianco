"""Regole Tecniche e Raccomandazioni AgID (13 feb 2020, ex art. 71 CAD).
Capitolo 2 di 3: Capitolo 4 del testo ufficiale (Raccomandazioni), sezioni
4.1 (Profilo dei certificati qualificati), 4.2 (Profilo dei certificati di
certificazione e validazione temporale), 4.3 (Formati di firme e sigilli
elettronici qualificati), 4.4 (Informazioni sullo stato dei certificati
qualificati di firma e sigillo). Testo ufficiale in
app/.source_cache/agid_reg_tec_cert_qual/raw.txt.

Modellazione (ADR-0007) e nota su Obbligo vs. Principio per le
"raccomandazioni": il testo (par. 2 §3, cap01.py "par. 2 §3") dichiara
esplicitamente che le "raccomandazioni" del presente capitolo 4 non sono
"obblighi" in senso stretto - la loro disapplicazione non invalida firme o
sigilli qualificati - ma vanno interpretate nel significato RFC 2119
(applicazione fortemente consigliata). Nel nostro schema, tuttavia, il nodo
Obbligo cattura ogni "prescrizione che impone un comportamento a un
soggetto" (CLAUDE.md/CONTEXT.md), indipendentemente dalla sanzionabilità in
senso legale stretto: ogni punto di 4.1/4.2/4.3/4.4 prescrive un
comportamento tecnico specifico al QTSP, quindi è modellato come Obbligo
(tipo "tecnico/sicurezza" salvo diversa indicazione), NON come Principio -
la natura di "raccomandazione RFC 2119" e non "obbligo legale in senso
stretto" resta documentata una sola volta nel nodo di riferimento
"par. 2 §3" (cap01.py), a cui ogni nodo di questo capitolo può essere
ricondotto in lettura, senza ripetere la precisazione su ciascuno dei 31
nodi (nessuno di essi porta perciò `sanzioni`, coerentemente con l'assenza
di sanzione legale propria delle raccomandazioni).

- Paragrafo introduttivo del capitolo 4 (impegno del QTSP + comunicazione
  all'Agenzia + pubblicazione sul sito istituzionale) -> Obbligo, tipo
  "informativo/trasparenza", soggetto QTSP obbligato (nessun destinatario
  "Agenzia": non è una categoria di soggetto censita).
- 4.1, punti 1-4 e 6-9: un nodo per punto numerato (contenuto prescrittivo
  proprio e distinto per ciascuno). Punto 5 (SubjectDN): spezzato nelle 4
  lettere a)-d), ciascuna con contenuto tecnico autonomo e sostanzialmente
  diverso (serialNumber / organizationName-title / dnQualifier /
  description-EORI), a differenza degli elenchi puramente enumerativi senza
  contenuto distinto lasciati in un solo nodo altrove nel censimento.
  Totale 4.1: 12 nodi (1,2,3,4,5a,5b,5c,5d,6,7,8,9).
- 4.2, punti 1-3: un nodo ciascuno. Punti 4 e 5 (estensioni dei certificati
  di certificazione / di marcatura temporale): spezzati per lettera
  (4: a-e, 5 nodi; 5: a-f, 6 nodi), stesso criterio di 4.1 punto 5 - ogni
  lettera individua un'estensione X.509 diversa con vincoli propri
  (keyUsage, basicConstraints, certificatePolicies, ecc.). Totale 4.2: 3 +
  5 + 6 = 14 nodi.
- 4.3: un solo paragrafo, un solo nodo (rinvio alla Decisione di Esecuzione
  (UE) 1506/2015 per i formati di firme/sigilli).
- 4.4: 3 paragrafi con contenuto prescrittivo distinto (OCSP/CRL
  DistributionPoints; ExpiredCertsOnCRL; accessibilità in rete delle
  informazioni di revoca/sospensione) -> 3 nodi.

tipo_obbligo assegnato: "tecnico/sicurezza" per i requisiti sul profilo
tecnico dei certificati (4.1 punti 1-4, 6, 8, 9; 4.2 tutti i punti; 4.3;
4.4 punti 1-2), "informativo/trasparenza" per i punti che riguardano
pubblicazione/accessibilità di informazioni (4.1 punto 7 - pubblicazione
testi limitazioni d'uso; 4.4 punto 3 - accessibilità in rete delle
informazioni di revoca/sospensione), "organizzativo" per i punti che
riguardano procedure/prova documentale interne al QTSP (4.1 punto 5b -
organizationName, richiede prova della volontà dell'organizzazione).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "par. 4 (intro)",
        "testo": "I QTSP che si impegnano a fornire - salvo diversa richiesta degli interessati - i servizi applicando le raccomandazioni del paragrafo 4 lo comunicano all'Agenzia, che pubblica tali informazioni sul proprio sito web istituzionale.",
        "testo_integrale": "I QTSP che si impegnano a fornire – salvo diversa richiesta degli interessati-i servizi oggetto del presente regolamento applicando le raccomandazioni di cui al paragrafo 4, lo comunicano all'Agenzia, che pubblica tali informazioni sul proprio sito web istituzionale.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.1 punto 1",
        "testo": "Il certificato qualificato è conforme alla specifica RFC 5280 e alle norme ETSI EN 319-412-1 v.1.1.1, EN 319-412-2 v.2.1.1, EN 319-412-3 v.1.1.1, EN 319-412-4 v.1.1.1.",
        "testo_integrale": "1. Conformità con quanto stabilito nella specifica RFC 5280 e nelle norme ETSI EN 319-412-1 versione 1.1.1, EN 319-412-2 versione 2.1.1, EN 319-412-3 versione 1.1.1, EN 319-412-4 versione 1.1.1 e EN 319-412-2 versione 2.1.1.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.1 punto 2",
        "testo": "L'estensione KeyUsage è presente e marcata critica; per i certificati qualificati di firma elettronica il solo KeyUsage ammesso è il «Type A» (ETSI EN 319-412-2).",
        "testo_integrale": "2. L'estensione KeyUsage è presente e marcata critica. Il solo KeyUsage ammesso per i certificati qualificati di firma elettronica è il \"Type A,\" come descritto nella citata norma ETSI EN 319-412-2.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.1 punto 3",
        "testo": "Per ottemperare agli allegati I lett. h), III lett. h) e IV lett. i) eIDAS, è utilizzato l'accessMethod id-ad-caIssuers, con accessLocation uniformResourceIdentifier.",
        "testo_integrale": "3. Al fine di ottemperare a quanto prescritto negli allegati I (lettera h), III (lettera h) e IV (lettera i) del regolamento eIDAS, è utilizzato l'accessMethod id-ad-caIssuers, con accessLocation uniformResourceIdentifier.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.1 punto 4",
        "testo": "L'estensione authorityKeyIdentifier (2.5.29.35) contiene almeno il campo keyIdentifier, non marcata critica.",
        "testo_integrale": "4. L'estensione authorityKeyIdentifier ( 2.5.29.35) contiene almeno il campo keyIdentifier, non marcata critica.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.1 punto 5 lett. a",
        "testo": "Il serialNumber (2.5.4.5) nei certificati di firma elettronica e autenticazione di siti web rilasciati a persone fisiche contiene il codice fiscale del titolare con prefisso TIN (es. TINIT-CCCNNN64T30H501H); se il titolare non ha codice fiscale italiano si usa TIN di altra autorità UE, ovvero i prefissi IDC/PAS per documento di riconoscimento, PNO per numero di registrazione nazionale; per persona fisica con permesso di soggiorno si applica EN 319-412-1 §5.1.3 punto 6 con prefisso RP; se la legge dello Stato di residenza non consente nessuno dei precedenti, si applica lo stesso punto 6 con prefisso NS, inserendo un codice univoco eventualmente derivato da uno dei predetti.",
        "testo_integrale": "a. Il serialNumber ( 2.5.4.5) - nei certificati di firma elettronica e autenticazione di siti web rilasciati a persone fisiche-contiene il codice fiscale del titolare indicato con il prefisso TIN, come prescritto dalla norma ETSI EN 319-412-1 (es. TINIT-CCCNNN64T30H501H). Esclusivamente nel caso in cui al titolare non sia stato assegnato un codice fiscale dall'autorità italiana è possibile indicare analogo numero di identificazione fiscale rilasciato da altra autorità dell'Unione utilizzando il prefisso TIN ovvero gli estremi di un documento di riconoscimento utilizzando i prefissi IDC o PAS ovvero un numero di registrazione nazionale utilizzando il prefisso PNO, come prescritto dalla norma EN 319-412-1. Nel caso in cui il titolare sia una persona fisica non dotata di codice fiscale o carta di identità italiana, ma dotata di permesso di soggiorno, si applica quanto previsto dal punto 6 del paragrafo 5.1.3 della norma EN 319-412-1 utilizzando il prefisso RP. Nei casi in cui la legge dello Stato di residenza della persona fisica non consenta l'utilizzo di nessuno dei precedenti codici, si applica quanto previsto dal punto 6 del paragrafo 5.1.3 della norma EN 319-412-1 utilizzando il prefisso NS per identificare lo schema nazionale. In tale evenienza, il prestatore di servizi fiduciari deve inserire un codice univoco, eventualmente derivato da uno dei predetti.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Applicabile ai certificati di firma elettronica e di autenticazione di siti web rilasciati a persone fisiche.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.1 punto 5 lett. b",
        "testo": "L'organizationName (2.5.4.10) può indicare l'appartenenza/affiliazione del titolare all'organizzazione solo se il QTSP ha e conserva prova della volontà dell'organizzazione a tale uso e dell'obbligo di quest'ultima di richiedere la revoca se il titolare lascia l'organizzazione; se presente, gli stessi vincoli si applicano all'attributo title (ruolo in linguaggio naturale, opzionalmente seguito da «::» + codice ISTAT della professione); l'organizationName non è utilizzato se il titolare è un semplice cliente dell'organizzazione.",
        "testo_integrale": "b. L'organizationName ( 2.5.4.10) dei certificati di firma elettronica, eventualmente utilizzato per indicare l'appartenenza o l'affiliazione del titolare all'organizzazione e esclusivamente nel caso in cui il prestatore di servizi fiduciari abbia avuto e conservi prova della volontà dell'organizzazione medesima a tale uso e che la stessa si assuma l'obbligo di richiedere la revoca del certificato nel caso in cui il titolare del certificato lasci l'organizzazione. Nel caso in cui l'organizationName sia presente, i medesimi vincoli si applicano anche all'eventuale codifica dell'attributo title. L'attributo title, se presente, contiene il ruolo del titolare in linguaggio naturale e, facoltativamente, una seconda parte costituita da un codice numerico derivato dai codici delle professioni pubblicati da ISTAT. Nel caso in cui sia presente, il codice ISTAT della professione è preceduto dalla stringa :: (esadecimale 0x3A3A, e title=descrizioneInLinguaggioNaturale::codiceNumerico). L'organizationName non è utilizzato nel caso in cui il titolare sia un semplice cliente dell'organizzazione.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Applicabile solo se il QTSP intende valorizzare l'organizationName nei certificati di firma elettronica.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.1 punto 5 lett. c",
        "testo": "Il dnQualifier (2.5.4.46) contiene il codice identificativo del titolare presso il prestatore del servizio, univoco nell'ambito del prestatore stesso.",
        "testo_integrale": "c. Il dnQualifier ( 2.5.4.46) che contiene il codice identificativo del titolare presso il prestatore del servizio. Tale codice è univoco nell'ambito del prestatore del servizio.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.1 punto 5 lett. d",
        "testo": "È possibile inserire nell'attributo description (2.5.4.13) il codice EORI del Regolamento (UE) n.312/2009, preceduto dal testo «EORI:».",
        "testo_integrale": "d. La possibilità di inserire nell'attributo description ( 2.5.4.13) il codice EORI (Economic Operator Registration and Identification) di cui al Regolamento (UE) №312/2009 del 16 aprile 2009 e successive modificazioni. In tal caso il codice stesso è preceduto dal testo EORI e dal carattere \":\" (esadecimale 0x3A).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Facoltativo: applicabile solo se il QTSP intende valorizzare il codice EORI nell'attributo description.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.1 punto 6",
        "testo": "Per normalizzare l'uso del «legal person semantics identifier» (ETSI EN 319-412-1 §5.1.4), nel caso di organizzazioni prive sia di partita IVA sia di NTR ma dotate solo di codice fiscale, si può usare la modalità del numero 3 del §5.1.4, con i caratteri «CF» (es. CF:IT-97735020584).",
        "testo_integrale": "6. Al fine di normalizzare l'uso della sintassi dall'identificatore 'legal person semantics identifier' descritto nel paragrafo 5.1.4 della norma ETSI EN 319-412-1, nel caso di organizzazioni non dotate né di partita IVA né di NTR, ma solamente del codice fiscale, è possibile utilizzare la modalità descritta al numero 3 del paragrafo 5.1.4, utilizzando i due caratteri \"CF\" (esempio: CF:IT-97735020584).",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Applicabile alle organizzazioni prive sia di partita IVA sia di NTR, dotate solo di codice fiscale.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.1 punto 7",
        "testo": "Salvo quanto disposto dalle norme ETSI citate, eventuali ulteriori limiti d'uso sono inseriti nell'attributo explicitText del campo userNotice dell'estensione certificatePolicies; sul sito dell'Agenzia sono pubblicati testi e codifiche delle limitazioni d'uso, di cui è auspicabile la garanzia agli utenti.",
        "testo_integrale": "7. Salvo quanto disposto nelle citate norme ETSI, eventuali ulteriori limiti d'uso sono inseriti nell'attributo explicitText del campo userNotice dell'estensione certificatePolicies. Sul sito istituzionale dell'Agenzia sono pubblicati i testi e le codifiche delle limitazioni d'uso che è auspicabile siano garantite agli utenti.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.1 punto 8",
        "testo": "È fortemente sconsigliato l'uso del carattere wildcard «*» in tutti i nomi di dominio nei certificati qualificati di autenticazione di siti web.",
        "testo_integrale": "8. È fortemente sconsigliato l'utilizzo dei caratteri wildcard come * (esadecimale 0x2A) in tutti i nomi di dominio nei certificati qualificati di autenticazione di siti web.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.1 punto 9",
        "testo": "Ulteriori estensioni possono essere inserite nel certificato purché conformi agli standard citati nel provvedimento e non marcate critiche.",
        "testo_integrale": "9. Ulteriori estensioni possono essere inserite nel certificato purché conformi agli standard citati nel presente provvedimento e non marcate critiche.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.2 punto 1",
        "testo": "Il profilo dei certificati di certificazione è conforme alla specifica RFC 5280.",
        "testo_integrale": "1. Il profilo dei certificati di certificazione è conforme alla specifica RFC 5280.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.2 punto 2",
        "testo": "Il profilo dei certificati di marcatura temporale è conforme alla norma ETSI EN 319-422 v.1.1.1.",
        "testo_integrale": "2. Il profilo dei certificati di marcatura temporale è conforme alla norma ETSI EN 319-422 versione 1.1.1.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.2 punto 3",
        "testo": "Per la codifica dei certificati si usa il formato ASN.1–DER (ISO/IEC 8824, 8825), in binario o alfanumerico via Base64 (RFC 1421), con intestazione/coda RFC 1421 eventualmente assenti; estensione file .cer/.der per il formato binario, .b64 per l'alfanumerico.",
        "testo_integrale": "3. Per la codifica dei certificati deve essere utilizzato il formato ASN.1 – DER (ISO/IEC 8824, 8825) in rappresentazione binaria o alfanumerica, ottenuta applicando la trasformazione Base64 (RFC 1421 e successive modifiche); l'intestazione e la coda previsti in RFC 1421 possono essere assenti. Nel primo caso il file contenente il certificato deve assumere l'estensione cer o der, nel secondo caso b64.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.2 punto 4 lett. a",
        "testo": "I certificati di certificazione contengono l'estensione keyUsage (2.5.29.15) con i valori keyCertSign e CRLSign (bit #5 e #6 a 1), marcata critica.",
        "testo_integrale": "a. keyUsage ( 2.5.29.15) — contenente i valori keyCertSign e CRLSign (bit #5 e #6 impostati a 1); l'estensione è marcata critica;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.2 punto 4 lett. b",
        "testo": "I certificati di certificazione contengono l'estensione basicConstraints (2.5.29.19) con CA=true, marcata critica.",
        "testo_integrale": "b. basicConstraints ( 2.5.29.19) — contenente il valore CA=true; l'estensione è marcata critica;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.2 punto 4 lett. c",
        "testo": "I certificati di certificazione contengono l'estensione certificatePolicies (2.5.29.32) con uno o più PolicyIdentifier:code e le URL dei relativi CPS (può contenere l'OID generico RFC 5280 2.5.29.32.0), non marcata critica.",
        "testo_integrale": "c. certificatePolicies ( 2.5.29.32) — contenente uno o più identificativi delle PolicyIdentifier:code e le URL dei relativi CPS. Può contenere l'OID geerico previsto dall'\\ :RFC:`5280 (2.5.29.32.0)); l'estensione non è marcata critica;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.2 punto 4 lett. d",
        "testo": "I certificati di certificazione contengono l'estensione subjectKeyIdentifier (2.5.29.14) con il valore keyIdentifier, non marcata critica.",
        "testo_integrale": "d. subjectKeyIdentifier ( 2.5.29.14) — contenente il valore keyIdentifier per identificare il certificato l'estensione non è marcata critica;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.2 punto 4 lett. e",
        "testo": "Nei certificati di certificazione, ulteriori estensioni possono essere inserite purché conformi agli standard citati nel provvedimento e non marcate critiche.",
        "testo_integrale": "e. Ulteriori estensioni possono essere inserite nel certificato purché conformi agli standard citati nel presente provvedimento e non marcate critiche.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.2 punto 5 lett. a",
        "testo": "I certificati di marcatura temporale contengono l'estensione keyUsage (2.5.29.15) con il valore digitalSignature (bit #0 a 1), marcata critica.",
        "testo_integrale": "a. keyUsage ( 2.5.29.15) — contenente il valore digitalSignature (bit #0 impostato a 1); l'estensione è marcata critica;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.2 punto 5 lett. b",
        "testo": "I certificati di marcatura temporale contengono l'estensione extendedKeyUsage (2.5.29.37) con esclusivamente keyPurposeId impostato su timeStamping, marcata critica.",
        "testo_integrale": "b. extendedKeyUsage ( 2.5.29.37) — contenente esclusivamente il campo keyPurposeId impostato su timeStamping; l'estensione è marcata critica;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.2 punto 5 lett. c",
        "testo": "I certificati di marcatura temporale contengono l'estensione certificatePolicies (2.5.29.32) con uno o più PolicyIdentifier e le URL del relativo CPS, non marcata critica.",
        "testo_integrale": "c. certificatePolicies ( 2.5.29.32) — contenente uno o più identificativi delle PolicyIdentifier e le URL del relativo CPS; l'estensione non è marcata critica;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.2 punto 5 lett. d",
        "testo": "I certificati di marcatura temporale contengono l'estensione authorityKeyIdentifier (2.5.29.35) con almeno il keyIdentifier corrispondente al subjectKeyIdentifier del certificato di certificazione usato per sottoscrivere il certificato di marcatura, non marcata critica.",
        "testo_integrale": "d. authorityKeyIdentifier ( 2.5.29.35) — contenente almeno il valore keyIdentifier corrispondente al :code:'subjectKeyIdentifier: del certificato di certificazione utilizzato per sottoscrivere il certificato di marcatura temporale; l'estensione non è marcata critica;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.2 punto 5 lett. e",
        "testo": "I certificati di marcatura temporale contengono l'estensione subjectKeyIdentifier (2.5.29.14) con il valore keyIdentifier, non marcata critica.",
        "testo_integrale": "e. subjectKeyIdentifier ( 2.5.29.14) — contenente il valore keyIdentifier per identificare il certificato; l'estensione non è marcata critica;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.2 punto 5 lett. f",
        "testo": "Nei certificati di marcatura temporale, ulteriori estensioni possono essere inserite purché conformi agli standard citati nel provvedimento e non marcate critiche.",
        "testo_integrale": "f. Ulteriori estensioni possono essere inserite nel certificato purché conformi agli standard citati nel presente provvedimento e non marcate critiche.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.3",
        "testo": "Nella realizzazione di servizi e applicazioni per la generazione di firme e sigilli elettronici qualificati, i QTSP si attengono alla Decisione di Esecuzione (UE) n.1506/2015 dell'8 settembre 2015 e successive modificazioni.",
        "testo_integrale": "Nella realizzazione di servizi e applicazioni per la generazione di firme e sigilli elettronici qualificati, i prestatori di servizi fiduciari qualificati si attengono alle disposizioni emanate con la Decisione di Esecuzione (UE) № 1506/2015 dell'8 settembre 2015 e successive modificazioni.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.4 §1",
        "testo": "Le informazioni sullo stato del certificato preferibilmente sono rese disponibili tramite OCSP ed eventualmente CRL; i certificati qualificati contengono l'estensione authorityInfoAccess (1.3.6.1.5.5.7.1.1) con accessDescription/accessMethod id-ad-ocsp (1.3.6.1.5.5.7.48.1) e accessLocation con l'URI dell'OCSP Responder, ed eventualmente l'estensione CRLDistributionPoints (2.5.29.31); le estensioni non sono marcate critiche.",
        "testo_integrale": "Le informazioni afferenti lo stato del certificato preferibilmente sono rese disponibili attraverso il servizio OCSP ed eventualmente anche tramite liste di revoca (CRL). A tal fine i certificati qualificati contengono l'estensione authorityInfoAccess ( 1.3.6.1.5.5.7.1.1) contenente il campo accessDescription con l'attributo accessMethod, che contiene l'identificativo id-ad-ocsp ( 1.3.6.1.5.5.7.48.1) e l'attributo accessLocation, che contiene l'URI che punta all'OCSP Responder e, eventualmente, l'estensione CRLDistributionPoints ( 2.5.29.31). Le estensioni non sono marcate critiche.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.4 §2",
        "testo": "Le CRL contengono l'estensione ExpiredCertsOnCRL (2.5.29.60), prevista dallo standard X.509.",
        "testo_integrale": "Le CRL contengono l'estensione ExpiredCertsOnCRL ( 2.5.29.60), prevista dallo standard X.509.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "par. 4.4 §3",
        "testo": "Le informazioni sulla revoca e sospensione dei certificati sono liberamente accessibili in rete.",
        "testo_integrale": "Le informazioni sulla revoca e sospensione dei certificati sono liberamente accessibili in rete.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = []

INDICE_ARTICOLI_LOCALE = [
    "par. 4 (intro)",
    "par. 4.1 punto 1",
    "par. 4.1 punto 2",
    "par. 4.1 punto 3",
    "par. 4.1 punto 4",
    "par. 4.1 punto 5 lett. a",
    "par. 4.1 punto 5 lett. b",
    "par. 4.1 punto 5 lett. c",
    "par. 4.1 punto 5 lett. d",
    "par. 4.1 punto 6",
    "par. 4.1 punto 7",
    "par. 4.1 punto 8",
    "par. 4.1 punto 9",
    "par. 4.2 punto 1",
    "par. 4.2 punto 2",
    "par. 4.2 punto 3",
    "par. 4.2 punto 4 lett. a",
    "par. 4.2 punto 4 lett. b",
    "par. 4.2 punto 4 lett. c",
    "par. 4.2 punto 4 lett. d",
    "par. 4.2 punto 4 lett. e",
    "par. 4.2 punto 5 lett. a",
    "par. 4.2 punto 5 lett. b",
    "par. 4.2 punto 5 lett. c",
    "par. 4.2 punto 5 lett. d",
    "par. 4.2 punto 5 lett. e",
    "par. 4.2 punto 5 lett. f",
    "par. 4.3",
    "par. 4.4 §1",
    "par. 4.4 §2",
    "par. 4.4 §3",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "par. 4.1 punto 1"),
        "nodo_a": ("obbligo", None, "par. 4 (intro)"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "textual",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "par. 4.2 punto 4 lett. a"),
        "nodo_a": ("obbligo", None, "par. 4.2 punto 1"),
        "tipo_relazione": "specifica",
        "evidence_type": "textual",
        "confidence": 0.65,
    },
]
