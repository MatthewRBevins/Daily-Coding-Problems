matrix = [
    ["B", "B", "W"],
    ["W", "W", "W"],
    ["W", "W", "W"],
    ["B", "B", "B"]
]

pos = [2,2]

fixedPos = [pos[0]-1, pos[1]-1]
char = matrix[fixedPos[0]][fixedPos[1]]
c = "G"
if fixedPos[1]-1 > -1:
    if matrix[fixedPos[0]][fixedPos[1]-1] == char:
        matrix[fixedPos[0]][fixedPos[1] - 1] = c
if fixedPos[1]+1 < len(matrix[0]):
    if matrix[fixedPos[0]][fixedPos[1]+1] == char:
        matrix[fixedPos[0]][fixedPos[1] + 1] = c
if fixedPos[0]-1 > -1:
    if matrix[fixedPos[0] - 1][fixedPos[1]] == char:
        matrix[fixedPos[0] - 1][fixedPos[1]] = c
    if fixedPos[1]-1 > -1:
        if matrix[fixedPos[0]-1][fixedPos[1]-1] == char:
            matrix[fixedPos[0] - 1][fixedPos[1] - 1] = c
    if fixedPos[1]+1 < len(matrix[0]):
        if matrix[fixedPos[0]-1][fixedPos[1]+1] == char:
            matrix[fixedPos[0] - 1][fixedPos[1] + 1] = c
if fixedPos[0]+1 < len(matrix):
    if matrix[fixedPos[0] + 1][fixedPos[1]] == char:
        matrix[fixedPos[0] + 1][fixedPos[1]] = c
    if fixedPos[1] - 1 > -1:
        if matrix[fixedPos[0] + 1][fixedPos[1]-1] == char:
            matrix[fixedPos[0] + 1][fixedPos[1]-1] = c
    if fixedPos[1] + 1 < len(matrix[0]):
        if matrix[fixedPos[0] + 1][fixedPos[1]+1] == char:
            matrix[fixedPos[0] + 1][fixedPos[1]+1] = c
matrix[fixedPos[0]][fixedPos[1]] = c
print(matrix)