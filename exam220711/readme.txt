Una catena di supermercati assegna ad ogni cliente un punto per ogni euro di 
spesa effettuato. Alla fine dell'anno vuole premiare i 10 clienti che hanno 
totalizzato il punteggio più alto. 
Il file clienti.csv è formato da due colonne in cui la prima contiene i codici 
identificativi dei clienti (ad ongi cliente è assegnato un codice alfanumerico 
univoco di 9 cifre) mentre la seconda colonna contiene i punteggi.

Un esempio di file di input è il seguente:

AHDKS83I9,2508
AIGDS7901,3018
GBDUEOSA9,1200
YTSPAJ561,5071
LOPABEYU5,1273
AYU781KS0,9017
AUDBAHJ56,8718
AUIEWPJ14,1401
AYUDSJKAE,500
AUIHYUS73,9181
GHNBSAUI8,108
ABDY8329I,1129
QUETSA711,10320
IAPWB8916,2890

Scrivere un programma che crei un file result.csv contenente i codici dei 10 clienti con 
i punteggi più alti e il relativo punteggio (nello stesso formato del file clienti.csv). 
La soluzione sviluppata NON deve caricare l'intero contenuto del file in memoria (supponiamo 
che il file dei clienti sia molto lungo).

Nel caso del file di input dell'esempio, il file di output conterrà le seguenti righe:

QUETSA711,10320
AUIHYUS73,9181
AYU781KS0,9017
AUDBAHJ56,8718
YTSPAJ561,5071
AIGDS7901,3018
IAPWB8916,2890
AHDKS83I9,2508
AUIEWPJ14,1401
LOPABEYU5,1273

BONUS:
Implementare la seguente ottimizzazione: mantenere una lista ordinata dei 10 clienti con 
i punteggi più alti, ogni volta che viene letto un nuovo cliente dal file, se la lista contiene 
già 10 elementi, confrontare il punteggio del cliente con l'ultimo della lista. Se il suo punteggio 
è maggiore, inserire il cliente in modo tale da mantenere la lista ordinata per punteggio in ordine 
crescente.