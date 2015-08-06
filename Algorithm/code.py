no = input()
f = []
v=[]
for i in range(no):
    frnd = raw_input()
    f.append(frnd)
for i in f:
    c=0
    m=f.index(i)
    mn,nn = 0,0
    n =[]
    for j in i:
        if(j=='Y'):
            c+=1
            nn = mn
            n.append(nn)
        mn= mn + 1
    v.append(n)
se=[]
for e in v:
    se.append(set(e))
group =0
print se
for w in se:
    ll= len(w)
    for ww in se:
        lll=len(ww)
        if(len(list(ww & w))==ll or len(list(ww & w))==lll):
            se.remove(ww)
            if(len(ww)==1):
                group+=1
                se.remove(ww)

print len(se)

for w in se:
    for ww in se:
        if(ww == w):
            group = 1
        else:
            if(list(ww & w)):
                    group += 1
