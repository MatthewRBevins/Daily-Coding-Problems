import copy
N = [5, 1, 2, 7, 3, 4]
k = 3
def findParts(N, k, curPart, curIndex, parts):
    m = 1000
    if len(parts) == k:
        maxsum = 0
        for i in parts:
            if sum(i) > maxsum:
                maxsum = sum(i)
        return maxsum
    if len(parts) == k-1:
        c = copy.deepcopy(parts)
        c.append(N[curIndex:])
        s = findParts(N, k, curPart + 1, len(N), c)
        if s < m:
            m = s
    else:
        totalPartsLen = 0
        for i in parts:
            totalPartsLen += len(parts)
        for i in range(1,len(N) - totalPartsLen):
            c = copy.deepcopy(parts)
            c.append(N[curIndex:curIndex+i])
            s = findParts(N, k, curPart+1, curIndex+i, c)
            if s < m:
                m = s
    return m
print(findParts(N, k, 0, 0, []))