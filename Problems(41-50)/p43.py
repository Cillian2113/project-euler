from itertools import permutations
def subStringDivisibility():
	perms = permutations("0123456789")
	perms = [int(''.join(perm)) for perm in perms if int(perm[3]) % 2 == 0 and int(perm[2]+perm[3]+perm[4]) % 3 == 0 and int(perm[5]) % 5 == 0 and int(perm[4]+perm[5]+perm[6]) % 7 == 0 and int(perm[5]+perm[6]+perm[7]) % 11 == 0 and int(perm[6]+perm[7]+perm[8]) % 13 == 0 and int(perm[7]+perm[8]+perm[9]) % 17 == 0]
	return sum(perms)

print(subStringDivisibility())
