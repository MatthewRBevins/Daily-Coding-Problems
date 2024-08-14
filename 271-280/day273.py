def findFixedPoint(arr):
    for i,j in enumerate(arr):
        if i == j:
            return i
    return False

a1 = [-6, 0, 2, 40]
a2 = [1, 5, 7, 8]
print(findFixedPoint(a1))
print(findFixedPoint(a2))
