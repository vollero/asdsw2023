**Progetto: Sistema di Chat Distribuito Peer-to-Peer**

**Obiettivo del Progetto**

Lo scopo di questo progetto è lo sviluppo di un sistema di chat distribuito che utilizza un'infrastruttura peer-to-peer (P2P) per inoltrare i messaggi. 
Gli studenti saranno responsabili della progettazione dell'architettura del sistema, del protocollo di comunicazione tra i nodi dell'infrastruttura e del modello 
di interfacciamento dei client.

**Specifiche del Progetto**

 **Architettura del Sistema**: 

 L'architettura del sistema dovrebbe essere completamente distribuita, il che significa che non ci dovrebbe essere un nodo centrale. Ogni nodo nel sistema dovrebbe essere sia un client (che invia e riceve messaggi) sia un server (che inoltra i messaggi ad altri nodi).

 **Protocollo di Comunicazione**: 

 Gli studenti devono progettare un protocollo di comunicazione per lo scambio di messaggi tra i nodi. 
 Questo protocollo dovrebbe supportare almeno le seguenti operazioni:

   **Registrazione**: Un nodo deve poter registrarsi nella rete, informando gli altri nodi della sua presenza.

   **Inoltro dei messaggi**: Un nodo deve poter inoltrare un messaggio a tutti gli altri nodi nella rete.

   **Ricezione dei messaggi**: Un nodo deve poter ricevere messaggi da altri nodi.

   **Disconnessione**: Un nodo deve poter notificare gli altri nodi quando lascia la rete.

 **Modello di Interfacciamento dei Client**: 

 Gli studenti devono progettare un'interfaccia utente o un'interfaccia a riga di comando per i client. 
 Questa interfaccia dovrebbe permettere agli utenti di inviare messaggi, visualizzare i messaggi ricevuti, e vedere  lo stato della connessione alla rete.

 **Sicurezza e Privacy**: Il sistema dovrebbe implementare misure di sicurezza di base, come la criptazione dei  messaggi e l'autenticazione degli utenti. Inoltre, il sistema dovrebbe rispettare la privacy degli utenti, non  conservando i messaggi più a lungo del necessario e non rivelando le informazioni degli utenti a terzi senza il loro  consenso.

 **Tolleranza ai Guasti**: Il sistema dovrebbe essere in grado di gestire guasti dei nodi senza perdita di messaggi.  Se un nodo si disconnette improvvisamente, il sistema dovrebbe essere in grado di ri-routare i messaggi attraverso  altri nodi.

 **Scalabilità**: Il sistema dovrebbe essere in grado di gestire un numero elevato di nodi e di messaggi. Gli studenti dovrebbero pensare a come possono progettare il sistema per essere il più scalabile possibile.

 **Implementazione**: L'implementazione del progetto deve essere realizzata in Python, utilizzando la programmazione  concorrente con l'uso di processi e/o thread. Deve inoltre gestire la comunicazione tra processi in rete.

 **Test**: Gli studenti devono fornire test appropriati per verificare la corretta funzionalità del sistema. Questi test dovrebbero coprire tutte le funzionalità chiave del sistema e dovrebbero essere automatizzati per quanto possibile.

 **Consegna del Progetto**

 Gli studenti dovranno fornire il codice sorgente del progetto, la documentazione del progetto 
(che include la descrizione dell'architettura del sistema, del protocollo di comunicazione e del modello di interfacciamento dei client), e i test. 
Il tutto deve essere presentato in un formato facilmente accessibile e leggibile.
