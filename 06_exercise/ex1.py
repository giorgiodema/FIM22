from tkinter import N
from typing import Dict
import os

#
# Variabili Globali
#

__consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
__vowels = 'AEIOU'


#
# Funzioni
#

#TODO: implementa la funzione
def consonanti(s:str)->str:
    """
    ritorna la stringa contenente solo consonanti 
    nello stesso ordine
    """
    raise NotImplementedError

#TODO: implementa la funzione
def vocali(s:str)->str:
    """
    ritorna la stringa contenente solo vocali 
    nello stesso ordine
    """
    raise NotImplementedError

#
# Classe Paziente
#

class Paziente:
    
    #
    # Costruttore
    #
    def __init__(self,nome:str,cognome:str,dn:str,cn:str,sesso:str) -> None:
        self.nome = nome
        self.cognome = cognome
        self.dn = dn
        self.cn = cn
        self.sesso = sesso
        # inizializza il dizionario Paziente.__codice_comuni che ha come 
        # chiave i nomi dei comuni (con lettere maiuscole) e come valori
        # i codici di 4 cifre dei comuni
        if Paziente.__codici_comuni == None:
            Paziente.__codici_comuni = Paziente.__inizializzaCodiciComuni()

    #
    # Metodi
    #
    #TODO: implementa il metodo in modo che restituisca una stringa con tutti gli attributi del 
    # oggetto e il codice fiscale
    def __str__(self):
        raise NotImplementedError

    #TODO: implementa il metodo che calcola il codice fiscale del paziente utilizzando
    # le funzioni ausiliarie definite sotto (ricorda che per scrivere codice più leggibile
    # è meglio scomporre funzioni lunghe in più funzioni). Puoi trovare qui le istruzioni 
    # su come calcolare il codice fiscale http://gratis.pietrelcinanet.com/codice_fiscale/codice.htm
    def cf(self)->str:
        """
        Ritorna una stringa che rappresenta il codice fiscale del paziente
        """
        raise NotImplementedError

    #
    # Funzioni Ausiliarie
    #
    def __inizializzaCodiciComuni():
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

    def __codiceCognome(cognome):
        #TODO: implementa la funzione che data in input la stringa del cognome
        # calcola le prime 3 cifre del codice fiscale

        # Ai fini del calcolo del codice fiscale tutti i cognomi sono da 
        # considerarsi come privi di spazi o di apici, quindi ad esempio 
        # DE LUCA è da considerarsi come DELUCA, D'ACUNTO come DACUNTO 
        # e così via.

        # estraggo vocali e consonanti nell'ordine

        # Il cognome presenta tre o più consonanti: in tal caso i primi 
        # tre caratteri del codice fiscale saranno le prime tre consonanti 
        # del cognome, prese nell'ordine.

        # Il cognome presenta solo due consonanti ed è composto da almeno 
        # tre lettere: in tal caso si considereranno, nell'ordine, le due 
        # consonanti e la prima vocale del cognome. Ad esempio GORI diviene 
        # GRO, LIETO diviene LTI, etc.

        # Il cognome presenta una sola consonante ed è composto da almeno tre 
        # lettere: in tal caso si considereranno, nell'ordine, l'unica consonante 
        # e le prime due vocali del cognome. Ad esempio, ALEA diviene LAE, MAIO 
        # diviene MAI, etc.

        # Il cognome non contiene consonanti: in tal caso si considerano, 
        # nell'ordine, le prime tre vocali del cognome e, qualora queste fossero 
        # meno di tre, si completa con tante X quante ne mancano (ovviamente, a 
        # meno di cognomi di una sola lettera - ipotesi abbastanza scartabile - 
        # di X ne occorrerà una sola). Ad esempio AIUOA diviene AIU, AO diviene 
        # AOX, etc.

        # l cognome è composto da meno di tre lettere: in tal caso si considereranno,
        #  nell'ordine, le eventuali consonanti, le eventuali vocali e tante X 
        # quante ne occorrono per avere tre caratteri (ovviamente, a meno di 
        # cognomi d'una sola lettera - ipotesi abbastanza scartabile - di X ne 
        # occorrerà una sola). Ad esempio, RE diviene REX, IH diviene HIX, etc.
        raise NotImplementedError

    def __codiceNome(nome):
        #TODO: implementa la funzione che data in input la stringa del nome calcola 
        # le tre cifre del codice fiscale relative al nome

        # Il nome presenta almeno quattro consonanti: in tal caso si considerano, 
        # nell'ordine, la prima, la terza e la quarta consonante. 
        # Ad esempio BARBARA diviene BBR.

        # Altrimenti si procede come con il cognome
        raise NotImplementedError

    def __codiceDataSesso(data,sesso):
        #TODO: implementa la funzione che data in input le stringe relative alla data
        # di nascita ( nel formato gg/mm/yyyy ) e al sesso (M o F) calcola le 5 cifre relative alla data 
        # di nascita e al sesso

        # caratteri indicativi della data di nascita e del sesso sono in tutto 5. 
        # I primi due sono gli ultimi due numeri dell'anno di nascita, ad esempio 
        # 1977 diviene 77, 1956 diviene 56, 1902 diviene 02, etc.

        # Dopo tali due numeri segue una lettera che tiene conto del mese di nascita 
        # secondo la tabella dei mesi

        # Il soggetto è di sesso maschile: Il tal caso si prenderà in considerazione semplicemente il 
        # giorno di nascita. I numeri minori di dieci vanno considerati con uno zero iniziale. 
        # Dunque tali numeri saranno compresi tra 01 e 31. 
        # Il soggetto è di sesso femminile: In tal caso si prende in considerazione il giorno di 
        # nascita e lo si incrementa di 40 unità. Tali numeri saranno dunque compresi tra 41 e 71
        raise NotImplementedError

    def __codiceComune(comune):
        #TODO: implementa la funzione che data in input la stringa con il nome 
        # del comune ritorna il codice del comune (puoi usare il dizionario 
        # Paziente.__codici_comuni)

    #
    # attributi della classe Paziente
    #

    # dizionario che contiene i codici di tutti i comuni Italiani, viene 
    # inizializzato la prima volta che viene instanziato un oggetto Paziente
    # la chiave è il nome del comune (con lettere maiuscole) e la chiave è 
    # il codice di 4 cifre del comune
    __codici_comuni:Dict[str,str] = None

    __tabella_mesi:Dict[int,str] = {
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

    __tabella_controllo_dispari:Dict[str,int] = {
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

    __tabella_controllo_pari:Dict[str,int] = {
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

    __tabella_controllo_somma:Dict[int,str] = {
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
    # Il programma legge i dati dei pazienti dal file "pazienti.csv" e crea un 
    # oggetto della classe Paziente per ogni paziente nel file. Gli oggetti pazienti vengono salvati in una lista e 
    # successivamente l'intera lista viene ordinata utilizzando come chiave nome e cognome (in questo ordine) e 
    # gli elementi della lista vengono stampati a schermo, stampando per ogni paziente i dati anagrafici e il codice fiscale.
    pass