Un file .csv (comma separated values) contiene valori separati da virgole. 
La prima riga contiene i nomi degli attributi, mentre ogni riga successiva
si riferisce ad un elemento del dataset e contiene un valore per ogni attributo
(vedi esempio più avanti).

E' dato il file province-italiane.csv contenente dati sulle province italiane, 
In particolare ogni riga contiene: sigla, nome provincia e regione di appartenenza 
di una provincia. I dati sono ordinati per nome provincia.
Di seguito sono riportate le prima righe del file:

Sigla,Provincia,Regione
AG,Agrigento,Sicilia
AL,Alessandria,Piemonte
AN,Ancona,Marche
AO,Aosta,Valle d'Aosta
AQ,L'Aquila,Abruzzo
AR,Arezzo,Toscana
AP,Ascoli-Piceno,Marche
...

Scrivere un programma che restituisca in output un nuovo file chiamato 
"regioni.csv" contenente una riga per regione in cui ogni riga contenga il nome 
della regione, una virgola e l'elenco delle sue province ordinate in ordine alfabetico
separate da spazi.
Anche le righe del file devono essere ordinate per nome della regione in ordine 
alfabetico.
Di seguito sono riportate le prime righe del file "regioni.csv":

Abruzzo, Chieti L'Aquila Pescara Teramo 
Basilicata, Matera Potenza 
Calabria, Catanzaro Cosenza Crotone Reggio-Calabria Vibo-Valentia 
Campania, Avellino Benevento Caserta Napoli Salerno 
...