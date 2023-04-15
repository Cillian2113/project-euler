def selfPowers():
	series = 0
	for n in range(1,1001):
		series += n**n
	return str(series)[-10:]

print(selfPowers())
