def SquareDigitChains():
    Count89 = 0
    Goesto1 = [1]
    Goesto89 = [89]
    #Because the largest sum of squares of digits for numbers to 10,000,000 is 567, we can just calculate wether the first 567 numbers go to 1 or 89
    for num in range(1,568):
        originalnum = num
        print(num)
        while True:
            if num == 1:
                Goesto1.append(originalnum)
                break
            if num == 89:
                Goesto89.append(originalnum)
                break
            else:
                stringnumber = str(num)
                num = 0
                for digit in stringnumber:  
                    num += int(digit)**2
    for num in range(1,10000000):
        stringnumber = str(num)
        num = 0
        for digit in stringnumber:  
                num += int(digit)**2
        if num in Goesto89:
            Count89 += 1
    return Count89


print(SquareDigitChains())
