def largestpalindrome():
	biggest = 0
	empty = ''
	for x in range (999):
		for y in range (999):
			if x*y > biggest and str(x*y) == empty.join(reversed(str(x*y))):
				biggest = x*y
	return max

print(largestpalindrome())
