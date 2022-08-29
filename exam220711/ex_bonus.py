import os

if __name__=="__main__":
    f = open(os.path.join("exam220711","data","clienti.csv"),"r",encoding="utf-8")

    clienti = []
    for line in f:
        line = line.split(",")
        codice = line[0]
        punteggio = int(line[1])

        if len(clienti)==10 and punteggio < clienti[-1][1]:
            continue

        idx = 0
        while idx < len(clienti) and clienti[idx][1]>punteggio:
            idx += 1

        if idx == len(clienti):
            clienti.append((codice,punteggio))
        else:
            clienti = clienti[0:idx] + [(codice,punteggio)] + clienti[idx:]
        
        if len(clienti)>10:
            clienti = clienti[0:10]

    f.close()

    f = open(os.path.join("exam220711","result_bonus.csv"),"w",encoding="utf-8")
    for c in clienti:
        f.write(f"{c[0]},{c[1]}\n")
    f.close()