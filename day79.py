import copy
array = [10,5,1]
def check_ndc(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

def check(array):
    for i in range(len(array)):
        a = copy.deepcopy(array)
        del a[i]
        if check_ndc(a):
            return True
    return False
print(check(array))
