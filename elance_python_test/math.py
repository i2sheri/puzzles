"""
Write a Program which calculates and prints the Optimal Order Quantity for the production of LCD sets.
Following is the formula to calculate Optimal Order Quantity:

Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C and H:

Fixed cost per order, denoted by C, is $50.
Annual holding cost per unit, denoted by H, is $30.

Only the Annual Demand Quantity (D) of the product varies. The values of D are supplied as input to your program in a comma separated sequence.

Example

Let us assume the following comma separated input sequence is given to the program:

100,150,180

The output of the program should be:

18,22,24

Note: If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)

Note: You should assume that input to the program is from console input (raw_input)
"""

ip = map(int, raw_input().split(','))
l = ['%d' %round(((100.0*d/30) ** .5)) for d in ip]
print ','.join(l)

#ip = raw_input().split(',')
#l = ['%d' %round(((100.0*int(d)/30) ** .5)) for d in ip]
