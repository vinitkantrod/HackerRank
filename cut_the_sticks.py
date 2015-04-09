no = raw_input()
arr = raw_input().split()[:int(no)]
arr = map(int,arr)
count = []
while(len(arr)!=0):
    arr1=[]
    m = min(arr)
    #print m
    cou=0
    for i in range(0,len(arr)):
        c = arr[i]-m
        #print c
        if(c!=0):
           arr1.append(c)
           cou =cou + 1
           count.append(cou)
        else:
            print arr[i],'deleted'
            del arr[i]
    arr = arr1
for k in count:
    print k
