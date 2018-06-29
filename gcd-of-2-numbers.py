def gcd(a,b):
	x=max(a,b)
	y=min(a,b)
	while((x%y)!=0):
		prev=y
		y=x%y
		x=prev
	print(y)
