matrix = [[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]

i1 = 1
j1 = 1
i2 = 3
j2 = 3
matches = 0
for i in range(len(matrix)):
 for j in range(len(matrix[i])):
  if (i <= i1 or j <= j1) and matrix[i][j] < matrix[i1][j1]:
   matches += 1
  if (i >= i2 or j >= j2) and matrix[i][j] > matrix[i2][j2]:
   matches += 1
print(matches)