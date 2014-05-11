"""banner.p will be available in level5"""

import pickle

obj = pickle.load(open("banner.p", "rb"))
f = open("5_op.txt", "w")
for l in obj:
    str = ""
    for tup in l:
        f.write(tup[0]*tup[1])
    f.write('\n')
