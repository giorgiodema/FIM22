

from typing import List


def foo(l:List):
    if type(l) != list:
        raise ValueError(\
            "function foo takes a list argument, not {}"\
            .format(type(l)))
    for e in l:
        print(e)

foo([1,2,3])
foo(2)