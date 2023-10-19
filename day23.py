board = [[False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False],
         [False,False,False,False,False,False,False,False,False,False,False,False]]
# first number is row number
start = [3,0]
end = [0,0]
def genPossibleMoves(pos, prevMoves):
    moves = []
    # up
    if pos[0]-1 > -1:
        moves.append([pos[0]-1, pos[1]])
    # down
    if pos[0]+1 < len(board):
        moves.append([pos[0]+1, pos[1]])
    # right
    if pos[1]+1 < len(board[0]):
        moves.append([pos[0], pos[1]+1])
    # left
    if pos[1]-1 > -1:
        moves.append([pos[0], pos[1]-1])
    goodMoves = []
    for i in range(len(moves)):
        good = True
        for j in prevMoves:
            if (moves[i][0] == j[0] and moves[i][1] == j[1]) or board[moves[i][0]][moves[i][1]]:
                good = False
                break
        if good:
            goodMoves.append(moves[i])
    return goodMoves

def move(pos, moves, prevMoves):
    prevMoves.append(pos)
    possible = genPossibleMoves(pos, prevMoves)
    if pos[0] == end[0] and pos[1] == end[1]:
        return [prevMoves, moves]
    if len(possible) == 0:
        return None
    bestMove = [[],len(board)*len(board[0])]
    for i in possible:
        cMove = move(i, moves+1, prevMoves[0:moves])
        if cMove is not None and cMove[1] < bestMove[1]:
            bestMove = cMove
    return bestMove

nav = move(start, 0, [])
if len(nav[0]) == 0 and nav[1] > 0:
    print("IMPOSSIBLE")
else:
    print("You can complete the maze in " + str(nav[1]) + " steps by using the path " + str(nav[0]))
