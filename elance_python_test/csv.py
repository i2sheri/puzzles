"""
Write a program which will receive a comma separated sequence of numbers.
Suppose a particular input number is represented by "n". 
The program should find the greatest "n" digit number which is divisible by "n" itself. 
The output should be comma separated.

The greatest n digit number is denoted by "n" number of 9's occurring,
  like, the greatest 6 digit number is 999999 or the greatest 4 digit number is 9999.
Note that although the greatest 4 digit number is 9999, it is not divisible by 4, but 9996 is divisible by 4.

Examples

If the following input is supplied to program:

2,5,8

Then, the output should be:

98,99995,99999992

Note: You should assume that input to the program is from console input (raw_input) 
"""
numbers = raw_input().split(',')
res = []
for n in numbers:
    x = int(n)
    great = int(('9'*x))
    great -= great%x
    res.append(str(great))
print ','.join(res)
