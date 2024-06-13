adj = dict({
    1: [2, 4, 5],
    2: [1, 4, 5, 3, 6],
    3: [2, 5, 6],
    4: [1, 2, 5, 7, 8],
    5: [1, 2, 3, 4, 6, 7, 8, 9],
    6: [2, 3, 5, 8, 9],
    7: [4, 5, 8],
    8: [7, 4, 5, 6, 9],
    9: [8, 5, 6]
})
def checkMatching(num1, num2):
    matches = []
    for i in adj[num1]:
        if i in adj[num2]:
            matches.append(i)
    return matches
def hasMatch(arr1, arr2):
    for i in arr1:
        if i in arr2:
            return True
    return False
def checkValid(seq):
    for i in range(1, len(seq)):
        if (seq[i] in adj[seq[i-1]] or hasMatch(seq[:i], checkMatching(seq[i], seq[i-1]))) and not seq[i] in seq[:i] and not seq[i] in seq[i+1:]:
            pass
        else:
            return False
    return True
import copy
valids = 0
def findValids(N, seq):
    global valids
    if len(seq) >= N:
        if checkValid(seq):
            valids += 1
        return
    for i in range(1,10):
        s = copy.deepcopy(seq)
        s.append(i)
        findValids(N, s)
findValids(3, [])
print(valids)