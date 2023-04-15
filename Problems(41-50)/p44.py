from math import sqrt
def pentagonNumbers():
	for x in range(1,10000): #10000 is just a guess placeholder for the upper limit
		for y in range(1,x):
			if ispentagonal(pentagonal(x)-pentagonal(y)) and ispentagonal(pentagonal(x)+pentagonal(y)):
				return pentagonal(x)-pentagonal(y)

def ispentagonal(n):
	return (1+sqrt(1+24*n))%6==0

def pentagonal(n):
	return n*(3*n-1)/2

print(pentagonNumbers())
