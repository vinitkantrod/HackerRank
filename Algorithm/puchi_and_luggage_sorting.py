no = input()
v = []
for i in range(no):
    n = input()
    l = []
    ll = []
    for j in range(n):
        l.append(input())
    for k in range(len(l)):
        m = l[k]
        count = 0
        for p in range(k,len(l)):
            if(m>l[p]):
                count+=1
        ll.append(count)
    v.append(ll)
for e in v:
    print(' '.join((str(x)) for x in e))

