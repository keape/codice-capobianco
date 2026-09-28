"""ETSI TS 119 612 V2.4.1 (2025-08) - Electronic Signatures and Trust
Infrastructures (ESI); Trusted Lists. Fonte 21 (la numerazione degli id e'
risolta per riferimento dalla sessione principale in app/seed.py - questo
modulo NON tocca seed.py). Capitolo 8: Annex H (informative) Locating a TL
(H.1, H.2), Annex I (informative) Usage of trusted lists (I.1, I.2, I.3),
Annex J (normative) Migration of EU MS trusted lists in the context of
Regulation (EU) No 910/2014. Testo ufficiale in
app/.source_cache/etsi_119_612/cap08.txt (letto sempre con selettore `:raw`,
altrimenti il tool tronca le righe lunghe a 768 caratteri introducendo "..."
e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_119_612/manifest.json.

Modellazione (ADR-0007), stesso criterio gia' applicato alle altre fonti ETSI
censite (ETSI EN 319 401/319 412/319 421/319 422, ETSI TS 119 432) e adattato
alle clausole/sottoclausole di uno standard tecnico: un nodo per ogni
clausola/sottoclasse numerata che porta contenuto proprio. Questo capitolo
copre 6 righe: 1 Obbligo (Annex J, normativo) e 5 Principi (Annex H.1, H.2,
I.1, I.2, I.3, tutti informativi). Scelte voce per voce:

- Annex H.1 (Introduction) -> 1 Principio "altro". Una sola frase ("This
  annex provides guidance on how to locate TLs"): dichiara l'oggetto
  dell'annesso informativo, nessun verbo prescrittivo e nessun soggetto
  obbligato. Non e' "scopo/ambito di applicazione" (non delimita il perimetro
  normativo dello standard, si limita a enunciare il contenuto dell'annesso).
- Annex H.2 (Locating a TL) -> 1 Principio "altro". Due paragrafi
  descrittivi: la Commissione europea pubblica la List Of Trusted Lists
  (LOTL) con i link alle TL notificate dagli Stati membri (formato leggibile
  e XML) e, per i servizi basati su PKI, le informazioni sul paese
  dell'emittente di un token di servizio fiduciario orientano verso lo Stato
  membro da cui recuperare la TL. Descrizione di un assetto istituzionale,
  nessun "shall" e nessun comportamento imposto a un soggetto censito ->
  Principio.
- Annex I.1 (Introduction) -> 1 Principio "altro". Enuncia che l'annesso
  descrive un esempio di modello d'uso delle TL e che il modello non intende
  limitare le modalita' realizzative ma identifica le funzionalita' attese.
- Annex I.2 (Example of model for the usage of trusted lists in the context
  of signature validation) -> 1 Principio "altro" per l'intera sottoclausola,
  incluse le due premesse puntate (convalida X.509 / ETSI TS 102 853;
  "Service digital identifiers" come trust anchor), la sequenza a)-f) di
  derivazione delle informazioni dalle TL e la chiusura sulla combinazione con
  altre fonti di informazioni di CA. La sequenza e' un modello esemplificativo
  in un annesso informativo: non contiene "shall"/"should" e non impone
  comportamenti a un soggetto identificato (i passi sono coniugati al
  presente descrittivo: "is validated", "are selected", "can be asked"),
  quindi non genera Obblighi. Un solo nodo (non uno per lettera): i passi
  a)-f) sono fasi consecutive di un unico esempio, prive di soggetto e di
  precettivita' autonome.
- Annex I.3 (Policy elements for trust anchor management) -> 1 Principio
  "altro". Definizione degli elementi di policy per la gestione delle trust
  anchor (tipi, stato e altre proprieta' dei servizi fiduciari accettabili) e
  regola di policy di esempio i)-ii) con i tre ServiceStatus ammessi
  (Under Supervision, Supervision of Service in Cessation, Accredited), URIs
  compresi, riportati verbatim in `testo_integrale`. Anche qui nessun verbo
  prescrittivo: "can specify", "can be defined", "can be".
- Annex J (Migration of EU MS trusted lists in the context of Regulation (EU)
  No 910/2014) -> 1 Obbligo "procedurale". L'annesso e' normativo e usa
  "shall" in modo massiccio: il valore 'Service current status' dei servizi
  elencati nelle TL degli Stati membri UE al 30 giugno 2016 "shall be
  executed on the day the Regulation applies (i.e. 01 July 2016)", con le
  variazioni di stato di approvazione, il mantenimento dell'identificatore
  RootCA-QC, la migrazione dei qualificatori della Qualifications extension,
  la specificazione ulteriore del tipo di servizio e la regola del rapporto
  di valutazione di conformita' entro il 1° luglio 2017. Soggetto obbligato:
  il TLSO / lo scheme nazionale che gestisce la trusted list -> categoria
  "QTSP/gestore" (ruolo obbligato). Un solo nodo per l'intero annesso e NON
  uno per lettera: le lettere a)-e) non sono clausole autonome ma casi
  alternativi della stessa operazione di migrazione, retti da un unico
  chapeau condiviso ("The migration ... shall be executed ... as follows:"
  seguito da a)-e)); spezzarle in 5 nodi lascerebbe il chapeau orfano o
  duplicato in ogni nodo, quindi la granularita' ADR-0007 si ferma qui. Il
  testo di tutte le lettere e' comunque integralmente in `testo_integrale`,
  con i marcatori di lettera/numero (a)-e), i)-vi), 1)-5)) e i rientri logici
  conservati.

Testo verbatim (ADR-0010), nessuna elisione: i wrap fisici del PDF sono
ricomposti con uno spazio singolo, i marcatori "<!-- Page N -->" (paratesto)
sono esclusi, i rientri logici di elenchi/lettere sono conservati. Due punti
di attenzione, risolti in ricomposizione senza togliere parole:
1) in Annex I.3 e in Annex J il wrap spezza a meta' due URI registrati
   ("Svcstatus/" + "supervisionincessation" e "Trusted" + "List/Svcstatus"):
   lo spazio di wrap e' stato rimosso per non introdurre una spazio dentro
   un URI (artefatto di impaginazione, non contenuto);
2) in Annex J e)2) l'estrazione `pdftotext -layout` concatena la coda di un
   valore di stato con la testa del successivo
   (".../supervisionrevoked://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/
   deprecatedbynationallaw") e manca la virgoletta di apertura prima di
   "http://..." in vi)/iv) ("...granted" to
   http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn"): sono difetti
   del testo ufficiale/estrazione, riprodotti verbatim e non corretti (ADR-0010
   vieta di riscrivere il testo; la correzione sarebbe una congettura).

Nessun nodo, nessun item di indice per il blocco "History" in coda al file
(tabella "Document history": V1.1.1 ... V2.4.1, date e "Publication"): e'
paratesto di versionamento, fuori perimetro come il front matter e la
clausola 2. Le intestazioni di annesso ("Annex H (informative): Locating a
TL", "Annex I (informative): Usage of trusted lists", "Annex J (normative):
Migration of EU MS trusted lists ...") non generano nodo autonomo: portano
solo la titolazione dell'annesso, che e' incorporata nel nome del primo (o
unico) nodo dell'annesso stesso. La caption "Figure I.1" e' contenuta nel
nodo I.2 (nessuna figura e' estraibile come nodo).

Citazioni esterne notate ma NON trasformate in relazioni (vietato in questa
fase: il cross-fonte e' la fase 6 della sessione principale, ADR-0009):
Regolamento (UE) No 910/2014 [i.10], Direttiva 1999/93/EC [i.3], IETF RFC
5280 [12], ETSI TS 102 853 [i.1]. `RELAZIONI` contiene solo rimandi testuali
puntuali a clausole della stessa Fonte, tutti tratti da Annex J ("within a
Service information extension (clause 5.5.9)", "additionalServiceInformation
extension (clause 5.5.9.4)", "Qualifications extension (clause 5.5.9.2)",
"For each service of a type defined in clause 5.5.1.2"/"5.5.1.3"): 5
relazioni "richiama", dal solo nodo Obbligo di questo capitolo (Annex J),
confidence None (nessuno score LLM e' stato prodotto). Le stringhe dei
`riferimento` di destinazione E i tipi di nodo sono stati concordati con i
subagent proprietari dei capitoli di destinazione (cap03 per 5.5.1.2/5.5.1.3,
cap04 per 5.5.9/5.5.9.2.0/5.5.9.4), perche' il registro risolve per
(tipo, fonte_id, riferimento) e un nome o un tipo approssimato farebbe
fallire il merge con KeyError: 5.5.1.2, 5.5.1.3, 5.5.9.2.0 e 5.5.9.4 sono
nodi Obbligo; 5.5.9 (Service information extensions) e' invece un nodo
Principio ("altro") di pura intestazione di raggruppamento, creato da cap04
proprio per rendere citabile il rinvio a "clause 5.5.9".

Due rimandi testuali di Annex J NON sono stati trasformati in relazioni,
perche' privi di nodo di destinazione in questa estrazione:
- "(clause 6)" (service history instance, ripetuto in a) i), a) v), b) i),
  b) iii), c) i), c) ii), d) i), d) ii), e) i), e) ii)): la clausola 6 e' una
  intestazione di puro raggruppamento senza testo proprio nel sorgente
  (confermato dal subagent cap05, che non le assegna alcun nodo: i suoi nodi
  sono 6.1-6.5), e cap04 conferma di non avere un nodo nemmeno per 5.6
  (Service history instance, intestazione di raggruppamento) ne' per un
  5.6.0 General. Non esiste quindi un nodo che copra la clausola richiamata:
  la relazione non e' stata dirottata ne' su "clausola 5.6.1 (Service type
  identifier)" ne' su "clausola 5.5.10 (Service history)" — sarebbe
  un'inferenza su un rinvio la cui numerazione e' tra l'altro eccedentaria
  rispetto al documento vigente, non il riscontro testuale letterale;
- "(clause 5.5.9.2)" (Qualifications extension) e' anch'essa
  un'intestazione di raggruppamento senza nodo proprio (il primo nodo e'
  5.5.9.2.0 General): cap04 ha indicato come destinazione esatta per il
  rinvio all'estensione "clausola 5.5.9.2.0 (General)", ed e' quella la
  relazione inserita.

`testo` e' la sintesi in italiano (bozza LLM compressa); `testo_integrale` e'
il testo ufficiale inglese integrale. La costruzione delle relazioni
cross-fonte e' demandata alla Fase 6 della sessione principale (ADR-0009).
"""

RIGHE_OBBLIGHI: list[dict] = [
    {
        "riferimento": "Annex J (Migration of EU MS trusted lists in the context of Regulation (EU) No 910/2014)",
        "testo": (
            "Annex J (normativo) disciplina la migrazione del valore 'Service current status' dei servizi "
            "elencati nelle trusted list degli Stati membri UE alla data del 30 giugno 2016, da eseguirsi il "
            "1° luglio 2016 (data di applicazione del Regolamento (UE) n. 910/2014). a) Per i servizi di "
            "tipo CA/QC: variazione dello stato di approvazione "
            "(undersupervision/supervisionincessation/accredited -> granted; "
            "supervisionceased/supervisionrevoked -> withdrawn), con informazione sullo stato precedente "
            "fornita in ordine decrescente di data e ora tramite una service history instance (clausola 6); "
            "l'identificatore RootCA-QC eventualmente presente va mantenuto nelle nuove informazioni "
            "collegate allo stato; il tipo di servizio va ulteriormente specificato con "
            "additionalServiceInformation 'for electronic signatures'; i qualificatori della Qualifications "
            "extension eventualmente usati vanno migrati (QCWithSSCD -> QCWithQSCD, QCNoSSCD -> QCNoQSCD, "
            "QCSSCDStatusAsInCert -> QCQSCDStatusAsInCert, QCStatement mantenuto e completato con QCForESig, "
            "QCForLegalPerson -> NotQualified); dal termine della migrazione l'eventuale variazione di stato "
            "segue il Regolamento e lo schema nazionale di approvazione; in mancanza di rapporto di "
            "valutazione di conformita' trasmesso dal TSP entro il 1° luglio 2017 lo stato passa da granted "
            "a withdrawn, salvo che sia gia' withdrawn. b) Per i servizi CertStatus/OCSP/QC e "
            "CertStatus/CRL/QC: le stesse variazioni di stato (granted / withdrawn), la specificazione 'for "
            "electronic signatures' e la stessa regola del 1° luglio 2017. c) Per i servizi TSA/QTST, EDS/Q, "
            "EDS/REM/Q, QESValidation/Q e PSES/Q: lo stato passa a withdrawn sia da "
            "undersupervision/supervisionincessation/accredited sia da supervisionceased/supervisionrevoked; "
            "per QESValidation/Q e PSES/Q il tipo di servizio va ulteriormente specificato con "
            "additionalServiceInformation indicante se e' fornito per firme e/o sigilli elettronici. d) Per "
            "i servizi di tipo definito nella clausola 5.5.1.2: "
            "undersupervision/supervisionincessation/accredited -> recognisedatnationallevel; "
            "supervisionceased/supervisionrevoked -> deprecatedatnationallevel, con specificazione del tipo "
            "su firme elettroniche, sigilli elettronici e/o autenticazione di siti web. e) Per i servizi di "
            "tipo definito nella clausola 5.5.1.3: "
            "undersupervision/supervisionincessation/accredited/setbynationallaw -> "
            "recognisedatnationallevel; supervisionceased/supervisionrevoked/deprecatedbynationallaw -> "
            "deprecatedatnationallevel; dal termine della migrazione le variazioni di stato seguono il "
            "Regolamento e lo schema nazionale."
        ),
        "testo_integrale": (
            "Annex J Migration of EU MS trusted lists in the context of Regulation (EU) No 910/2014: The "
            "migration of the 'Service current status' value of services listed in EU MS trusted list as of "
            "the day before the date Regulation (EU) No 910/2014 [i.10] applies (i.e. 30 June 2016) shall be "
            "executed on the day the Regulation applies (i.e. 01 July 2016) as follows:\na) For each service "
            "of type \"http://uri.etsi.org/TrstSvc/Svctype/CA/QC\":\ni) A change in the service approval status "
            "shall occur as follows and information on the previous approval status shall be provided in "
            "descending order of status change date and time (i.e. the date and time on which the subsequent "
            "approval status became effective) by making use of a service history instance (clause 6):\n1) "
            "The services having, as of the day before the date Regulation applies, 'Service current status' "
            "value \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/undersupervision\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionincessation\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/accredited\" shall be given the new 'Service "
            "current status' value \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted\".\n2) The "
            "services having, as of the day before the date Regulation applies, 'Service current status' "
            "value \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionceased\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionrevoked\", shall be given the new "
            "'Service current status' value "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn\".\nii) When the listed service is "
            "further identified by using the \"http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/RootCA-QC\" "
            "identifier which is included in the additionalServiceInformation extension (clause 5.5.9.4) "
            "within a Service information extension (clause 5.5.9), this information shall be kept in the "
            "new 'Service current status' related information.\niii) The service type shall be further "
            "specified through the use of an additionalServiceInformation extension (clause 5.5.9.4) within "
            "a Service information extension (clause 5.5.9) by using the identifier indicating that the "
            "service is \"for electronic signatures\", i.e. that the nature of the qualified certificates for "
            "which the qualified status has been granted as being qualified certificates for electronic "
            "signatures (as specified in clause 5.5.9.4).\niv) When the listed service was making use of a "
            "Qualifications extension (clause 5.5.9.2) within a Service information extension (clause "
            "5.5.9), the same used extension shall be kept in the new 'Service current status' related "
            "information but the used qualifiers shall be migrated as follows:\n1) The "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCWithSSCD\" qualifier shall be migrated to "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCWithQSCD\".\n2) The "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCNoSSCD\" qualifier shall be migrated to "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCNoQSCD\".\n3) The "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCSSCDStatusAsInCert\" qualifier shall be "
            "migrated to \"http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCQSCDStatusAsInCert \".\n4) The "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCStatement\" qualifier shall be kept and "
            "complemented with the http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCForESig "
            "qualifier.\n5) The \"http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCForLegalPerson\" "
            "qualifier shall be migrated to "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/NotQualified\".\nv) From the time the above "
            "migration has been executed (i.e. no later than 1 July 2016), a change in the service approval "
            "status value may occur in accordance with the requirements laid down in the Regulation and the "
            "applicable national approval scheme and supervisory activities. In that case, information on "
            "the previous approval status shall be provided in descending order of status change date and "
            "time (i.e. the date and time on which the subsequent approval status became effective) by "
            "making use of a service history instance (clause 6).\nvi) When no conformity assessment report "
            "is submitted by the corresponding TSP to the supervisory body by which it is supervised by the "
            "one year anniversary day of the Regulation application (i.e. 1 July 2017), a change in the "
            "service approval status value shall occur from the value "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted\" to "
            "http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn\" unless the 'Service current "
            "status' is already set to this latter value.\nb) For each service of type "
            "\"http://uri.etsi.org/TrstSvc/Svctype/CertStatus/OCSP/QC\" and of type "
            "\"http://uri.etsi.org/TrstSvc/Svctype/CertStatus/CRL/QC\":\ni) A change in the service approval "
            "status shall occur as follows and information on the previous approval status shall be provided "
            "in descending order of status change date and time (i.e. the date and time on which the "
            "subsequent approval status became effective) by making use of a service history instance "
            "(clause 6):\n1) The services having, as of the day before the date Regulation applies, 'Service "
            "current status' value \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/undersupervision\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionincessation\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/accredited\" shall be given the new 'Service "
            "current status' value \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted\".\n2) The "
            "services having, as of the day before the date Regulation applies, 'Service current status' "
            "value \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionceased\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionrevoked\", shall be given the new "
            "'Service current status' value "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn\".\nii) The service type shall be "
            "further specified through the use of an additionalServiceInformation extension (clause 5.5.9.4) "
            "within a Service information extension (clause 5.5.9) by using the identifier indicating that "
            "the service is \"for electronic signatures\", i.e. that the nature of the qualified certificates "
            "for which the qualified status has been granted as being qualified certificates for electronic "
            "signatures (as specified in clause 5.5.9.4).\niii) From the time the above migration has been "
            "executed (i.e. no later than 1 July 2016), a change in the service approval status value may "
            "occur in accordance with the requirements laid down in the Regulation and the applicable "
            "national approval scheme and supervisory activities. In that case, information on the previous "
            "approval status shall be provided in descending order of status change date and time (i.e. the "
            "date and time on which the subsequent approval status became effective) by making use of a "
            "service history instance (clause 6).\niv) When no conformity assessment report is submitted by "
            "the corresponding TSP to the supervisory body by which it is supervised by the one year "
            "anniversary day of the Regulation application (i.e. 1 July 2017), a change in the service "
            "approval status value shall occur from the value "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted\" to "
            "http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn\" unless the 'Service current "
            "status' is already set to this latter value.\nc) For each service of type "
            "\"http://uri.etsi.org/TrstSvc/Svctype/TSA/QTST\", of type "
            "\"http://uri.etsi.org/TrstSvc/Svctype/EDS/Q\", of type "
            "\"http://uri.etsi.org/TrstSvc/Svctype/EDS/REM/Q\", of type "
            "\"http://uri.etsi.org/TrstSvc/Svctype/QESValidation/Q\", and of type "
            "\"http://uri.etsi.org/TrstSvc/Svctype/PSES/Q\":\ni) A change in the service approval status shall "
            "occur as follows and information on the previous approval status shall be provided in "
            "descending order of status change date and time (i.e. the date and time on which the subsequent "
            "approval status became effective) by making use of a service history instance (clause 6).\n1) "
            "The service having, as of the day before the date Regulation applies, 'Service current status' "
            "value \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/undersupervision\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionincessation\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/accredited\" shall be given the new 'Service "
            "current status' value \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn\".\n2) The "
            "services having, as of the day before the date Regulation applies, 'Service current status' "
            "value \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionceased\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionrevoked\", shall be given the new "
            "'Service current status' value "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/withdrawn\".\nii) From the time the above "
            "migration has been executed (i.e. no later than 1 July 2016), a change in the service approval "
            "status value may occur in accordance with the requirements laid down in the Regulation and the "
            "applicable national approval scheme and supervisory activities. In that case, information on "
            "the previous approval status shall be provided in descending order of status change date and "
            "time (i.e. the date and time on which the subsequent approval status became effective) by "
            "making use of a service history instance (clause 6). For services of type "
            "\"http://uri.etsi.org/TrstSvc/Svctype/QESValidation/Q\", and of type "
            "\"http://uri.etsi.org/TrstSvc/Svctype/PSES/Q\", the service type shall be further specified "
            "through the use of an additionalServiceInformation extension (clause 5.5.9.4) within a Service "
            "information extension (clause 5.5.9) by using the identifier indicating whether it is provided "
            "for electronic signatures and/or for electronic seals (as specified in clause 5.5.9.4).\nd) For "
            "each service of a type defined in clause 5.5.1.2:\ni) A change in the service approval status "
            "shall occur as follows and information on the previous approval status shall be provided in "
            "descending order of status change date and time (i.e. the date and time on which the subsequent "
            "approval status became effective) by making use of a service history instance (clause 6):\n1) "
            "The service having, as of the day before the date Regulation applies, 'Service current status' "
            "value \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/undersupervision\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionincessation\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/accredited\" shall be given the new 'Service "
            "current status' value "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/recognisedatnationallevel\".\n2) The services "
            "having, as of the day before the date Regulation applies, 'Service current status' value "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionceased\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionrevoked\", shall be given the new "
            "'Service current status' value "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/deprecatedatnationallevel\".\nii) From the "
            "time the above migration has been executed (i.e. no later than 1 July 2016), a change in the "
            "service approval status value may occur in accordance with the requirements laid down in the "
            "Regulation and the applicable national approval scheme and supervisory activities. In that "
            "case, information on the previous approval status shall be provided in descending order of "
            "status change date and time (i.e. the date and time on which the subsequent approval status "
            "became effective) by making use of a service history instance (clause 6). When applicable, the "
            "service type shall be further specified through the use of an additionalServiceInformation "
            "extension (clause 5.5.9.4) within a Service information extension (clause 5.5.9) by using the "
            "identifier indicating whether it is provided for electronic signatures, for electronic seals "
            "and/or for web site authentication (as specified in clause 5.5.9.4).\ne) For each service of a "
            "type defined in clause 5.5.1.3:\ni) A change in the service approval status shall occur as "
            "follows and information on the previous approval status shall be provided in descending order "
            "of status change date and time (i.e. the date and time on which the subsequent approval status "
            "became effective) by making use of a service history instance (clause 6):\n1) The service "
            "having, as of the day before the date Regulation applies, 'Service current status' value "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/undersupervision\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionincessation\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/accredited\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/setbynationallaw\" shall be given the new "
            "'Service current status' value "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/recognisedatnationallevel\".\n2) The services "
            "having, as of the day before the date Regulation applies, 'Service current status' value "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionceased\", or "
            "\"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionrevoked://uri.etsi.org/TrstSvc/Trus"
            "tedList/Svcstatus/deprecatedbynationallaw\" shall be given the new 'Service current status' "
            "value \"http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/deprecatedatnationallevel\".\nii) From "
            "the time the above migration has been executed (i.e. no later than 1 July 2016), a change in "
            "the service approval status value may occur in accordance with the requirements laid down in "
            "the Regulation and the applicable national approval scheme and supervisory activities. In that "
            "case, information on the previous approval status shall be provided in descending order of "
            "status change date and time (i.e. the date and time on which the subsequent approval status "
            "became effective) by making use of a service history instance (clause 6)."
        ),
        "tipo_obbligo": "procedurale",
        "stato": "vigente",
        "severita": None,
        "sanzioni": None,
        "condizione_applicabilita": (
            "Si applica alla migrazione dei valori di 'Service current status' dei servizi elencati nelle "
            "trusted list degli Stati membri UE alla data del 30 giugno 2016, eseguita il 1° luglio 2016 "
            "(data di applicazione del Regolamento (UE) n. 910/2014); le regole c)-e) valgono per i tipi di "
            "servizio ivi rispettivamente definiti, e la variazione a withdrawn per mancato rapporto di "
            "valutazione di conformita' scatta al 1° luglio 2017."
        ),
        "soggetti": [
            {"categoria": "QTSP/gestore", "ruolo": "obbligato"},
        ],
    },
]

RIGHE_PRINCIPI: list[dict] = [
    {
        "riferimento": "Annex H.1 (Introduction)",
        "testo": (
            "H.1 enuncia l'oggetto dell'Annex H: l'annesso fornisce indicazioni (guidance) su come "
            "individuare le trusted list (TL). Nessun requisito prescrittivo."
        ),
        "testo_integrale": (
            "H.1 Introduction: This annex provides guidance on how to locate TLs."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "oggetti_giuridici": ["altro"],
    },
    {
        "riferimento": "Annex H.2 (Locating a TL)",
        "testo": (
            "Per consentire l'accesso in modo agevole alle trusted list di tutti gli Stati membri, la "
            "Commissione europea pubblica una lista centrale con i link ai luoghi in cui le trusted list "
            "sono pubblicate come notificate dagli Stati membri: la List Of Trusted Lists (LOTL), "
            "disponibile sia in formato leggibile dall'uomo sia in formato XML adatto all'elaborazione "
            "automatica (macchina). Per i servizi basati su PKI, le informazioni sul paese dell'emittente di "
            "un token di servizio fiduciario (certificati, anche qualificati, token di marca temporale, "
            "risposte OCSP firmate, CRL firmate) forniscono un indizio sullo Stato membro dal quale la TL "
            "puo' essere recuperata."
        ),
        "testo_integrale": (
            "H.2 Locating a TL: In order to allow access to the trusted lists of all Member States in an "
            "easy manner, the European Commission publishes a central list with links to the locations where "
            "the trusted lists are published as notified by Member States. This central list, called the "
            "List Of Trusted Lists (LOTL), is available in both a human readable format and in a format "
            "suitable for automated (machine) processing XML.\nWith regards to PKI based services, the "
            "country related information of the issuer of a trust service token (e.g. (qualified) "
            "certificates, time-stamping tokens, signed OCSP responses, signed CRLs) provides as hint the MS "
            "indication where the TL can be retrieved from."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "oggetti_giuridici": ["altro"],
    },
    {
        "riferimento": "Annex I.1 (Introduction)",
        "testo": (
            "L'Annex I (informativo) descrive un esempio di modello per l'uso delle trusted list: il modello "
            "non intende limitare le modalita' con cui un'implementazione puo' essere costruita, ma "
            "identifica le funzionalita' che possono essere attese dai sistemi che applicano le trusted list."
        ),
        "testo_integrale": (
            "I.1 Introduction: This annex describes an example of model for the usage of trusted lists. This "
            "model is not aimed to restrict how an implementation can be built but identifies the "
            "functionality that can be expected from systems applying trusted lists."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "oggetti_giuridici": ["altro"],
    },
    {
        "riferimento": "Annex I.2 (Example of model for the usage of trusted lists in the context of signature validation)",
        "testo": (
            "Esempio di modello d'uso delle trusted list nella convalida delle firme (Figura I.1). Le "
            "informazioni delle trusted list possono essere usate nel processo di convalida del percorso di "
            "certificazione di un'applicazione: la convalida basata su X.509 (IETF RFC 5280) o su ETSI TS "
            "102 853 sulla verifica di firma richiede informazioni sui certificati di CA utilizzabili come "
            "trust anchor per il servizio fiduciario richiesto; quando i \"Service digital identifiers\" sono "
            "usati come trust anchor nella convalida di firme elettroniche, servono solo la chiave pubblica "
            "e il subject name associato, e i piu' certificati che rappresentano la stessa chiave pubblica "
            "sono considerati certificati trust anchor con informazioni identiche. Le informazioni possono "
            "essere derivate da una o piu' trusted list come segue: a) si valida la fonte della trusted list "
            "per assicurare che le informazioni provengano da un emittente fidato (es. con firma digitale "
            "validata tramite un certificato noto come proveniente da un'autorita' riconosciuta); b) si "
            "selezionano le voci di CA dalla trusted list in base alle regole della trust policy "
            "applicabile; c) i certificati di CA delle voci selezionate, opzionalmente con i metadati "
            "associati, sono conservati insieme alle trust anchor; d) la trusted list e' verificata "
            "regolarmente per variazioni dello stato di servizio delle CA gia' caricate dal TL nel trust "
            "anchor store; la trusted list e' anche verificata regolarmente per nuove voci; e) si puo' "
            "chiedere conferma a un utente umano o a un operatore prima di aggiungere una voce al trust "
            "anchor store; f) informazioni di CA da piu' trusted list possono essere caricate nel trust "
            "anchor store. Le informazioni di CA provenienti dalle trusted list possono essere combinate con "
            "informazioni di CA del trust anchor store o di qualsiasi archivio di certificati di CA caricato "
            "per altre vie, manualmente o automaticamente."
        ),
        "testo_integrale": (
            "I.2 Example of model for the usage of trusted lists in the context of signature validation: "
            "Figure I.1: Example of model for the usage of TL in the context of signature "
            "validation\nInformation from trusted lists can be used in the certificate path validation "
            "process for an application as follows:\n• Certificate path validation based upon X.509 (see IETF "
            "RFC 5280 [12]) or ETSI TS 102 853 [i.1] on signature verification requires information on CA "
            "certificates that can be used as trust anchors for an application requiring a particular trust "
            "service.\n• When \"Service digital identifiers\" are used as trust anchors in the context of "
            "validating electronic signatures for which signer's certificate is to be validated against TL "
            "information, only the public key and the associated subject name are needed as trust anchor "
            "information. When more than one certificate is representing the public key identifying the "
            "service, they are considered as trust anchor certificates conveying identical information with "
            "regards to the information strictly required as Trust Anchor information.\nThis information can "
            "be derived from one or more trusted lists as follows:\na) The source of the trusted list is "
            "validated to ensure that the information comes from a trusted issuer (e.g. using a digital "
            "signature validated using a certificate known to come from a recognized authority).\nb) CA "
            "entries are selected from the trusted list based on the rules of the applicable trust "
            "policy.\nc) CA certificates from the selected entries, optionally with associated meta data, are "
            "held with the trust anchors.\nd) The trusted list is checked regularly for changes to the "
            "service status of the CAs in the trust anchor store which were previously loaded from the "
            "trusted list. The trusted list is also regularly checked for new entries.\ne) A human user or "
            "operator can be asked for confirmation before an entry is added to the trust anchors store.\nf) "
            "CA information from multiple trusted lists can be loaded into the trust anchors store.\nCA "
            "Information from trusted lists can be combined with CA information in the trust anchor store or "
            "from any trusted CA certificate store loaded by other means, manually or in an automated way."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "oggetti_giuridici": ["firma elettronica", "firma elettronica qualificata"],
    },
    {
        "riferimento": "Annex I.3 (Policy elements for trust anchor management)",
        "testo": (
            "Gli elementi di policy per la gestione delle trust anchor possono specificare i tipi, lo stato "
            "e ogni altra proprieta' rilevante dei servizi fiduciari o delle altre entita' fidate i cui "
            "certificati sono accettabili come trust anchor; possono essere definiti localmente per una "
            "comunita' di utenti, dal fornitore dell'applicazione o dal fornitore del sistema. Esempio di "
            "regola di policy per un'applicazione che richiede TSP supervisionati o accreditati per "
            "l'emissione di certificati qualificati, in linea con la direttiva 1999/93/CE, per firme "
            "elettroniche qualificate: i) ServiceType uguale a http://uri.etsi.org/TrstSvc/Svctype/CA/QC; e "
            "ii) ServiceStatus pari a Under Supervision, Supervision of Service in Cessation oppure "
            "Accredited."
        ),
        "testo_integrale": (
            "I.3 Policy elements for trust anchor management: Policy elements for trust anchor management "
            "can specify the types, status and any other relevant properties of trust services or other "
            "trusted entities whose certificates are acceptable as trust anchors.\nThese policy elements can "
            "be defined, locally, for a community of users, by the application provider or by the system "
            "provider.\nAn example policy rule for an application that requires TSPs supervised or accredited "
            "for issuing qualified certificates in line with Directive 1999/93/EC [i.3] for qualified "
            "electronic signatures can be:\ni) ServiceType equals: http://uri.etsi.org/TrstSvc/Svctype/CA/QC; "
            "and\nii) ServiceStatus is:\n- Under Supervision "
            "(http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/undersupervision); or\n- Supervision of "
            "Service in Cessation "
            "(http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/supervisionincessation); or\n- Accredited "
            "(http://uri.etsi.org/TrstSvc/Svcstatus/TrustedList/Svcstatus/accredited)."
        ),
        "tipo_principio": "altro",
        "stato": "vigente",
        "condizione_applicabilita": None,
        "oggetti_giuridici": ["firma elettronica qualificata"],
    },
]

INDICE_ARTICOLI_LOCALE: list[str] = [
    "Annex H.1 (Introduction)",
    "Annex H.2 (Locating a TL)",
    "Annex I.1 (Introduction)",
    "Annex I.2 (Example of model for the usage of trusted lists in the context of signature validation)",
    "Annex I.3 (Policy elements for trust anchor management)",
    "Annex J (Migration of EU MS trusted lists in the context of Regulation (EU) No 910/2014)",
]

MAPPATURA_LOCALE: dict[str, list[str]] = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = [
    {
        "nodo_da": ("obbligo", None, "Annex J (Migration of EU MS trusted lists in the context of Regulation (EU) No 910/2014)"),
        "nodo_a": ("principio", None, "clausola 5.5.9 (Service information extensions)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex J (Migration of EU MS trusted lists in the context of Regulation (EU) No 910/2014)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.2.0 (General)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex J (Migration of EU MS trusted lists in the context of Regulation (EU) No 910/2014)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.9.4 (additionalServiceInformation Extension)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex J (Migration of EU MS trusted lists in the context of Regulation (EU) No 910/2014)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.2 (Regulation (EU) No 910/2014 non qualified trust service types)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
    {
        "nodo_da": ("obbligo", None, "Annex J (Migration of EU MS trusted lists in the context of Regulation (EU) No 910/2014)"),
        "nodo_a": ("obbligo", None, "clausola 5.5.1.3 (Trust service types not defined in Regulation (EU) No 910/2014 but nationally defined)"),
        "tipo_relazione": "richiama",
        "evidence_type": "textual",
        "confidence": None,
    },
]


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
