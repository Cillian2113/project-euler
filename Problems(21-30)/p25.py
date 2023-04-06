def fibonacciSequence():
	sequence = [1,1]
	i = 1
	while sequence[i] < 10**999:
		i+=1
		sequence.append(sequence[i-1]+sequence[i-2])
	return len(sequence)

print(fibonacciSequence())
