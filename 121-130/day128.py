OGTower = [
    [9,8,7,6,5,4,3,2,1],
    [],
    []
]

def makeMove(tower, start, end):
    tt = tower.copy()
    temp = min(tower[start])
    del tower[start][tower[start].index(min(tower[start]))]
    tower[end].append(temp)
    return tt

def checkTower(tower):
    return len(tower[0]) == 0 and len(tower[1]) == 0

def moveOptions(tower):
    options = []
    for i in range(len(tower)):
        for j in range(len(tower)):
            if i != j and len(tower[i]) > 0 and not 1 in tower[i] and (len(tower[j]) == 0 or min(tower[i]) < min(tower[j])):
                options.append([i,j])
    return options

def completeTower(tower, size):
    while not checkTower(tower):
        for i in range(len(tower)):
            if 1 in tower[i]:
                if i == len(tower)-1:
                    tower = makeMove(tower, i, 0)
                    print("Move " + str(i) + " to " + str(0))
                else:
                    tower = makeMove(tower, i, i+1)
                    print("Move " + str(i) + " to " + str(i+1))
                break
        o = moveOptions(tower)
        if len(o) == 0:
            break
        tower = makeMove(tower, o[0][0], o[0][1])
        print("Move " + str(o[0][0]) + " to " + str(o[0][1]))
        
        
completeTower(OGTower, 8)