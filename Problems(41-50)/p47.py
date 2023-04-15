def distinctPrimesFactors():
	n = 646
	while True:
		factored = set(primefactorisation(n))
		if len(factored) == 4:
			if len(set(primefactorisation(n+1))) != 4:
				n += 1
				continue
			if len(set(primefactorisation(n+2))) != 4:
				n += 1
				continue
			if len(set(primefactorisation(n+3))) != 4:
				n += 1
				continue
			return n
		n += 1

def primefactorisation(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors

print(distinctPrimesFactors())
