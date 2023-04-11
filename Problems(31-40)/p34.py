from math import factorial
def digitFactorials():
	total = 0
	for n in range(10,2540160):
		numbers = list(str(n))
		numbers = [ factorial(int(x)) for x in numbers ]
		if sum(numbers) == n:
			total += n
	return total


print(digitFactorials())
