'''
def substring(string):
    l = len(string)
    return [string[i:j+1] for i in xrange(l) for j in xrange(i,l)]
'''

no = input()
v=[]
for i in range(no):
    c = 0
    d1 = {}
    d2 = {}
    a = raw_input()
    b = raw_input()
    for i in a:
        d1[i] = a.count(i)
    for j in b:
        d2[j] = b.count(j)
    print d1, d2
    l= d1.keys()
    for k in l:
        if(d2.has_key(k)):
            c +=1
    if(c>0):
        v.append("YES")
    else:
        v.append("NO")

for w in v:
    print w
'''
    a1 = substring(a)
    b1 = substring(b)
    for j in a1:
        for k in b1:
            if(j == k):
                c = c + 1
    if(c>0):
        v.append("YES")
    else:
        v.append("NO")
for e in v:
    print e
'''
