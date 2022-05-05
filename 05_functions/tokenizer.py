import string
from typing import List

def remove_punctuation(s:str)->str:
    s_new = ""
    for c in s:
        if c in string.punctuation:
            s_new = s + " "
        else:
            s = s + c
    return s


def tokenize(s:str)->List[str]:
    if s == "":
        return []
    start = 0
    end = start
    while s[end] != " ":
        end +=1
        if end >= len(s):
            return [s]
    cont = end
    while s[cont] == " ":
        cont +=1
    return [s[start:end]] + tokenize(s[cont:])


l = tokenize("Hello, welcome to the FIM course")