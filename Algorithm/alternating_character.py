no = input()
v = []
for i in range(no):
    c=0
    a = raw_input()
    for i in range(len(a)-1):
        if(a[i]==a[i+1]):
            c = c+1
    v.append(c)
for e in v:
    print e
            
