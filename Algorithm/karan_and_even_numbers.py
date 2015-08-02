l = raw_input().split()
l = map(int,l)
for i in l:
    if(i!=-1):
        if(i%2==0):
            print i
    else:
        break

