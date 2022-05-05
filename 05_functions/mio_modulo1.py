def sum(a:float,b:float)->float:
    return a+b

def pow(base:float,exp:int)->float:
    res = 1.
    for i in range(exp):
        res *= base
    return res

print("2^3 + 3^2 = {}"
    .format(sum(pow(2,3),pow(3,2))))