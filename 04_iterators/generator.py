from typing import List


def list_with_index(l:List):
    for i in range(len(l)):
        yield (i,l[i])

l = ["a","b","c","d"]
for e in list_with_index(l):
    print(e)