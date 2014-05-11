import requests
import re

code = 12345
code = 8022 #86
i = 1
dig = re.compile('[0-9]+$')
while i < 400:
    res = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % code)
    print i, res.content
    try:
        #code = int(res.content[-5:].strip())
        code = re.search(dig, res.content).group(0)
    except:
        print "Exception"
        break
    i += 1
