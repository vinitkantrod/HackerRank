n = input()
l = []
for i in xrange(n):
    PAN = raw_input()
    alp = PAN[:5]+PAN[-1]
    if(alp.isalpha() and alp.isupper() and PAN[5:-1].isdigit()):
        l.append("YES")
    else:
        l.append("NO")
for e in l:
    print e
'''
l = []
for i in range(no):
    s = raw_input()
    if(len(s)>10):
        l.append("NO")
    elif(len(s)==10):
        s = list(s)
        f = True
        i = 0
        if(f == True):
            while(i >= 0 and i < 5 and f == True):
                o = ord(s[i])
                if(o < 65 or o > 90):
                    l.append("NO")
                    f = False
                else:
                    i += 1
            while(f == True and i<9 and i>=5):
                o = ord(s[i])
                if(o < 48 and o > 57):
                    l.append("NO")
                    f = False
                else:
                    i += 1
            while(f == True and i < len(s)):
                if(o < 65 and o > 90):
                    l.append("NO")
                    f = False
                else:
                    i += 1
            if(f == True):
                l.append("YES")
for e in l:
    print e
'''
