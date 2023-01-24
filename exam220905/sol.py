import os
import string

# function that returns the sorting
# key for alphabetic ordering
def get_alphabetic_sort_key(x):
    return x[0]

# function that returns the sorting
# key for ordering by number of 
# occurrences
def get_occurrences_sort_key(x):
    return x[1]

# read the text file
f = open(os.path.join("exam220905","text.txt"),"r",encoding="utf-8")
text = f.read()
f.close()

# tokenization
words = text.split(" ")

# create the dictionary occ_counter to 
# count the occurrences of each word
occ_counter = {}
for w in words:
    if w not in occ_counter:
        occ_counter[w] = 1
    else:
        occ_counter[w] += 1
# create a list of tuples in which the first
# element is the word and the second element
# is the number of occurrences
words_occ = []
for k in occ_counter:
    words_occ.append((k,occ_counter[k]))

# words and occurrences sorted in
# alphabetic order
alphabetic_ordered = sorted(words_occ,key=get_alphabetic_sort_key)
# words and occurrences sorted 
# by number of occurrences
occurrence_ordered = sorted(words_occ,key=get_occurrences_sort_key,reverse=True)

# write solutions to files
f = open(os.path.join("exam220905","words.txt"),"w",encoding="utf-8")
for e in alphabetic_ordered:
    print(f"{e[0]},{e[1]}",file=f)
f.close()

f = open(os.path.join("exam220905","words_bonus.txt"),"w",encoding="utf-8")
for e in occurrence_ordered:
    print(f"{e[0]},{e[1]}",file=f)
f.close()

