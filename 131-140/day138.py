n = 16
coinVals = [25, 10, 5, 1]
coinsToUse = []
while n not in coinVals:
    for i in coinVals:
        if n > i:
            n -= i
            coinsToUse.append(i)
            break
coinsToUse.append(n)
print(coinsToUse)