from timeit import timeit
array: [int] = [3, 4, -1, 1]
def h(arr):
    arr.sort()
    if not 1 in arr:
        return 1
    for i,v in enumerate(arr):
        if v > 0:
            if i == len(arr)-1:
                return arr[len(arr)-1]+1
            if arr[i+1] - v > 1:
                return v+1
print(timeit(lambda: h(array)))
