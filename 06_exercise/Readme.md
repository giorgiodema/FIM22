# Istruzioni
L'esercitazione di oggi consiste nello scrivere un programma per calcolare il codice fiscale. Le istruzioni su come 
calcolare il codice fiscale si trovano <a href=http://gratis.pietrelcinanet.com/codice_fiscale/codice.htm>qui</a>. In particolare 
il calcolo del codice fiscale (per semplicità ci limitiamo al solo caso di cittadino Italiano) richiede le seguenti 
informazioni:
- Nome
- Cognome
- Data di nascita
- Comune di nascita
- Sesso

Inoltre serve il codice del comune di nascita. Il file "Elenco-comuni-italiani.csv" contiene i nomi di tutti i comuni 
italiani e i relativi codici. E' un file in formato csv, perciò la prima riga contiene informazioni sul tipo di dato 
contenuto in ogni colonna. In particolare noi siamo interessati alle seguenti colonne:
- colonna 6 : contiene il nome del comune
- colonna 20: contiene il codice del comune (4 cifre)

Il primo programma che andremo a scrivere definisce la classe Paziente che ha come attributi i dati anagrafici e un 
metodo per calcolare il codice fiscale. La classe Paziente inoltre ridefinisce il metodo "__str__" in modo tale che 
ritorni una stringa contenente tutti gli attributi del paziente più il codice fiscale. 
Il programma inoltre legge i dati dei pazienti dal file "pazienti.csv" e crea un 
oggetto della classe Paziente per ogni paziente nel file. Gli oggetti pazienti vengono salvati in una lista e 
successivamente l'intera lista viene ordinata utilizzando come chiave nome e cognome (in questo ordine) e 
gli elementi della lista vengono stampati a schermo, stampando per ogni paziente i dati anagrafici e il codice fiscale.

Il secondo programma utilizza la classe Paziente del programma precedente per creare un Iteratore che legge le righe del 
file "pazienti.csv" una alla volta e ritorna i soli pazienti di sesso maschile. Utilizzare l'iteratore per scrivere su file "pazienti_maschi.txt" il codice fiscale dei soli pazienti maschi, uno per riga.