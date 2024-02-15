matrix = [
    [1,0,0,0],
    [1,0,1,1],
    [1,0,1,1],
    [0,1,0,0]
]
def checkRectangleSize(matrix, r, c):
    size = 0
    minVertSize = -1
    for i in range(r,len(matrix)):
        curVertSize = 1
        if matrix[i][c] == 1:
            size += 1
        for j in range(c, len(matrix[0])):
            if matrix[i][j] == 1:
                curVertSize += 1
            if minVertSize == -1:
                minVertSize = curVertSize
            elif curVertSize < minVertSize:
                minVertSize = curVertSize
    return size * minVertSize

print(checkRectangleSize(matrix, 1, 2))