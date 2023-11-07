#0,0,0,0,0
#0,0,0,0,0
#0,0,0,0,0
#O,0,0,0,0
#0,0,0,0,0

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
    # Diagonals
    for i in range(2*(len(b)-2)+1):
        ii = i + 1
        x = 0
        y = 0
        totalQueens = 0
        if ii >= len(b):
            x = len(b)-1
            y = ii-(len(b)-1)
        else:
            x = ii
            y = 0
        while x >= 0 and y < len(b):
            totalQueens += b[y][x]
            if totalQueens > 1:
                return True
            x -= 1
            y += 1

    for i in range(2*(len(b)-2)+1):
        ii = i + 1
        x = 0
        y = 0
        totalQueens = 0
        if ii >= len(b):
            x = ii-len(b)+1
            y = 0
        else:
            x = 0
            y = len(b)-ii-1
        while x < len(b) and y < len(b):
            totalQueens += b[y][x]
            if totalQueens > 1:
                return True
            x += 1
            y += 1
    return False

def genBoard(n):
    b = []
    for i in range(n):
        b.append([])
        for j in range(n):
            b[i].append(0)
    return b

def findPossibilities(b, num, level):
    bb = b.copy()
    if isThreatening(bb):
        return num
    else:
        num += 1
    for i in range(len(bb)):
        for j in range(len(bb)):
            if bb[i][j] != 1:
                bb[i][j] = 1
                num = findPossibilities(bb, num, level+1)
                bb[i][j] = 0
    return num

def doIt(n):
    a = genBoard(n)
    return findPossibilities(a, 0, 0)
print(doIt(3))
