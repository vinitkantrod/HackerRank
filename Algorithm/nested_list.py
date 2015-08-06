no = input()
ll = []
max = 0
for i in range(no):
    a = raw_input()
    b = input()
    l = []
    l.append(a)
    l.append(b)
    ll.append(l)
max = ll[0][1]
for i in ll:
    if max < ll[i][1]:
        max = ll[i][1]
for j in ll:
    if max == ll[i][1]:
        del ll[i]
print ll
'''
for i in ll:
    for j in ll:
        if ll[i][1]<ll[j][1]:
            max = ll[i][1]
        else:
            max = ll[j][1]
print min
'''
