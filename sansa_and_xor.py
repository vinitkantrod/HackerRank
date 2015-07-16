no = int(raw_input())
for t in xrange(no):
    N = int(raw_input())
    a = map(int, raw_input().split())
    print a
    ans = 0
    for i in xrange(N):
        print i+1, N-i
        if (i+1)%2==1 and (N -i) % 2 == 1:
            ans ^= a[i]
    print(ans)
