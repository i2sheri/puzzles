import re
pwds = raw_input().split(',')
res = []
s = re.compile('[a-z]')
c = re.compile('[A-Z]')
d = re.compile('[0-9]')
for p in pwds:
    if len(p) >=4 and len(p) <= 6 and re.search(p, s) and re.search(p, c) and (re.search(p, '*') or re.search(p, '#') or re.search(p, '+') or re.search(p, '@')):
        res.append(p)
print ','.join(res)


"""
A bank has implemented criteria for determining whether
  the transaction passwords typed by customers of the bank are valid or not.

Following are the criteria for checking the transaction password:

1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [*#+@]
4. Minimum length of transaction password: 4
5. Maximum length of transaction password: 6
6. No space is allowed

Write a program which will accept a sequence of comma separated transaction passwords
  and will check them according to the bank's criteria.
Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

Abc@1,a B1#,2w3E*,2We#3345

Then, the output of the program should be:

Abc@1,2w3E*

Note: You should assume that input to the program is from console input (raw_input)
"""
