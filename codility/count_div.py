# https://codility.com/programmers/lessons/3
# https://codility.com/demo/results/demoPXYYER-4PW/

def solution(a, b, k):
  r = b/k - a/k
  if r < 0: return 0
  if a%k == 0: r+=1
  return r
