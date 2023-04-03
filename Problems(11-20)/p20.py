from math import factorial
def factorialDigitSum(num):
	sum = 0
	for x in str(factorial(num)):
		sum += int(x)
	return sum
	
print(factorialDigitSum(100))
