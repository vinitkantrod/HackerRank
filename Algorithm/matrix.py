
def memo(f):
    save = {}
    def func(*args):
        if args in save:
            return save[args]
        ret = f(*args)
        save[args] = ret
        return ret
    return func

@memo
def f(root, parent): # cut all
    ret = 0
    for x, w in sub[root]:
        if x == parent:
            continue
        if bad[x]:
            ret += w + f(x, root)
        else:
            ret += min(w + g(x, root), f(x, root))
    return ret

@memo
def g(root, parent): # root is good: cut all but one bad
    s = f(root, parent)
    ret = 10**100
    for x, w in sub[root]:
        if x == parent:
            continue
        if bad[x]:
            delta = -w
        else:
            delta = g(x, root) - min(w + g(x, root), f(x, root))
        now = s + delta
        if now < ret:
            ret = now
    return ret

getnums = lambda: map(int, raw_input().strip().split())
n, k = getnums()
sub = [[] for x in xrange(n)]
bad = [False] * n
for x in xrange(n-1):
    a, b, w = getnums()
    sub[a].append((b, w))
    sub[b].append((a, w))
for x in xrange(k):
    a = input()
    bad[a] = True
if bad[0]:
    print f(0, -1)
else:
    print min(f(0, -1), g(0, -1))
