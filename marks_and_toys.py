n, k = map(int,raw_input().split())
t = map(int,raw_input().split()[:n])
t = sorted(t)
c, i = 0, 0
toys = 0
while(c <= k):
    if((c+t[i])<= k):
        c = c + t[i]
        i = i + 1
        toys += 1
    else:
        break
print toys
