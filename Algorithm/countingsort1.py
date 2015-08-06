n = input()
no = map(int,raw_input().split()[:n])
di = dict((i,0) for i in range(100))
d = dict((i,no.count(i)) for i in no)
for k in set(di.keys()) and set(d.keys()):
    di[k]=d[k]
print(' '.join((str(i)) for i in di.values()))
