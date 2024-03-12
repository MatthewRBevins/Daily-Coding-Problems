matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
newMatrix = [

]
for j in range(len(matrix)):
    newMatrix.append([])
    for i in range(len(matrix)-1,-1,-1):
        newMatrix[j].append(matrix[i][j])
print(newMatrix)