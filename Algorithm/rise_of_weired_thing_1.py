no = input()
e, o, ll = [], [], []
sum1, sum2 = 0, 0
a = map(int,raw_input().split()[:no])
for j in a:
    if(j%2 == 0):
        e.append(j)
        sum1 = sum1 + j
    else:
        o.append(j)
        sum2 = sum2 + j
e.append(sum1)
o.append(sum2)
e, o = sorted(e), sorted(o)
ll = e + o
print(' '.join((str(w)) for w in ll))
