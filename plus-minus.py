n = input()
a = map(int,raw_input().split())
c1 = 0
c2 = 0
c3 = 0
for i in a:
    if(i>0):
        c1+=1 
    if(i<0):
        c2+=1
    if(i==0):
        c3+=1
l = float(len(a))
b,c,d = c1/l, c2/l, c3/l
print("{0:.3f}".format(b))
print("{0:.3f}".format(c))
print("{0:.3f}".format(d))
