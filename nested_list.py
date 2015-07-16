no = input()
ll = []
for i in range(no):
    a = raw_input()
    b = input()
    l = []
    l.append(a)
    l.append(b)
    ll.append(l)
min = ll[0][1]
for i in ll:
    for j in ll:
        if ll[i][1]<ll[j][1]:
            min = ll[i][1]
        else:
            min = ll[j][1]
print min
