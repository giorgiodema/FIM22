

def sum(a,b,abs=False):
    print(a)
    print(b)
    if not abs:
        return a + b
    else:
        s = a + b
        if s >= 0:
            return s
        else:
            return -s

c = sum(2,b=1)
print(c)