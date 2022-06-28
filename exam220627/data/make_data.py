import random
import string
from functools import reduce
from datetime import date,timedelta

random.seed(9)

N_PATIENTS = 10

def generate_random_id(length=7):
    chars = string.ascii_letters[26:]+"0123456789"
    id = reduce(lambda x,y:x+y,[random.choice(chars) for i in range(length)])
    return id

def generate_random_date():
    while True:
        try:
            year = random.randint(2020,2021)
            month = random.randint(1,12)
            day = random.randint(1,30)
            d = date(year,month,day)
            return d
        except:
            ValueError

ids = []
while len(ids) < N_PATIENTS:
    id = generate_random_id()
    if id not in ids:
        ids.append(id)

dates_in = [generate_random_date() for x in range(N_PATIENTS)]
dates_out = [x + timedelta(days=random.randint(1,100)) for x in dates_in]

lines_in = [f"{pat},{din}" for (pat,din) in zip(ids,dates_in)]
lines_out = [f"{pat},{dout}" for (pat,dout) in zip(ids,dates_out)]

random.shuffle(lines_in)
random.shuffle(lines_out)

with open("ex1/data/ingressi.csv","w",encoding="utf-8") as f:
    for line in lines_in:
        print(line,file=f)

with open("ex1/data/uscite.csv","w",encoding="utf-8") as f:
    for line in lines_out:
        print(line,file=f)


