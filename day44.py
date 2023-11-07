arr = [2,4,1,3,5]
inv = 0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[i] > arr[j] and i < j:
            inv += 1
print(inv)
