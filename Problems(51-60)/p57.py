def squareRootConvergents():
    top = 3
    bottom = 2
    counter = 0
    for _ in range(999):
        temptop = 2*bottom+top
        tempbottom = bottom+top
        top = temptop
        bottom = tempbottom
        if len(str(top)) > len(str(bottom)):
            counter += 1
    return counter

print(squareRootConvergents())