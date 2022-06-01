from typing import List

# l'istruzione yield crea implicitamente un 
# iteratore con il metodo __next__. E' come 
# se l'esecuzione della funzione venisse messa 
# in pausa e ripresa ad ogni chiamata di __next__
def list_with_index(l:List):
    for i in range(len(l)):
        yield (i,l[i])

l = ["a","b","c","d"]
for e in list_with_index(l):
    print(e)