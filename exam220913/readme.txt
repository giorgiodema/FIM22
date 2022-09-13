Sono dati due file corso1.txt e corso2.txt contenenti cognome e nome degli studenti di due corsi di laurea (uno per riga) ordinati in ordine alfabetico. Scrivere un programma in cui venga implementato un oggetto che permetta l'iterazione degli studenti di entrambi i file in ordine alfabetico. L'iteratore dovrà restituire tuple di due elementi in cui il primo elemento è una stringa contenente cognome e nome dello studente, mentre il secondo elemento è un intero con valore 1 se lo studente appartiene al corso1 oppure 2 se lo studente appartiene al corso2. Gli elementi devono essere restituiti in ordine alfabetico (per cognome e nome) indipendentemente dal corso di appartenenza.
Utilizzare quanto realizzato per creare un file studenti.txt che conterrà la lista degli studenti di entrambi i corsi (uno per riga) con il relativo corso di appartenenza, ordinati per ordine alfabetico.

Ad esempio se il contenuto del file corso1.txt è il seguente:
Bianchi Leonardo
Costa Sofia
De Luca Giulia
Esposito Francesco
Greco Alessandro
Longo Aurora
Morelli Alice
Pellegrini Lorenzo
Rossetti Mattia
Rossi Guido

Mentre il conenuto del file corso2.txt è il seguente:
Bruno Andrea
Conti Gabriele
D'Angelo Ginevra
Farina Emma
Mazza Giorgia
Natale Beatrice
Paoli Riccardo
Rossi Mario
Venditti Tommaso

Il contenuto del file studenti.txt sarà:
Bianchi Leonardo, 1
Bruno Andrea, 2
Conti Gabriele, 2
Costa Sofia, 1
D'Angelo Ginevra, 2
De Luca Giulia, 1
Esposito Francesco, 1
Farina Emma, 2
Greco Alessandro, 1
Longo Aurora, 1
Mazza Giorgia, 2
Morelli Alice, 1
Natale Beatrice, 2
Paoli Riccardo, 2
Pellegrini Lorenzo, 1
Rossetti Mattia, 1
Rossi Guido, 1
Rossi Mario, 2
Venditti Tommaso, 2

BONUS
Implementare l'iteratore senza usare il metodo sort. Sfruttare il fatto che entrambi i file sono già ordinati in ordine alfabetico per restituire il risultato ordinato.