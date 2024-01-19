string = "figehaeci"
chars = ["a","e","i"]
def findAllIndices(char, string):
    a = []
    for i in range(len(string)):
        if string[i] == char:
            a.append(i)
    return a
charIndices = []
for i in chars:
    charIndices.append(findAllIndices(i, string))

def rangee(settt, i):
    sett = settt.copy()
    sett.append(i)
    sett.sort()
    return sett[len(sett)-1] - sett[0]

def findLowestRange(settt, options):
    lowestRange = 100
    lowestIndex = 0
    print("***")
    sett = settt.copy()
    for i in range(len(options)):
        if rangee(sett, options[i]) < lowestRange:
            lowestRange = rangee(sett, options[i])
            lowestIndex = i
    return options[lowestIndex]
settt = []
for i in charIndices:
    l = findLowestRange(settt, i)
    settt.append(l)
settt.sort()
print(string[settt[0]:settt[len(settt)-1]+1])