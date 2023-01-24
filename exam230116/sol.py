from typing import Dict,List
if __name__=="__main__":
    
    regioni:Dict[str,List[str]] = {}
    f = open("province-italiane.csv","r",encoding="utf-8")
    f.readline()
    for line in f:
        l = line.strip().split(",")
        sigla   = l[0]
        provincia = l[1]
        regione = l[2]
        if regione not in regioni:
            regioni[regione] = [provincia]
        else:
            regioni[regione].append(provincia)
    f.close()
    
    f = open("regioni.csv","w",encoding="utf-8")
    print("Regione, Elenco Province",file=f)
    for k in sorted(regioni.keys()):
        f.write(k)
        f.write(", ")
        for p in sorted(regioni[k]):
            f.write(p)
            f.write(" ")
        f.write("\n")
    f.close()
