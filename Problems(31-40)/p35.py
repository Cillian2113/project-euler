def circularPrimes():
	primes = primeNumbers(1000000)
	total = 2
	for n in primes:
		circular = True
		for number in ['0','2','4','5','6','8']:
			if number in str(n):
				circular = False
		if circular is False:
			continue
		combinations = [rotateDigits(n,k) for k in range(len(str(n)))]
		print(combinations)
		for perm in combinations:
			if int(perm) in primes:
				continue
			else:
				circular = False
				break
		if circular is True:
			total += 1
			print(n)
	return total

def primeNumbers(num):
	prime = [True for i in range(num+1)]
	primes = []
	p = 2
	while (p * p <= num):
		if (prime[p] is True):
			for i in range(p * p, num+1, p):
				prime[i] = False
		p += 1
	for p in range(2, num+1):
		if prime[p]:
			primes.append(p)
	return primes

def rotateDigits(num, k):
  num_list = list(str(num))
  num_list = num_list[k:] + num_list[:k]
  return int(''.join(num_list))

print(circularPrimes())
