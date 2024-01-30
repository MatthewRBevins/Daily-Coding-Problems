OGTower = [
    [3,2,1],
    [],
    []
]

def makeMove(tower, start, end):
    print("***")
    print(tower)
    print(start)
    print(len(tower[start])-1)
    temp = tower[start][len(tower[start])-1]
    del tower[start][len(tower[start])-1]
    tower[end].append(len(tower[start])-1)
    return tower

def completeTower(tower, path):
    if len(tower[2]) == 3:
        return True
    options =  []
    for i in range(len(tower)):
        if len(tower[i]) > 0:
            for j in range(len(tower)):
                if not [i, j] in path:
                    options.append([i,j])
    for i in options:
        t = makeMove(tower, i[0], i[1])
        p = path.copy()
        p.append(i)
        if completeTower(tower, p) == True:
            return True
    return False

print(completeTower(OGTower, []))