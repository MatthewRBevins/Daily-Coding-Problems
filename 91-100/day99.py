array = [100,4,200,1,3,2]
arraySet = set(array)
longest = 0
for i in range(len(array)):
    if not array[i]-1 in arraySet:
        j = array[i]
        while j in arraySet:
            j += 1
        l = j - array[i]
        if l > longest:
            longest = l
print(longest)