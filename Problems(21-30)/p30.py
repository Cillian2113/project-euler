def digitFifthPowers():
	total = 0
	for number in range(2,999999):
		numsum = 0
		for x in str(number):
			numsum += int(x)**5
		if numsum == number:
			total += number
			print(number)
	return total

print(digitFifthPowers())
