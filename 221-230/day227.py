board = [
    ['a','b','c','d'],
    ['e','f','g','h'],
    ['i','j','k','l'],
    ['m','n','o','p']
]
dictionary = ['fglp', 'ijgd', 'mnkh', 'zzfa']
def posToWord(board, poses):
    word = ""
    for i in poses:
        word += board[i[0]][i[1]]
    return word
def maxlen(arr):
    b = 0
    for i in arr:
        if len(i) > b:
            b = len(i)
    return b
m = maxlen(dictionary)
def adjacent(pos1, pos2):
    ads = [
        [pos1[0]+1, pos1[1]],
        [pos1[0]-1, pos1[1]],
        [pos1[0], pos1[1]+1],
        [pos1[0], pos1[1]-1],
        [pos1[0]+1, pos1[1]+1],
        [pos1[0]-1, pos1[1]-1],
        [pos1[0]+1, pos1[1]-1],
        [pos1[0]-1, pos1[1]+1]
    ]
    return pos2 in ads
def solve(board, currentPoses, wordsList, level):
    if posToWord(board, currentPoses) in dictionary:
        wordsList.append(posToWord(board, currentPoses))
    if len(currentPoses) == m:
        return wordsList
    for i in range(len(board)):
        for j in range(len(board)):
            c = currentPoses.copy()
            if (not [i, j] in currentPoses) and (len(c) == 0 or adjacent([i, j], c[len(c)-1])):
                c.append([i, j])
                l = 0
                l += level
                s = solve(board, c, wordsList, l+1)
                for k in range(len(s)):
                    if not s[k] in wordsList:
                        wordsList.append(s[k])
            del c[len(c)-1]
    return wordsList

print(solve(board, [], [], 0))