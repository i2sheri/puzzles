       
"""
Write a program which takes 4 inputs, where each input consists of 2 numbers in the format x,y.
You are required to print a two dimensional array having x rows and y columns for each input.
The elements of the arrays should be whole numbers starting from 1 and incrementing by 1. 

Example

Suppose the following 4 inputs are given to the program:

2,2
2,3
3,3
3,4

Then, the output of the program should be:

[[1, 2], [3, 4]]
[[1, 2, 3], [4, 5, 6]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

Note: You should assume that input to the program is from console input (raw_input)
"""
l = []
for x in xrange(4):
    l.append(raw_input())

for t in l:
    ct = 0
    x = int(t[0])
    y = int(t[2])
    row = []
    for i in xrange(x):
        col = []
        for j in xrange(y):
            ct = ct + 1
            col.append(ct)
        row.append(col)
    print row 
