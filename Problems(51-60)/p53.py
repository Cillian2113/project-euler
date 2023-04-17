from math import comb
def combinatoricsSelections():
	total = 0
	for n in range(1,101):
		for r in range(n):
			if comb(n,r) > 1000000:
				total += 1
	return total

print(combinatoricsSelections())
