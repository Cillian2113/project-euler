from math import sqrt
def summationprimes(limit):
	total = 5
	x = 5
	while x<limit:
		if isprime(x):
			total += x
		x += 2
	return total

def isprime(num):
	flag = True
	for x in range(2, round(sqrt(num))+1):
		if num % x == 0:
			flag = False
	return flag

print(summationprimes(2000000))
