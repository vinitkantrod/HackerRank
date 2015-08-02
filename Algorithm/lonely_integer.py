no = raw_input()
no = int(no)
arr = raw_input().split()[:no]
arr = map(int,arr)
a = dict((i,arr.count(i)) for i in arr)
for k,v in a.items():
    if(a[k]==1):
        print k
