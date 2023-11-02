initSet = [1,2,3]
# []
# [1],[2],[3],[4],[5]
# [1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]
# [1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]
#, [1,2,3,4],[1,2,3,5],[1,2,4,5],[1,3,4,5],[2,3,4,5]
# first loop - number of items to keep out
sets = []
def genSubsets(s, j):
    print(j)
    if j >= len(initSet)-1 or len(s) > len(initSet):
        sets.append(s)
        return s
    for i in j+1,range(len(initSet)):
        # Case without current element
        genSubsets(s,i)
        # Case with current element
        s.append(initSet[i])
        genSubsets(s,i)
    return s
print(genSubsets(initSet, 0))
