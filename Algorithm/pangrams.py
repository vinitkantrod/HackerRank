import string
d = string.ascii_lowercase
dirr = {}
strr = raw_input()
for c in strr:
    if c in d:
        dirr[c]=strr.count(c)

l = len(dirr.keys())
if(l==26):
    print "pangram"
else:
    print "not pangram"
