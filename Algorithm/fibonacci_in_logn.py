def power(n):
    l = [[1,1],[1,0]]
    if n == 0:
        return 0
    else:
        for i in xrange(2,n):
            multiply(l)
    return l[0][0]

def multiply(l):
    M = [[1,1],[1,0]]
    x = l[0][0]*M[0][0] + l[0][1]*M[1][0]
    y = l[0][0]*M[0][1] + l[0][1]*M[1][1]
    z = l[1][0]*M[0][0] + l[1][1]*M[1][0]
    w = l[1][0]*M[0][1] + l[1][1]*M[1][1]
    
    l[0][0] = x
    l[0][1] = y
    l[1][0] = z
    l[1][1] = w
    return l

print power(input())
