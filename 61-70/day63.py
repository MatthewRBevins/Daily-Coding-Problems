matrix = [['F','A','C','I'],['O','B','Q','P'],['A','N','O','B'],['M','A','S','S']]
word = "FOAM"

def rotate(matrix):
    final = []
    for i in range(len(matrix)):
        final.append([])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            final[j].append(matrix[i][j])
    return final

def checkForWord(matrix, word):
    r = rotate(matrix)
    for i in matrix:
        w = ''.join(i)
        if w == word:
            return True
    for i in r:
        w = ''.join(i)
        if w == word:
            return True
    return False

print(checkForWord(matrix, word))
