

from typing import List

def insertion_sort(l:List)->None:
    for i in range(len(l)-1):
        current = l[i]
        for j in range(i,len(l)):
            if l[j] < current:
                current = l[j]
                l[j] = l[i]
                l[i] = current


l = [1,9,3,6,2,4,5,8,7]
insertion_sort(l)
print(l)