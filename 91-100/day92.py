hashmap = dict({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []})
toSort = []
for i in hashmap.keys():
    toSort.append([len(hashmap[i]), i])
toSort.sort()
def mapper(val):
    return val[1]
valid = True
for i in range(1, len(toSort)):
    if toSort[i][0] - toSort[i-1][0] != 1:
        valid = False
        print('el bruh')
        break
if valid:
    print(list(map(mapper, toSort)))