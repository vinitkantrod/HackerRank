import sys, math
def rs():
    return sys.stdin.readline().strip()
def ri():
    return int(sys.stdin.readline().strip())
def ras():
    return list(sys.stdin.readline().strip())
def rai():
    return map(int,sys.stdin.readline().strip().split())
c= 1000000007
f = lambda v: (v ** (v - 2)) % c
n = ri()

for x in xrange(n):
  k = ri()
  arr = rai()
  if k==1:
    print f(arr[0])
    continue
  r = 1
  for o in arr:
    r = r * f(o) % c
    r = r * o % c
  print int(r * sum(arr)**(k-2)) % c
    
