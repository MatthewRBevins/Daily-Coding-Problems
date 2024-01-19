arr = [1,1,0,1]

def checkCanReach(arr):
    i = 0
    prevI = -1
    while i < len(arr):
        i = i + arr[i]
        if i == len(arr)-1:
            return True
        if i == prevI:
            return False
        prevI = i
    return False

print(checkCanReach(arr))