arr = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
arr2 = [
    [True,True,True,True],
    [True,True,True,True],
    [True,True,True,True]
]
def checkNeighbor(r, c, v, arr2):
    poss = []
    # left
    if c-1 > -1 and arr[r][c-1] == v and arr2[r][c-1]:
        poss.append([r,c-1])
    # right
    if c+1 < len(arr[0]) and arr[r][c+1] == v and arr2[r][c+1]:
        poss.append([r,c+1])
    # top
    if r-1 > -1 and arr[r-1][c] == v and arr2[r-1][c]:
        poss.append([r-1,c])
    # bottom
    if r+1 < len(arr) and arr[r+1][c] == v and arr2[r+1][c]:
        poss.append([r+1,c])
    return poss
def checkForPos(v):
    poss = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == v:
                poss.append([i,j])
    return poss
string = "ABCCED"
def doIt(level, string, pos, arr2):
    if level == 0:
        for i in checkForPos(string[0]):
            a = doIt(level+1, string, i, arr2)
            if a:
                return True
        return False
    else:
        arr2[pos[0]][pos[1]] = False
        poss = checkNeighbor(pos[0], pos[1], string[level], arr2)
        if len(poss) == 0:
            return False
        else:
            for i in poss:
                if level == len(string)-1:
                    return True
                else:
                    a = doIt(level+1, string, i, arr2)
                    if a == True:
                        return True
            return False
print(doIt(0, string, None, arr2))