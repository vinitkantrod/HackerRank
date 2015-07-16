n = input()
w = map(int,raw_input().split()[:])
w = sorted(w)
print w
if(len(w)>1):
    i = 0
    c = 1
    s = range(w[i],w[i]+5)
    while(i < len(w)):
        if w[i] in s:
            i = i+1
        else:
            c = c + 1
            s = range(w[i],w[i]+5)
else:
    c = 1
print c

