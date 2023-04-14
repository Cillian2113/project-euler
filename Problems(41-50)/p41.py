from itertools import permutations
def pandigitalPrime():
	# cannot be 8 or 9 or 5 or 6 digits as divisible by 3
	# Has to be  7 digits
	perm = permutations("7654321")
	for i in perm:
		n = int(''.join(i))
		print(n)
		if isItPrime(n):
			return i

def isItPrime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(pandigitalPrime())
