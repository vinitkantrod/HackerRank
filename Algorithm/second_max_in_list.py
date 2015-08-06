no = input()
a = map(int,raw_input().split()[:no])
a = a.sort()
while(a[-2]!=a[-1]):
    print a[-2]
    
