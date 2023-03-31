def sumSquareDifference():
	squaresum = 0
	for i in range(1,101): squaresum+=i
	squaresum = squaresum**2
	sumsquare = 0
	for i in range(1,101): sumsquare+=i**2
	return squaresum - sumsquare

print(sumSquareDifference())
