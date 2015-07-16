from fractions import gcd

def minAverage(dist, n):
    d = [[0] * n for i in xrange(n+1)]    
    for i in xrange(1, n+1):
        for j in xrange(n):
            d[i][j] = min([d[i-1][k] + dist[k][j] for k in xrange(n) if k != j]) 
    pmin = ()
    qmin = 1
    for i in xrange(n):
        
        pmax = 0
        qmax = 1
        for j in xrange(n):
            p = d[n][i] - d[j][i]
            q = n - j
            if p*qmax > q*pmax:
                pmax, qmax = p, q
        
        if pmax*qmin < qmax*pmin:
            pmin, qmin = pmax, qmax
    
    g = gcd(pmin, qmin)
    return pmin/g, qmin/g

n = input()
distances = list()
for i in range(n):
    distances.append(map(int, raw_input().split()))

print("%i/%i" % minAverage(distances, n))
