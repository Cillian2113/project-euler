from math import sqrt
#This algorithm is very inefficient taking apporximately 3 minutes in my codespace to execute> I will try to revise it at a later point

def nonAbundantSums():
	abundantNums = []
	for x in range(12,28124):
		if sumProperDivisors(x) > x:
			abundantNums.append(x)

	numbers = [x for x in range(28123)]

	for x in range (len(abundantNums)):
		for y in range (x, len(abundantNums)):
				print(x,y)
				temp = abundantNums[x]+abundantNums[y]
				if temp < 28123:
					numbers[temp] = 0

	total = sum(numbers)
	return total

def sumProperDivisors(n):
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

print(nonAbundantSums())
