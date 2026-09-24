"""ETSI EN 319 422 V1.1.1 (2016-03) - Electronic Signatures and Trust
Infrastructures (ESI); Time-stamping protocol and time-stamp token profiles.
Fonte 19 (la numerazione degli id e' risolta per riferimento dalla sessione
principale in app/seed.py - questo modulo NON tocca seed.py). Capitolo 1:
clausole 1 (Scope), 2 (References: 2.1 Normative references, 2.2 Informative
references), 3 (Definitions and abbreviations: 3.1 Definitions, 3.2
Abbreviations). Testo ufficiale in
app/.source_cache/etsi_319_422/cap01.txt (letto sempre con selettore `:raw`,
altrimenti il tool tronca le righe lunghe a 768 caratteri introducendo "..."
e mutilando la copia verbatim). Manifest di split:
app/.source_cache/etsi_319_422/manifest.json.

Modellazione (ADR-0007), stesso criterio gia' applicato alle altre fonti
ETSI gia' censite (ETSI EN 319 401, ETSI EN 319 412, ETSI EN 319 421) e
adattato alle clausole/sottoclausole di uno standard tecnico: un nodo per
ogni clausola/sottoclasse numerata che porta contenuto proprio; per le
clausole di cornice prive di requisito numerato un solo nodo Principio
dedicato. Questo capitolo non contiene alcun requisito numerato: 0 Obblighi,
3 Principi. Scelte voce per voce:

- Clausola 1 (Scope) -> 1 Principio "scopo/ambito di applicazione",
  riferimento "clausola 1 (Scope)". Perimetro in senso proprio: dichiara che
  il documento definisce un profilo per il protocollo di marcatura temporale
  e per il token di marca temporale definiti in IETF RFC 3161 (con
  aggiornamento opzionale ESSCertIDv2 in IETF RFC 5816), cosa supporta un
  time-stamping client e cosa supporta un time-stamping server; esclude
  esplicitamente dall'ambito la validazione delle marche temporali (definita
  in ETSI EN 319 102) e rinvia all'Annex C per il media type e l'estensione
  di file dei token di marca temporale. Nessun verbo prescrittivo ("shall"/
  "should") e nessun soggetto obbligato: e' dichiarazione di perimetro, non
  prescrizione. La clausola non contiene NOTE ufficiali.
- Clausola 2 (References: 2.1 Normative references, 2.2 Informative
  references) -> NESSUN nodo, NESSUN item di indice. E' bibliografia/
  paratesto puro: un elenco di documenti citati numerati [1]-[7] (normative)
  e [i.1]-[i.6] (informative) con le sole regole redazionali ETSI su
  riferimenti specifici/non specifici e le NOTE ETSI sulla validita' a lungo
  termine degli hyperlink, nessun contenuto normativo autonomo ne' effetto
  giuridico proprio. Stesso trattamento gia' riservato alla clausola 2 di
  ETSI EN 319 401 e di ETSI EN 319 421 (cap01). Si noti che la conversione
  PDF->markdown spezza l'elenco informative con un'interruzione di pagina
  ("***ETSI***" / "<!-- Page 6 -->" prima di [i.4]): paratesto spurio che
  conferma l'assenza di contenuto prescrittivo.
- Clausola 3.1 (Definitions) -> 1 Principio "definitorio" riassuntivo, NON
  un nodo per singolo termine: la clausola e' un glossario piatto senza
  struttura a lettere/numeri propria, quindi 4 nodi sarebbero 4 item di
  indice fittizi per un'unica clausola. Definisce 4 termini propri del
  documento: time-stamp; time-stamp token; Time-Stamping Authority (TSA);
  Time-Stamping Unit (TSU). In `testo_integrale` sono riportate tutte e
  quattro le definizioni verbatim, precedute dalla formula introduttiva
  ufficiale ("For the purposes of the present document, the following terms
  and definitions apply:"). La clausola non contiene NOTE ufficiali.
- Clausola 3.2 (Abbreviations) -> 1 Principio "definitorio" riassuntivo. La
  clausola elenca le abbreviazioni usate nel documento, precedute dalla
  formula introduttiva ufficiale ("For the purposes of the present document,
  the following abbreviations apply:"). La tabella PDF->markdown risulta
  parzialmente disallineata (la riga "|HTTPS RFC Request For Comments|..."
  accorpa in una sola cella l'etichetta HTTPS e l'abbreviazione RFC, con le
  rispettive forme estese distribuite tra le celle): le coppie sono quindi
  ricostruite in forma esplicita "ETICHETTA: Forma estesa." in
  `testo_integrale`, come gia' fatto per la clausola 3.3 di ETSI EN 319 421.
  Oltre alle sei abbreviazioni della tabella principale (ASN, EU, HTTP,
  HTTPS, RFC, TLS), la clausola riporta in coda, fuori tabella, anche TSA
  (Time-Stamping Authority) e TSU (Time-Stamping Unit): sono incluse in
  `testo_integrale` per completezza verbatim della clausola (ADR-0010).

Nessun Obbligo in questo capitolo: nessuna delle clausole coperte contiene un
verbo prescrittivo che imponga un comportamento a un soggetto identificabile.
La costruzione di relazioni e' demandata alla Fase 6 della sessione principale
(ADR-0009).
"""

RIGHE_OBBLIGHI: list[dict] = []

RIGHE_PRINCIPI = [
    {
        "riferimento": "clausola 1 (Scope)",
        "testo": (
            "Il documento definisce un profilo per il protocollo di marcatura temporale e per il token di "
            "marca temporale definiti in IETF RFC 3161, incluso l'aggiornamento opzionale ESSCertIDv2 in IETF "
            "RFC 5816; definisce cosa supporta un time-stamping client e cosa supporta un time-stamping "
            "server. La validazione delle marche temporali e' fuori ambito ed e' definita in ETSI EN 319 102. "
            "L'Annex C definisce il media type e l'estensione di file per i token di marca temporale."
        ),
        "testo_integrale": (
            "1 Scope: The present document defines a profile for the time-stamping protocol and the "
            "time-stamp token defined in IETF RFC 3161 [1] including optional ESSCertIDv2 update in IETF RFC "
            "5816 [4]. It defines what a time-stamping client supports and what a time-stamping server "
            "supports. Time-stamp validation is out of scope and is defined in ETSI EN 319 102 [i.4]. Annex C "
            "defines media type and file-extension for time-stamp tokens."
        ),
        "tipo_principio": "scopo/ambito di applicazione",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.1 (Definitions)",
        "testo": (
            "La clausola definisce 4 termini propri del documento: 'time-stamp' (dati in forma elettronica "
            "che legano altri dati elettronici a un momento determinato, provando che quei dati esistevano a "
            "quel momento); 'time-stamp token' (oggetto dati definito in IETF RFC 3161, che rappresenta una "
            "marca temporale); 'Time-Stamping Authority (TSA)' (Trust Service Provider che emette marche "
            "temporali usando una o piu' unita' di marcatura); 'Time-Stamping Unit (TSU)' (insieme di "
            "hardware e software gestito come unita' con una sola chiave di firma di marca temporale attiva "
            "per volta)."
        ),
        "testo_integrale": (
            "3.1 Definitions: For the purposes of the present document, the following terms and definitions "
            "apply: time-stamp: data in electronic form which binds other electronic data to a particular "
            "time establishing evidence that these data existed at that time time-stamp token: data object "
            "defined in IETF RFC 3161 [1], representing a time-stamp Time-Stamping Authority (TSA): Trust "
            "Service Provider which issues time-stamp using one or more time-stamping units Time-Stamping "
            "Unit (TSU): set of hardware and software which is managed as a unit and has a single time-stamp "
            "signing key active at a time"
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
    {
        "riferimento": "clausola 3.2 (Abbreviations)",
        "testo": (
            "La clausola elenca le abbreviazioni usate nel documento: ASN (Abstract Syntax Notation), EU "
            "(Europe), HTTP (HyperText Transfer Protocol), HTTPS (Hypertext Transfer Protocol over TLS), RFC "
            "(Request For Comments), TLS (Transport Layer Security), TSA (Time-Stamping Authority), TSU "
            "(Time-Stamping Unit)."
        ),
        "testo_integrale": (
            "3.2 Abbreviations: For the purposes of the present document, the following abbreviations apply: "
            "ASN: Abstract Syntax Notation. EU: Europe. HTTP: HyperText Transfer Protocol. HTTPS: Hypertext "
            "Transfer Protocol over TLS. RFC: Request For Comments. TLS: Transport Layer Security. TSA: "
            "Time-Stamping Authority. TSU: Time-Stamping Unit."
        ),
        "tipo_principio": "definitorio",
        "stato": "vigente",
    },
]

INDICE_ARTICOLI_LOCALE = [
    "clausola 1 (Scope)",
    "clausola 3.1 (Definitions)",
    "clausola 3.2 (Abbreviations)",
]

MAPPATURA_LOCALE = {rif: [rif] for rif in INDICE_ARTICOLI_LOCALE}

RELAZIONI: list[dict] = []


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from seed_data.lib import verifica_copertura

    verifica_copertura(INDICE_ARTICOLI_LOCALE, MAPPATURA_LOCALE)
    print(f"OK: {len(RIGHE_OBBLIGHI)} obblighi, {len(RIGHE_PRINCIPI)} principi, "
          f"{len(INDICE_ARTICOLI_LOCALE)} item di indice coperti.")
