stock = [9, 11, 8, 5, 7, 10]
best = 0
for i,j in enumerate(stock):
    price = j
    bestPrice = 0
    for k in range(j,len(stock)):
        if stock[k]-price > bestPrice:
            bestPrice = stock[k]-price
    if bestPrice > best:
        best = bestPrice
print(best)
