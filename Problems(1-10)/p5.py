def smallestevendivisblenumber():
	x = 20
	loop ="on"
	while loop == "on":
		x+=20
		c = 0
		for i in range(11,21):
			if x%i == 0:
				c+=1
		if c == 10:
			return x





print(smallestevendivisblenumber())
