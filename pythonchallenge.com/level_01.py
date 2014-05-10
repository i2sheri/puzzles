# My original solution
"""
# import re
small = re.compile('[a-z]')
for s in question:
    if re.match(small, s):
        if s == 'z':
            print 'b',
        elif s == 'y':
            print 'a',
        else:
            print chr(ord(s)+2),
    else:
        print s,
"""

import string

QUESTION = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc "
            "dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr "
            "gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw "
            "ml rfc spj.")


# Recommended Approach
CIPHER = string.lowercase[:]
print QUESTION.translate(string.maketrans(CIPHER, CIPHER[2:] + 'ab'))
