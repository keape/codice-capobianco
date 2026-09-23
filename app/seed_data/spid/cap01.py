"""DPCM 24 ottobre 2014 (SPID) - artt. 1-6: Definizioni, Oggetto e finalità,
Soggetti partecipanti, Ruolo dell'Agenzia, Attributi dell'identità digitale,
Livelli di sicurezza.

Estrazione granulare ADR-0007 dal testo ufficiale vigente al 21/09/2026
(fonte: app/.source_cache/spid/cap01.txt). Copertura completa comma/lettera:
nessun discrimine di rilevanza, incluse le definizioni (art. 1) e le
disposizioni di scopo/ambito di applicazione (art. 2).

Note di modellazione:

- Le clausole introduttive puramente elencative, prive di contenuto
  normativo autonomo, NON ricevono una riga propria (stesso criterio già
  applicato in app/seed_data/cad/cap01.py per "Ai fini del presente codice
  si intende per:"): art. 1 c.1 ("Ai fini del presente decreto si intende
  per:"), art. 3 c.1 ("I soggetti pubblici o privati che partecipano allo
  SPID sono:") e art. 6 c.1 ("Lo SPID e' basato su tre livelli di
  sicurezza di autenticazione informatica:") sono tutte intro pure e
  confluiscono solo nelle lettere che seguono. Art. 4 c.1 e' invece
  indicizzato a se' ("L'Agenzia cura l'attivazione dello SPID, svolgendo,
  in particolare, le seguenti attivita':") perche' contiene un obbligo
  generale autonomo (curare l'attivazione dello SPID) oltre a introdurre
  le lettere a)-c).

- Art. 1 c.1 lett.i) (definizione di "fornitore di servizi") contiene, oltre
  alla definizione, due frasi ulteriori: una descrittiva del flusso
  procedurale (inoltro delle richieste di identificazione informatica ai
  gestori) e una di non discriminazione degli utenti in base al gestore
  dell'identita' digitale. Si e' scelto di NON scindere questa lettera in
  righe separate: la granularita' di riferimento del censimento (ADR-0007)
  e' il comma/lettera, non la singola frase, e il repo non ha precedenti di
  indicizzazione infra-lettera (vedi es. art. 35 c.3 e art. 91 c.2 in
  app/seed_data/cad/cap04.py e cap07.py, dove frasi multiple restano
  accorpate in un'unica riga). La frase di non discriminazione e' pero'
  sostanzialmente duplicata, in forma piu' estesa e autonoma, dall'intero
  art. 6 c.4 ("I fornitori di servizi non possono discriminare l'accesso ai
  propri servizi sulla base del gestore di identita' che l'ha fornita"):
  la sovrapposizione di contenuto tra le due disposizioni e' resa esplicita
  con una relazione "si sovrappone a" tra art. 1 c.1 lett.i) e art. 6 c.4,
  che preserva l'informazione senza violare la granularita' comma/lettera.

- Le clausole "I fornitori di servizi non possono discriminare..." (art. 6
  c.4) e, per continuita' logica, la definizione di "fornitore di servizi"
  (art. 1 c.1 lett.i), non hanno un soggetto obbligato tecnicamente
  imposto in senso stretto (nessun "deve"): seguendo il precedente di
  app/seed_data/cad/cap07.py (art. 75 c.2, "Chiunque puo' partecipare al
  SPC...", tipo_principio "non discriminazione" senza `soggetti`), l'art. 6
  c.4 e' modellato come Principio di tipo "non discriminazione".

- Le clausole che assegnano una facolta'/discrezionalita' a un soggetto
  identificabile senza imporgli un comportamento vincolato (art. 5 c.2,
  l'utente "puo' chiedere" ulteriori attributi secondari) restano Principio
  (tipo "altro"): non c'e' un comportamento imposto, solo una facolta'
  esercitabile a discrezione del titolare. Diversamente, art. 6 c.5 ("I
  fornitori di servizi scelgono il livello di sicurezza necessario per
  accedere ai propri servizi") alloca invece una responsabilita' operativa
  di sistema (chi decide il livello di sicurezza nell'architettura SPID,
  analogamente ai casi "il certificatore indica..."/"il certificatore
  determina..." di app/seed_data/dpcm/cap03.py, modellati come Obbligo
  procedurale) ed e' quindi modellato come Obbligo procedurale sul
  fornitore di servizi.

- L'Agenzia (AgID) e' destinataria di molte disposizioni (art. 4, art. 5
  c.3, art. 6 c.2) ma non compare tra le categorie di soggetto del
  censimento: le righe corrispondenti sono Obblighi senza chiave
  `soggetti` (pattern gia' in uso per le norme indirizzate ad AgID nel
  censimento CAD).

Nessuna relazione cross-fonte (verso CAD/eIDAS/eIDAS2/DPCM 22-2-2013) e'
tentata in questo modulo, e nessuna relazione verso gli altri capitoli
SPID (cap02, cap03): solo rinvii testuali interni agli artt. 1-6 stessi.
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "art. 4 c.1",
        "testo": "L'Agenzia cura l'attivazione dello SPID, svolgendo in particolare le attività elencate alle lettere a), b) e c) del presente articolo.",
        "testo_integrale": "L'Agenzia cura l'attivazione dello SPID, svolgendo, in particolare, le seguenti attività:",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 4 c.1 lett.a)",
        "testo": "AgID gestisce l'accreditamento dei gestori dell'identità digitale e dei gestori di attributi qualificati tramite apposite convenzioni; i regolamenti attuativi disciplinano l'adesione dei fornitori di servizi allo SPID e il contributo economico che i gestori accreditati riconoscono all'Agenzia, commisurato alla copertura dei suoi costi.",
        "testo_integrale": "gestisce l'accreditamento dei gestori dell'identità digitale e dei gestori di attributi qualificati, stipulando con essi apposite convenzioni. Con i regolamenti di cui al presente articolo sono disciplinate le convenzioni per l'adesione allo SPID da parte dei fornitori di servizi ed è regolato il contributo che i gestori dell'identità digitale accreditati allo SPID riconoscono all'Agenzia, da determinarsi nella misura necessaria alla copertura dei costi sostenuti da quest'ultima;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 4 c.1 lett.b)",
        "testo": "AgID cura l'aggiornamento del registro SPID e vigila sull'operato dei soggetti partecipanti, potendo conoscere - tramite il gestore dell'identità digitale - i dati identificativi dell'utente e verificare le modalità con cui le identità digitali sono state rilasciate e utilizzate.",
        "testo_integrale": "cura l'aggiornamento del registro SPID e vigila sull'operato dei soggetti che partecipano allo SPID, anche con possibilità di conoscere, tramite il gestore dell'identità digitale, i dati identificativi dell'utente e verificare le modalità con cui le identità digitali sono state rilasciate e utilizzate;",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 4 c.1 lett.c)",
        "testo": "AgID stipula apposite convenzioni con i soggetti che attestano la validità degli attributi identificativi e consentono la verifica dei documenti d'identità; i gestori dell'identità digitale e i gestori di attributi qualificati sono tenuti ad aderire a tali convenzioni secondo le modalità indicate nei regolamenti attuativi.",
        "testo_integrale": "stipula apposite convenzioni con i soggetti che attestano la validità degli attributi identificativi e consentono la verifica dei documenti di identità. A tali convenzioni i gestori dell'identità digitale e i gestori degli attributi qualificati sono tenuti ad aderire secondo le modalità indicate nei regolamenti di cui al presente articolo.",
        "tipo_obbligo": "organizzativo",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 4 c.2",
        "testo": "Entro trenta giorni dalla pubblicazione del decreto, l'Agenzia, sentito il Garante per la protezione dei dati personali, definisce con proprio regolamento le regole tecniche e le modalità attuative per la realizzazione dello SPID.",
        "testo_integrale": "Entro trenta giorni dalla pubblicazione del presente decreto, l'Agenzia, sentito il Garante per la protezione dei dati personali, definisce con proprio regolamento le regole tecniche e le modalità attuative per la realizzazione dello SPID.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "entro trenta giorni dalla pubblicazione del decreto",
    },
    {
        "riferimento": "art. 4 c.3",
        "testo": "Entro sessanta giorni dalla pubblicazione del decreto, l'Agenzia, sentito il Garante per la protezione dei dati personali, definisce con proprio regolamento le modalità di accreditamento dei soggetti SPID.",
        "testo_integrale": "Entro sessanta giorni dalla pubblicazione del presente decreto, l'Agenzia, sentito il Garante per la protezione dei dati personali, definisce con proprio regolamento le modalità di accreditamento dei soggetti SPID.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "entro sessanta giorni dalla pubblicazione del decreto",
    },
    {
        "riferimento": "art. 4 c.4",
        "testo": "Entro sessanta giorni dalla pubblicazione del decreto, l'Agenzia, sentito il Garante per la protezione dei dati personali, definisce con regolamento le procedure che consentono ai gestori dell'identità digitale di rilasciare l'identità digitale anche tramite altri sistemi di identificazione informatica conformi ai requisiti dello SPID.",
        "testo_integrale": "Entro sessanta giorni dalla pubblicazione del presente decreto, l'Agenzia, sentito il Garante per la protezione dei dati personali, definisce con proprio regolamento le procedure necessarie a consentire ai gestori dell'identità digitale, tramite l'utilizzo di altri sistemi di identificazione informatica conformi ai requisiti dello SPID, il rilascio dell'identità digitale.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "condizione_applicabilita": "entro sessanta giorni dalla pubblicazione del decreto",
    },
    {
        "riferimento": "art. 5 c.1",
        "testo": "Le identità digitali rilasciate all'utente devono contenere obbligatoriamente il codice identificativo, gli attributi identificativi e almeno un attributo secondario, funzionale alle comunicazioni tra il gestore dell'identità digitale e l'utente.",
        "testo_integrale": "Le identità digitali rilasciate all'utente contengono obbligatoriamente il codice identificativo, gli attributi identificativi e almeno un attributo secondario, funzionale alle comunicazioni tra il gestore dell'identità digitale e l'utente.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
            {"categoria": "Utente/titolare", "ruolo": "destinatario"},
        ],
    },
    {
        "riferimento": "art. 5 c.3",
        "testo": "L'Agenzia stabilisce, nell'ambito dei regolamenti di cui all'art. 4, le modalità e le regole tecniche con cui i gestori dell'identità digitale e i gestori di attributi qualificati curano e rendono disponibile ai fornitori di servizi la verifica degli attributi; gli attributi qualificati sono verificati dal fornitore di servizi presso il gestore di attributi qualificati.",
        "testo_integrale": "L'Agenzia stabilisce, nell'ambito dei regolamenti di cui all'art. 4, le modalità e le regole tecniche con le quali i gestori dell'identità digitale e i gestori degli attributi qualificati curano e rendono disponibile la verifica degli attributi stessi ai fornitori di servizi. Gli attributi qualificati sono verificati dal fornitore di servizi presso il gestore di attributi qualificati.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "destinatario"},
            {"categoria": "Terza parte", "ruolo": "obbligato"},
        ],
    },
    {
        "riferimento": "art. 6 c.1 lett.a)",
        "testo": "Nel primo livello di sicurezza (corrispondente al Level of Assurance LoA2 dello standard ISO/IEC DIS 29115), il gestore dell'identità digitale rende disponibili sistemi di autenticazione informatica a un fattore, quale la password, secondo il decreto e i regolamenti attuativi dell'Agenzia.",
        "testo_integrale": "nel primo livello, corrispondente al Level of Assurance LoA2 dello standard ISO/IEC DIS 29115, il gestore dell'identità digitale rende disponibili sistemi di autenticazione informatica a un fattore, quale la password, secondo quanto previsto dal presente decreto e dai regolamenti di cui all'art. 4;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 6 c.1 lett.b)",
        "testo": "Nel secondo livello di sicurezza (LoA3 ISO/IEC DIS 29115), il gestore dell'identità digitale rende disponibili sistemi di autenticazione informatica a due fattori, non necessariamente basati su certificati digitali, con chiavi private custodite su dispositivi conformi ai requisiti dell'Allegato 3 della direttiva 1999/93/CE.",
        "testo_integrale": "nel secondo livello, corrispondente al Level of Assurance LoA3 dello standard ISO/IEC DIS 29115, il gestore dell'identità digitale rende disponibili sistemi di autenticazione informatica a due fattori, non basati necessariamente su certificati digitali, le cui chiavi private siano custodite su dispositivi che soddisfano i requisiti di cui all'Allegato 3 della Direttiva 1999/93/CE del Parlamento europeo, secondo quanto previsto dal presente decreto e dai regolamenti di cui all'art. 4;",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 6 c.1 lett.c)",
        "testo": "Nel terzo livello di sicurezza (LoA4 ISO/IEC DIS 29115), il gestore dell'identità digitale rende disponibili sistemi di autenticazione informatica a due fattori basati su certificati digitali, con chiavi private custodite su dispositivi conformi ai requisiti dell'Allegato 3 della direttiva 1999/93/CE.",
        "testo_integrale": "nel terzo livello, corrispondente al Level of Assurance LoA4 dello standard ISO/IEC DIS 29115, il gestore dell'identità digitale rende disponibili sistemi di autenticazione informatica a due fattori basati su certificati digitali, le cui chiavi private siano custodite su dispositivi che soddisfano i requisiti di cui all'Allegato 3 della Direttiva 1999/93/CE del Parlamento europeo, secondo quanto previsto dal presente decreto e dai regolamenti di cui all'art. 4.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 6 c.2",
        "testo": "L'Agenzia valuta e autorizza gli strumenti e le tecnologie di autenticazione informatica consentiti per ciascun livello, nonché i criteri per la loro valutazione e assegnazione al relativo livello di sicurezza; i gestori dell'identità digitale rendono pubbliche le relative decisioni dell'Agenzia secondo le modalità da essa indicate.",
        "testo_integrale": "L'Agenzia valuta e autorizza l'uso degli strumenti e delle tecnologie di autenticazione informatica consentiti per ciascun livello, nonché i criteri per la valutazione dei sistemi di autenticazione informatica e la loro assegnazione al relativo livello di sicurezza. In tale ambito, i gestori dell'identità digitale rendono pubbliche le decisioni dell'Agenzia con le modalità indicate dalla stessa.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 6 c.3",
        "testo": "I gestori dell'identità digitale garantiscono che l'autenticazione informatica avvenga tramite software e soluzioni tecniche che non richiedono ai fornitori di servizi di dotarsi di dispositivi proprietari, fissi o mobili; sono ammesse soluzioni tecniche con caricamento del software necessario per l'autenticazione informatica.",
        "testo_integrale": "I gestori dell'identità digitale garantiscono che l'autenticazione informatica avvenga attraverso software e soluzioni tecniche che non richiedono ai fornitori di servizi di dotarsi di dispositivi, fissi o mobili, proprietari. Sono consentite soluzioni tecniche che prevedono il caricamento del software necessario per effettuare l'autenticazione informatica.",
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "art. 6 c.5",
        "testo": "I fornitori di servizi scelgono il livello di sicurezza necessario per l'accesso ai propri servizi.",
        "testo_integrale": "I fornitori di servizi scelgono il livello di sicurezza necessario per accedere ai propri servizi.",
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "soggetti": [{"categoria": "Terza parte", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "art. 1 c.1 lett.a)",
        "testo": "Definisce «Agenzia»: l'Agenzia per l'Italia Digitale.",
        "testo_integrale": "Agenzia: l'Agenzia per l'Italia Digitale;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 1 c.1 lett.b)",
        "testo": "Definisce «attributi»: informazioni o qualità di un utente utilizzate per rappresentarne l'identità, lo stato, la forma giuridica o altre caratteristiche peculiari.",
        "testo_integrale": "attributi: informazioni o qualità di un utente utilizzate per rappresentare la sua identità, il suo stato, la sua forma giuridica o altre caratteristiche peculiari;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 1 c.1 lett.c)",
        "testo": "Definisce «attributi identificativi»: nome, cognome, luogo e data di nascita, sesso, ovvero ragione o denominazione sociale, sede legale, nonché il codice fiscale o la partita IVA e gli estremi del documento d'identità utilizzato ai fini dell'identificazione.",
        "testo_integrale": "attributi identificativi: nome, cognome, luogo e data di nascita, sesso, ovvero ragione o denominazione sociale, sede legale, nonché il codice fiscale o la partita IVA e gli estremi del documento d'identità utilizzato ai fini dell'identificazione;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 1 c.1 lett.d)",
        "testo": "Definisce «attributi secondari»: il numero di telefonia fissa o mobile, l'indirizzo di posta elettronica, il domicilio fisico e digitale, nonché eventuali altri attributi individuati dall'Agenzia, funzionali alle comunicazioni.",
        "testo_integrale": "attributi secondari: il numero di telefonia fissa o mobile, l'indirizzo di posta elettronica, il domicilio fisico e digitale, nonché eventuali altri attributi individuati dall'Agenzia, funzionali alle comunicazioni;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 1 c.1 lett.e)",
        "testo": "Definisce «attributi qualificati»: le qualifiche, le abilitazioni professionali e i poteri di rappresentanza e qualsiasi altro tipo di attributo attestato da un gestore di attributi qualificati.",
        "testo_integrale": "attributi qualificati: le qualifiche, le abilitazioni professionali e i poteri di rappresentanza e qualsiasi altro tipo di attributo attestato da un gestore di attributi qualificati;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 1 c.1 lett.f)",
        "testo": "Definisce «autenticazione informatica»: la verifica, effettuata dal gestore dell'identità digitale su richiesta del fornitore di servizi, della validità delle credenziali di accesso presentate dall'utente, al fine di convalidarne l'identificazione informatica.",
        "testo_integrale": "autenticazione informatica: verifica effettuata dal gestore dell'identità digitale, su richiesta del fornitore di servizi, della validità delle credenziali di accesso presentate dall'utente allo stesso gestore, al fine di convalidarne l'identificazione informatica;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 c.1 lett.g)",
        "testo": "Definisce «codice identificativo»: il particolare attributo assegnato dal gestore dell'identità digitale che consente di individuare univocamente un'identità digitale nell'ambito dello SPID.",
        "testo_integrale": "codice identificativo: il particolare attributo assegnato dal gestore dell'identità digitale che consente di individuare univocamente un'identità digitale nell'ambito dello SPID;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 c.1 lett.h)",
        "testo": "Definisce «credenziale di accesso»: il particolare attributo di cui l'utente si avvale, unitamente al codice identificativo, per accedere in modo sicuro, tramite autenticazione informatica, ai servizi qualificati erogati in rete dai fornitori di servizi che aderiscono allo SPID.",
        "testo_integrale": "credenziale di accesso: il particolare attributo di cui l'utente si avvale, unitamente al codice identificativo, per accedere in modo sicuro, tramite autenticazione informatica, ai servizi qualificati erogati in rete dai fornitori di servizi che aderiscono allo SPID;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 c.1 lett.i)",
        "testo": "Definisce «fornitore di servizi»: il fornitore dei servizi della società dell'informazione (art. 2 c.1 lett.a) del d.lgs. 70/2003) o dei servizi di un'amministrazione o ente pubblico erogati agli utenti in rete; i fornitori inoltrano le richieste di identificazione informatica dell'utente ai gestori dell'identità digitale e ne ricevono l'esito, e nell'accettare l'identità digitale non discriminano gli utenti in base al gestore che l'ha fornita.",
        "testo_integrale": "fornitore di servizi: il fornitore dei servizi della società dell'informazione definiti dall'art. 2, comma 1, lettera a), del decreto legislativo 9 aprile 2003, n. 70, o dei servizi di un'amministrazione o di un ente pubblico erogati agli utenti attraverso sistemi informativi accessibili in rete. I fornitori di servizi inoltrano le richieste di identificazione informatica dell'utente ai gestori dell'identità digitale e ne ricevono l'esito. I fornitori di servizi, nell'accettare l'identità digitale, non discriminano gli utenti in base al gestore dell'identità digitale che l'ha fornita;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 c.1 lett.l)",
        "testo": "Definisce «gestori dell'identità digitale»: le persone giuridiche accreditate allo SPID che, quali gestori di servizio pubblico, previa identificazione certa dell'utente, assegnano, rendono disponibili e gestiscono gli attributi utilizzati dallo stesso ai fini dell'identificazione informatica, oltre a fornire i servizi di attribuzione dell'identità digitale, distribuzione e interoperabilità delle credenziali, riservatezza delle informazioni gestite e autenticazione informatica degli utenti.",
        "testo_integrale": "gestori dell'identità digitale: le persone giuridiche accreditate allo SPID che, in qualità di gestori di servizio pubblico, previa identificazione certa dell'utente, assegnano, rendono disponibili e gestiscono gli attributi utilizzati dal medesimo utente al fine della sua identificazione informatica. Essi inoltre, forniscono i servizi necessari a gestire l'attribuzione dell'identità digitale degli utenti, la distribuzione e l'interoperabilità delle credenziali di accesso, la riservatezza delle informazioni gestite e l'autenticazione informatica degli utenti;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 c.1 lett.m)",
        "testo": "Definisce «gestori di attributi qualificati»: i soggetti accreditati ai sensi dell'art. 16 che hanno il potere di attestare il possesso e la validità di attributi qualificati, su richiesta dei fornitori di servizi.",
        "testo_integrale": "gestori di attributi qualificati: i soggetti accreditati ai sensi dell'art. 16 che hanno il potere di attestare il possesso e la validità di attributi qualificati, su richiesta dei fornitori di servizi;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 1 c.1 lett.n)",
        "testo": "Definisce «identificazione informatica»: l'identificazione di cui all'art. 1, comma 1, lettera u-ter) del CAD (d.lgs. 82/2005).",
        "testo_integrale": "identificazione informatica: l'identificazione di cui all'art. 1, comma 1, lettera u-ter) del decreto legislativo 7 marzo 2005, n. 82 (di seguito «CAD»);",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 c.1 lett.o)",
        "testo": "Definisce «identità digitale»: la rappresentazione informatica della corrispondenza biunivoca tra un utente e i suoi attributi identificativi, verificata attraverso l'insieme dei dati raccolti e registrati in forma digitale secondo le modalità del decreto e dei suoi regolamenti attuativi.",
        "testo_integrale": "identità digitale: la rappresentazione informatica della corrispondenza biunivoca tra un utente e i suoi attributi identificativi, verificata attraverso l'insieme dei dati raccolti e registrati in forma digitale secondo le modalità di cui al presente decreto e dei suoi regolamenti attuativi;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 c.1 lett.p)",
        "testo": "Definisce «revoca dell'identità digitale»: la disattivazione definitiva dell'identità digitale.",
        "testo_integrale": "revoca dell'identità digitale: disattivazione definitiva dell'identità digitale;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 c.1 lett.q)",
        "testo": "Definisce «sospensione dell'identità digitale»: la disattivazione temporanea dell'identità digitale.",
        "testo_integrale": "sospensione dell'identità digitale: disattivazione temporanea dell'identità digitale;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 c.1 lett.r)",
        "testo": "Definisce «registrazione»: l'insieme delle procedure informatiche, organizzative e logistiche con cui, secondo i criteri di gestione e protezione del decreto e dei suoi regolamenti attuativi, è attribuita un'identità digitale a un utente, previa raccolta, verifica e certificazione degli attributi da parte del gestore dell'identità digitale, garantendo l'assegnazione e la consegna sicura delle credenziali di accesso prescelte.",
        "testo_integrale": "registrazione: l'insieme delle procedure informatiche, organizzative e logistiche mediante le quali, con adeguati criteri di gestione e protezione previsti dal presente decreto e dai suoi regolamenti attuativi, è attribuita un'identità digitale a un utente, previa raccolta, verifica e certificazione degli attributi da parte del gestore dell'identità digitale, garantendo l'assegnazione e la consegna delle credenziali di accesso prescelte in modalità sicura;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 c.1 lett.s)",
        "testo": "Definisce «registro SPID»: il registro, tenuto dall'Agenzia e accessibile al pubblico, contenente l'elenco dei soggetti abilitati a operare come gestori dell'identità digitale, gestori degli attributi qualificati e fornitori di servizi.",
        "testo_integrale": "registro SPID: registro, tenuto dall'Agenzia, accessibile al pubblico, contenente l'elenco dei soggetti abilitati a operare in qualità di gestori dell'identità digitale, di gestori degli attributi qualificati e di fornitori di servizi;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "art. 1 c.1 lett.t)",
        "testo": "Definisce «servizio qualificato»: il servizio per la cui erogazione è necessaria l'identificazione informatica dell'utente.",
        "testo_integrale": "servizio qualificato: servizio per la cui erogazione è necessaria l'identificazione informatica dell'utente;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 c.1 lett.u)",
        "testo": "Definisce «SPID»: il Sistema pubblico dell'identità digitale, istituito ai sensi dell'art. 64 del CAD, come modificato dall'art. 17-ter del d.l. 21 giugno 2013, n. 69, convertito con modificazioni dalla l. 9 agosto 2013, n. 98.",
        "testo_integrale": "SPID: il Sistema pubblico dell'identità digitale, istituito ai sensi dell'art. 64 del CAD, modificato dall'art. 17-ter del decreto-legge 21 giugno 2013, n. 69, convertito, con modificazioni, dalla legge 9 agosto 2013, n. 98;",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 1 c.1 lett.v)",
        "testo": "Definisce «utente»: la persona fisica o giuridica, titolare di un'identità digitale SPID, che utilizza i servizi erogati in rete da un fornitore di servizi, previa identificazione informatica.",
        "testo_integrale": "utente: persona fisica o giuridica, titolare di un'identità digitale SPID, che utilizza i servizi erogati in rete da un fornitore di servizi, previa identificazione informatica.",
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 2 c.1",
        "testo": "Il decreto stabilisce le caratteristiche dello SPID ai sensi dell'art. 64 del CAD, come modificato dall'art. 17-ter del d.l. n. 69 del 2013.",
        "testo_integrale": "Il presente decreto stabilisce le caratteristiche dello SPID ai sensi dell'art. 64 del CAD, come modificato dall'art. 17-ter del decreto-legge n. 69 del 2013.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 2 c.2",
        "testo": "Lo SPID consente agli utenti di avvalersi di gestori dell'identità digitale e di gestori di attributi qualificati, per permettere ai fornitori di servizi l'immediata verifica della propria identità e degli eventuali attributi qualificati che li riguardano.",
        "testo_integrale": "Ai sensi di tali disposizioni lo SPID consente agli utenti di avvalersi di gestori dell'identità digitale e di gestori di attributi qualificati, per consentire ai fornitori di servizi l'immediata verifica della propria identità e di eventuali attributi qualificati che li riguardano.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 3 c.1 lett.a)",
        "testo": "Tra i soggetti pubblici o privati che partecipano allo SPID rientrano i gestori dell'identità digitale.",
        "testo_integrale": "i gestori dell'identità digitale;",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 3 c.1 lett.b)",
        "testo": "Tra i soggetti pubblici o privati che partecipano allo SPID rientrano i gestori degli attributi qualificati.",
        "testo_integrale": "i gestori degli attributi qualificati;",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 3 c.1 lett.c)",
        "testo": "Tra i soggetti pubblici o privati che partecipano allo SPID rientrano i fornitori di servizi.",
        "testo_integrale": "i fornitori di servizi;",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 3 c.1 lett.d)",
        "testo": "Tra i soggetti pubblici o privati che partecipano allo SPID rientra l'Agenzia.",
        "testo_integrale": "l'Agenzia;",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 3 c.1 lett.e)",
        "testo": "Tra i soggetti pubblici o privati che partecipano allo SPID rientrano gli utenti.",
        "testo_integrale": "gli utenti.",
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 3 c.2",
        "testo": "I partecipanti allo SPID, esclusi gli utenti, costituiscono un sistema aperto e cooperante che consente loro di comunicare utilizzando meccanismi di interazione, standard tecnologici e protocolli indicati dal decreto e precisati nelle regole tecniche definite dall'Agenzia nell'ambito dei regolamenti di cui all'art. 4.",
        "testo_integrale": "I soggetti di cui al comma 1, esclusi gli utenti, costituiscono un sistema aperto e cooperante che consente loro di comunicare utilizzando meccanismi di interazione, standard tecnologici e protocolli indicati nel presente decreto e precisati nelle regole tecniche definite dall'Agenzia nell'ambito dei regolamenti di cui all'art. 4.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 5 c.2",
        "testo": "Al momento della richiesta di rilascio dell'identità digitale, l'utente può chiedere che siano registrati ulteriori attributi secondari.",
        "testo_integrale": "Al momento della richiesta di rilascio dell'identità digitale, l'utente può chiedere che siano registrati ulteriori attributi secondari.",
        "tipo_principio": "altro",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
    {
        "riferimento": "art. 6 c.4",
        "testo": "I fornitori di servizi non possono discriminare l'accesso ai propri servizi in base al gestore di identità che ha fornito l'identità digitale.",
        "testo_integrale": "I fornitori di servizi non possono discriminare l'accesso ai propri servizi sulla base del gestore di identità che l'ha fornita.",
        "tipo_principio": "non discriminazione",
        "stato": "vigente",
        "oggetti_giuridici": ["identificazione elettronica"],
    },
]

INDICE_ARTICOLI_LOCALE = [
    "art. 1 c.1 lett.a)",
    "art. 1 c.1 lett.b)",
    "art. 1 c.1 lett.c)",
    "art. 1 c.1 lett.d)",
    "art. 1 c.1 lett.e)",
    "art. 1 c.1 lett.f)",
    "art. 1 c.1 lett.g)",
    "art. 1 c.1 lett.h)",
    "art. 1 c.1 lett.i)",
    "art. 1 c.1 lett.l)",
    "art. 1 c.1 lett.m)",
    "art. 1 c.1 lett.n)",
    "art. 1 c.1 lett.o)",
    "art. 1 c.1 lett.p)",
    "art. 1 c.1 lett.q)",
    "art. 1 c.1 lett.r)",
    "art. 1 c.1 lett.s)",
    "art. 1 c.1 lett.t)",
    "art. 1 c.1 lett.u)",
    "art. 1 c.1 lett.v)",
    "art. 2 c.1",
    "art. 2 c.2",
    "art. 3 c.1 lett.a)",
    "art. 3 c.1 lett.b)",
    "art. 3 c.1 lett.c)",
    "art. 3 c.1 lett.d)",
    "art. 3 c.1 lett.e)",
    "art. 3 c.2",
    "art. 4 c.1",
    "art. 4 c.1 lett.a)",
    "art. 4 c.1 lett.b)",
    "art. 4 c.1 lett.c)",
    "art. 4 c.2",
    "art. 4 c.3",
    "art. 4 c.4",
    "art. 5 c.1",
    "art. 5 c.2",
    "art. 5 c.3",
    "art. 6 c.1 lett.a)",
    "art. 6 c.1 lett.b)",
    "art. 6 c.1 lett.c)",
    "art. 6 c.2",
    "art. 6 c.3",
    "art. 6 c.4",
    "art. 6 c.5",
]

MAPPATURA_LOCALE = {
    "art. 1 c.1 lett.a)": ["art. 1 c.1 lett.a)"],
    "art. 1 c.1 lett.b)": ["art. 1 c.1 lett.b)"],
    "art. 1 c.1 lett.c)": ["art. 1 c.1 lett.c)"],
    "art. 1 c.1 lett.d)": ["art. 1 c.1 lett.d)"],
    "art. 1 c.1 lett.e)": ["art. 1 c.1 lett.e)"],
    "art. 1 c.1 lett.f)": ["art. 1 c.1 lett.f)"],
    "art. 1 c.1 lett.g)": ["art. 1 c.1 lett.g)"],
    "art. 1 c.1 lett.h)": ["art. 1 c.1 lett.h)"],
    "art. 1 c.1 lett.i)": ["art. 1 c.1 lett.i)"],
    "art. 1 c.1 lett.l)": ["art. 1 c.1 lett.l)"],
    "art. 1 c.1 lett.m)": ["art. 1 c.1 lett.m)"],
    "art. 1 c.1 lett.n)": ["art. 1 c.1 lett.n)"],
    "art. 1 c.1 lett.o)": ["art. 1 c.1 lett.o)"],
    "art. 1 c.1 lett.p)": ["art. 1 c.1 lett.p)"],
    "art. 1 c.1 lett.q)": ["art. 1 c.1 lett.q)"],
    "art. 1 c.1 lett.r)": ["art. 1 c.1 lett.r)"],
    "art. 1 c.1 lett.s)": ["art. 1 c.1 lett.s)"],
    "art. 1 c.1 lett.t)": ["art. 1 c.1 lett.t)"],
    "art. 1 c.1 lett.u)": ["art. 1 c.1 lett.u)"],
    "art. 1 c.1 lett.v)": ["art. 1 c.1 lett.v)"],
    "art. 2 c.1": ["art. 2 c.1"],
    "art. 2 c.2": ["art. 2 c.2"],
    "art. 3 c.1 lett.a)": ["art. 3 c.1 lett.a)"],
    "art. 3 c.1 lett.b)": ["art. 3 c.1 lett.b)"],
    "art. 3 c.1 lett.c)": ["art. 3 c.1 lett.c)"],
    "art. 3 c.1 lett.d)": ["art. 3 c.1 lett.d)"],
    "art. 3 c.1 lett.e)": ["art. 3 c.1 lett.e)"],
    "art. 3 c.2": ["art. 3 c.2"],
    "art. 4 c.1": ["art. 4 c.1"],
    "art. 4 c.1 lett.a)": ["art. 4 c.1 lett.a)"],
    "art. 4 c.1 lett.b)": ["art. 4 c.1 lett.b)"],
    "art. 4 c.1 lett.c)": ["art. 4 c.1 lett.c)"],
    "art. 4 c.2": ["art. 4 c.2"],
    "art. 4 c.3": ["art. 4 c.3"],
    "art. 4 c.4": ["art. 4 c.4"],
    "art. 5 c.1": ["art. 5 c.1"],
    "art. 5 c.2": ["art. 5 c.2"],
    "art. 5 c.3": ["art. 5 c.3"],
    "art. 6 c.1 lett.a)": ["art. 6 c.1 lett.a)"],
    "art. 6 c.1 lett.b)": ["art. 6 c.1 lett.b)"],
    "art. 6 c.1 lett.c)": ["art. 6 c.1 lett.c)"],
    "art. 6 c.2": ["art. 6 c.2"],
    "art. 6 c.3": ["art. 6 c.3"],
    "art. 6 c.4": ["art. 6 c.4"],
    "art. 6 c.5": ["art. 6 c.5"],
}

RELAZIONI = [
    {
        "nodo_da": ("principio", None, "art. 1 c.1 lett.a)"),
        "nodo_a": ("obbligo", None, "art. 4 c.1"),
        "tipo_relazione": "definisce",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("principio", None, "art. 1 c.1 lett.l)"),
        "nodo_a": ("obbligo", None, "art. 5 c.1"),
        "tipo_relazione": "definisce",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("principio", None, "art. 1 c.1 lett.o)"),
        "nodo_a": ("obbligo", None, "art. 5 c.1"),
        "tipo_relazione": "definisce",
        "evidence_type": "textual",
        "confidence": 0.7,
    },
    {
        "nodo_da": ("principio", None, "art. 1 c.1 lett.u)"),
        "nodo_a": ("principio", None, "art. 2 c.1"),
        "tipo_relazione": "definisce",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("principio", None, "art. 1 c.1 lett.i)"),
        "nodo_a": ("principio", None, "art. 6 c.4"),
        "tipo_relazione": "si sovrappone a",
        "evidence_type": "textual",
        "confidence": 0.85,
    },
    {
        "nodo_da": ("principio", None, "art. 3 c.2"),
        "nodo_a": ("obbligo", None, "art. 4 c.2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, "art. 4 c.1 lett.a)"),
        "nodo_a": ("obbligo", None, "art. 4 c.3"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "art. 4 c.1 lett.c)"),
        "nodo_a": ("obbligo", None, "art. 4 c.2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.6,
    },
    {
        "nodo_da": ("obbligo", None, "art. 5 c.3"),
        "nodo_a": ("obbligo", None, "art. 4 c.2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.8,
    },
    {
        "nodo_da": ("obbligo", None, "art. 6 c.1 lett.a)"),
        "nodo_a": ("obbligo", None, "art. 4 c.2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, "art. 6 c.1 lett.b)"),
        "nodo_a": ("obbligo", None, "art. 4 c.2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
    {
        "nodo_da": ("obbligo", None, "art. 6 c.1 lett.c)"),
        "nodo_a": ("obbligo", None, "art. 4 c.2"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": 0.75,
    },
]
