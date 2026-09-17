"""Moduli di autoria granulare per fonte (ADR-0007).

Ogni sottopacchetto `app/seed_data/<fonte>/` contiene un modulo per
capitolo (`cap01.py`, `cap02.py`, ...), autorato indipendentemente (anche
da subagent paralleli) e unito da `app/seed_data/lib.py::inserisci_capitoli`.
Vedi `docs/procedura-import-granulare.md` per il workflow completo.
"""
