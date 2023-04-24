def powerfulDigitSum():
	max = 0
	for a in range(1,100):
		for b in range(1,100):
			if sumDigits(a**b) > max:
				max = sumDigits(a**b)
	return max


def sumDigits(n):
	r = 0
	while n:
		r, n = r + n % 10, n // 10
	return r

print(powerfulDigitSum())
