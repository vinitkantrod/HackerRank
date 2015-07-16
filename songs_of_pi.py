pi = '31415926535897932384626433833'
l = []
for _ in range(input()):
    if pi.startswith(''.join([str(len(x)) for x in list(raw_input().split())])):
        l.append("It's a pi song.")
    else:
        l.append("It's not a pi song.")
for e in l:
    print e
