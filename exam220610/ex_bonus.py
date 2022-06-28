import os

if __name__=="__main__":
    
    patologie = {}

    f = open(os.path.join("exam220610","data","pazienti.csv"),"r",encoding="utf-8")
    for line in f:
        line = line.split(",")
        cf = line[0]
        data = line[1]
        pat = line[2].strip()

        if pat not in patologie:
            patologie[pat] = 1
        else:
            patologie[pat] += 1
    f.close()

    f = open(os.path.join("exam220610","result_bonus.txt"),"w",encoding="utf-8")
    for p in sorted(patologie.keys()):
        f.write(f"{p} {patologie[p]}\n")
    f.close()


