numbers = [10, 7, 76, 415]
for i in range(len(numbers)):
    numbers[i] = str(numbers[i])
def enhancedSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and int(str(arr[i]) + str(arr[j])) > int(str(arr[j]) + str(arr[i])):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr
print("".join(enhancedSort(numbers)))
