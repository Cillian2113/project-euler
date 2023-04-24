def lychrelNumbers():
	nums = 0
	for n in range(1,10000):
		if islychrel(n):
			nums += 1
	return nums

def islychrel(n):
	for _ in range(50):
		n = n + int(str(n)[::-1])
		if str(n) == str(n)[::-1]:
			return False
	return True

print(lychrelNumbers())
