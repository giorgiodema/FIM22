import os
from sol1 import Paziente

class IteratorePazientiMaschi:

    def __init__(self,path) -> None:
        self.f = open(path,"r",encoding="utf-8")
        self.f.readline()

    def __iter__(self):
        return self

    def __next__(self)->Paziente:
        line = self.f.readline()
        if line=="":
            self.f.close()
            raise StopIteration
        line = line.split(",")
        # continue iterating the file utill either we find
        # a male patient or the end of file is reached
        while line[4].strip()!="M":
            line = self.f.readline()
            if line=="":
                self.f.close()
                raise StopIteration
            line = line.split(",")
        return Paziente(line[0],line[1],line[2],line[3],line[4].strip())

if __name__=="__main__":
    it = IteratorePazientiMaschi(os.path.join("data","pazienti.csv"))
    f = open("pazienti_maschi.txt","w")
    for p in it:
        f.write(f"{p.cf()}\n")
    f.close()