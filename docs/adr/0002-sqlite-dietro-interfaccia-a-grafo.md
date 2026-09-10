# Storage su SQLite dietro un'interfaccia a grafo astratta, non un graph DB dedicato

Contesto: il censimento è un knowledge graph (ADR-0001). La scala finale attesa è alta (decine di fonti, centinaia di obblighi ciascuna → migliaia di nodi), scala alla quale un graph DB dedicato (Neo4j/Memgraph) sarebbe naturale per le query di navigazione multi-hop. Il pilota (eIDAS+CAD) è invece piccolo, e l'ambiente è locale senza dipendenza da server esterni (stessa filosofia di sgsi-rag).

Deciso: tabelle SQLite (`obblighi`, `relazioni`) incapsulate dietro un'interfaccia di accesso a grafo (es. "vicini di questo nodo per tipo di relazione", "cammino tra due nodi fino a N salti"), senza SQL scritto ad-hoc sparso nel codice applicativo.

Perché: a scala di pilota SQLite basta e non introduce un secondo motore da installare/gestire in locale. La scala finale attesa rende comunque probabile una migrazione futura a un graph DB dedicato: tenendo il codice applicativo dietro un'interfaccia a grafo invece che dietro SQL diretto, quella migrazione diventa "cambiare l'implementazione dietro l'interfaccia" invece di "riscrivere il motore di interrogazione".
