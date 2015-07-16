no = input()
a = map(int,raw_input().split()[:no])
a = set(a)
b = max(a)
a = a.remove(b)
c = max(a)
print c
