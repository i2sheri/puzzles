s = raw_input()
l = len(s)
res = set()
for i in xrange(1, l+1):
    p = 0
    while p+i <= l:
        res.add(s[p:p+i])
        p += 1
print len(res)
