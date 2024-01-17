rules = ['A NW B', 'A N B']
def checkRules(rules):
    northsouth = []
    eastwest = []
    for i in rules:
        i = i.split(" ")
        if "E" in i[1]:
            if i[0] in eastwest and i[2] in eastwest:
                if eastwest.index(i[0]) > eastwest.index(i[2]):
                    return False
            if i[0] in eastwest and i[2] not in eastwest:
                eastwest.insert(eastwest.index(i[0])+1,i[2])
            if i[2] in eastwest and i[0] not in eastwest:
                eastwest.insert(eastwest.index(i[2])-1,i[0])
            else:
                eastwest.append(i[0])
                eastwest.append(i[2])
        if "W" in i[1]:
            if i[2] in eastwest and i[0] in eastwest:
                if eastwest.index(i[2]) > eastwest.index(i[0]):
                    return False
            if i[2] in eastwest and i[0] not in eastwest:
                eastwest.insert(eastwest.index(i[2])+1,i[0])
            if i[0] in eastwest and i[2] not in eastwest:
                eastwest.insert(eastwest.index(i[0])-1,i[2])
            else:
                eastwest.append(i[2])
                eastwest.append(i[0])
        if "N" in i[1]:
            if i[0] in northsouth and i[2] in northsouth:
                if northsouth.index(i[0]) > northsouth.index(i[2]):
                    return False
            if i[0] in northsouth and i[2] not in northsouth:
                northsouth.insert(northsouth.index(i[0])+1,i[2])
            if i[2] in northsouth and i[0] not in northsouth:
                northsouth.insert(northsouth.index(i[2])-1,i[0])
            else:
                northsouth.append(i[0])
                northsouth.append(i[2])
        if "S" in i[1]:
            if i[2] in northsouth and i[0] in northsouth:
                if northsouth.index(i[2]) > northsouth.index(i[0]):
                    return False
            if i[2] in northsouth and i[0] not in northsouth:
                northsouth.insert(northsouth.index(i[2])+1,i[0])
            if i[0] in northsouth and i[2] not in northsouth:
                northsouth.insert(northsouth.index(i[0])-1,i[2])
            else:
                northsouth.append(i[2])
                northsouth.append(i[0])
    return True
print(checkRules(rules))