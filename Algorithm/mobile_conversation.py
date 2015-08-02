no = input()
d={}
for i in range(no):
    a,b = map(int,raw_input().split())
    d[a] =b
bal = 0
m = max(d.keys())
bal = m
recharge = bal
while(d):
    m = max(d.keys())
    if(bal >= m):
        bal = bal - m 
        bal = bal + d[m]
        del d[m]
    else:
        recharge += (m-bal)
        bal = d[m]
        del d[m]
print recharge
        
        
    
