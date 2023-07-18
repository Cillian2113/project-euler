def powerfulDigitCounts():
    counter = 0
    #all one digit integers: 9
    #no 2 digit numbers as always too many digits
    for x in range(1,10):
        n = 1
        while len(str(x**n)) == n:
            n+=1
            counter+=1
    return counter



print(powerfulDigitCounts())