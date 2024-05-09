words = ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']
def removeStartingChar(arr):
    for i in range(len(arr)):
        arr[i] = arr[i][1:]
    return arr
def conflicts(arrr1, arrr2):
    arr1 = arrr1.copy()
    arr2 = arrr2.copy()
    i = 0
    while i < len(arr1):
        if not arr1[i] in arr2:
            del arr1[i]
            i -= 1
        i += 1
    i = 0
    while i < len(arr2):
        if not arr2[i] in arr1:
            del arr2[i]
            i -= 1
        i += 1
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return True
    return False
done = []
def sortWords(arr, l):
    curChar = ''
    curArr = []
    comparisons = []
    sorted = []
    for i in arr:
        if curChar != '' and i[0] != curChar:
            verifiedArr = True
            rem = removeStartingChar(curArr)
            if len(rem) < 2:
                verifiedArr = False
            if verifiedArr and not rem in done:
                done.append(rem)
                comparisons.append(sortWords(rem, 1))
            curArr = [i]
        else:
            curArr.append(i)
        curChar = i[0]
        if not i[0] in sorted:
            sorted.append(i[0])
    verifiedArr = True
    rem = removeStartingChar(curArr)
    if len(rem) < 2:
        verifiedArr = False
    if verifiedArr and not rem in done:
        done.append(rem)
        comparisons.append(sortWords(rem, 1))
    toInsert = 0
    if l or not l:
        for i in comparisons:
            if not conflicts(sorted, i):
                for j in i:
                    if j in sorted:
                        toInsert = sorted.index(j)
                    else:
                        sorted.insert(toInsert+1, j)
    return sorted
print(sortWords(words, 0))