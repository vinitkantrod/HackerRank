import math
no = input()
v = []
for i in range(no):
    k,n = map(int,raw_input().split())
    nodes = int(math.pow(k,n+1)-1)/(k-1)
    l,sum = nodes,0
    while(l!=0):
        sum = sum + l%10
        l = l/10
    v.append(sum)
for e in v:
    print e
        
