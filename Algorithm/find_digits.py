no = raw_input()
no = int(no)
v=[]
for i in range(no):
    a = raw_input()
    count = 0
    for j in a:
        if(j!='0'):
            a,j = int(a),int(j)
            if(a%j == 0):
                count = count+1
    v.append(count)
for k in v:
    print k
