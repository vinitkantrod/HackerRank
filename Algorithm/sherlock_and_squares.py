no = input()
import math
v=[]
for i in range(no):
    count=0
    a,b = raw_input().split()
    a,b = int(a),int(b)
    count = int(math.floor(math.sqrt(b))-math.ceil(math.sqrt(a))+1)
    v.append(count)
for e in v:
    print e
