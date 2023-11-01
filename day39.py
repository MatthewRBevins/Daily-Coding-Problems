board = [
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,1,1,1,0],
[0,1,1,1,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]
]

def calcNeighbors(r, c):
    neighbors = 0
    if r != 0 and board[r-1][c] == 1:
        neighbors += 1
    if r < len(board)-1 and board[r+1][c] == 1:
        neighbors += 1
    if c != 0 and board[r][c-1] == 1:
        neighbors += 1
    if c < len(board[c])-1 and board[r][c+1] == 1:
        neighbors += 1
    return neighbors

while True:
    print(board)
    for r in range(len(board)):
        for c in range(len(board[r])):
            n = calcNeighbors(r, c)
            if board[r][c] == 1 and n == 0 or n == 1:
                board[r][c] = 0
            elif board[r][c] == 1 and n > 3:
                board[r][c] = 0
            elif board[r][c] == 0 and n == 3:
                board[r][c] = 1
    input("")
