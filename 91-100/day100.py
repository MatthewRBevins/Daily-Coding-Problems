path = [[0,0],[1,1],[1,2]]

def findPath(pos1, pos2):
    moves = 0
    while pos1 != pos2:
        if pos1[0] < pos2[0]:
            pos1[0] += 1
        elif pos1[0] > pos2[0]:
            pos1[0] -= 1
        if pos1[1] < pos2[1]:
            pos1[1] += 1
        elif pos1[1] > pos2[1]:
            pos1[1] -= 1
        moves += 1
    return moves
totalMoves = 0
for i in range(len(path)-1):
    totalMoves += findPath(path[i], path[i+1])
print(totalMoves)