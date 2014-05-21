import itertools
a = [1, 11, 21, 1211, 111221]
i = 0
s = '1'
while i < 30:
    res = ['%s%s' %(len(list(chk)),num) for num, chk in itertools.groupby(s)]
    s = ''.join(res)
    i += 1
print len(s)
