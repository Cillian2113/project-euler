from math import sqrt
def nthprime(n):
	count = 0
	number = 0
	while count < n+1:
		number += 1
		if isprime(number):
			count+=1
	return number

#Program considers 1 a prime a prime number and program has had to be adjusted to consider this
def isprime(num):
	flag = True
	for x in range(2, round(sqrt(num))+1):
		if num % x == 0:
			flag = False
	return flag

print(nthprime(10001))
