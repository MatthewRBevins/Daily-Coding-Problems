matrix = [
    [".", ".", ".", "K", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", "B", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "P", "."],
    [".", ".", ".", ".", ".", ".", ".", "R"],
    [".", ".", "N", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "Q", ".", "."]
]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "K":
            # pawn
            if i + 1 < 8 and j - 1 > 0 and matrix[i+1][j-1] == "P":
                print("CHECK | PAWN")
            if i + 1 < 8 and j + 1 < 8 and matrix[i+1][j+1] == "P":
                print("CHECK | PAWN")
            # knight
            if i + 2 < 8 and j + 1 < 8 and matrix[i+2][j+1] == "N":
                print("CHECK | KNIGHT")
            if i + 2 < 8 and j - 1 > 0 and matrix[i+2][j-1] == "N":
                print("CHECK | KNIGHT")
            if i - 2 > 0 and j + 1 < 8 and matrix[i-2][j+1] == "N":
                print("CHECK | KNIGHT")
            if i - 2 > 0 and j - 1 > 0 and matrix[i-2][j-1] == "N":
                print("CHECK | KNIGHT")
            if i + 1 < 8 and j + 2 < 8 and matrix[i+1][j+2] == "N":
                print("CHECK | KNIGHT")
            if i - 1 > 0 and j + 2 < 8 and matrix[i-1][j+2] == "N":
                print("CHECK | KNIGHT")
            if i + 1 < 8 and j - 2 > 0 and matrix[i+1][j-2] == "N":
                print("CHECK | KNIGHT")
            if i - 1 > 0 and j - 2 > 0 and matrix[i-1][j-2] == "N":
                print("CHECK | KNIGHT")
            # bishop/queen
            ii = 0 + i
            jj = 0 + j
            for k in range(8):
                ii -= 1
                jj -= 1
                if ii < 0 or ii > len(matrix)-1 or jj < 0 or jj > len(matrix)-1:
                    break
                if matrix[ii][jj] == "Q" or matrix[ii][jj] == "B":
                    print("CHECK | QUEEN OR BISHOP")
            ii = 0 + i
            jj = 0 + j
            for k in range(8):
                ii += 1
                jj += 1
                if ii < 0 or ii > len(matrix)-1 or jj < 0 or jj > len(matrix)-1:
                    break
                if matrix[ii][jj] == "Q" or matrix[ii][jj] == "B":
                    print("CHECK | QUEEN OR BISHOP")
            ii = 0 + i
            jj = 0 + j
            for k in range(8):
                ii += 1
                jj -= 1
                if ii < 0 or ii > len(matrix)-1 or jj < 0 or jj > len(matrix)-1:
                    break
                if matrix[ii][jj] == "Q" or matrix[ii][jj] == "B":
                    print("CHECK | QUEEN OR BISHOP")
            ii = 0 + i
            jj = 0 + j
            for k in range(8):
                ii -= 1
                jj += 1
                if ii < 0 or ii > len(matrix)-1 or jj < 0 or jj > len(matrix)-1:
                    break
                if matrix[ii][jj] == "Q" or matrix[ii][jj] == "B":
                    print("CHECK | QUEEN OR BISHOP")
            # rook/queen
            ii = 0 + i
            jj = 0 + j
            for k in range(8):
                ii -= 1
                if ii < 0 or ii > len(matrix)-1 or jj < 0 or jj > len(matrix)-1:
                    break
                if matrix[ii][jj] == "Q" or matrix[ii][jj] == "B":
                    print("CHECK | QUEEN OR ROOK")
            ii = 0 + i
            jj = 0 + j
            for k in range(8):
                ii += 1
                if ii < 0 or ii > len(matrix)-1 or jj < 0 or jj > len(matrix)-1:
                    break
                if matrix[ii][jj] == "Q" or matrix[ii][jj] == "B":
                    print("CHECK | QUEEN OR ROOK")
            ii = 0 + i
            jj = 0 + j
            for k in range(8):
                jj -= 1
                if ii < 0 or ii > len(matrix)-1 or jj < 0 or jj > len(matrix)-1:
                    break
                if matrix[ii][jj] == "Q" or matrix[ii][jj] == "B":
                    print("CHECK | QUEEN OR ROOK")
            ii = 0 + i
            jj = 0 + j
            for k in range(8):
                jj += 1
                if ii < 0 or ii > len(matrix)-1 or jj < 0 or jj > len(matrix)-1:
                    break
                if matrix[ii][jj] == "Q" or matrix[ii][jj] == "B":
                    print("CHECK | QUEEN OR ROOK")