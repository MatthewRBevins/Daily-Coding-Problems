# 0 = a, 1 = b, 2 = c, 3 = d, 4 = e, 5 = f, 6 = g
adjacencyList = [
    [1, 3, 6, 5],
    [0, 2, 4],
    [1, 5],
    [0, 4, 6],
    [1, 3],
    [0, 2, 6],
    [0, 3, 5]
]
def checkConnected(connections, total, done, list):
    for i in connections:
        if not i in done:
            done.append(i)
            n = checkConnected(list[i], total, done.copy(), list)
            if n:
                return True
        if len(done) == total:
            return True
    return False
m = False
for i in range(len(adjacencyList)):
    for j in range(len(adjacencyList[i])):
        removedEdge = adjacencyList.copy()
        del removedEdge[i][j]
        del removedEdge[j][removedEdge[j].index(removedEdge[i][j])]
        if checkConnected(removedEdge[0], 7, [], removedEdge):
            print("NOT MINIMALLY CONNECTED")
            m = True
            break
    if m:
        break
if not m:
    print("MINIMALLY CONNECTED")
# delete edge
# check whether connected recursively