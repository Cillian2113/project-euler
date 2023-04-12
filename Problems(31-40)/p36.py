def doubleBasePalindromes():
	total = 0
	for n in range(1,1000000):
		if ispalindrome(n):
			if ispalindrome("{0:b}".format(n)):
				total += n
	return total

def ispalindrome(n):
	if str(n) == ''.join(reversed(str(n))):
		return True
	return False

print(doubleBasePalindromes())
