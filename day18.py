def a(arr, k):
    f = []
    for i in range(len(arr)-k+1):
        f.append(max(arr[i:i+k]))
    return f
print(a([10,5,2,7,8,7],3))
