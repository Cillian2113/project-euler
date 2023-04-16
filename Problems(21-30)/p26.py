def reciprocalCycles():
	longest = 1
	num = 1
	for n in range(3, 1000, 2):
		p = 1
		while (10 ** p) % n != 1 and n % 5:
			p += 1
		if p > longest:
			longest = p
			num = n
	return num

print(reciprocalCycles())
