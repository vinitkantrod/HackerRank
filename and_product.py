from math import log
mask = 2**32 - 1
T=input()

for _ in xrange(T):
    A,B=(int(i) for i in raw_input().split())
    print (A&B)&(mask - 2**int(log(B-A,2)))

