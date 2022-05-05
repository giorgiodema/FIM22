def abs(a):
    return a if a >= 0 else -a


if __name__ == "__main__":
    
    a = int(input("Inserisci un intero a:"))
    b = int(input("Inserisci un intero b:"))

    s = abs(a) + abs(b)
    print("|a| + |b| = {}".format(s))