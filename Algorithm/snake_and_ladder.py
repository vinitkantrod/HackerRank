no = input()
vv = []
for i in range(no):
    a = input()
    l, s =[], []
    for j in range(a):
        l.append(map(int,raw_input().split()))
    b = input()
    for k in range(b):
        s.append(map(int,raw_input().split()))
    
    l.extend(s)
    D = {}
    for m, n in l:
        D[m]=n
    V = set()
    S = set()
    S.add(1)
    moves = 0
    while 100 not in S:
        moves += 1
        S2 = set()
        for a in S:
            for d in range(1,7):
                n = a + d
                if n in D:
                    n = D[n]
                if n in V:
                    continue
                V.add(n)
                S2.add(n)
        S = S2
        if(moves>100):
            moves = -1
            break
    vv.append(moves)
for e in vv:
    print e
                    
    
