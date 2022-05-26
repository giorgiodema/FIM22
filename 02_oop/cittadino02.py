from datetime import date
class Cittadino:
   """ Classe per rappresentare un cittadino """
   numero_istanze = 0
   def __init__(self,
                   nome:str,cognome:str,
                   datan:date,
                   comune:str,
                   sesso:str) -> None:
      
       Cittadino.numero_istanze += 1
       self.nome = nome
       self.cognome = cognome
       self.datan = datan
       self.comune = comune
       self.sesso = sesso

   # Viene chiamata dall'interprete quando
   # l'oggetto viene eliminato dal garbage
   # collector
   def __del__(self):
       Cittadino.numero_istanze -= 1

c1 = Cittadino("Mario","Rossi",date(1990,7,2),"Roma","M")
print(Cittadino.numero_istanze)
del c1
print(Cittadino.numero_istanze)



  

