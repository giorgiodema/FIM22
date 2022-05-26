from datetime import date

class Cittadino:
    """
    Classe per rappresentare un cittadino 
    italiano, la classe contiene tutte le 
    informazioni necessarie per calcolare 
    il codice fiscale
    """
    def __init__(self,
                    nome:str,cognome:str,
                    datan:date,
                    comune:str,
                    sesso:str) -> None:
        
        self.nome = nome
        self.cognome = cognome
        self.datan = datan
        self.comune = comune
        self.sesso = sesso

    def cf(self) -> str:
        return  self.nome + \
                self.cognome + \
                str(self.datan) + \
                str(self.comune) + \
                self.sesso


c1 = Cittadino("Mario","Rossi",date(1990,7,2),"Roma","M")

c1.datan = date(1995,8,10)
print(c1.datan)
print(c1.cf())



    