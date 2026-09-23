"""Estrazione granulare DPCM 24/10/2014 (SPID) - artt. 7-12: Rilascio delle
identità digitali, Gestione delle identità digitali, Uso illecito delle
identità digitali, Accreditamento dei gestori dell'identità digitale,
Obblighi dei gestori dell'identità digitale, Cessazione/subentro/sospensione/
revoca dell'attività dei gestori dell'identità digitale.

Testo ufficiale vigente al 21/09/2026, fonte app/.source_cache/spid/cap02.txt (ADR-0007).
Modulo generato secondo il contratto di app/seed_data/lib.py: nessun discrimine di rilevanza,
copertura completa comma/lettera per comma/lettera. Il "gestore dell'identità digitale" SPID
è modellato con la categoria soggetto "QTSP/gestore" (equivalente funzionale al QTSP eIDAS).

Correzione 2026-09-21: l'estrazione originaria (nonostante l'etichetta della Fonte 5,
"testo vigente comprensivo delle modifiche del DPCM 19 ottobre 2021") riportava per
errore il testo previgente 2014 su art. 7 c.9, art. 10 c.3/c.4, art. 12. In sede di
import del DPCM 19/10/2021 come Fonte 6 (vedi app/seed_data/dpcm2021/cap01.py) sono
stati corretti: art. 7 c.9 e art. 10 c.3 lett.g) (rinvio al regolamento (UE) 2016/679
aggiunto), aggiunte le lettere art. 10 c.3 lett.0-b) e lett.c-bis) (nuovi requisiti di
accreditamento), aggiornato il rinvio di art. 10 c.4, art. 12 c.1 (termine 30->60
giorni, contenuto), art. 12 c.2 (integrazione), art. 12 c.3 marcato "abrogato" (comma
soppresso dal 2021), aggiunto art. 12 c.5-bis (nuovo).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 7 c.1",
        "testo": "Il gestore dell'identità digitale rilascia le identità digitali su domanda "
                 "dell'interessato, previa verifica della sua identità e mediante consegna in "
                 "modalità sicura delle credenziali di accesso; nell'ambito della propria "
                 "struttura organizzativa, i gestori individuano il responsabile delle attività "
                 "di verifica dell'identità del richiedente.",
        "testo_integrale": "Le identità digitali sono rilasciate, a domanda dell'interessato, "
                            "dal gestore dell'identità digitale, previa verifica dell'identità "
                            "del soggetto richiedente e mediante consegna in modalità sicura "
                            "delle credenziali di accesso. Nell'ambito della propria struttura "
                            "organizzativa, i gestori delle identità digitali individuano il "
                            "responsabile delle attività di verifica dell'identità del soggetto "
                            "richiedente.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 c.2 lett.a)",
        "testo": "Il gestore può verificare l'identità del richiedente che sottoscrive il "
                 "modulo di adesione allo SPID tramite esibizione a vista di un documento "
                 "d'identità valido e, per le persone giuridiche, della procura attestante i "
                 "poteri di rappresentanza.",
        "testo_integrale": "identificazione del soggetto richiedente che sottoscrive il modulo "
                            "di adesione allo SPID, tramite esibizione a vista di un valido "
                            "documento d'identità e, nel caso di persone giuridiche, della "
                            "procura attestante i poteri di rappresentanza;",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 c.2 lett.b)",
        "testo": "Il gestore può verificare l'identità del richiedente mediante identificazione "
                 "informatica tramite documenti digitali di identità validi ai sensi di legge, "
                 "che prevedano il riconoscimento a vista del richiedente all'atto "
                 "dell'attivazione, quali la tessera sanitaria-carta nazionale dei servizi "
                 "(TS-CNS), la CNS o carte ad essa conformi.",
        "testo_integrale": "identificazione informatica tramite documenti digitali di identità, "
                            "validi ai sensi di legge, che prevedono il riconoscimento a vista "
                            "del richiedente all'atto dell'attivazione, fra cui la tessera "
                            "sanitaria-carta nazionale dei servizi (TS-CNS), CNS o carte ad essa "
                            "conformi;",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 c.2 lett.c)",
        "testo": "Il gestore può verificare l'identità del richiedente mediante identificazione "
                 "informatica tramite un'altra identità digitale SPID di livello di sicurezza "
                 "pari o superiore a quella oggetto della richiesta.",
        "testo_integrale": "identificazione informatica tramite altra identità digitale SPID di "
                            "livello di sicurezza pari o superiore a quella oggetto della "
                            "richiesta;",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 c.2 lett.d)",
        "testo": "Il gestore può verificare l'identità del richiedente mediante acquisizione del "
                 "modulo di adesione allo SPID sottoscritto con firma elettronica qualificata o "
                 "con firma digitale.",
        "testo_integrale": "acquisizione del modulo di adesione allo SPID sottoscritto con "
                            "firma elettronica qualificata o con firma digitale;",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 c.2 lett.e)",
        "testo": "Il gestore può verificare l'identità del richiedente mediante identificazione "
                 "informatica fornita da sistemi informatici preesistenti all'introduzione dello "
                 "SPID che risultino aver adottato, a seguito di apposita istruttoria "
                 "dell'Agenzia, regole di identificazione informatica con livelli di sicurezza "
                 "uguali o superiori a quelli definiti dal presente decreto.",
        "testo_integrale": "identificazione informatica fornita da sistemi informatici "
                            "preesistenti all'introduzione dello SPID che risultino aver "
                            "adottato, a seguito di apposita istruttoria dell'Agenzia, regole di "
                            "identificazione informatica caratterizzate da livelli di sicurezza "
                            "uguali o superiori a quelli definiti nel presente decreto.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 c.3",
        "testo": "Con i regolamenti attuativi di cui all'art. 4, l'Agenzia definisce le "
                 "modalità con cui la verifica dell'identità di cui al comma 2 è effettuata "
                 "secondo i più alti livelli di controllo disponibili, anche in relazione ai "
                 "livelli di sicurezza di cui all'art. 6.",
        "testo_integrale": "Con i regolamenti di cui all'art. 4, l'Agenzia definisce le "
                            "modalità con le quali la verifica dell'identità di cui al comma 2 "
                            "è effettuata secondo i più alti livelli di controllo disponibili, "
                            "anche in relazione ai livelli di sicurezza di cui all'art. 6.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 7 c.4",
        "testo": "Nei casi di cui alle lettere b), c) ed e) del comma 2, i dati di adesione "
                 "sono forniti direttamente dall'interessato, utilizzando i moduli informatici "
                 "messi a disposizione in rete dal gestore dell'identità digitale.",
        "testo_integrale": "Nei casi di cui alle lettere b), c) ed e) del comma 2 i dati di "
                            "adesione vengono forniti direttamente, utilizzando i moduli "
                            "informatici posti a disposizione in rete dal gestore dell'identità "
                            "digitale.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Nei casi di identificazione di cui al comma 2, lettere "
                                     "b), c) ed e).",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 c.5",
        "testo": "Al fine di documentare la corretta attribuzione dell'identità digitale, i "
                 "gestori conservano, per il periodo di cui al comma 8 e in relazione alla "
                 "modalità di identificazione utilizzata ai sensi del comma 2, copia per "
                 "immagine del documento d'identità esibito e del modulo di cui alla lettera "
                 "a), copia del log della transazione per i casi di cui alle lettere b), c) ed "
                 "e), o il modulo firmato digitalmente di cui alla lettera d), nonché i "
                 "documenti e i dati utilizzati per l'associazione e la verifica degli "
                 "attributi.",
        "testo_integrale": "I gestori dell'identità digitale, al fine di poter documentare la "
                            "corretta attribuzione della stessa, conservano per il periodo "
                            "prescritto dal comma 8, in relazione alle modalità di "
                            "identificazione di cui al comma 2, copia per immagine del "
                            "documento di identità esibito e del modulo di cui alla lettera a), "
                            "copia del log della transazione di cui alle lettere b), c) ed e) o "
                            "il modulo firmato digitalmente di cui alla lettera d), nonché i "
                            "documenti e i dati utilizzati per l'associazione e la verifica "
                            "degli attributi.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 c.6",
        "testo": "Ricevuta la richiesta di adesione, i gestori effettuano la verifica degli "
                 "attributi identificativi del richiedente utilizzando prioritariamente i "
                 "servizi convenzionali di cui all'art. 4, comma 1, lettera c).",
        "testo_integrale": "I gestori dell'identità digitale, ricevuta la richiesta di "
                            "adesione, effettuano la verifica degli attributi identificativi "
                            "del richiedente utilizzando prioritariamente i servizi "
                            "convenzionali di cui all'art. 4, comma 1, lettera c).",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 c.7",
        "testo": "Quando le informazioni necessarie per la verifica degli attributi "
                 "identificativi non sono accessibili tramite i servizi convenzionali di cui al "
                 "comma 6, i gestori effettuano tali verifiche sulla base di documenti, dati o "
                 "informazioni ottenibili da archivi delle amministrazioni certificanti, ai "
                 "sensi dell'art. 43, comma 2, del d.P.R. 28 dicembre 2000, n. 445, secondo i "
                 "criteri e le modalità stabiliti dall'Agenzia con i regolamenti di cui all'art. "
                 "4, fatto salvo il caso di cui al comma 2, lettera e).",
        "testo_integrale": "Nei casi in cui le informazioni necessarie per la verifica degli "
                            "attributi identificativi non siano accessibili tramite i servizi "
                            "convenzionali di cui al comma 6, i gestori dell'identità digitale "
                            "effettuano tali verifiche sulla base di documenti, dati o "
                            "informazioni ottenibili da archivi delle amministrazioni "
                            "certificanti, ai sensi dell'art. 43, comma 2, del decreto del "
                            "Presidente della Repubblica 28 dicembre 2000, n. 445, secondo i "
                            "criteri e le modalità stabilite dall'Agenzia con i regolamenti di "
                            "cui all'art. 4, fatto salvo il caso di cui al comma 2, lettera e).",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Quando le informazioni necessarie non sono accessibili "
                                     "tramite i servizi convenzionali di cui al comma 6; non si "
                                     "applica al caso di identificazione di cui al comma 2, "
                                     "lettera e).",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 c.8",
        "testo": "I gestori conservano la documentazione relativa al processo di adesione per "
                 "venti anni dalla scadenza o dalla revoca dell'identità digitale e, decorso "
                 "tale termine, la cancellano; salvo il caso di subentro ai sensi dell'art. 12, "
                 "il gestore che cessa l'attività prima della scadenza del termine trasmette la "
                 "documentazione all'Agenzia, che la conserva fino alla scadenza del periodo.",
        "testo_integrale": "I gestori dell'identità digitale conservano la documentazione "
                            "inerente al processo di adesione per un periodo pari a venti anni "
                            "decorrenti dalla scadenza o dalla revoca dell'identità digitale. "
                            "Alla scadenza del predetto termine, i gestori cancellano la "
                            "suddetta documentazione. Salvo il subentro ai sensi dell'art. 12, "
                            "il gestore che cessa l'attività prima della scadenza del termine di "
                            "cui al presente comma trasmette la medesima documentazione "
                            "all'Agenzia, che la conserva fino alla scadenza del suddetto "
                            "periodo.",
        "tipo_obbligo": "di conservazione",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 7 c.9",
        "testo": "I dati personali raccolti ai sensi del presente decreto sono trattati e "
                 "conservati dal gestore nel rispetto della normativa in materia di protezione "
                 "dei dati personali di cui al regolamento (UE) 2016/679 (GDPR) e al d.lgs. 30 "
                 "giugno 2003, n. 196 (modifica introdotta dal DPCM 19 ottobre 2021, art. 2).",
        "testo_integrale": "I dati personali raccolti ai sensi del presente decreto sono "
                            "trattati e conservati nel rispetto della normativa in materia di "
                            "tutela dei dati personali di cui al regolamento (UE) 2016/679 e al "
                            "decreto legislativo 30 giugno 2003, n. 196.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 8 c.1",
        "testo": "Salvo il caso in cui l'aggiornamento degli attributi identificativi avvenga "
                 "automaticamente tramite le convenzioni di cui all'art. 4, comma 1, lettera "
                 "c), l'utente è obbligato a informare tempestivamente il gestore di ogni "
                 "variazione degli attributi comunicati in precedenza; il gestore provvede "
                 "tempestivamente ai necessari aggiornamenti, dopo aver verificato le "
                 "informazioni fornite secondo le modalità di cui all'art. 7, comma 7.",
        "testo_integrale": "Fatto salvo il caso in cui l'aggiornamento degli attributi "
                            "identificativi avvenga in modalità automatica tramite le "
                            "convenzioni previste all'art. 4, comma 1, lettera c), gli utenti "
                            "sono obbligati a informare tempestivamente il gestore "
                            "dell'identità digitale di ogni variazione degli attributi "
                            "previamente comunicati. Il gestore dell'identità digitale provvede "
                            "tempestivamente ai necessari aggiornamenti, avendo verificato le "
                            "informazioni fornite secondo le modalità di cui all'art. 7, comma "
                            "7.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Salvo il caso in cui l'aggiornamento degli attributi "
                                     "identificativi avvenga in modalità automatica tramite le "
                                     "convenzioni di cui all'art. 4, comma 1, lettera c).",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "obbligato"},
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 8 c.2",
        "testo": "Fatti salvi i casi previsti dall'art. 9, l'utente può chiedere in qualsiasi "
                 "momento e a titolo gratuito al gestore la sospensione o la revoca della "
                 "propria identità digitale, ovvero la modifica dei propri attributi secondari "
                 "e delle proprie credenziali di accesso, e il gestore provvede tempestivamente "
                 "a tali richieste; l'Agenzia, con i regolamenti di cui all'art. 4, stabilisce "
                 "le procedure per consentire agli utenti la rimozione dei dati contenuti "
                 "nell'identità digitale.",
        "testo_integrale": "Fatti salvi i casi previsti dall'art. 9, l'utente può chiedere al "
                            "gestore dell'identità digitale, in qualsiasi momento e a titolo "
                            "gratuito, la sospensione o revoca della propria identità digitale "
                            "ovvero la modifica dei propri attributi secondari e delle proprie "
                            "credenziali di accesso. A tali richieste il gestore dell'identità "
                            "digitale provvede tempestivamente. L'Agenzia, con i regolamenti di "
                            "cui all'art. 4, stabilisce le procedure per consentire agli utenti "
                            "la rimozione dei dati contenuti nell'identità digitale.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Fatti salvi i casi previsti dall'art. 9.",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 8 c.3",
        "testo": "Il gestore revoca l'identità digitale se ne riscontra l'inattività per oltre "
                 "ventiquattro mesi, oppure in caso di decesso della persona fisica o di "
                 "estinzione della persona giuridica, utilizzando i servizi messi a "
                 "disposizione dalle convenzioni di cui all'art. 4, comma 1, lettera c) o, "
                 "quando l'informazione non sia disponibile in tali ambiti, attivando opportune "
                 "e documentate verifiche delle informazioni ricevute.",
        "testo_integrale": "Il gestore dell'identità digitale revoca l'identità digitale se "
                            "riscontra l'inattività della stessa per un periodo superiore a "
                            "ventiquattro mesi o in caso di decesso della persona fisica o di "
                            "estinzione della persona giuridica, utilizzando i servizi messi a "
                            "disposizione dalle convenzioni di cui all'art. 4, comma 1, lettera "
                            "c), ovvero, laddove l'informazione non sia disponibile in tali "
                            "ambiti, attivando opportune e documentate verifiche delle "
                            "informazioni ricevute.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 8 c.4",
        "testo": "Su richiesta dell'utente, il gestore gli segnala ogni avvenuto utilizzo delle "
                 "credenziali di accesso, inviandone gli estremi a uno degli attributi "
                 "secondari indicati a tale scopo dall'utente stesso, secondo le regole "
                 "tecniche definite con i regolamenti di cui all'art. 4.",
        "testo_integrale": "Il gestore dell'identità digitale, su richiesta dell'utente, gli "
                            "segnala ogni avvenuto utilizzo delle credenziali di accesso, "
                            "inviandone gli estremi ad uno degli attributi secondari a tale "
                            "scopo indicato dall'utente stesso, secondo le regole tecniche "
                            "definite con i regolamenti di cui all'art. 4.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Su richiesta dell'utente.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 8 c.5",
        "testo": "I gestori di identità SPID possono stipulare accordi con le pubbliche "
                 "amministrazioni per importare nel sistema SPID identità digitali da esse "
                 "rilasciate, conformemente a quanto previsto dall'art. 7.",
        "testo_integrale": "I gestori di identità SPID possono stipulare accordi con pubbliche "
                            "amministrazioni al fine di importare nel sistema SPID identità "
                            "digitali rilasciate dalle pubbliche amministrazioni conformemente "
                            "a quanto previsto dall'art. 7.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 9 c.1",
        "testo": "Se l'utente ritiene, anche a seguito della segnalazione di cui all'art. 8, "
                 "comma 4, che la propria identità digitale sia stata utilizzata abusivamente o "
                 "fraudolentemente da un terzo, può chiedere, con le modalità indicate nei "
                 "regolamenti di cui all'art. 4, la sospensione immediata dell'identità "
                 "digitale al gestore e, se conosciuto, al fornitore di servizi presso cui è "
                 "stata utilizzata; salvo che la richiesta sia inviata via posta elettronica "
                 "certificata o sottoscritta con firma digitale o firma elettronica qualificata, "
                 "il gestore e l'eventuale fornitore di servizi contattato verificano, anche "
                 "tramite uno o più attributi secondari, la provenienza della richiesta da "
                 "parte del titolare e ne confermano la ricezione.",
        "testo_integrale": "Nel caso in cui l'utente ritenga, anche a seguito della "
                            "segnalazione di cui all'art. 8, comma 4, che la propria identità "
                            "digitale sia stata utilizzata abusivamente o fraudolentemente da "
                            "un terzo, può chiedere, con le modalità indicate nei regolamenti "
                            "di cui all'art. 4, la sospensione immediata dell'identità digitale "
                            "al gestore della stessa e, se conosciuto, al fornitore di servizi "
                            "presso il quale essa risulta essere stata utilizzata. Salvo il "
                            "caso in cui la richiesta sia inviata tramite posta elettronica "
                            "certificata, o sottoscritta con firma digitale o firma elettronica "
                            "qualificata, il gestore dell'identità digitale e il fornitore di "
                            "servizi eventualmente contattato verificano, anche attraverso uno "
                            "o più attributi secondari, la provenienza della richiesta di "
                            "sospensione da parte del soggetto titolare dell'identità digitale "
                            "e forniscono la conferma della ricezione della medesima richiesta.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Se la richiesta di sospensione non è inviata tramite posta "
                                     "elettronica certificata né sottoscritta con firma digitale "
                                     "o firma elettronica qualificata, gestore e fornitore di "
                                     "servizi contattato devono verificarne la provenienza.",
        "soggetti": [
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 9 c.2",
        "testo": "Nel caso previsto dal comma 1, il gestore sospende tempestivamente "
                 "l'identità digitale per un periodo massimo di trenta giorni, informandone il "
                 "richiedente; scaduto tale periodo, l'identità digitale è ripristinata o "
                 "revocata ai sensi del comma 3.",
        "testo_integrale": "Nel caso previsto dal comma 1, il gestore dell'identità digitale "
                            "sospende tempestivamente l'identità digitale per un periodo "
                            "massimo di trenta giorni informandone il richiedente. Scaduto tale "
                            "periodo, l'identità digitale è ripristinata o revocata ai sensi "
                            "del comma 3.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Nel caso previsto dal comma 1.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 9 c.3",
        "testo": "Il gestore revoca l'identità digitale se, entro i termini previsti dal comma "
                 "2, riceve dall'interessato copia della denuncia presentata all'autorità "
                 "giudiziaria per gli stessi fatti su cui si basa la richiesta di sospensione.",
        "testo_integrale": "Il gestore revoca l'identità digitale se, nei termini previsti dal "
                            "comma 2, riceve dall'interessato copia della denuncia presentata "
                            "all'autorità giudiziaria per gli stessi fatti su cui è basata la "
                            "richiesta di sospensione.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 c.1",
        "testo": "Le modalità di richiesta di accreditamento sono definite nei regolamenti "
                 "attuativi adottati dall'Agenzia ai sensi dell'art. 4, che possono contenere "
                 "ulteriori criteri per l'accreditamento delle pubbliche amministrazioni.",
        "testo_integrale": "Le modalità di richiesta di accreditamento sono definite nei "
                            "regolamenti attuativi adottati dall'Agenzia ai sensi dell'art. 4, "
                            "che possono contenere ulteriori criteri per l'accreditamento delle "
                            "pubbliche amministrazioni.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 10 c.2",
        "testo": "Accolta la richiesta, l'Agenzia stipula apposita convenzione secondo lo "
                 "schema definito nei regolamenti di cui all'art. 4 e dispone l'iscrizione del "
                 "richiedente nel registro SPID, consultabile per via telematica.",
        "testo_integrale": "A seguito dell'accoglimento della richiesta, l'Agenzia stipula "
                            "apposita convenzione secondo lo schema definito nell'ambito dei "
                            "regolamenti di cui all'art. 4 e dispone l'iscrizione del "
                            "richiedente nel registro SPID, consultabile in via telematica.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "destinatario"}],
    },
    {
        "riferimento": "art. 10 c.3 lett.a)",
        "testo": "Per ottenere l'accreditamento, il richiedente deve avere forma giuridica di "
                 "società di capitali e un capitale sociale non inferiore a cinque milioni di "
                 "euro.",
        "testo_integrale": "avere forma giuridica di società di capitali e un capitale sociale "
                            "non inferiore a cinque milioni di euro;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 c.3 lett.0-b)",
        "testo": "Per ottenere l'accreditamento, il richiedente deve essere una persona "
                 "giuridica riconosciuta, con un patrimonio o un capitale sociale non inferiore "
                 "a trecentomila euro e con un'organizzazione consolidata e pienamente "
                 "operativa sotto tutti gli aspetti pertinenti per la fornitura dei servizi "
                 "(lettera introdotta dal DPCM 19 ottobre 2021, art. 3).",
        "testo_integrale": "essere una persona giuridica riconosciuta, con un patrimonio o un "
                            "capitale sociale non inferiore a trecentomila euro e con "
                            "un'organizzazione consolidata e pienamente operativa sotto tutti "
                            "gli aspetti pertinenti per la fornitura dei servizi;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 c.3 lett.b)",
        "testo": "Per ottenere l'accreditamento, il richiedente deve garantire che i "
                 "rappresentanti legali, i soggetti preposti all'amministrazione e i "
                 "componenti degli organi di controllo possiedano i requisiti di onorabilità "
                 "richiesti a chi svolge funzioni di amministrazione, direzione e controllo "
                 "presso banche ai sensi dell'art. 26 del d.lgs. 1° settembre 1993, n. 385.",
        "testo_integrale": "garantire il possesso, da parte dei rappresentanti legali, dei "
                            "soggetti preposti all'amministrazione e dei componenti degli "
                            "organi preposti al controllo, dei requisiti di onorabilità "
                            "richiesti ai soggetti che svolgono funzioni di amministrazione, "
                            "direzione e controllo presso banche ai sensi dell'art. 26 del "
                            "decreto legislativo 1° settembre 1993, n. 385;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 c.3 lett.c)",
        "testo": "Per ottenere l'accreditamento, il richiedente deve dimostrare la capacità "
                 "organizzativa e tecnica necessaria per svolgere l'attività di gestione "
                 "dell'identità digitale.",
        "testo_integrale": "dimostrare la capacità organizzativa e tecnica necessaria per "
                            "svolgere l'attività di gestione dell'identità digitale;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 c.3 lett.c-bis)",
        "testo": "Per ottenere l'accreditamento, il richiedente deve disporre, per il "
                 "risarcimento dei danni causati con dolo o colpa a qualsiasi persona fisica o "
                 "giuridica a causa del mancato adempimento degli obblighi connessi alla "
                 "gestione del sistema SPID, di un'adeguata copertura assicurativa di almeno "
                 "1,5 milioni di euro annui e 150.000 euro per singolo sinistro (lettera "
                 "introdotta dal DPCM 19 ottobre 2021, art. 3).",
        "testo_integrale": "disporre, per il risarcimento dei danni causati, con dolo o colpa, "
                            "a qualsiasi persona fisica o giuridica a causa del mancato "
                            "adempimento degli obblighi connessi alla gestione del sistema "
                            "SPID, di una adeguata copertura assicurativa di almeno 1,5 milioni "
                            "di euro annui e centocinquantamila euro per singolo sinistro;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 c.3 lett.d)",
        "testo": "Per ottenere l'accreditamento, il richiedente deve utilizzare personale "
                 "dotato delle conoscenze, dell'esperienza e delle competenze necessarie per i "
                 "servizi da fornire; in particolare, il personale addetto alla realizzazione e "
                 "gestione del sistema informatico deve possedere, in relazione alle attività "
                 "svolte, competenza gestionale e adeguata conoscenza delle procedure operative "
                 "e di sicurezza e delle regole tecniche applicabili, e il gestore provvede al "
                 "suo periodico aggiornamento professionale.",
        "testo_integrale": "utilizzare personale dotato delle conoscenze specifiche, "
                            "dell'esperienza e delle competenze necessarie per i servizi da "
                            "fornire. In particolare, il personale addetto alla realizzazione e "
                            "gestione del sistema informatico deve possedere, in relazione alle "
                            "attività da svolgere, la competenza gestionale, l'appropriata "
                            "conoscenza e padronanza delle procedure operative e di sicurezza, "
                            "nonché delle regole tecniche da applicare. Il gestore provvede al "
                            "periodico aggiornamento professionale del personale;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 c.3 lett.e)",
        "testo": "Per ottenere l'accreditamento, il richiedente deve comunicare all'Agenzia i "
                 "nominativi e il profilo professionale dei soggetti responsabili delle "
                 "specifiche funzioni individuate nei regolamenti attuativi adottati "
                 "dall'Agenzia ai sensi dell'art. 4.",
        "testo_integrale": "comunicare all'Agenzia i nominativi e il profilo professionale dei "
                            "soggetti responsabili delle specifiche funzioni individuate nei "
                            "regolamenti attuativi adottati dall'Agenzia ai sensi dell'art. 4;",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 c.3 lett.f)",
        "testo": "Per ottenere l'accreditamento, il richiedente deve possedere la "
                 "certificazione di conformità alla norma ISO/IEC 27001 del proprio sistema di "
                 "gestione per la sicurezza delle informazioni, rilasciata da un terzo "
                 "indipendente autorizzato secondo le norme vigenti in materia.",
        "testo_integrale": "essere in possesso della certificazione di conformità del proprio "
                            "sistema di gestione per la sicurezza delle informazioni ad essi "
                            "relative, alla norma ISO/IEC 27001, rilasciata da un terzo "
                            "indipendente a tal fine autorizzato secondo le norme vigenti in "
                            "materia;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 c.3 lett.g)",
        "testo": "Per ottenere l'accreditamento, il richiedente deve trattare i dati personali "
                 "nel rispetto del regolamento (UE) 2016/679 (GDPR) e del d.lgs. 30 giugno "
                 "2003, n. 196 (modifica introdotta dal DPCM 19 ottobre 2021, art. 3).",
        "testo_integrale": "trattare i dati personali nel rispetto del regolamento (UE) "
                            "2016/679 e del decreto legislativo 30 giugno 2003, n. 196;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 c.3 lett.h)",
        "testo": "Per ottenere l'accreditamento, il richiedente deve possedere la "
                 "certificazione di qualità ISO 9001, sue successive modifiche o norme "
                 "equivalenti.",
        "testo_integrale": "essere in possesso della certificazione di qualità ISO 9001, "
                            "successive modifiche o norme equivalenti.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 10 c.5",
        "testo": "L'Agenzia procede, d'ufficio o su segnalazione motivata di soggetti pubblici "
                 "o privati, a controlli volti ad accertare il permanere dei requisiti previsti "
                 "dal presente decreto; se accerta la mancanza dei requisiti per l'iscrizione "
                 "nel registro SPID e, decorso il termine fissato per il loro ripristino, "
                 "questi non sono ripristinati, l'Agenzia, con provvedimento motivato "
                 "notificato all'interessato, può adottare le azioni previste dall'art. 12.",
        "testo_integrale": "L'Agenzia procede, d'ufficio o su segnalazione motivata di soggetti "
                            "pubblici o privati, a controlli volti ad accertare la permanenza "
                            "della sussistenza dei requisiti previsti dal presente decreto. Se, "
                            "all'esito dei controlli, accerta la mancanza dei requisiti "
                            "richiesti per l'iscrizione nel registro SPID, decorso il termine "
                            "fissato per consentire il ripristino degli stessi, l'Agenzia, con "
                            "provvedimento motivato notificato all'interessato, può adottare le "
                            "azioni previste dall'art. 12.",
        "tipo_obbligo": "sanzionatorio",
        "stato": "vigente",
        "sanzioni": "Sospensione dell'attività di attribuzione di identità digitali o revoca "
                    "dell'accreditamento, secondo le azioni previste dall'art. 12.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "destinatario"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.a)",
        "testo": "I gestori dell'identità digitale utilizzano sistemi affidabili che "
                 "garantiscono la sicurezza tecnica e crittografica dei procedimenti, in "
                 "conformità a criteri di sicurezza riconosciuti in ambito europeo o "
                 "internazionale.",
        "testo_integrale": "utilizzano sistemi affidabili che garantiscono la sicurezza tecnica "
                            "e crittografica dei procedimenti, in conformità a criteri di "
                            "sicurezza riconosciuti in ambito europeo o internazionale;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.b)",
        "testo": "I gestori adottano adeguate misure contro la contraffazione, idonee a "
                 "garantire riservatezza, integrità e sicurezza nella generazione delle "
                 "credenziali di accesso.",
        "testo_integrale": "adottano adeguate misure contro la contraffazione, idonee anche a "
                            "garantire la riservatezza, l'integrità e la sicurezza nella "
                            "generazione delle credenziali di accesso;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.c)",
        "testo": "I gestori effettuano un monitoraggio continuo per rilevare usi impropri o "
                 "tentativi di violazione delle credenziali di accesso dell'identità digitale "
                 "di ciascun utente, sospendendo l'identità digitale in caso di attività "
                 "sospetta.",
        "testo_integrale": "effettuano un monitoraggio continuo al fine rilevare usi impropri o "
                            "tentativi di violazione delle credenziali di accesso dell'identità "
                            "digitale di ciascun utente, procedendo alla sospensione "
                            "dell'identità digitale in caso di attività sospetta;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.d)",
        "testo": "I gestori effettuano, con cadenza almeno annuale, un'analisi dei rischi.",
        "testo_integrale": "effettuano, con cadenza almeno annuale, un'analisi dei rischi;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.e)",
        "testo": "I gestori definiscono il piano per la sicurezza dei servizi SPID, lo "
                 "trasmettono all'Agenzia e ne garantiscono l'aggiornamento.",
        "testo_integrale": "definiscono il piano per la sicurezza dei servizi SPID, da "
                            "trasmettere all'Agenzia, e ne garantiscono l'aggiornamento;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.f)",
        "testo": "I gestori allineano le procedure di sicurezza agli standard internazionali, "
                 "la cui conformità è certificata da un terzo abilitato.",
        "testo_integrale": "allineano le procedure di sicurezza agli standard internazionali, "
                            "la cui conformità è certificata da un terzo abilitato;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.g)",
        "testo": "I gestori conducono, con cadenza almeno semestrale, il «Penetration Test».",
        "testo_integrale": "conducono, con cadenza almeno semestrale, il «Penetration Test»;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.h)",
        "testo": "I gestori garantiscono la continuità operativa dei servizi afferenti allo "
                 "SPID.",
        "testo_integrale": "garantiscono la continuità operativa dei servizi afferenti allo "
                            "SPID;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.i)",
        "testo": "I gestori effettuano ininterrottamente l'attività di monitoraggio della "
                 "sicurezza dei sistemi, garantendo la gestione degli incidenti da parte di "
                 "un'apposita struttura interna.",
        "testo_integrale": "effettuano ininterrottamente l'attività di monitoraggio della "
                            "sicurezza dei sistemi, garantendo la gestione degli incidenti da "
                            "parte di un'apposita struttura interna;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.l)",
        "testo": "I gestori garantiscono la gestione sicura delle componenti riservate delle "
                 "identità digitali degli utenti, assicurando che non siano rese disponibili a "
                 "terzi, inclusi i fornitori di servizi, nemmeno in forma cifrata.",
        "testo_integrale": "garantiscono la gestione sicura delle componenti riservate delle "
                            "identità digitali degli utenti, assicurando che le stesse non "
                            "siano rese disponibili a terzi, ivi compresi i fornitori di "
                            "servizi stessi, neppure in forma cifrata;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.m)",
        "testo": "I gestori garantiscono la disponibilità delle funzioni, l'applicazione dei "
                 "modelli architetturali e il rispetto delle disposizioni previste dal presente "
                 "decreto e dai regolamenti attuativi adottati dall'Agenzia ai sensi dell'art. "
                 "4.",
        "testo_integrale": "garantiscono la disponibilità delle funzioni, l'applicazione dei "
                            "modelli architetturali e il rispetto delle disposizioni previste "
                            "dal presente decreto e dai regolamenti attuativi adottati "
                            "dall'Agenzia ai sensi dell'art. 4;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.n)",
        "testo": "I gestori si sottopongono, con cadenza almeno biennale, a una verifica di "
                 "conformità alle disposizioni vigenti da parte di un organismo di valutazione "
                 "accreditato ai sensi del Regolamento CE 765/2008, e inviano all'Agenzia "
                 "l'esito della verifica, redatto dall'organismo in lingua inglese, entro tre "
                 "giorni lavorativi dalla ricezione.",
        "testo_integrale": "si sottopongono, con cadenza almeno biennale, ad una verifica di "
                            "conformità alle disposizioni vigenti da parte di un organismo di "
                            "valutazione accreditato ai sensi del Regolamento CE 765/2008 del "
                            "Parlamento Europeo e del Consiglio del 9 luglio 2008. Inviano "
                            "all'Agenzia l'esito della verifica, redatto dall'organismo di "
                            "valutazione in lingua inglese, entro tre giorni lavorativi dalla "
                            "sua ricezione;",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.o)",
        "testo": "I gestori informano tempestivamente l'Agenzia e il Garante per la protezione "
                 "dei dati personali di eventuali violazioni di dati personali, secondo le "
                 "modalità individuate nei regolamenti adottati ai sensi dell'art. 4.",
        "testo_integrale": "informano tempestivamente l'Agenzia e il Garante per la protezione "
                            "dei dati personali su eventuali violazioni di dati personali, "
                            "secondo le modalità individuate nei regolamenti adottati ai sensi "
                            "dell'art. 4;",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.p)",
        "testo": "I gestori adeguano i propri sistemi a seguito degli aggiornamenti emanati "
                 "dall'Agenzia.",
        "testo_integrale": "adeguano i propri sistemi a seguito degli aggiornamenti emanati "
                            "dall'Agenzia;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 11 c.1 lett.q)",
        "testo": "I gestori inviano all'Agenzia, in forma aggregata, i dati da questa richiesti "
                 "a fini statistici, che potranno essere resi pubblici.",
        "testo_integrale": "inviano all'Agenzia, in forma aggregata, i dati da questa richiesti "
                            "a fini statistici, che potranno essere resi pubblici.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "condizione_applicabilita": "Nel rispetto dei regolamenti attuativi adottati "
                                     "dall'Agenzia ai sensi dell'art. 4.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 12 c.1",
        "testo": "Il gestore comunica all'Agenzia e agli utenti a cui ha attribuito l'identità "
                 "digitale l'intenzione di cessare la propria attività, almeno sessanta giorni "
                 "prima della cessazione, indicando i gestori sostitutivi e le modalità "
                 "tecniche e operative per il trasferimento delle identità digitali, nel "
                 "rispetto delle indicazioni fornite dall'Agenzia ai sensi dell'art. 4 "
                 "(termine e contenuto modificati dal DPCM 19 ottobre 2021, art. 4).",
        "testo_integrale": "Il gestore dell'identità digitale comunica all'Agenzia e agli "
                            "utenti a cui ha attribuito l'identità digitale l'intenzione di "
                            "cessare la propria attività almeno sessanta giorni prima della "
                            "data di cessazione, indicando i gestori sostitutivi e le modalità "
                            "tecniche e operative per il trasferimento delle identità "
                            "digitali, nel rispetto delle indicazioni fornite dall'Agenzia ai "
                            "sensi dell'art. 4.",
        "tipo_obbligo": "informativo/trasparenza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 12 c.2",
        "testo": "Previo invio all'Agenzia della dichiarazione di accettazione e il recepimento "
                 "di eventuali prescrizioni dell'Agenzia sulle modalità del trasferimento, e "
                 "previa acquisizione del consenso degli utenti, il gestore sostitutivo "
                 "subentra nella gestione delle identità digitali rilasciate dal gestore "
                 "cessato e nella conservazione delle informazioni di cui all'art. 7, comma 8 "
                 "(integrato dal DPCM 19 ottobre 2021, art. 4).",
        "testo_integrale": "Il gestore sostitutivo, previo invio all'Agenzia della "
                            "dichiarazione di accettazione, recepimento di eventuali "
                            "prescrizioni dell'Agenzia in ordine alle modalità del "
                            "trasferimento, e previa acquisizione del consenso degli utenti, "
                            "subentra nella gestione delle identità digitali rilasciate dal "
                            "gestore cessato e nella conservazione delle informazioni di cui "
                            "all'art. 7, comma 8.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "Previo invio all'Agenzia della dichiarazione di "
                                     "accettazione, recepimento di eventuali prescrizioni "
                                     "dell'Agenzia sulle modalità del trasferimento, e previa "
                                     "acquisizione del consenso degli utenti.",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 12 c.3",
        "testo": "Salvo quanto disposto al comma 2, il gestore che cessa la propria attività "
                 "revoca le identità digitali rilasciate, scaduto il termine previsto dal comma "
                 "1 (comma soppresso dal DPCM 19 ottobre 2021, art. 4 c.1 lett.c); testo "
                 "riportato per completezza storica, non più vigente).",
        "testo_integrale": "Salvo quanto disposto al comma 2, il gestore dell'identità "
                            "digitale che cessa la propria attività, scaduto il termine del "
                            "periodo previsto al comma 1, revoca le identità digitali "
                            "rilasciate.",
        "tipo_obbligo": "procedurale",
        "stato": "abrogato",
        "condizione_applicabilita": "Salvo il caso di subentro previsto dal comma 2; scaduto il "
                                     "termine di trenta giorni di cui al comma 1 (testo "
                                     "previgente, comma soppresso dal 2021).",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 12 c.4",
        "testo": "Previo accertamento della violazione delle disposizioni del presente decreto "
                 "e dei regolamenti attuativi ex art. 4, l'Agenzia può disporre la sospensione "
                 "dell'attività di attribuzione di identità digitali per un periodo da un mese "
                 "a un anno oppure, nei casi più gravi, la revoca dell'accreditamento del "
                 "gestore.",
        "testo_integrale": "L'Agenzia, previo accertamento della violazione delle disposizioni "
                            "di cui al presente decreto e dei regolamenti attuativi adottati ai "
                            "sensi dell'art. 4, può disporre la sospensione dell'attività di "
                            "attribuzione di identità digitali per un periodo minimo di un mese "
                            "e massimo di un anno o, nei casi più gravi, la revoca "
                            "dell'accreditamento del gestore dell'identità digitale.",
        "tipo_obbligo": "sanzionatorio",
        "stato": "vigente",
        "sanzioni": "Sospensione dell'attività di attribuzione di identità digitali da un "
                    "minimo di un mese a un massimo di un anno oppure, nei casi più gravi, "
                    "revoca dell'accreditamento del gestore.",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "destinatario"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 10 c.4",
        "testo": "I requisiti di forma giuridica e capitale sociale minimo (lettera a), di "
                 "onorabilità dei rappresentanti (lettera b) e di copertura assicurativa "
                 "(lettera c-bis) del comma 3 non si applicano alle pubbliche amministrazioni "
                 "che chiedono l'accreditamento come gestore dell'identità digitale (rinvio "
                 "aggiornato dal DPCM 19 ottobre 2021, art. 3).",
        "testo_integrale": "Le lettere a), b) e c-bis) del comma 3 non si applicano alle "
                            "pubbliche amministrazioni che chiedono l'accreditamento al fine "
                            "di svolgere l'attività di gestore dell'identità digitale.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 12 c.5",
        "testo": "In caso di revoca dell'accreditamento del gestore dell'identità digitale si "
                 "applicano le disposizioni relative alla cessazione dell'attività previste dal "
                 "presente articolo.",
        "testo_integrale": "In caso di revoca dell'accreditamento del gestore dell'identità "
                            "digitale si applicano le disposizioni relative alle cessazioni di "
                            "cui al presente articolo.",
        "tipo_principio": "equivalenza giuridica",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 12 c.5-bis",
        "testo": "Se, a seguito della cessazione dell'attività di un gestore o della revoca "
                 "del suo accreditamento, nessun altro gestore è disponibile a subentrare "
                 "secondo le modalità del comma 2, l'Agenzia, con determinazione del direttore "
                 "generale che reca anche prescrizioni sulle modalità del trasferimento, "
                 "ridistribuisce le identità digitali rilasciate dal gestore cessato o "
                 "revocato tra tutti gli altri gestori, in proporzione alla quota di identità "
                 "SPID già rilasciate da ciascuno alla data della cessazione o della revoca "
                 "(comma introdotto dal DPCM 19 ottobre 2021, art. 4).",
        "testo_integrale": "Nel caso in cui, a seguito della cessazione dell'attività da parte "
                            "di un gestore dell'identità digitale o della revoca del suo "
                            "accreditamento, nessun altro gestore è disponibile a subentrare "
                            "con le modalità del comma 2, l'Agenzia, con determinazione del "
                            "direttore generale recante anche prescrizioni in ordine alle "
                            "modalità del trasferimento, provvede a ridistribuire le identità "
                            "digitali rilasciate dal gestore cessato o revocato tra tutti gli "
                            "altri gestori che subentreranno nella relativa gestione in misura "
                            "proporzionale alla ripartizione percentuale, tra gli stessi, di "
                            "tutte le identità SPID rilasciate alla data della cessazione o "
                            "della revoca.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 7 c.1",
    "art. 7 c.2 lett.a)",
    "art. 7 c.2 lett.b)",
    "art. 7 c.2 lett.c)",
    "art. 7 c.2 lett.d)",
    "art. 7 c.2 lett.e)",
    "art. 7 c.3",
    "art. 7 c.4",
    "art. 7 c.5",
    "art. 7 c.6",
    "art. 7 c.7",
    "art. 7 c.8",
    "art. 7 c.9",
    "art. 8 c.1",
    "art. 8 c.2",
    "art. 8 c.3",
    "art. 8 c.4",
    "art. 8 c.5",
    "art. 9 c.1",
    "art. 9 c.2",
    "art. 9 c.3",
    "art. 10 c.1",
    "art. 10 c.2",
    "art. 10 c.3 lett.a)",
    "art. 10 c.3 lett.0-b)",
    "art. 10 c.3 lett.b)",
    "art. 10 c.3 lett.c)",
    "art. 10 c.3 lett.c-bis)",
    "art. 10 c.3 lett.d)",
    "art. 10 c.3 lett.e)",
    "art. 10 c.3 lett.f)",
    "art. 10 c.3 lett.g)",
    "art. 10 c.3 lett.h)",
    "art. 10 c.4",
    "art. 10 c.5",
    "art. 11 c.1 lett.a)",
    "art. 11 c.1 lett.b)",
    "art. 11 c.1 lett.c)",
    "art. 11 c.1 lett.d)",
    "art. 11 c.1 lett.e)",
    "art. 11 c.1 lett.f)",
    "art. 11 c.1 lett.g)",
    "art. 11 c.1 lett.h)",
    "art. 11 c.1 lett.i)",
    "art. 11 c.1 lett.l)",
    "art. 11 c.1 lett.m)",
    "art. 11 c.1 lett.n)",
    "art. 11 c.1 lett.o)",
    "art. 11 c.1 lett.p)",
    "art. 11 c.1 lett.q)",
    "art. 12 c.1",
    "art. 12 c.2",
    "art. 12 c.3",
    "art. 12 c.4",
    "art. 12 c.5",
    "art. 12 c.5-bis",
]

MAPPATURA_LOCALE = {
    "art. 7 c.1": ["art. 7 c.1"],
    "art. 7 c.2 lett.a)": ["art. 7 c.2 lett.a)"],
    "art. 7 c.2 lett.b)": ["art. 7 c.2 lett.b)"],
    "art. 7 c.2 lett.c)": ["art. 7 c.2 lett.c)"],
    "art. 7 c.2 lett.d)": ["art. 7 c.2 lett.d)"],
    "art. 7 c.2 lett.e)": ["art. 7 c.2 lett.e)"],
    "art. 7 c.3": ["art. 7 c.3"],
    "art. 7 c.4": ["art. 7 c.4"],
    "art. 7 c.5": ["art. 7 c.5"],
    "art. 7 c.6": ["art. 7 c.6"],
    "art. 7 c.7": ["art. 7 c.7"],
    "art. 7 c.8": ["art. 7 c.8"],
    "art. 7 c.9": ["art. 7 c.9"],
    "art. 8 c.1": ["art. 8 c.1"],
    "art. 8 c.2": ["art. 8 c.2"],
    "art. 8 c.3": ["art. 8 c.3"],
    "art. 8 c.4": ["art. 8 c.4"],
    "art. 8 c.5": ["art. 8 c.5"],
    "art. 9 c.1": ["art. 9 c.1"],
    "art. 9 c.2": ["art. 9 c.2"],
    "art. 9 c.3": ["art. 9 c.3"],
    "art. 10 c.1": ["art. 10 c.1"],
    "art. 10 c.2": ["art. 10 c.2"],
    "art. 10 c.3 lett.a)": ["art. 10 c.3 lett.a)"],
    "art. 10 c.3 lett.0-b)": ["art. 10 c.3 lett.0-b)"],
    "art. 10 c.3 lett.b)": ["art. 10 c.3 lett.b)"],
    "art. 10 c.3 lett.c)": ["art. 10 c.3 lett.c)"],
    "art. 10 c.3 lett.c-bis)": ["art. 10 c.3 lett.c-bis)"],
    "art. 10 c.3 lett.d)": ["art. 10 c.3 lett.d)"],
    "art. 10 c.3 lett.e)": ["art. 10 c.3 lett.e)"],
    "art. 10 c.3 lett.f)": ["art. 10 c.3 lett.f)"],
    "art. 10 c.3 lett.g)": ["art. 10 c.3 lett.g)"],
    "art. 10 c.3 lett.h)": ["art. 10 c.3 lett.h)"],
    "art. 10 c.4": ["art. 10 c.4"],
    "art. 10 c.5": ["art. 10 c.5"],
    "art. 11 c.1 lett.a)": ["art. 11 c.1 lett.a)"],
    "art. 11 c.1 lett.b)": ["art. 11 c.1 lett.b)"],
    "art. 11 c.1 lett.c)": ["art. 11 c.1 lett.c)"],
    "art. 11 c.1 lett.d)": ["art. 11 c.1 lett.d)"],
    "art. 11 c.1 lett.e)": ["art. 11 c.1 lett.e)"],
    "art. 11 c.1 lett.f)": ["art. 11 c.1 lett.f)"],
    "art. 11 c.1 lett.g)": ["art. 11 c.1 lett.g)"],
    "art. 11 c.1 lett.h)": ["art. 11 c.1 lett.h)"],
    "art. 11 c.1 lett.i)": ["art. 11 c.1 lett.i)"],
    "art. 11 c.1 lett.l)": ["art. 11 c.1 lett.l)"],
    "art. 11 c.1 lett.m)": ["art. 11 c.1 lett.m)"],
    "art. 11 c.1 lett.n)": ["art. 11 c.1 lett.n)"],
    "art. 11 c.1 lett.o)": ["art. 11 c.1 lett.o)"],
    "art. 11 c.1 lett.p)": ["art. 11 c.1 lett.p)"],
    "art. 11 c.1 lett.q)": ["art. 11 c.1 lett.q)"],
    "art. 12 c.1": ["art. 12 c.1"],
    "art. 12 c.2": ["art. 12 c.2"],
    "art. 12 c.3": ["art. 12 c.3"],
    "art. 12 c.4": ["art. 12 c.4"],
    "art. 12 c.5": ["art. 12 c.5"],
    "art. 12 c.5-bis": ["art. 12 c.5-bis"],
}

RELAZIONI = [
    {
        "nodo_da": ("obbligo", None, "art. 7 c.4"),
        "nodo_a": ("obbligo", None, "art. 7 c.2 lett.b)"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 c.4"),
        "nodo_a": ("obbligo", None, "art. 7 c.2 lett.c)"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 c.4"),
        "nodo_a": ("obbligo", None, "art. 7 c.2 lett.e)"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 c.5"),
        "nodo_a": ("obbligo", None, "art. 7 c.2 lett.a)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 c.5"),
        "nodo_a": ("obbligo", None, "art. 7 c.2 lett.b)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 c.5"),
        "nodo_a": ("obbligo", None, "art. 7 c.2 lett.c)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 c.5"),
        "nodo_a": ("obbligo", None, "art. 7 c.2 lett.d)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 c.5"),
        "nodo_a": ("obbligo", None, "art. 7 c.2 lett.e)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 c.5"),
        "nodo_a": ("obbligo", None, "art. 7 c.8"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 c.7"),
        "nodo_a": ("obbligo", None, "art. 7 c.6"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 c.7"),
        "nodo_a": ("obbligo", None, "art. 7 c.2 lett.e)"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 7 c.8"),
        "nodo_a": ("obbligo", None, "art. 12 c.2"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 8 c.1"),
        "nodo_a": ("obbligo", None, "art. 7 c.7"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 8 c.2"),
        "nodo_a": ("obbligo", None, "art. 9 c.1"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 c.1"),
        "nodo_a": ("obbligo", None, "art. 8 c.4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 c.2"),
        "nodo_a": ("obbligo", None, "art. 9 c.1"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 c.2"),
        "nodo_a": ("obbligo", None, "art. 9 c.3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 9 c.3"),
        "nodo_a": ("obbligo", None, "art. 9 c.2"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "art. 10 c.4"),
        "nodo_a": ("obbligo", None, "art. 10 c.3 lett.a)"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "art. 10 c.4"),
        "nodo_a": ("obbligo", None, "art. 10 c.3 lett.b)"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 10 c.5"),
        "nodo_a": ("obbligo", None, "art. 10 c.3 lett.a)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 12 c.4"),
        "nodo_a": ("obbligo", None, "art. 10 c.5"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 12 c.2"),
        "nodo_a": ("obbligo", None, "art. 12 c.1"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 12 c.3"),
        "nodo_a": ("obbligo", None, "art. 12 c.2"),
        "tipo_relazione": "deroga a",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "art. 12 c.3"),
        "nodo_a": ("obbligo", None, "art. 12 c.1"),
        "tipo_relazione": "è condizionato da",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("principio", None, "art. 12 c.5"),
        "nodo_a": ("obbligo", None, "art. 12 c.4"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]
