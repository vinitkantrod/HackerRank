import re
l = []
for i in range(input()):
    a = raw_input()
    r = re.match('^[a-z]{0,4}[\d]{2,8}[A-Z]{3,}$', a, flags=0)
    if r:
        l.append("VALID")
    else:
        l.append("INVALID")
for e in l:
    print e
