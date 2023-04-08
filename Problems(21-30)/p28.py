def numberSpiralDiagonals():
	n = 500 #matrix size 1001 minus 1 to not include the middle then halved as we only want one of each diagonal
	total = 1 + 2/3*n*(8*n**2+15*n+13) #calculated the summation of each of the 4 sequences
	return int(total)

print(numberSpiralDiagonals())
