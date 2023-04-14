alphabet = {
	"A":1,
	"B":2,
	"C":3,
	"D":4,
	"E":5,
	"F":6,
	"G":7,
	"H":8,
	"I":9,
	"J":10,
	"K":11,
	"L":12,
	"M":13,
	"N":14,
	"O":15,
	"P":16,
	"Q":17,
	"R":18,
	"S":19,
	"T":20,
	"U":21,
	"V":22,
	"W":23,
	"X":24,
	"Y":25,
	"Z":26,
}
def codedTriangleNumbers():
	triangles = triangleNumbers(200)
	with open('p042_words.txt') as f:
		words = f.readlines()
		words = words[0].replace('"','').split(",")

	count = 0

	for word in words:
		total = 0
		for letter in word:
			total += alphabet[letter]
		if total in triangles:
			count += 1

	return count

def triangleNumbers(limit):
	triangles = []
	n = 1
	while n <= limit:
		triangles.append(int(0.5*n*(n+1)))
		n += 1
	return triangles

print(codedTriangleNumbers())
