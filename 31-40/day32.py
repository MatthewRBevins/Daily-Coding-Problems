# USD, CAN, MEX, GBP
rates = [[1, 2, 4, 0.5], [0.5, 1, 2, 0.25], [0.25, 0.5, 1, 0.125], [2, 4, 8, 1]]

def trade(amount, start, convertTo):
    return rates[start][convertTo] * amount

def arbitrage(currency, amount, level, initVal, initCur):
    if level == 5:
        finalTrade = trade(amount, currency, initCur)
        if finalTrade > initVal:
            return True
        else:
            return False
    isArbitrage = False
    for i in range(len(rates)):
        if arbitrage(i, trade(amount, currency, i), level+1, initVal, initCur) == True:
            isArbitrage = True
            break
    return isArbitrage

print(arbitrage(0, 100, 0, 100, 0))
