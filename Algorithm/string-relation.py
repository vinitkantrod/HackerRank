l = []
for _ in xrange(input()):
    s = raw_input()
    a = s.count('a')
    b = s.count('b')
    c = s.count('c')
    lens = len(s)
    if(a==lens or b==lens or c==lens):
        l.append(lens)
    elif(a%2==0 and b%2==0 and c%2==0):
        l.append(2)
    elif(a%2==1 and b%2==1 and c%2==1):
        l.append(2)
    else:
        l.append(1)
for e in l:
    print e
