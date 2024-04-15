array = [1, 3, 1, 2, 0, 1]
array2 = [1, 2, 1, 0, 0]
def checkCan(array, index):
    if index == len(array)-1:
        return True
    for i in range(array[index]+1):
        if i != 0:
            a = checkCan(array, index+i)
            if a:
                return True
    return False
print(checkCan(array2, 0))