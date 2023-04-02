from math import factorial
def latticePaths(gridsize):
	return factorial(2*gridsize)/(factorial(gridsize)*factorial(gridsize))

print(latticePaths(20))

#In a 20x20 grid, there are horizontal edges and vertical edges.
#To get to the other end, the user must follow 20 horizontal edges and 20 vertical.
#We will calculate the amount of different combinations of edges that sum to 20 horizontal and 20 vertical
