no = raw_input()
arr = raw_input().split()[:int(no)]
arr = map(int,arr)
count = []
while(len(arr)!=0):
    arr1=[]
    m = min(arr)
    #print m
    cou=0
    for i in range(0,(len(arr))):
        c = arr[i]-m
        cou = cou+1
        #print c
        if(c!=0):
           arr1.append(c)
           print cou
           #count.append(cou)
        else:
            print arr[i],'deleted'
            del arr[i]
    count.append(cou)
    arr = arr1
#for k in count:
    #print k
print(' '.join((str(e)) for e in count))
