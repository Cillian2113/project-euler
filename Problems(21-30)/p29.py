def distinctPowers():
	distinctnums = []
	for a in range(2,101):
		for b in range(2,101):
			if not(a**b in distinctnums):
				distinctnums.append(a**b)
				print(len(distinctnums))
	return len(distinctnums)


print(distinctPowers())
