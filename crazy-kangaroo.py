tc = int(raw_input())
while (tc>0):
	tc = tc - 1
	a, b, m = map(int, raw_input().split())
	print (b/m)-(a-1)/m
"""
no = input()
v = []
for i in range(no):
    count = 0
    a,b,m = raw_input().split()
    a,b,m = int(a),int(b),int(m)
    for j in range(a,b+1):
        if(j%m==0):
            count += 1
    v.append(count)
for e in v:
    print e
"""
