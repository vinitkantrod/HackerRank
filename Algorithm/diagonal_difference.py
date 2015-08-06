no = input()
l = []
for i in range(no):
    a = map(int,raw_input().split())
    l.append(a)
s1 = 0
for j in xrange(no):
    for k in xrange(no):
        if(j==k):
            s1 = s1 + l[j][k]    
l.reverse()
s2 = 0
for m in xrange(no):
    for n in xrange(no):
        if(m==n):
            s2 = s2 + l[m][n]
print abs(s1-s2)
