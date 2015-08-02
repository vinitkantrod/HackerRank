
from math import hypot, atan2, pi
def polar(x, y):      
    k = 180.0 * atan2(y, x) / pi
    if k<0: k+=360
    return  k,hypot(x, y)
  
n = int(raw_input())
ans1 = []
ans = []
d = dict()
for i in range(n):
    x,y = map(int,raw_input().split())
    ans.append([x,y])
    ans1.append(polar(x,y))

'''
for i in ind:
    print ans[i][0],ans[i][1]
'''
