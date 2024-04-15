tri = [[1], [2,3], [1,5,1]]
def calcMax(row, col, sum):
    print(str(row) + " - " + str(sum))
    if row == len(tri)-1:
        return sum
    bestSum = 0
    # left
    s = 0
    s += sum
    s += tri[row+1][col]
    s = calcMax(row+1, col, s)
    if s > bestSum:
        bestSum = s
    # right
    s = 0
    s += sum
    s += tri[row+1][col+1]
    s = calcMax(row+1, col+1, s)
    if s > bestSum:
        bestSum = s
    return bestSum
print(calcMax(0,0,1))