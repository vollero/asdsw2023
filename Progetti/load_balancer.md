**Progetto: Sistema di Bilanciamento del Carico per Server di Trasferimento File**

**Obiettivo del Progetto**

Lo scopo di questo progetto è sviluppare un protocollo e un sistema di bilanciamento del carico tra più server di trasferimento file. 
Gli studenti saranno responsabili della progettazione del load balancer, che deve gestire dinamicamente un insieme variabile di server identici e tenere traccia dei trasferimenti file secondo una politica di comunicazione da loro scelta.

**Specifiche del Progetto**

  **Architettura del Sistema**: L'architettura del sistema dovrebbe includere un load balancer e un insieme di server di trasferimento file. 
  Il load balancer dovrebbe essere in grado di gestire dinamicamente un numero variabile di server identici.

  **Gestione dinamica dei server**: Il load balancer deve essere in grado di aggiungere e rimuovere server in modo dinamico. 
  Gli studenti devono progettare un protocollo per l'aggiunta e la rimozione dei server, che potrebbe includere la notifica al load balancer quando un nuovo server è disponibile o quando un server esistente non è più disponibile.

  **Bilanciamento del carico**: Il load balancer deve distribuire i trasferimenti file tra i server in modo da bilanciare il carico tra di essi. Gli studenti devono decidere come il load balancer determina quale server utilizzare per un trasferimento file, che potrebbe basarsi su fattori come il numero attuale di trasferimenti file in corso su ogni server o la quantità di risorse disponibili su ogni server.

  **Tracciamento dei trasferimenti file**: Il load balancer deve tenere traccia dei trasferimenti file. Gli studenti devono progettare una politica di comunicazione per il tracciamento dei trasferimenti file, che potrebbe includere la notifica al load balancer all'inizio e alla fine di ogni trasferimento file.

  **Interrogazione e redirezione dei client**: Gli studenti devono progettare un protocollo per l'interrogazione del load balancer e la redirezione dei client verso il server specifico con cui effettueranno il trasferimento. Questo protocollo potrebbe includere la richiesta da parte del client di un trasferimento file, la selezione da parte del load balancer del server da utilizzare, e la redirezione del client verso quel server.

  **Sicurezza**: Il sistema dovrebbe implementare misure di sicurezza di base, come l'autenticazione degli utenti e dei server e la criptazione delle comunicazioni.

  **Tolleranza ai Guasti**: Il sistema dovrebbe essere in grado di gestire guasti dei server senza interruzioni nei trasferimenti file. Se un server si disconnette improvvisamente, il load balancer dovrebbe essere in grado di redirigere il trasferimento file verso un altro server.

  **Implementazione**: L'implementazione del progetto deve essere realizzata in Python, utilizzando la programmazione concorrente con l'uso di processi e/o thread. Deve inoltre gestire la comunicazione tra processi in rete.

**Consegna del Progetto**

Gli studenti dovranno fornire il codice sorgente del progetto, la documentazione del progetto (che include la descrizione del sistema di bilanciamento del carico, 
dei protocolli di gestione dei server, di bilanciamento del carico, di tracciamento dei trasferimenti file e di interrogazione e redirezione dei client), e i test. 
Il tutto deve essere presentato in un formato facilmente accessibile e leggibile.
