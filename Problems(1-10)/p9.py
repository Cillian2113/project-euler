def PythagoreanTriplet():
	combinations = [(i, 1000-i-k, k) for i in range(1,999) for k in range(1,1000-i)]
	for x in combinations:
		if x[0]**2+x[1]**2==x[2]**2:
			return x[0]*x[1]*x[2]


print(PythagoreanTriplet())
