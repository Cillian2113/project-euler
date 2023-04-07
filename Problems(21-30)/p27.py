#pip install sympy
import sympy
primes = list(sympy.primerange(0, 1000))

def quadraticPrimes():
	nmax = 0
	for a in range(-999,1000,2):
		for b in primes:
			print(primeSequence(a,b), a,b)
			if primeSequence(a,b) > nmax:
				numbers = [a,b]
				nmax = primeSequence(a,b)
	return nmax,numbers

def primeSequence(a,b):
	n = 0
	while isprime(n**2+n*a+b) is True:
		n+=1
	return n

def isprime(number):
    if number <= 1:
        return False
    for x in range(2, number):
        if not number % x:
            return False
    return True

print(quadraticPrimes())
