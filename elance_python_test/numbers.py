"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 1000 and 1200 (both included).
The numbers obtained should be printed in a comma separated sequence on a single line.
"""

print ','.join([str(n) for n in range(1000, 1201) if n%7 == 0 and n%5 != 0])
