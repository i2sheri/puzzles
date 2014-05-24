# https://codility.com/programmers/lessons/TapeEquilibrium

def solution(a):
    sum = 0
    for x in a:
        sum += x
    res = None
    temp = 0
    for x in xrange(len(a)-1):
        temp += a[x]
        sum -= a[x]
        d = abs(sum - temp)
        if x == 0:
            res = d
        elif res > d:
            res = d
    return res

solution(map(int,raw_input().split()))
