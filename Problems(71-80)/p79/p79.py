import itertools

with open('0079_keylog.txt') as f:
	randomchars = f.readlines()
	
#I worked out only the numbers [0,1,2,3,6,7,8,9] exist in the verification entries

for n in range(len(randomchars)):
	randomchars[n] = randomchars[n].replace("\n",'')

numberset = ['0','1','2','3','6','7','8','9']
combinations = list(itertools.permutations(numberset))
combinations = [''.join(combination) for combination in combinations]

for n in range(len(combinations)):
	test = True
	for m in range(len(randomchars)):
		c1 = combinations[n].find(randomchars[m][0])
		c2 = combinations[n].find(randomchars[m][1])
		c3 = combinations[n].find(randomchars[m][2])
		if not(c3>c2>c1):
			test = False
			break
	if test:
		print(combinations[n])
