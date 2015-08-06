v = []
for _ in range(input()):
    l = []
    m = input()
    n = input()
    c1 = 0
    flag = False
    a = map(int,raw_input().split()[:n])
    for i in range(n):
        c1 = c1 + 1
        c2 = 0
        for j in range(i+1,n):
            c2 = c2 + 1
            if((a[i]+a[j])==m):
                flag = True
                c1 = i+1
                c2 = j+1
                break
        if(flag == True):
            break
    l.append(c1)
    l.append(c2)
    v.append(l)
for e in v:
    print(' '.join((str(w)) for w in e))
