a = raw_input()
sum = 0
d = {'1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6, '0':6}
for i in a:
    for k in d.keys():
        if(i==k):
            sum = sum + d[k]
print sum
