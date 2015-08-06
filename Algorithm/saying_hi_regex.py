import re
l = []
for i in range(input()):
    a = raw_input()
    if re.match('^hi\s[^d]',a, flags = re.I):
        l.append(a)
for e in l:
    print e
