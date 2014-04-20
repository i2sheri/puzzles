n = int(raw_input())
ints = raw_input()
ser = ints.split()
ap = []
for a in ser:
    ap.append(int(a))
diff = []
for i in xrange(0,n-1):
    diff.append(ap[i+1]-ap[i])
index = 0
d = 0
for i in xrange(0, n-2):
    if diff[i] == diff[i+1]:
        d = diff[i]
        continue
    else:
        index = i+2
missing = ap[0] + (index-1)*d
print missing
