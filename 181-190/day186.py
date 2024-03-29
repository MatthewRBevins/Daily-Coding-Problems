arr = [5, 10, 15, 20, 25]
def checkDiff(cArr):
    arr1 = []
    arr2 = []
    for i in range(len(arr)):
        if i in cArr:
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])
    return abs(sum(arr1) - sum(arr2))
def recurse(cArr, level):
    if len(cArr) == len(arr):
        return checkDiff(cArr)
    best = sum(arr)
    for i in range(-1, len(arr)):
        if not i in cArr or i == -1:
            c = cArr.copy()
            c.append(i)
            a = recurse(c, 1)
            if a < best:
                best = a
    return best
print(recurse([], 0))