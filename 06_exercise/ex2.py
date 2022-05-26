import os
from sol1 import Paziente

class IteratorePazientiMaschi:

    def __init__(self,path) -> None:
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __next__(self)->Paziente:
        raise NotImplementedError

if __name__=="__main__":
    # programma utilizza la classe Paziente del programma precedente per creare un Iteratore che legge le righe del 
    # file "pazienti.csv" una alla volta e ritorna i soli pazienti di sesso maschile. Utilizzare l'iteratore per scrivere su file "pazienti_maschi.txt" il codice fiscale dei soli pazienti maschi, uno per riga.
    it = IteratorePazientiMaschi(os.path.join("data","pazienti.csv"))
    f = open("pazienti_maschi.txt","w")
    for p in it:
        f.write(f"{p.cf()}\n")
    f.close()