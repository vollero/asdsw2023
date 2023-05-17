**Progetto: Sistema di Replicazione di File Distribuito Peer-to-Peer**

**Obiettivo del Progetto**

Lo scopo di questo progetto è sviluppare un sistema di replicazione di file distribuito che utilizza un'infrastruttura peer-to-peer (P2P) per supportare il caricamento e la replicazione dei file. Gli studenti saranno responsabili della progettazione dell'architettura del sistema, del protocollo di comunicazione tra i nodi dell'infrastruttura e del modello di interfacciamento dei client.

**Specifiche del Progetto**

**Architettura del Sistema**: 

L'architettura del sistema dovrebbe essere completamente distribuita, il che significa che non ci dovrebbe essere un nodo centrale. Ogni nodo nel sistema dovrebbe essere sia un client (che carica e accede ai file) sia un server (che memorizza e replica i file).

**Protocollo di Comunicazione**: 

Gli studenti devono progettare un protocollo di comunicazione per lo scambio di informazioni e file tra i nodi. Questo protocollo dovrebbe supportare almeno le seguenti operazioni:

* **Registrazione**: Un nodo deve poter registrarsi nella rete, informando gli altri nodi della sua presenza.
* **Caricamento dei file**: Un nodo deve poter caricare un file nella rete, che verrà replicato su un certo numero di altri nodi.
* **Accesso ai file**: Un nodo deve poter accedere a un file, indipendentemente dal nodo in cui il file è stato caricato originariamente.
* **Replicazione dei file**: Un nodo deve poter replicare i file su altri nodi, secondo una politica di replicazione predefinita.
* **Disconnessione**: Un nodo deve poter notificare gli altri nodi quando lascia la rete.

**Modello di Interfacciamento dei Client**: 

Gli studenti devono progettare un'interfaccia utente o un'interfaccia a riga di comando per i client. Questa interfaccia dovrebbe permettere agli utenti di caricare file, accedere ai file, e vedere lo stato della connessione alla rete.

**Sicurezza e Privacy**: 

Il sistema dovrebbe implementare misure di sicurezza di base, come la criptazione dei file e l'autenticazione degli utenti. Inoltre, il sistema dovrebbe rispettare la privacy degli utenti, non conservando i file più a lungo del necessario e non rivelando le informazioni degli utenti a terzi senza il loro consenso.

**Tolleranza ai Guasti**: 

Il sistema dovrebbe essere in grado di gestire guasti dei nodi senza perdita di file. Se un nodo si disconnette improvvisamente, il sistema dovrebbe essere in grado di recuperare il file da altre repliche disponibili nella rete.

**Scalabilità**: 

Il sistema dovrebbe essere in grado di gestire un numero elevato di nodi e di file. Gli studenti dovrebbero pensare a come possono progettare il sistema per essere il più scalabile possibile.

**Implementazione**: 

L'implementazione del progetto deve essere realizzata in Python, utilizzando la programmazione concorrente con l'uso di processi e/o thread. Deve inoltre gestire la comunicazione
