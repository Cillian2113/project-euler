def truncatablePrimes():
	total = 0
	primes = primeNumbers(1000000)
	for x in primes:
		truncatable = True
		if x > 10:
			for n in range(-len(str(x))+1,len(str(x))):
				if n < 0:
					if int(str(x)[:n]) in primes:
						continue
					else:
						truncatable = False
						break
				if n == 0:
					continue
				if n > 0:
					if int(str(x)[n:]) in primes:
						continue
					else:
						truncatable = False
						break
			if truncatable is True:
				total += x
	return total




	return None




def primeNumbers(num):
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


print(truncatablePrimes())
