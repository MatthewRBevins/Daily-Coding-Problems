def listReverse(lst, i, j):
    a = lst[i:j+1]
    a.reverse()
    return lst[0:i] + list(a) + lst[j+1:]

arr = [9,3,4,1,2,7,6,8,5]

for i in arr:
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr = listReverse(arr, j, j+1)
print(arr)