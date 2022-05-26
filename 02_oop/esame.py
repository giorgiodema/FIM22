

class Esame:
    def __init__(self,corso,matricola,voto,data) -> None:
        self.corso = corso
        self.matricola = matricola
        self.voto = voto
        self.data = data

    def __str__(self):
        return f"codice corso:{self.corso}, matricola studente:{self.matricola},voto:{self.voto},data:{self.data}"

def get_key(v:Esame):
    return v.matricola

f = open("voti_esame.txt","r",encoding='utf-8')
f.readline()
voti = []
for line in f:
    l = line.split(",")
    voti.append(Esame(l[0].strip(),l[1].strip(),l[2].strip(),l[3].strip()))

voti.sort(key=get_key)
for v in voti:
    print(v)