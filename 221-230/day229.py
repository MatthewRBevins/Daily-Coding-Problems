snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
def findLowest(space, turn, ending):
    bestTurns = 100
    if space >= 100 or turn >= ending:
        return turn
    for i in range(6):
        s = 0
        s += space
        s += i
        if s in snakes:
            s = snakes[s]
        elif s in ladders:
            s = ladders[s]
        t = findLowest(s, turn+1, ending)
        if t < bestTurns:
            bestTurns = t
    return bestTurns
e = 0
f = findLowest(0, 0, e)
while True:
    e += 1
    f = findLowest(0, 0, e)
    if f != e:
        break
print(f)