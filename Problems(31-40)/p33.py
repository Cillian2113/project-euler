def digitCancellingFractions():
	product =  1
	for n in range(1,10):
		for c in range(1,10):
			for d in range(1,10):
				if 9*n*(c-d) == c*(d-n) and c != d and c != n and d != n:
					product = product*((10*n+c)/(10*c+d))
	return product

print(digitCancellingFractions())
