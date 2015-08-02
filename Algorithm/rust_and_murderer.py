def close(A,N,S,X):
    return not( (S,X) in A or (X,S) in A )
def f(A,N,S,X):
    if close(A,N,S,X): return 1
    for i in xrange(N):
        if i!=S and i!=X and close(A,N,S,i) and close(A,N,i,X): return 2
    for i in xrange(N):
        if i!=S and i!=X and close(A,N,S,i):
            for j in xrange(N):
                if j!=S and j!=X and j!=i and close(A,N,i,j) and close(A,N,j,X): return 3
    return 4
            
for T in xrange(int(raw_input())):
    N,M = map(int,raw_input().split())
    A = []
    for i in xrange(M): A.append(tuple(map(int,raw_input().split())))
    S = int(raw_input())
    A = set(A)
    #print N,M,A,S
    #want to know dist S to X not touching A
    lt = []
    for X in xrange(1,1+N):
        if X!=S:
            lt.append(str(f(A,N,S,X)))
    print " ".join(lt)

