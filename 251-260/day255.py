graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
matrix = []
for i in range(len(graph)):
    a = []
    for j in range(len(graph)):
        a.append(0)
    matrix.append(a)
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if j in graph[i]:
            matrix[i][j] = 1
print(matrix)