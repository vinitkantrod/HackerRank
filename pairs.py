n, k = map(int,raw_input().split())
a = set(map(long,raw_input().split()[:n]))
print(len([1 for i in a if i + k in a]))
