import re
l =[]
n = input()
for i in range(n):
    a = raw_input()
    s = re.sub('-', " ", a)
    s = s.split(" ")
    l.append(s)
for e in l:
    print "CountryCode="+e[0]+",LocalAreaCode="+e[1]+",Number="+e[2]
