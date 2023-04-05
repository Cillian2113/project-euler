import csv
import string

def nameScores():
	with open('p022_names.txt', newline='') as f:
		reader = csv.reader(f)
		data = list(reader)[0]
	sorted_data = sorted(data)

	alphabet = {}
	i = 1
	for letter in string.ascii_uppercase:
		alphabet[letter] = i
		i += 1

	sum = 0
	nth_word = 0
	for word in sorted_data:
		nth_word += 1
		temp = 0
		for letter in word:
			temp += alphabet[letter]
		sum += temp*(nth_word)
	return sum

print(nameScores())
