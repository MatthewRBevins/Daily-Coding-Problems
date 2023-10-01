def a(arr, k):
    for i in arr:
        if (k-i) in arr:
            return True
    return False
arr = [10, 15, 3, 7]
k = 17
print(a(arr, k))
