no = input()
v=[]
for i in range(no):
    sum=0
    b,w = raw_input().split()
    x,y,z = raw_input().split()
    b,w,x,y,z=int(b),int(w),int(x),int(y),int(z)
    if(x==y):
        sum = b*x+w*y
        v.append(sum)
    elif(x<y):
        if(y>(x+z)):
            sum = b*x + w*(x+z)
            v.append(sum)
        elif(y<=(x+z)):
            sum=b*x + w*y
            v.append(sum)            
    elif(x>y):
        if(x>(y+z)):
            sum = b*(y+z) + w*y
            v.append(sum)
        elif(x<=(y+z)):
            sum = b*x + w*z
            v.append(sum)
for e in v:
    print e
