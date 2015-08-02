l = []
w = []
no = input()
for _ in range(no):
    s = raw_input()
    s = s.split()
    kw = 'hackerrank'
    ls = len(s)
    if(ls==1):
        if(s[0]==kw):
            l.append(0)
        else:
            l.append(-1)
    elif(ls>1):
        if(s[0] == kw and s[ls-1] == kw):
            l.append(0)
        elif(s[0] == kw):
            l.append(1)
        elif(s[ls-1] == kw):
            l.append(2)
        elif(s[0]!=kw and s[ls-1]!= kw):
            l.append(-1)
for e in l:
    print e
