def counter(n):
    count = 0
    while n != 1:
        s = bin(n)[2:]
        if s.count('0') == len(s) - 1:
            n = int(s[:-1], 2)
        else:
            n = int(s[1:], 2)
        count += 1

    if count % 2 == 0:
        print 'Richard'
    else:
        print 'Louise'

t = int(raw_input())
for i in xrange(t):
    s = int(raw_input())
    counter(s)
