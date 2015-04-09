n,t = raw_input().split()
n,t = int(n),int(t)
v = [] 
l = raw_input().split()[:n]
l = map(int,l)
for i in range(t):
    min_no=3
    ind,out = raw_input().split()
    ind,out = int(ind),int(out)
    for j in range(ind,out+1):
        #print l[j], min_no, type(l[j]), type(min_no)
        if(l[j]<min_no):
            min_no=l[j]
    v.append(min_no)

for k in v:
    print k
            
