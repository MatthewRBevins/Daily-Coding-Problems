def array_swap(array, in1, in2):
    temp = array[in2]
    array[in2] = array[in1]
    array[in1] = temp
    return array

p = [2, 1, 0]
array = ["a", "b", "c"]
done = []
for i in range(len(array)):
    if not p[i] in done:
        array = array_swap(array, i, p[i])
        done.append(i)
print(array)