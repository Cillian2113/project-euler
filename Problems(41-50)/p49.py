from itertools import permutations
def primePermutations():
	fourdigitprimes = [x for x in primesList(10000) if x > 1000]
	for a in fourdigitprimes:
		if a == 1487:
			continue
		perms = [int(''.join(perm)) for perm in permutations(str(a))]
		for d in range(1000,int((10000-a)/2)+1):
			if a+d in fourdigitprimes and a+2*d in fourdigitprimes:
				if a+d in perms and a+2*d in perms:
					return str(a)+str(a+d)+str(a+2*d)

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

print(primePermutations())
