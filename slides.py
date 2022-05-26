l = [1,2,3,4]

class EvenIterator:

    def __init__(self,l) -> None:
        self.data = l
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.data)-1:
            raise StopIteration
        elem = self.data[self.current_index]
        while elem % 2 != 0 and self.current_index <= len(self.data)-1:
            self.current_index += 1
            elem = self.data[self.current_index]
        if elem % 2 == 0:
            self.current_index += 1
            return elem
        else:
            raise StopIteration


class ReverseIterator:
    
    def __init__(self,l) -> None:
        self.data = l
        self.star_idx = len(l) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.star_idx >= 0:
            elem = self.data[self.star_idx]
            self.star_idx -= 1
            return elem
        else:
            raise StopIteration

    def rewind(self):
        self.star_idx = len(self.data) - 1

def reverse_iterator(l):
    start_idx = len(l)-1
    while start_idx >=0:
        yield l[start_idx]
        start_idx -=1

it = ReverseIterator(l)
for e in it:
    print(e)

it.rewind()

for e in it:
    print(e)


