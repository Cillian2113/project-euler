from math import sqrt
def goldbachsOtherConjecture():
	n = 4
	primelist = primesList(10000) #I set a generic upper limit here for the primes I calculated, could be set lower to improve the efficiency if the answer is already known
	while True:
		number = 2*n+1
		if number in primelist: #To loop through every odd composite number I looped through all odd numbers that aren't prime
			n += 1
			continue
		shortenedprimelist = [prime for prime in primelist if prime < number]
		found = False
		for prime in shortenedprimelist: #The inner loop checks through every prime less than the odd composite number
			if (sqrt((number - prime)/2)) % 1 == 0: #Checks if there is a whole square number that can satisfy the conjecture
				found = True
				break
		if found is False: #If there is no whole number found after looping through each prime this number disproves the conjecture and we return it
			return number
		n += 1

def primesList(num):
	prime = [True for i in range(num+1)]
	primes = []
	p = 2
	while p * p <= num:
		if prime[p] is True:
			for i in range(p * p, num+1, p):
				prime[i] = False
		p += 1
	for p in range(2, num+1):
		if prime[p]:
			primes.append(p)
	return primes

print(goldbachsOtherConjecture())
