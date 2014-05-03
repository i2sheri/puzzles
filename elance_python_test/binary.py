"""
Write a program which will accept 4 digit binary numbers each separated by a comma
  as its input and then check whether they are divisible by 3 or not.
The numbers that are divisible by 3 are to be printed, separated by a comma.

Example

Suppose the following input is given to the program:

0011,0100,0101,1001

Then, the output of the program should be:

0011, 1001

Note: You should assume that input to the program is from console input (raw_input) """

bins = raw_input().split(',')
copy = [i for i in bins if int(i, 2)%3 == 0]
print ','.join(copy)
