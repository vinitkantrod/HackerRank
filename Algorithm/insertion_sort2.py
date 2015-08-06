def insertionSort(a,swap):
    for i in range(1,len(a)):
        t = a[i]
        p = i
        while(p>0 and a[p-1]>t):
            a[p] = a[p-1]
            p -= 1
            swap = swap+1
        a[p] = t
    print swap

no = input()
a = list(map(int,raw_input().split()[:no]))
c = 0
insertionSort(a,c)
