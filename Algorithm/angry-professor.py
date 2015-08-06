no = input()
v = []
for i in range(no):
    n,k = raw_input().split()
    n,k = int(n), int(k)
    l = raw_input().split()[:n]
    l = map(int,l)
    count = 0
    for j in l:
        if(j<=0):
            count = count + 1
    if(count>=k):
        v.append("No")
    else:
        v.append("Yes")

for w in v:
    print w
