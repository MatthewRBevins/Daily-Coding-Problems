def calcSums(powers, curSum, possSums):
    if len(curSum) == len(powers):
        return [curSum]
    for i in range(-1, len(powers)):
        c = curSum.copy()
        if i == -1:
            c.append(0)
            for i in calcSums(powers, c, possSums):
                possSums.append(i)
        elif not powers[i] in curSum:
            c.append(powers[i])
            for i in calcSums(powers, c, possSums):
                possSums.append(i)
    return possSums

powers = [1, 7, 49]
print(calcSums(powers, [], []))