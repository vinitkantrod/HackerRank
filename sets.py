n1 = input()
a = map(int,raw_input().split()[:n1])
n2 = input()
b = map(int,raw_input().split()[:n2])
a,b = set(a),set(b)
s = a.symmetric_difference_update(b)
for i in sorted(a):
    print i
