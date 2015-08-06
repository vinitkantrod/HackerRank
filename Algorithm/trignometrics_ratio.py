import operator

def f(n):
    return reduce(operator.mul, range(1,n+1),1)

l = []
for _ in range(input()):
    x = input()
    sinof_x = x - (x**3/f(3)) + (x**5/f(5)) - (x**7/f(7)) + (x**9/f(9))
    l.append(sinof_x)
    cosof_x = 1 - (x**2/f(2)) + (x**4/f(4)) - (x**6/f(6)) + (x**8/f(8))
    l.append(cosof_x)

for e in l:
    print("%.3f"%e)
