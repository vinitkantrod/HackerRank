def alternative(stri,de):
    l = len(s)
    for j in range(l):
        if(stri[j]=='a'):
             if(((j+1)>l) and (stri[j+1]=='a')):
                de = de + 1
        if(stri[j]=='b'):
             if(((j+1)>l) and (stri[j+1]=='b')):
                de = de + 1
    return de

no = raw_input()
no = int(no)
v = []
for i in range(no):
    d = 0
    s = raw_input()
    s = s.lower()
    dele = alternative(s,d)

print dele

