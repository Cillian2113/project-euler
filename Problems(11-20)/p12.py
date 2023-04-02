from math import sqrt
def triangleNumbersDivisibility():
	i = 1
	num = 1
	while True:
		i += 1
		num += i
		print(factors(num), num)
		if factors(num) > 500:
			return num


def factors(number):
	factors = 0
	j = 1
	if (number % 2) != 0:
		while j<=sqrt(number):
			if j == sqrt(number):
				factors+=0.5
			elif (number % j) == 0:
				factors+=1
			j+=2
		return factors*2
	while j<=sqrt(number):
		if j == sqrt(number):
			factors+=0.5
		elif (number % j) == 0:
			factors+=1
		j+=1
	return factors*2


print(triangleNumbersDivisibility())
