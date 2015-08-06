no = raw_input()
for i in range(int(no)):
    m,n = raw_input().split()
    m,n = int(m),int(n)
    st1 = raw_input()
    l = len(st1)
    for i in range(l):
        if(l<=6):
            a.append(st1[i:i+l])
        
