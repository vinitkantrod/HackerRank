no = input()
v = []
for i in range(no):
    a = input()
    b = raw_input().split()[:a]
    l = []
    l = sorted(b,reverse=True)
    v.append(l)
for e in v:
    print(' '.join((str(w)) for w in e))
