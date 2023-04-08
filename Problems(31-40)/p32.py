from math import sqrt
def pandigitalNumbers():
	total = 0
	#product has to be four digits for there to be 9 digits in the equation
	for product in range (1000,9999):
		if pandigital(product):
			total += product
	return total

def pandigital(product):
	for divisor in range(2,int(sqrt(product))):
		if product % divisor == 0:
			stringnumbers = str(divisor)+str(product/divisor)+str(product)
			#line below could be written nicer
			if all([str(1) in stringnumbers,str(2) in stringnumbers,str(3) in stringnumbers,str(4) in stringnumbers,str(5) in stringnumbers,str(6) in stringnumbers,str(7) in stringnumbers,str(8) in stringnumbers,str(9) in stringnumbers]):
				return True
	return False

print(pandigitalNumbers())
