def lcm(a,b):
	x=max(a,b)
	y=min(a,b)
	c=y
	while((c%x)!=0):
		c+=y
	print(c)
	

