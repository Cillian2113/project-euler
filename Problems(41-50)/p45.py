from math import sqrt
def triangularPentagonalHexagonal():
	n = 286
	while True:
		if isPentagonal(n*(n+1)/2) and isHexagonal(n*(n+1)/2):
			return n*(n+1)/2
		n += 1

def isPentagonal(n):
	return (1+sqrt(1+24*n))%6 == 0

def isHexagonal(n):
	return (1+sqrt(1+8*n))%4 == 0

print(triangularPentagonalHexagonal())
