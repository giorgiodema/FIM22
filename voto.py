

class Voto:
    def __init__(self,esame,matricola,voto,data) -> None:
        self.esame = esame
        self.matricola = matricola
        self.voto = voto
        self.data = data

    def __str__(self):
        return f"codice esame:{self.esame}, matricola studente:{self.matricola},voto:{self.voto},data:{self.data}"

def get_key(v:Voto):
    return v.matricola

f = open("voti_esame.txt","r",encoding='utf-8')
f.readline()
voti = []
for line in f:
    l = line.split(",")
    voti.append(Voto(l[0].strip(),l[1].strip(),l[2].strip(),l[3].strip()))

voti.sort(key=get_key)
for v in voti:
    print(v)