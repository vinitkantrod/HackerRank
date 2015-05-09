a = raw_input()
d = {}
c=0
l = len(a)
flag =True
for i in d:
    d[i] = i.count(i)
if(l%2==0):
    for j in d.values():
        if(j%2==1):
            flag = False
            break
elif(l%2==1):
    for k in d.values():
        if(k%2==1):
            c = c+1
    if(c%2==0):
        flag=False

if(flag==False):
    print("NO")
else:
    print("YES")
    
    
