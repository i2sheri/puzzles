# https://codility.com/programmers/lessons/FrogJmp

def solution(X, Y, D):
    r = (Y-X)/D 
    if (Y-X)%D > 0:
        r += 1
    return r

solution(10, 85, 30)
