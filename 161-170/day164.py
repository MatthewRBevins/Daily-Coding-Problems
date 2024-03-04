arr = [1,2,4,6,5,3,2]
for i in range(len(arr)):
    if arr[i] in arr[i+1:]:
        print(arr[i])
        break