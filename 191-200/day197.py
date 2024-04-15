array = [1,2,3,4,5]
k = 2
for i in range(k):
    array.insert(0, array[len(array)-1])
    del array[len(array)-1]
print(array)