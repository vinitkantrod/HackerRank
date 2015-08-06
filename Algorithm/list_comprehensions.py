v = []
x = input()
y = input()
z = input()
n = input()
for i in range(0,x+1):
    for j in range(0,x+1):
        for k in range(0,x+1):
            a =[]
            if((i+j+k)!=n):
                a.append(i)
                a.append(j)
                a.append(k)
                v.append(a)
print v.sort()
