import os

# This class implements an Iterator (by implementing the method __next__) and 
# it is also an iterable (because it implements the method __iter__ that return the 
# instance self).
class StudentiIter:

    def __init__(self) -> None:
        # initialization: read the content of the two files in the lists l1 and l2
        f1 = open(os.path.join("exam220913","corso1.txt"),"r",encoding="utf-8")
        f2 = open(os.path.join("exam220913","corso2.txt"),"r",encoding="utf-8")
        self.l1 = f1.readlines()
        self.l2 = f2.readlines()
        # close the files after finished
        f1.close()
        f2.close()

    # iter return the object itself, because the class StudentIter implements
    # an iterator
    def __iter__(self):
        return self

    def __next__(self):
        # If both lists are empty then there are no
        # more element to return
        if len(self.l1)==0 and len(self.l2)==0:
            raise StopIteration
        # If only the first list contains elements then 
        # the iterator should return those elements
        if len(self.l1)>0 and len(self.l2)==0:
            e = (self.l1[0].strip(),1)
            self.l1 = self.l1[1:]
            return e
        # If only the second list contains elements then
        # the iterator should return those elements
        if len(self.l2)>0 and len(self.l1)==0:
            e = (self.l2[0].strip(),2)
            self.l2 = self.l2[1:]
            return e
        # If both lists contains elements then the iterator
        # should return the first element in alphabetic order
        # and remove the returned element from the list
        e1 = (self.l1[0].strip(),1)
        e2 = (self.l2[0].strip(),2)
        if e1[0] <= e2[0]:
            self.l1 = self.l1[1:]
            return e1
        else:
            self.l2 = self.l2[1:]
            return e2
        

# Instantiate the iterator and write the result to file
f = open(os.path.join("exam220913","studenti.txt"),"w",encoding="utf-8")
for s in StudentiIter():
    print(f"{s[0]}, {s[1]}",file=f)
f.close()