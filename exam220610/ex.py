import os

if __name__=="__main__":
    
    pazienti = {}
    patologie = set()

    f = open(os.path.join("exam220610","data","pazienti.csv"),"r",encoding="utf-8")
    for line in f:
        line = line.split(",")
        cf = line[0]
        data = line[1]
        pat = line[2].strip()

        patologie.add(pat)

        if cf not in pazienti:
            pazienti[cf] = set([pat])
        else:
            pazienti[cf].add(pat)
    f.close()

    f = open(os.path.join("exam220610","result.txt"),"w",encoding="utf-8")
    for c in sorted(pazienti.keys()):
        f.write(f"{c} ")
        for p in pazienti[c]:
            f.write(f"{p} ")
        f.write("\n")
    f.close()

    print(f"Il numero di patologie distinte è: {len(patologie)}")


