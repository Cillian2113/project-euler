def maximumPathSum2():
	with open('p067_triangle.txt') as f:
		triangle = f.readlines()
	for x in range (len(triangle)):
		triangle[x] = triangle[x].replace('\n','')
		triangle[x] = triangle[x].split(' ')
	for y in range(1,100):
		for x in range (len(triangle[100-y])-1):
			triangle[100-y-1][x] = int(triangle[100-y-1][x])
			triangle[100-y-1][x] += int(max(triangle[100-y][x],triangle[100-y][x+1]))
	return triangle[0][0]

print(maximumPathSum2())