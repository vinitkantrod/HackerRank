d1,m1,y1 = map(int,raw_input().split())
d2,m2,y2 = map(int,raw_input().split())
fine = 0
s1 = 0
s2=  0
s1 = (365*y1) + (y1/4) - (y1/400) + d1 + (153*m1+8)/5
s2 = (365*y2) + (y2/4) - (y2/400) + d2 + (153*m2+8)/5
fine = abs(s1-s2)
print fine
