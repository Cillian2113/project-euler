from itertools import permutations
def permutatedMultiples():
	for y in [1,10,100,1000]: #iterate through each digit range
		for x in range(1000*y,1600*y): #1600 as greater will have another digit when multiplied by 6
			if has_doubles(x):
				continue
			if checkmultiple(x):
				return x

def checkmultiple(n):
	perms = [int(''.join(perm)) for perm in permutations(str(n))]
	if n*2 not in perms:
		return False
	if n*3 not in perms:
		return False
	if n*4 not in perms:
		return False
	if n*5 not in perms:
		return False
	if n*6 not in perms:
		return False
	return True

def has_doubles(n):
	return len(set(str(n))) < len(str(n))

print(permutatedMultiples())
