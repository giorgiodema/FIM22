Il file ingressi.csv ha come prima colonna il codice del paziente (un codice alfanumerico univoco a 7 cifre) e la data in cui il paziente è stato ricoverato (nel formato YYYY-MM-DD). 
Il file uscite.csv ha come prima colonna il codice del paziente e come seconda colonna la data di dimissione.
In entrambi i file è presente solo una riga per paziente (non ci sono duplicati) e ogni paziente è presente in entrambi i file.
Scrivere un programma che crei un file ricoveri.csv avente come prima colonna il codice del paziente, come seconda colonna la data di ingresso e come terza colonna la data di dimissione.
Le righe del file ricoveri.csv devono essere ordinate in ordine crescente per codice paziente.
Ad esempio, supponiamo che il file ingressi.csv contenga le seguenti righe:

HI6EYGS,2020-02-28
K21KKPD,2020-12-09
M0EZMFJ,2020-07-26
RVCMA0D,2020-12-12
Y5IBP1H,2020-06-04
AHMMVAF,2021-08-07
3XRILAV,2020-10-24
I8B6F58,2021-04-19
NO0FRNZ,2021-04-06
63FV9CY,2020-01-09

E il file uscite.csv le seguenti righe:

63FV9CY,2020-02-21
Y5IBP1H,2020-07-03
K21KKPD,2020-12-10
M0EZMFJ,2020-09-06
3XRILAV,2021-01-10
I8B6F58,2021-05-24
NO0FRNZ,2021-04-21
HI6EYGS,2020-04-24
RVCMA0D,2021-01-09
AHMMVAF,2021-10-03

Il file di output sarà il seguente:

3XRILAV,2020-10-24,2021-01-10
63FV9CY,2020-01-09,2020-02-21
AHMMVAF,2021-08-07,2021-10-03
HI6EYGS,2020-02-28,2020-04-24
I8B6F58,2021-04-19,2021-05-24
K21KKPD,2020-12-09,2020-12-10
M0EZMFJ,2020-07-26,2020-09-06
NO0FRNZ,2021-04-06,2021-04-21
RVCMA0D,2020-12-12,2021-01-09
Y5IBP1H,2020-06-04,2020-07-03

BONUS:
Trovare il paziente che è stato ricoverato più a lungo e stampare a schermo il codice del paziente e la durata del ricovero in giorni.
SUGGERIMENTO:
usare il package datetime, o in alternativa supporre che ogni mese sia composto da 30 giorni, nel primo caso la soluzione sarà:

3XRILAV,78

mentre invece nel secondo caso sarà:

3XRILAV,81