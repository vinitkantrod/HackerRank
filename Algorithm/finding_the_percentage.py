no = input()
di = {}
for i in range(no):
    a,b,c,d = raw_input().split()
    b,c,d = float(b),float(c),float(d)
    di[a]=[b,c,d]
sum = 0
v = []
key = raw_input()
if key in di.keys():
    j = di[key]
    for jj in j:
        sum = sum + float(jj)
sum = sum/3.0
v.append(sum)
for e in v:
    print("%.2f"%(e))
