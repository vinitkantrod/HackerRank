no = input()
l = []
for i in range(no):
    n = input()
    a = map(int,raw_input().split()[:n])
    ans = 0
    for j in xrange(n):
        for k in xrange(n):
            if(a[j]==a[k]):
                pass
            else:
                if((a[j]+a[k])%2==0):
                    ans = ans + 1
    l.append(ans/2)
for e in l:
    print e
