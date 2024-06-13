import copy
def arrayCompare(arr1, arr2):
    for i in arr1:
        if i in arr2:
            return True
    return False
def checkConnected(graph):
    c = []
    for i in graph:
        if ((not i[0] in c) and arrayCompare(c, i[1])) or len(c) == 0:
            c.append(i[0])
            for j in i[1]:
                if not j in c:
                    c.append(j)
    return len(c) >= len(graph)

g = [[1, [2, 3]], [2, [1, 3]], [3, [1, 2]]]
bridges = []
if not checkConnected(g):
    print("NOT CONNECTED")
else:
    for i in range(len(g)):
        gg = copy.deepcopy(g)
        gg.pop(i)
        if not checkConnected(gg):
            bridges.append(g[i])
    print(bridges)