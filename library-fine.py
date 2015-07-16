ad = map(int,raw_input().split())
ed = map(int,raw_input().split())


if(ad[2]>ed[2]):
	fine = 10000
	print fine

elif(ad[2]==ed[2]):
	if(ad[1]>ed[1]):
		diff = ad[1]-ed[1]
		fine = diff*500
		print fine

	elif(ad[1]==ed[1]):
		diff = ad[0]-ed[0]
		if(diff>0):
			fine = diff*15
			print fine
		else:
			print "0"
	else:
		print "0"
else:
	print "0"