matrix = [
    [1,0,0,0,0],
    [0,0,1,1,0],
    [0,1,1,0,0],
    [0,0,0,0,0],
    [1,1,0,0,1],
    [1,1,0,0,1]
]

islands = []
used = []

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == 1:
            isIsland = True
            if r-1 > -1:
                if c-1 > -1:
                    if [r-1,c-1] in used:
                        isIsland = False
                if c+1 < len(matrix[0]):
                    if [r-1,c+1] in used:
                        isIsland = False
                if [r-1,c] in used:
                    isIsland = False
            if r+1 < len(matrix):
                if c-1 > -1:
                    if [r+1,c-1] in used:
                        isIsland = False
                if c+1 < len(matrix[0]):
                    if [r+1,c+1] in used:
                        isIsland = False
                if [r+1,c] in used:
                    isIsland = False
            if c+1 < len(matrix[0]):
                if [r,c+1] in used:
                    isIsland = False
            if c-1 > -1:
                if [r,c-1] in used:
                    isIsland = False
            if isIsland:
                islands.append([r,c])
            used.append([r,c])
print(islands)