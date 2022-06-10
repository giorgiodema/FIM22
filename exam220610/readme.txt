Dato un file csv contenente un elenco di pazienti con i seguenti dati:

- Codice Fiscale
- Data Ricovero
- Codice Patologia

crea un file result.txt contenente esattamente una riga per paziente. Ogni riga contiene il 
codice fiscale del paziente seguito da un singolo spazio e dai codici delle patologie per cui 
è stato ricoverato. Le righe devono essere ordinate per codice fiscale. 
NB: il codice di una patologia non deve essere ripetuto più volte nella stessa riga, anche 
se il paziente è stato ricoverato più volte per la stessa patologia essa va inserita una 
volta sola.

Ad esempio supponiamo che 
il file contenga le seguenti righe:

MZZMRM51D60A779P,18/01/2001,A90
BNDNDA97L42M273I,23/03/2004,B73
MZZMRM51D60A779P,12/12/2010,A95
BNDNDA97L42M273I,18/11/2011,B73

Il file di output conterrà le seguenti righe (in questo ordine):

BNDNDA97L42M273I B73
MZZMRM51D60A779P A90 A95

Inoltre il programma stampa su schermo il numero di patologie DISTINTE presenti nel database.
Nel caso il file di input sia quello dell'esempio precedente il programma stamperà 3.


BONUS:
Creare un file bonus.txt che contiene una riga per ogni patologia contenente 
il codice della patologia e il numero di occorrenze della patologia separato da uno spazio.
Nell'esempio precedente il file di output deve contenere le seguenti righe:

A90 1
A95 1
B73 2