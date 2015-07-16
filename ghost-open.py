no = raw_input()
s = []
for i in range(int(no)):
    a = input()
    a = int(a)
    q = a
    sum = 0
    if(a == 0):
        s.append(0)
        continue
    if(q == 1):
        s.append(1)
        continue
    while(q!=1):
        q = a / 2
        sum = sum + q
        if(a%2 == 1):
            q = q + 1
        a = q
    s.append(sum)
if(len(s)>=1):
    for e in s:
        print e
