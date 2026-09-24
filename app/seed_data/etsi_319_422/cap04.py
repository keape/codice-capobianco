"""ETSI EN 319 422 V1.1.1 (2016-03) - Electronic Signatures and Trust
Infrastructures (ESI); Time-stamping protocol and time-stamp token profiles.
Fonte 19 (la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 4:
clausola 9 (Additional requirements for qualified electronic time-stamps as
per Regulation (EU) No 910/2014) con la sottoclasse 9.1 (Regulation
compliance statement), e gli allegati NORMATIVI Annex A (Structure for the
policy field), Annex B (ASN.1 declarations), Annex C (Time-stamp token media
type and file-extension). Testo ufficiale in
app/.source_cache/etsi_319_422/cap04.txt (letto sempre con selettore `:raw`,
altrimenti il tool tronca le righe lunghe a 768 caratteri introducendo
ellissi e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_319_422/manifest.json.

Modellazione (ADR-0007), stesso criterio gia' applicato agli altri standard
ETSI censiti e ai capitoli cap01-cap03 di questa stessa fonte: un nodo per
ogni clausola/sottoclasse numerata che porta contenuto proprio, un solo nodo
Principio per le parti dichiarative/referenziali. Questo capitolo contiene 2
Obblighi e 2 Principi. Scelte voce per voce:

- Clausola 9 (Additional requirements for qualified electronic time-stamps
  as per Regulation (EU) No 910/2014) -> NESSUN nodo, NESSUN item di indice.
  E' un'intestazione di puro raggruppamento: il testo ufficiale non le
  associa alcun periodo proprio (la conversione PDF->markdown la rende come
  "## Additional requirements ..." senza il numero, seguita immediatamente
  da 9.1). Stesso trattamento riservato alle intestazioni di raggruppamento
  delle clausole 4, 5, 6 e 9 di ETSI EN 319 401/319 421.
- Clausola 9.1 (Regulation compliance statement) -> 1 Obbligo "tecnico/
  sicurezza", soggetto "QTSP/gestore" (obbligato), con
  `condizione_applicabilita` perche' l'intero contenuto e' condizionato alla
  dichiarazione di qualifica della marca temporale. Tre prescrizioni in un
  unico nodo (una sola clausola numerata, quindi un solo item di indice):
  (a) "should" - se il token e' dichiarato marca temporale elettronica
  qualificata ai sensi del Regolamento (UE) n. 910/2014, dovrebbe contenere
  una istanza dell'estensione qcStatements nel campo delle estensioni, con
  la sintassi di IETF RFC 3739, clausola 3.2.6; (b) "shall" - se
  l'estensione qcStatements e' presente, deve contenere una istanza dello
  statement "esi4-qtstStatement-1" come definito nell'Annex B; (c) "shall
  not" - l'estensione qcStatements non deve essere marcata come critical.
  Tutte e tre vincolano l'emittente (TSA/QTSP) nella costruzione del token,
  quindi Obbligo e non Principio; il registro modale misto ("should" +
  "shall") e' assorbito in un unico nodo perche' la clausola e' indivisibile
  ai fini dell'indice (la raccomandazione (a) e' comunque la condizione di
  applicazione della prescrizione (b)). Oggetto giuridico "marca temporale
  elettronica qualificata": NON riportato come `oggetti_giuridici` perche' lo
  schema del censimento ammette tale chiave solo sulle righe Principio
  (`principio_oggetti` in app/schema.sql; `inserisci_capitoli` in
  app/seed_data/lib.py non legge alcun oggetto dalle righe Obbligo) - il
  riferimento alla qualifica resta esplicito nel `testo` e nel
  `condizione_applicabilita`.
- Annex A (normative): Structure for the policy field -> 1 Obbligo "tecnico/
  sicurezza", soggetto "QTSP/gestore" (obbligato: la TSA che emette la marca
  temporale), con `condizione_applicabilita` ("quando la marca temporale e'
  emessa da una TSA conforme a ETSI EN 319 421"). Contiene un "shall
  include" che impone il contenuto del campo policy del TSTInfo, quindi
  Obbligo e non Principio nonostante l'allegato sia per lo piu' descrittivo:
  il requisito e' un'alternativa secca ("or") tra l'identificatore della
  clausola 5.2 di ETSI EN 319 421 [7] e l'identificatore proprio della TSA
  quando questa incorpora o vincola ulteriormente la policy.
- Annex B (normative): ASN.1 declarations -> 1 Principio "definitorio",
  oggetto giuridico "marca temporale elettronica qualificata". E' il modulo
  ASN.1 normativo: definisce gli object identifier id-etsi-tsts e
  id-etsi-tsts-EuQCompliance e lo statement esi4-qtstStatement-1
  (QC-STATEMENT identificato da id-etsi-tsts-EuQCompliance), con il commento
  normativo che ne fissa il significato ("By inclusion of this statement the
  issuer claims that this time-stamp token is issued as a qualified
  electronic time-stamp according to the REGULATION (EU) No 910/2014"). Non
  introduce obblighi propri: la prescrizione di includerlo e' gia' nella
  clausola 9.1 (che vi rinvia con "as defined in annex B"), qui si fissa
  soltanto la definizione tecnica autoritativa - quindi Principio
  "definitorio", stesso trattamento riservato all'Annex B di ETSI EN 319
  412-5. In `testo_integrale` il blocco ASN.1 e' riportato per intero, con i
  commenti "--" e l'interruzione di riga originale della definizione di
  id-etsi-tsts.
- Annex C (normative): Time-stamp token media type and file-extension -> 1
  Principio "definitorio". Dichiara, in conformita' a IETF RFC 6838 [i.6],
  il media type e l'estensione di file che identificano un token di marca
  temporale: "Application" / "vnd.etsi.timestamp-token", nessun parametro
  richiesto, considerazioni di codifica "binary", estensione "tst". Nessun
  verbo prescrittivo e nessun soggetto obbligato: e' una definizione di
  identificatori di formato. Nessun `oggetti_giuridici`: la definizione vale
  per il token di marca temporale in quanto tale, senza riferimento alla
  qualifica (che e' invece il perno della clausola 9.1 e dell'Annex B). La
  conversione PDF->markdown rende la tabella come un'unica riga piatta
  etichetta/valore alternati; in `testo_integrale` la riga e' riportata
  verbatim cosi' come resa dal sorgente, senza ricostruzione implicita (il
  `testo` sintetico esplicita invece le singole coppie).
- Clausola 2 (References) non ricade in questo capitolo ed e' comunque
  esclusa come paratesto/bibliografia, stesso trattamento gia' riservato
  alla clausola 2 di ETSI EN 319 401/319 421.

RELAZIONI resta vuota: il collegamento cross-fonte e' demandato alla Fase 6
della sessione principale (ADR-0009).
"""

RIGHE_OBBLIGHI = [
    {
        "riferimento": "clausola 9.1 (Regulation compliance statement)",
        "testo": (
            "Se un token di marca temporale e' dichiarato marca temporale elettronica qualificata ai sensi del "
            "Regolamento (UE) n. 910/2014, dovrebbe contenere una istanza dell'estensione qcStatements nel campo "
            "delle estensioni del token, con la sintassi definita nella clausola 3.2.6 di IETF RFC 3739; se "
            "l'estensione qcStatements e' presente, deve contenere una istanza dello statement "
            "\"esi4-qtstStatement-1\" come definito nell'Annex B; l'estensione qcStatements non deve essere "
            "marcata come critical."
        ),
        "testo_integrale": (
            "9.1 Regulation compliance statement: If a time-stamp token is claimed to be a qualified electronic "
            "time-stamp as per Regulation (EU) No 910/2014 [i.2], it should contain one instance of the "
            "qcStatements extension in the time-stamp token extension field with the syntax as defined in IETF "
            "RFC 3739 [i.3], clause 3.2.6. If the qcStatements extension is present, it shall contain one "
            "instance of the statement \"esi4-qtstStatement- 1\" as defined in annex B. The extension "
            "qcStatements shall not be marked as critical."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "quando la marca temporale e' dichiarata marca temporale elettronica qualificata ai sensi del "
            "Regolamento (UE) n. 910/2014"
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
    {
        "riferimento": "Annex A (Structure for the policy field)",
        "testo": (
            "Quando la marca temporale e' emessa da una TSA conforme a ETSI EN 319 421, il campo policy del "
            "TSTInfo deve includere l'identificatore specificato nella clausola 5.2 di ETSI EN 319 421, oppure "
            "l'identificatore proprio della TSA quando questa incorpora o vincola ulteriormente la policy."
        ),
        "testo_integrale": (
            "Annex A (normative): Structure for the policy field. When the time-stamp token is issued by a TSA "
            "that conforms to ETSI EN 319 421 [7], then the policy field in the TSTInfo shall include: - the "
            "identifier specified in clause 5.2 of ETSI EN 319 421 [7], or - TSA's own identifier when the TSA "
            "incorporates or further constrains the policy above."
        ),
        "tipo_obbligo": "tecnico/sicurezza",
        "stato": "vigente",
        "condizione_applicabilita": (
            "quando la marca temporale e' emessa da una TSA conforme a ETSI EN 319 421"
        ),
        "soggetti": [{"categoria": "QTSP/gestore", "ruolo": "obbligato"}],
    },
]

RIGHE_PRINCIPI = [
    {
        "riferimento": "Annex B (ASN.1 declarations)",
        "testo": (
            "Dichiarazioni ASN.1 normative che definiscono gli object identifier id-etsi-tsts e "
            "id-etsi-tsts-EuQCompliance e lo statement esi4-qtstStatement-1 (QC-STATEMENT identificato da "
            "id-etsi-tsts-EuQCompliance): con l'inclusione di tale statement l'emittente dichiara che il token "
            "di marca temporale e' emesso come marca temporale elettronica qualificata ai sensi del Regolamento "
            "(UE) n. 910/2014."
        ),
        "testo_integrale": (
            "Annex B (normative): ASN.1 declarations. -- object identifiers\n"
            "id-etsi-tsts OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4) etsi(0)\n"
            "id-tst-profile(19422) 1 }\n"
            "id-etsi-tsts-EuQCompliance OBJECT IDENTIFIER ::= { id-etsi-tsts 1 }\n"
            "-- statements\n"
            "esi4-qtstStatement-1 QC-STATEMENT ::= { IDENTIFIED BY id-etsi-tsts-EuQCompliance }\n"
            "-- By inclusion of this statement the issuer claims that this\n"
            "-- time-stamp token is issued as a qualified electronic time-stamp according to\n"
            "-- the REGULATION (EU) No 910/2014."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
        "oggetti_giuridici": ["marca temporale elettronica qualificata"],
    },
    {
        "riferimento": "Annex C (Time-stamp token media type and file-extension)",
        "testo": (
            "Definisce, in conformita' a IETF RFC 6838, il media type e l'estensione di file che identificano "
            "un token di marca temporale: nome del media type \"Application\", nome del sottotipo "
            "\"vnd.etsi.timestamp-token\", nessun parametro richiesto, considerazioni di codifica \"binary\", "
            "estensione di file \"tst\"."
        ),
        "testo_integrale": (
            "Annex C (normative): Time-stamp token media type and file-extension. The following media-type and "
            "file-extension are defined in accordance with IETF RFC 6838 [i.6] to identify a time-stamp token: "
            "Media Type name: Application Media Subtype name: vnd.etsi.timestamp-token Required parameters: "
            "none encoding considerations: binary File extension: tst"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 9.1 (Regulation compliance statement)",
    "Annex A (Structure for the policy field)",
    "Annex B (ASN.1 declarations)",
    "Annex C (Time-stamp token media type and file-extension)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_completezza_testo_integrale, verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    verifica_completezza_testo_integrale([sys.modules[__name__]])
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
