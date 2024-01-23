def findCoins(matrix, r, c, coins):
    bestOption = 0
    coins += matrix[r][c]
    if r == len(matrix)-1 and c == len(matrix[0])-1:
        return coins
    if r < len(matrix)-1 and findCoins(matrix, r+1, c, coins) > bestOption:
        bestOption = findCoins(matrix, r+1, c, coins)
    if c < len(matrix[0])-1 and findCoins(matrix, r, c+1, coins) > bestOption:
        bestOption = findCoins(matrix, r, c+1, coins)
    return bestOption
matrix = [
    [0,3,1,1],
    [2,0,0,4],
    [1,5,3,1]
]
print(findCoins(matrix, 0, 0, 0))