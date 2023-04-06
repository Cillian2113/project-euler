from itertools import permutations
def lexicographicPermutations():
	comb = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
	array = [x for x in comb]
	return array[999999]

print(lexicographicPermutations())
