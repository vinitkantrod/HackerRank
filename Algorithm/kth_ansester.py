
from math import log

def doit():
    p = input()
    pairs = []
    for x in xrange(p):
        a, b = map(int, raw_input().strip().split())
        pairs.append((a,b))
    q = input()
    limit = max(int(log(p + q) / log(2) + 2), 17) # levels
    ances = {a: [0] * limit for a, _ in pairs}

    # init
    for a, b in pairs:
        ances[a][0] = b
    # build
    for x in xrange(1, limit):
        for v in ances:
            p = ances[v][x-1]
            if p == 0:
                continue
            ances[v][x] = ances[p][x-1]
    #print ances

    def get(a, k):
        #print 'get', a, k
        if a not in ances:
            return 0
        if k == 0:
            return a
        i = 0
        while k >= (1<<(i+1)):
            i += 1
        k -= 1 << i
        return get(ances[a][i], k)

    # queries
    for i in xrange(q):
        nums = map(int, raw_input().strip().split())
        if nums[0] == 0: # add
            x, y = nums[1:]
            if y not in ances:
                ances[y] = [0]*limit
            ances[y][0] = x
            for k in xrange(1, limit):
                p = ances[y][k-1]
                if p == 0:
                    break
                ances[y][k] = ances[p][k-1]
            #print ances
        elif nums[0] == 1: # remove
            x = nums[1]
            del ances[x]
        else: # query
            x, k = nums[1:]
            if x not in ances:
                print 0
            else:
                while k > 0 and x > 0:
                    i = 0
                    while (k & (1<<i)) == 0:
                        i += 1
                    if i >= len(ances[x]):
                        x = 0
                        break
                    x = ances[x][i]
                    k -= 1 << i
                print x

t = input()
for x in xrange(t):
    doit()
