v = []
for _ in xrange(input()):
    l = []
    n, k = map(int,raw_input().split())
    a = map(int,raw_input().split())
    b = map(int,raw_input().split())
    c, d = 0, 0
    for i in xrange(n):
        for j in xrange(n):
            if((a[i]+b[j])==k):
                c += 1
    for i in xrange(n):
        for j in xrange(n-1,-1,-1):
            if(a[i++]+b[j] >= k):
                d += 1
    if(c==n or d==n):
        l.append"YES"
    else:
        l.append"NO"
        v.append(l)
for e in v:
    print(''.join((str(q)) for w in e))
