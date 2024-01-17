S = [12,1,61,5,9,2]
k = 26
def findSum(S, k, sol, indices, level):
    thisindices = indices.copy()
    thissol = sol.copy()
    if sum(thissol) > k:
        return False
    for j,i in enumerate(S):
        if not j in thisindices:
            thissol.append(i)
            thisindices.append(j)
            if sum(thissol) == k:
                return thissol
            else:
                s = findSum(S, k, thissol, thisindices, level+1)
                if s != False:
                    return s
                else:
                    thissol.pop()
                thisindices = thisindices[0:len(thisindices)-1]
    return False
print(findSum(S, k, [], [], 0))
