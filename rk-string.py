from sys import stdin 
def consecutive_groups(iterable):
	s=tuple(iterable)
	for size in range(1, len(s)+1):
		for index in range(len(s)+1-size):
			yield iterable[index:index+size]
for i in range(0,int(stdin.readline())):
	a=map(int,stdin.readline().split())
	b=raw_input()
	if len(b)<10**3:
		s=t=0
		for i in list(consecutive_groups(b)):
			if i.count('R')==a[0]:
				s+=1
			if i.count('K')==a[1]:
				t+=1
		print s,t
	else:
		c=[i for i, ltr in enumerate(b) if ltr=='R']
		d=[i for i, ltr in enumerate(b) if ltr=='K']
		c.insert(0,-1)
		c.append(len(b))
		d.insert(0,-1)
		d.append(len(b))
		r=0
		k=0
		for i in range(1,len(c)-a[0]):
			r+=((c[i]-c[i-1])*(c[i+a[0]]-c[i+a[0]-1]))
		for i in range(1,len(d)-a[1]):
			k+=((d[i]-d[i-1])*(d[i+a[1]]-d[i+a[1]-1]))
		print r,k
