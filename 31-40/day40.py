arr = [6,1,3,3,3,6,6]
def findSingle(arr):
    for i in arr:
        if len(list(filter(lambda x: x != i, arr))) == len(arr)-1:
            return i
    return -1
print(findSingle(arr))
