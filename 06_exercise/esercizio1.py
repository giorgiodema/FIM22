
__consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
__vowels = 'AEIOU'

tabella_mesi = {
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

    __codici_comuni = None
    
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
        codice += tabella_mesi[int(mm)]

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
        
    


if __name__=="__main__":
    # Ottavio,Grasso,18/5/2009,Inverso Pinasca,M
    p = Paziente("Barbara","Ih","18/5/2009","Inverso Pinasca","M")
    
    #GRSTTV09E18E311T
    print(p.cf())