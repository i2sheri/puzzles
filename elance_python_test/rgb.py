"""
Write a program which will convert the given RGB input values into
  the corresponding hexadecimal values preceded with a # sign.

A single input sequence will be provided, consisting of RGB values separated by "-".
Each RGB combination will be separated by ",".
The outputs should be comma separated and in uppercase.
Also, it should be checked if a color value is greater than 255.
In such a case, the output for the corresponding combination should be given as INVALID.

Note: Number 10, which has a hexadecimal value of A, must be represented as "0A" and not as "A".
The same rule applies to other single digit hexadecimal numbers.

Example

Suppose the following input sequence is supplied to the program:

12-13-14,45-156-23,234-234-256

The output of the program should be:

#0C0D0E,#2D9C17,INVALID

Note: You should assume that input to the program is from console input (raw_input) 
"""

colors = raw_input().split(',')
res = []
for c in colors:
    s = '#'
    rgb = c.split('-')
    for x in rgb:
        if int(x) > 255:
            s = 'INVALID'
            break
        else:
            s += '%X' %int(x)
    res.append(s)
print ','.join(res)
