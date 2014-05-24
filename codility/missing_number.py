"""
Array of distinct integers of size N is given.
It contains integers in the range [1, (N + 1)].
which means exactly one element is missing, find it.

1 < N < 1,00,000

Ex: [1, 2, 4, 6, 7, 8, 3]
Output: 5

Ex: [1, 3]
Output: 2

Complexity:
expected worst-case time complexity is O(N)
expected worst-case space complexity is O(1)
"""

def missing_number(ip):
  n = len(ip)
  sum = (n+2)*(n+1)/2
  for x in ip:
    sum -= x
  print sum

missing_number(map(int,raw_input().split()))
