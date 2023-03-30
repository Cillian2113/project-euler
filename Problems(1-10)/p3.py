#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def LargestPrimeFactor(num: int):
	n = 600851475143
	i = 2
	while i * i < n:
		while n%i == 0:
			n = n / i
		i = i + 1
	return n




print(LargestPrimeFactor(600851475143))
