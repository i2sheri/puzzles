# https://codility.com/demo/results/demoFKQD9G-9UY/

def solution(a):
    # write your code in Python 2.6
    sum = 0
    d = {}
    for x in A:
        sum += x
        d[x] = 1
    n = len(A)
    total = n * (n + 1)/2

    if sum == total and len(d) == n:
        return 1
    else:
        return 0

solution([4,1,3,2])
solution([4,1,2])
