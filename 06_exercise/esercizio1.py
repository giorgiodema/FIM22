
__consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
__vowels = 'AEIOU'



def consonanti(s):
    # estraggo consonanti nell'ordine
    consonanti = ""
    for c in s:
        if c in __consonants:
            consonanti += c
    return consonanti

def vocali(s):
    # estraggo consonanti nell'ordine
    vocali = ""
    for c in s:
        if c in __vowels:
            vocali += c
    return vocali



class Paziente:
    
    def __init__(self,nome:str,cognome:str,dn:str,cn:str,sesso:str) -> None:
        self.nome = nome
        self.cognome = cognome
        self.dn = dn
        self.cn = cn
        self.sesso = sesso
        if Paziente.__codici_comuni == None:
            Paziente.__codici_comuni = Paziente.inizializzaCodiciComuni()

    def cf(self):
        codice =  Paziente.codiceCognome(self.cognome) + Paziente.codiceNome(self.nome) + Paziente.codiceDataSesso(self.dn,self.sesso) + Paziente.codiceComune(self.cn)
        # Il carattere di controllo viene determinato nel modo seguente:
        # si assegnano ai caratteri in posizione dispari i corrispondenti valori contenuti nel
        # dizionario Paziente.__tabella_controllo_dispari e si assegnano ai caratteri in posizione pari i 
        # corrispondenti valori contenuti nel dizionario Paziente.__tabella_controllo_pari
        controllo_dispari = [Paziente.__tabella_controllo_dispari[x] for x in codice[0::2]]
        controllo_pari = [Paziente.__tabella_controllo_pari[x] for x in codice[1::2]]
        # si sommano tutti i valori così ottenuti, si divide il valore calcolato al punto precedente 
        # per 26 e si considera il resto di tale divisione in base al risultato così ottenuto si 
        # cerca il carattere di controllo nel dizionario Paziente.__tabella_controllo_somma
        somma = sum(controllo_dispari) + sum(controllo_pari)
        codice_controllo = Paziente.__tabella_controllo_somma[somma % 26]
        codice += codice_controllo
        return codice

    def inizializzaCodiciComuni():
        codici_comuni = {}
        f = open("data/Elenco-comuni-italiani.csv","r",encoding="utf-8")
        f.readline()
        for line in f:
            line = line.split(",")
            comune = line[5].strip().upper()
            codice = line[19].strip()
            codici_comuni[comune] = codice
        f.close()
        return codici_comuni

    def codiceCognome(cognome):
        # Ai fini del calcolo del codice fiscale tutti i cognomi sono da 
        # considerarsi come privi di spazi o di apici, quindi ad esempio 
        # DE LUCA è da considerarsi come DELUCA, D'ACUNTO come DACUNTO 
        # e così via.
        cognome = cognome.upper().replace("'","").replace(" ","")

        # estraggo vocali e consonanti nell'ordine
        cons= consonanti(cognome)
        vow = vocali(cognome)

        # Il cognome presenta tre o più consonanti: in tal caso i primi 
        # tre caratteri del codice fiscale saranno le prime tre consonanti 
        # del cognome, prese nell'ordine.
        if len(cons)>=3:
            return cons[0:3]

        # Il cognome presenta solo due consonanti ed è composto da almeno 
        # tre lettere: in tal caso si considereranno, nell'ordine, le due 
        # consonanti e la prima vocale del cognome. Ad esempio GORI diviene 
        # GRO, LIETO diviene LTI, etc.
        elif len(cons)==2 and len(vow)>=1:
            return cons + vow[0]

        # Il cognome presenta una sola consonante ed è composto da almeno tre 
        # lettere: in tal caso si considereranno, nell'ordine, l'unica consonante 
        # e le prime due vocali del cognome. Ad esempio, ALEA diviene LAE, MAIO 
        # diviene MAI, etc.
        elif len(cons)==1 and len(vow)>=2:
            return cons + vow[0:2]

        # l cognome non contiene consonanti: in tal caso si considerano, 
        # nell'ordine, le prime tre vocali del cognome e, qualora queste fossero 
        # meno di tre, si completa con tante X quante ne mancano (ovviamente, a 
        # meno di cognomi di una sola lettera - ipotesi abbastanza scartabile - 
        # di X ne occorrerà una sola). Ad esempio AIUOA diviene AIU, AO diviene 
        # AOX, etc.
        elif len(cons)==0:
            codice = vow
            if len(codice)<3:
                for i in range(0,3-len(codice)):
                    codice += "X"
            return codice

        # l cognome è composto da meno di tre lettere: in tal caso si considereranno,
        #  nell'ordine, le eventuali consonanti, le eventuali vocali e tante X 
        # quante ne occorrono per avere tre caratteri (ovviamente, a meno di 
        # cognomi d'una sola lettera - ipotesi abbastanza scartabile - di X ne 
        # occorrerà una sola). Ad esempio, RE diviene REX, IH diviene HIX, etc.
        else:
            codice = cons + vow
            if len(codice)<3:
                for i in range(0,3-len(codice)):
                    codice += "X"
            return codice

    def codiceNome(nome):
        # Il nome presenta almeno quattro consonanti: in tal caso si considerano, 
        # nell'ordine, la prima, la terza e la quarta consonante. 
        # Ad esempio BARBARA diviene BBR.
        nome = nome.upper().replace("'","").replace(" ","")
        cons = consonanti(nome)
        vows = vocali(nome)
        if len(cons)>=4:
            return cons[0]+cons[2:4]
        # Altrimenti si procede come con il cognome
        else:
            return Paziente.codiceCognome(nome)

    def codiceDataSesso(data,sesso):
        # caratteri indicativi della data di nascita e del sesso sono in tutto 5. 
        # I primi due sono gli ultimi due numeri dell'anno di nascita, ad esempio 
        # 1977 diviene 77, 1956 diviene 56, 1902 diviene 02, etc.
        gg,mm,yyyy = data.split("/")
        codice = yyyy[2:]

        # Dopo tali due numeri segue una lettera che tiene conto del mese di nascita 
        # secondo la tabella dei mesi
        codice += Paziente.__tabella_mesi[int(mm)]

        # Il soggetto è di sesso maschile: Il tal caso si prenderà in considerazione semplicemente il 
        # giorno di nascita. I numeri minori di dieci vanno considerati con uno zero iniziale. 
        # Dunque tali numeri saranno compresi tra 01 e 31. 
        # Il soggetto è di sesso femminile: In tal caso si prende in considerazione il giorno di 
        # nascita e lo si incrementa di 40 unità. Tali numeri saranno dunque compresi tra 41 e 71
        gg = int(gg)
        if sesso == "F":
            gg += 40
        gg = str(gg)
        if len(gg)==1:
            gg = "0"+gg
        codice += gg
        return codice

    def codiceComune(comune):
        comune = comune.upper()
        return Paziente.__codici_comuni[comune]

    __codici_comuni = None

    __tabella_mesi = {
        1:"A",
        2:"B",
        3:"C",
        4:"D",
        5:"E",
        6:"H",
        7:"L",
        8:"M",
        9:"P",
        10:"R",
        11:"S",
        12:"T"
    }

    __tabella_controllo_dispari = {
        "A":1,
        "B":0,
        "C":5,
        "D":7,
        "E":9,
        "F":13,
        "G":15,
        "H":17,
        "I":19,
        "J":21,
        "K":2,
        "L":4,
        "M":18,
        "N":20,
        "O":11,
        "P":3,
        "Q":6,
        "R":8,
        "S":12,
        "T":14,
        "U":16,
        "V":10,
        "W":22,
        "X":25,
        "Y":24,
        "Z":23,
        "0":1,
        "1":0,
        "2":5,
        "3":7,
        "4":9,
        "5":13,
        "6":15,
        "7":17,
        "8":19,
        "9":21
    }

    __tabella_controllo_pari = {
        "A":0,
        "B":1,
        "C":2,
        "D":3,
        "E":4,
        "F":5,
        "G":6,
        "H":7,
        "I":8,
        "J":9,
        "K":10,
        "L":11,
        "M":12,
        "N":13,
        "O":14,
        "P":15,
        "Q":16,
        "R":17,
        "S":18,
        "T":19,
        "U":20,
        "V":21,
        "W":22,
        "X":23,
        "Y":24,
        "Z":25,
        "0":0,
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9
    }

    __tabella_controllo_somma = {
        0:"A",
        1:"B",
        2:"C",
        3:"D",
        4:"E",
        5:"F",
        6:"G",
        7:"H",
        8:"I",
        9:"J",
        10:"K",
        11:"L",
        12:"M",
        13:"N",
        14:"O",
        15:"P",
        16:"Q",
        17:"R",
        18:"S",
        19:"T",
        20:"U",
        21:"V",
        22:"W",
        23:"X",
        24:"Y",
        25:"Z"
    }



        
    


if __name__=="__main__":
    p = Paziente("Giorgio","De Magistris","09/7/1995","Roma","M")
    print(p.cf())