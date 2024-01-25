def rotate(arr, k):
    return arr[k:] + arr[:k]
arr = [1,2,3,4,5,6]
print(rotate(arr, 2))