l = [1,2,3]
def genPos(l, arr):
    p = []
    arrs = []
    for i in l:
        arr.append(i)
        if len(arr) == len(l):
            arrs.append(arr)
            arr = []
        else:
            arrs.append(genPos(l, arr))
    return arrs
print(genPos(l, []))