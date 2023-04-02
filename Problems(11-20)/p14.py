def longestCollatzSequence():
	longest = 0
	lenlongest = 0
	for x in range(1,1000000):
		if lenCollatz(x) > lenlongest:
			longest = x
			lenlongest = lenCollatz(x)
	return longest

def lenCollatz(start):
	length = 1
	while start != 1:
		if start % 2 == 0:
			start = start/2
			length+= 1
		else:
			start = (3*start)+1
			length+=1
	return length

print(longestCollatzSequence())
