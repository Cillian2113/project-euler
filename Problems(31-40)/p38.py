def pandigitalMultiples():
	maxval = 918273645 #The biggest known example from the question, can ignore all other single digit integers
	#Cannot be a 2 digit integer with value 9 so we also ignore 9
	#Also can't be a 3 digit integer starting with 9
	#Final option is a 4 digit integer multiplied by (1,2). I will test all cases here
	for n in range(9000,10000):
		concatproduct = int(str(n)+str(n*2))
		if pandigital(concatproduct) and concatproduct > maxval:
			maxval = concatproduct
	return maxval

def pandigital(number):
	for x in range(1,10):
		if str(x) in str(number):
			continue
		else:
			return False
	return True

print(pandigitalMultiples())
