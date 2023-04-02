def numberLetterCount():
	numbers = {
		1000: 11,
		900: 11,
		800: 12,
		700: 12,
		600: 10,
		500: 11,
		400: 11,
		300: 12,
		200: 10,
		100: 10,
		90: 6,
		80: 6,
		70: 7,
		60: 5,
		50: 5,
		40: 5,
		30: 6,
		20: 6,
		19: 8,
		18: 8,
		17: 9,
		16: 7,
		15: 7,
		14: 8,
		13: 8,
		12: 6,
		11: 6,
		10: 3,
		9: 4,
		8: 5,
		7: 5,
		6: 3,
		5: 4,
		4: 4,
		3: 5,
		2: 3,
		1: 3,
		0: 0,
	}
	sum = 0
	for number in range(1,1001):
		if number in numbers:
			sum+=numbers[number]
			continue
		if number > 99:
			hundreds = int(number/100)
			sum += numbers[hundreds*100]+3
			number -= hundreds*100
		if number > 20:
			tens = int(number/10)
			sum+= numbers[tens*10]
			number -= tens*10
		sum+= numbers[number]
	return sum




print(numberLetterCount())
