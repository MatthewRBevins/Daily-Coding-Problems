path = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
index = 0
def findPath(path, index, jumps):
    if path[index] == 0 and index < len(path)-1:
        return 1000
    if index == len(path)-1:
        return jumps
    minJumps = 1000
    for j in range(1, path[index]+1):
        if index + j < len(path):
            i2 = index + j
            f = findPath(path, i2, jumps+1)
            if f < minJumps:
                minJumps = f
    return minJumps

print(findPath(path, 0, 0))