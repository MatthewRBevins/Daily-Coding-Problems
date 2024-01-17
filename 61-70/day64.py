board = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

def genMoves(board, x, y):
    moves = []
    if x + 1 < len(board):
        if y + 2 < len(board):
            moves.append([x+1,y+2])
        if y - 2 > -1:
            moves.append([x+1,y-2])
    if x - 1 > -1:
        if y + 2 < len(board):
            moves.append([x-1,y+2])
        if y - 2 > -1:
            moves.append([x-1,y-2])
    if x + 2 < len(board):
        if y + 1 < len(board):
            moves.append([x+2,y+1])
        if y - 1 > -1:
            moves.append([x+2,y-1])
    if x - 2 > -1:
        if y + 1 < len(board):
            moves.append([x-2,y+1])
        if y - 1 > -1:
            moves.append([x-2,y-1])
    return moves

def findTours(path, board, tours):
    if len(path) == len(board)*len(board):
        tours += 1
        return tours
    moves = genMoves(board, path[len(path)-1][0], path[len(path)-1][1])
    validMoves = []
    for move in moves:
        if not move in path:
            validMoves.append(move)
    if len(validMoves) == 0:
        #print('f')
        return tours
    for i in validMoves:
        newPath = path.copy()
        newPath.append(i)
        tours += findTours(newPath, board, tours)
    return tours

for x in range(len(board)):
    for y in range(len(board)):
        print('***')
        print(findTours([[x,y]], board, 0))