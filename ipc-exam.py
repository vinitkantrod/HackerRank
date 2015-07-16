no,m = raw_input().split()
no,m = int(no),int(m)
v=[]
for i in range(no):
    a = raw_input().split()[:m]
    v.append(a)
    
abc=[]
for i in v:
    print i
    for j in i:
        k = int(j)
        if(len(k)<m):
            print k
            k= z.fill(5)
            print type(k)
            abc.append(k)
            
        else:
            abc.append(j)
            
        