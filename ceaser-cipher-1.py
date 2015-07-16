no = input()
s = raw_input()[:no]
k = input()
ss = []
c = 0
k1 = 0
for i in s:
    o = ord(i)
    if(o>=97 and o<=122):
        if(o+k>122):
            while(o+k>122):
                o1 = 122-o
                if(o1<=k):
                    k1 = (o+k)-o1
                    k = k1-o
                else:
                    ss.append(chr(96+i))
                    break
                if(o+k<=122):
                    ss.append(chr(ord(i)+k))
        else:
            c = ord(i)+k
            ss.append(chr(c))
    else:
        ss.append(i)
print ss
