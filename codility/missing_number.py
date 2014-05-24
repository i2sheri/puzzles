#https://codility.com/programmers/lessons/PermMissingElem

def missing_number(ip):
  n = len(ip)
  sum = (n+2)*(n+1)/2
  for x in ip:
    sum -= x
  print sum

missing_number(map(int,raw_input().split()))
