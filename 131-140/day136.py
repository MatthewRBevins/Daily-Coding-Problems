matrix = [
    [1,0,0,0],
    [1,0,1,1],
    [1,0,1,1],
    [0,1,0,0]
]


def checkRectangleSize(matrix, r, c):
    size = 0
    minVertSize = -1
    for i in range(r, len(matrix)):
        curVertSize = 0
        if matrix[i][c] == 1:
            size += 1
            for j in range(c, len(matrix[0])):
                if matrix[i][j] == 1:
                    curVertSize += 1
                else:
                    break
            if minVertSize == -1:
                minVertSize = curVertSize
            elif curVertSize < minVertSize:
                minVertSize = curVertSize
        else:
            break
    return size * minVertSize

arr = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        s = checkRectangleSize(matrix, i, j)
        arr.append(s)
print(max(arr))