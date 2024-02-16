array = [4, 1, 3, 5, 6]
index = 0
minus = 0
plus = 0
while index-minus > -1 or index+plus < len(array):
    minus += 1
    plus += 1
    if index-minus > -1 and array[index-minus] > array[index]:
        print(index-minus)
        break
    if index+plus < len(array) and array[index+plus] > array[index]:
        print(index+plus)
        break
