import os


def get_sort_key(x):
    return x[1]


if __name__=="__main__":
    f = open(os.path.join("exam220711","data","clienti.csv"),"r",encoding="utf-8")

    clienti = []
    for line in f:
        line = line.split(",")
        codice = line[0]
        punteggio = int(line[1])
        if len(clienti)<10:
            clienti.append((codice,punteggio))
        else:
            min_punteggio = clienti[0][1]
            min_idx = 0
            for i in range(1,10):
                if clienti[i][1] < min_punteggio:
                    min_punteggio = clienti[i][1]
                    min_idx = i
            if min_punteggio < punteggio:
                clienti[min_idx] = (codice,punteggio)

    clienti.sort(key=get_sort_key,reverse=True)
    f.close()

    f = open(os.path.join("exam220711","result.csv"),"w",encoding="utf-8")
    for c in clienti:
        f.write(f"{c[0]},{c[1]}\n")
    f.close()