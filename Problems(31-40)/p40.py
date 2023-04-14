def champernownesConstant():
	number = str("0.")
	value = 1
	for x in range(1,1000000):
		number+=str(x)
	value*=int(number[2])*int(number[11])*int(number[101])*int(number[1001])*int(number[10001])*int(number[100001])*int(number[1000001])
	return value

print(champernownesConstant())
