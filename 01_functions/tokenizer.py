import string
from typing import List

def remove_punctuation(s:str)->str:
    """
    Replace the punctuation with white spaces
    """
    s_new = ""
    for c in s:
        if c in string.punctuation:
            s_new = s + " "
        else:
            s_new = s + c
    return s_new


def tokenize(s:str)->List[str]:
    """
    Recursive tokenizer. Given a string it returns a list
    of token.
    """
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
print(l)