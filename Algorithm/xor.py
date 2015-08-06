a = raw_input()
b = raw_input()
a,b = int(a),int(b)
m=a
n=b
max_value = 0
x = 0
for i in range(a,b+1):
    for j in range(a,b+1):
        if(i <= j):
            x = i ^ j
            if(max_value < x):
                max_value = x
                print i,'^',j," is %s"%max_value
print max_value
