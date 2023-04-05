from math import sqrt

def amicableNumbers():
	divisors = [(x,d(x)) for x in range(1,10000)]
	sum = 0
	for x in divisors:
		for y in divisors:
			if y[0] == x[1] and y[1] == x[0] and x[0] != y[0]:
				sum += x[0] + y[0]
	return int(sum/2) #Divide by 2 because it will count each amicable pair twice

def d(n):
	summation = 0
	j = 1
	if (n % 2) != 0:
		while j<=sqrt(n):
			if j == sqrt(n):
				summation += j
			elif (n % j) == 0:
				summation += j + (n/j)
			j+=2
		return int(summation-n)
	while j<=sqrt(n):
		if j == sqrt(n):
			summation += j
		elif (n % j) == 0:
			summation += j + (n/j)
		j+=1
	return int(summation-n)

print(amicableNumbers())
