no = raw_input()
v = []
for i in range(int(no)):
    sr = raw_input()
    rs = sr[::-1]
    flag = 1
    for i,j in zip(range(1,len(sr)),range(1,len(rs))):
        s1,s2 = sr[i],sr[i-1]
        r1,r2 = rs[j],rs[j-1]
        org_str = ord(s1)-ord(s2)
        rev_str = ord(r1)-ord(r2)
        if(org_str < 0):
            org_str = org_str *(-1)
        if(rev_str < 0):
            rev_str = rev_str * (-1)
        if(org_str != rev_str):
            flag = 0
            break
    if(flag == 0):
        v.append("Not Funny")
    else:
        v.append("Funny")

for vv in v:
    print vv
