**Progetto: Sistema di Catene di Calcolo Distribuito Dinamiche**

**Obiettivo del Progetto**

Lo scopo di questo progetto è sviluppare un protocollo e un sistema per la realizzazione di catene di calcolo distribuito dinamiche. Gli studenti saranno responsabili della progettazione di un server di front-end che riceve task di elaborazione descritti da un file JSON, come la realizzazione di un certo numero di inversioni di matrici, e che può delegare parte del calcolo a un insieme dinamico di server di calcolo collegati in logica a catena.

**Specifiche del Progetto**

**Architettura del Sistema**: L'architettura del sistema dovrebbe includere un server di front-end e un insieme di server di calcolo. Il server di front-end dovrebbe essere in grado di ricevere task di elaborazione e di delegare parte del calcolo ai server di calcolo.

**Gestione Dinamica dei Server di Calcolo**: Il server di front-end deve essere in grado di gestire dinamicamente un insieme di server di calcolo. Gli studenti devono progettare un protocollo per l'aggiunta e la rimozione dei server di calcolo, che potrebbe includere la notifica al server di front-end quando un nuovo server di calcolo è disponibile o quando un server di calcolo esistente non è più disponibile.

**Delega dei Task di Elaborazione**: Il server di front-end deve essere in grado di delegare parte dei task di elaborazione ai server di calcolo. Gli studenti devono progettare un protocollo per la delega dei task, che potrebbe includere l'invio del file JSON che descrive il task di elaborazione da parte del server di front-end al server di calcolo.

**Esecuzione dei Task di Elaborazione**: I server di calcolo devono essere in grado di eseguire i task di elaborazione e di restituire i risultati al server di front-end. Gli studenti devono progettare un protocollo per l'esecuzione dei task e per la restituzione dei risultati, che potrebbe includere l'invio dei risultati dell'elaborazione da parte del server di calcolo al server di front-end.

**Interfacciamento con il Server di Front-End**: Gli studenti devono progettare un'interfaccia utente o un'interfaccia a riga di comando per inoltrare un task di elaborazione al server di front-end. Questa interfaccia dovrebbe permettere agli utenti di inviare un file JSON che descrive il task di elaborazione e di ricevere i risultati dell'elaborazione.

**Sicurezza**: Il sistema dovrebbe implementare misure di sicurezza di base, come l'autenticazione degli utenti e dei server di calcolo e la criptazione delle comunicazioni.

**Tolleranza ai Guasti**: Il sistema dovrebbe essere in grado di gestire guasti dei server di calcolo senza interruzioni nell'elaborazione dei task. Se un server di calcolo si disconnette improvvisamente, il server di front-end dovrebbe essere in grado di delegare il task di elaborazione a un altro server di calcolo.

**Implementazione**: L'implementazione del progetto deve essere realizzata in Python, utilizzando la programmazione concorrente con l'uso di processi e/o thread. Deve inoltre gestire la comunicazione tra processi in rete.

**Consegna del Progetto**

Gli studenti dovranno fornire il codice sorgente del progetto, la documentazione del progetto (che include la descrizione del server di front-end, dei protocolli per la gestione dei server di calcolo, la delega dei task di elaborazione, l'esecuzione dei task e la restituzione dei risultati, e l'interfacciamento con il server di front-end), e i test. Il tutto deve essere presentato in un formato facilmente accessibile e leggibile.
