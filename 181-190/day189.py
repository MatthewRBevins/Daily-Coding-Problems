arr = [5, 1, 3, 5, 2, 3, 4, 1]
l = 0

for i in range(len(arr)):
    c = 0
    for j in range(i,len(arr)):
        if arr[j] not in arr[i:j]:
            c += 1
        else:
            break
    if c > l:
        l = c
print(l)