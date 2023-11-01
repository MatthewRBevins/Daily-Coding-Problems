def isThreatening(b):
    for i in range(len(b)):
        # Check whether rows have queens
        if sum(b[i]) > 1:
            return True
        colSum = 0
        for j in range(len(b)):
            colSum += b[j][i]
        if colSum > 1:
            return True
    if b[0][0] + b[1][1] + b[2][2] > 1:
        return True
    if b[0][2] + b[1][1] + b[2][0] > 1:
        return True
    if b[0][1]+b[1][0] > 1:
        return True
    if b[0][1] + b[1][2] > 1:
        return True
    if b[1][0] + b[2][1] > 1:
        return True
    if b[1][2] + b[2][1] > 1:
        return True
    return False

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
poss = []
def findPossibilities(b, num):
    print(b)
    if isThreatening(b):
        return num
    elif not b in poss:
        poss.append(b)
        num += 1
    for i in range(len(b)):
        for j in range(len(b)):
            if b[i][j] != 1:
                b[i][j] = 1
                num = findPossibilities(b, num)
    return num
print(findPossibilities(board, 0))
        
