# https://codility.com/demo/results/demo2E8KNM-6J6/
def solution(X, A):
    d = {}
    for x in range(X):
        d[x+1] = 1
    
    for min, pos in enumerate(A):
        if d.get(pos):
            d.pop(pos)
            if len(d) == 0:
                return min
    return -1

solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
