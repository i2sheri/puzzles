"""
Write a program to calculate the bill amount, in cents, for the units of power consumed.
Following are the rates applicable:

1. First 0-100 units: 60 cents per unit
2. Next 200 units: 70 cents per unit
3. Beyond 300 units: 80 cents per unit

The program should accept three different usage unit readings.

Example

If the following inputs are supplied:

305
180
120

Then, the output should be:

20400
11600
7400

Note: You should assume that input to the program is from console input (raw_input)
"""

res = 0
l = []
for r in xrange(3):
    l.append(int(raw_input()))
for r in l:
    if r > 300:
        res = (r-300)*80 + (100*60) + (200*70)
    elif r > 100:
        res = (r-100)*70 + (100*60)
    else:
        res = r*60
    print res
