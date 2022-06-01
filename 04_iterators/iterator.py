from typing import List

class ListWithIndex:
    """
    Iteratore che restituisce gli elementi di una lista insieme
    al rispettivo indice
    """

    def __init__(self,l:List) -> None:
        self.index = 0
        self.data = l

    # ListWithIndex è sia iterabile che iteratore, quindi __iter__
    # retstituisce l'oggetto stesso
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            elem = (self.index,self.data[self.index])
            self.index += 1
            return elem
        else:
            raise StopIteration()

l = ["a","b","c","d"]
# Il ciclo for converte l'espressione dopo "in"
# in un iteratore (chiamando il metodo __iter__)
# e ripete il blocco di codice all'interno per 
# ogni elemento dell'iteratore (assegnato alla 
# variabile e)
for e in ListWithIndex(l):
    print(e)