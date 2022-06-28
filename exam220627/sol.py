from typing import Dict,List,Tuple
import math
from datetime import date,timedelta

hosp:Dict[str,List[str]] = {}
f_in = open("exam220627/data/ingressi.csv","r",encoding="utf-8")
f_out = open("exam220627/data/uscite.csv","r",encoding="utf-8")

for line in f_in:
    line = line.split(",")
    pat = line[0]
    din = line[1].strip()
    hosp[pat] = [din]

for line in f_out:
    line = line.split(",")
    pat = line[0]
    dout = line[1].strip()
    hosp[pat].append(dout)

f_in.close()
f_out.close()

f_hosp = open("exam220627/ricoveri.txt","w",encoding="utf-8")
for pat in sorted(hosp.keys()):
    print(f"{pat},{hosp[pat][0]},{hosp[pat][1]}",file=f_hosp)
f_hosp.close()

length_max = 0
code = None
for pat in hosp.keys():
    din = hosp[pat][0].split("-")
    dout = hosp[pat][1].split("-")

    din_y = int(din[0])
    din_m = int(din[1])
    din_d = int(din[2])

    dout_y = int(dout[0])
    dout_m = int(dout[1])
    dout_d = int(dout[2])

    # solution with python datetime
    diff = date(dout_y,dout_m,dout_d)-date(din_y,din_m,din_d)
    diff = diff.days

    # or if we assume each month has 30 days than
    #diff = (dout_y-din_y)*365 + (dout_m-din_m)*30 + dout_d-din_d

    if diff > length_max:
        length_max = diff
        code = pat
    
print(f"{code},{length_max}")
