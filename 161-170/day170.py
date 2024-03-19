start = "dog"
end = "cat"
dict = ["dot", "dop", "dat", "cat"]
def checkOneOff(word1, word2):
    used = False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            if not used:
                used = True
            else:
                return False
    return True
def findPath(path, dict):
    if path[len(path)-1] == end:
        return path
    for i in range(len(dict)):
        if checkOneOff(path[len(path)-1], dict[i]):
            newPath = path.copy()
            newPath.append(dict[i])
            newDict = dict.copy()
            del newDict[i]
            nextIter = findPath(newPath, newDict)
            if nextIter != False:
                return nextIter
    return False
print(findPath([start], dict))