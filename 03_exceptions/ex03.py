from typing import List

# le eccezioni possono essere utilizzate per prevenire
# l'uso non corretto di una funzione, che potrebbe
# causare un comportamenteo non definito. La funzione 
# foo ha come argomento un parametro di tipo lista. 
# Se la funzione viene invocata con un parametro con 
# un tipo diverso la funzione lancia un'eccezione di tipo
# ValueError e il programma termina l'esecuzione
def foo(l:List):
    if type(l) != list:
        raise ValueError(\
            "function foo takes a list argument, not {}"\
            .format(type(l)))
    for e in l:
        print(e)

foo([1,2,3])
foo(2)