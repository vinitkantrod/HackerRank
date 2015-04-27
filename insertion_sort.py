no = input()
a = list(map(int,raw_input().split()[:no]))
temp = a[-1]
i = len(a)-1
while(temp < a[i-1]):
    a[i] = a[i-1]
    print(' '.join((str(e)) for e in a))
    i=i-1
    if(i==0):
        break
if(temp>=a[i-1]):
    a[i] = temp
print(' '.join((str(e)) for e in a))
