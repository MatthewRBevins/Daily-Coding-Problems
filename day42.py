S = [12,1,61,5,9,2]
k = 24
def findSum(S, k, sol, indices):
    if sum(sol) > k:
        return False
    for j,i in enumerate(S):
        if not j in indices:
            sol.append(i)
            indices.append(j)
            if sum(sol) == k:
                return sol
            else:
                s = findSum(S, k, sol, indices)
                if s != False:
                    return s
                indices = indices[0:len(indices)-1]
    return False
print(findSum(S, k, [], []))
