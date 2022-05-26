from typing import List


class ListWithIndex:

    def __init__(self,l:List) -> None:
        self.index = 0
        self.data = l

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
for e in ListWithIndex(l):
    print(e)