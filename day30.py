container = [3, 0, 1, 3, 0, 5]
total = 0
for i in range(max(container)):
    currentWithoutWall = 0
    canWall = False
    for j in container:
        if j > i:
            canWall = True
        if canWall:
            if j <= i:
                currentWithoutWall += 1
            else:
                total += currentWithoutWall
                currentWithoutWall = 0
print(total)
