array = [34, -50, 42, 14, -5, 86]

s = 0
prevs = [[]]
prevVals = [-1]
for i in range(len(array)):
    if array[i] < 0:
        prevs[len(prevs)-1].append(i)
        prevVals.append(s)
        prevs.append([i+1])
        s = 0
    s += array[i]
print(array[prevs[prevVals.index(max(prevVals))][0]:prevs[prevVals.index(max(prevVals))][1]])
