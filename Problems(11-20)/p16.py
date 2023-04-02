def powerDigitSum():
	sum = 0
	for x in str(2**100000):
		sum+=int(x)
	return sum

print(powerDigitSum())
