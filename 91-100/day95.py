l = [2,1,3]
# go through array
# check whether next elements are descending
# if so, replace previous element with next element up
# all other elements should be sorted
# condition for if 3,2,1

def checkIfNextElementsDescending(l, index):
    for i in range(index+2, len(l)):
        if l[i] > l[i-1]:
            return False
    return True

def findLocationOfNextElementUp(l, index):
    smallestDifferenceIndex = 0
    smallestDifferenceValue = 100
    for i in range(len(l)):
        if l[i] > l[index] and l[i]-l[index] < smallestDifferenceValue:
            smallestDifferenceValue = l[i]-l[index]
            smallestDifferenceIndex = i
    return [smallestDifferenceIndex, smallestDifferenceValue]

def sortArrayFromIndex(l, index):
    toSort = l[index:]
    toNotSort = l[:index]
    toSort.sort()
    for i in toSort:
        toNotSort.append(i)
    return toNotSort

def swapElements(l, index1, index2):
    temp = l[index1]
    l[index1] = l[index2]
    l[index2] = temp
    return l


if not checkIfNextElementsDescending(l, -1):
    l.sort()
    print(l)
else:
    for i in range(len(l)):
        if checkIfNextElementsDescending(l, i):
            print(i)
            nextElementUp = findLocationOfNextElementUp(l, i)
            l = swapElements(l, i, nextElementUp[0])
            l = sortArrayFromIndex(l, i+1)
            print(l)
            break