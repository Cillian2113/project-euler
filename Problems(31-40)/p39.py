from math import gcd
def integerRightTriangles():
	#a=m^2-n^2, b=2mn, c=m^2+n^2
	triples = []
	n,m = 1,2
	while m*m+1<1000:
		if n>=m: n,m = m%2,m+1
		z = m*m+n*n
		if z >= 1000: n=m;continue
		if gcd(n,m) == 1:
			triples.append((m*m-n*n,2*m*n,z))
		n += 1

	triples = [x for x in triples if sum(x) <= 1000]
	triples = [sum(x) for x in triples]
	return max(set(triples), key=triples.count)

print(integerRightTriangles())
