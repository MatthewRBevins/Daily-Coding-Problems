array = [34, -50, 42, 14, -5, 86]
def findMaxSub(array):
    s = [[]]
    index = 0
    posneg = 1
    for i in range(len(array)):
        if posneg * array[i] > 0:
            s[index].append(array[i])
        else:
            s[index] = sum(s[index])
            s.append([array[i]])
            index += 1
            posneg *= -1
    s[index] = sum(s[index])
    poss = [[]]
    index = 0
    for i in range(1,len(s)):
        if s[i] + s[i-1] > 0:
            poss[index].append(s[i])
        else:
            poss[index] = sum(poss[index])
            poss.append([])
            index += 1
    poss[index] = sum(poss[index])
    return max(0,max(poss))
print(findMaxSub(array))
