import re
sum = 0
n = input()
for i in range(n):
    a = raw_input()
    sum += len(re.findall('hackerrank',a, flags = re.I))
print sum
