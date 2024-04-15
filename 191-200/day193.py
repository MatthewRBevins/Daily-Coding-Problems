prices = [1, 3, 2, 8, 4, 10]
fee = 2
def checkPoss(money, step, bought):
    if step == len(prices)-1:
        return money
    best = 0
    for i in range(3):
        # buy
        if i == 0 and not bought:
            money -= prices[step]
            bought = True
        # sell
        elif i == 1 and bought:
            money += prices[step]
            bought = False
        # hold
        elif i == 2:
            pass
        n = checkPoss(money, step+1, bought)
        if n > best:
            best = n
    return best
print(checkPoss(0, 0, False))