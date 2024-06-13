arr = [1, 123, 509, 12, 39]
max = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j and arr[i] ^ arr[j] > max:
            max = arr[i] ^ arr[j]
print(max)