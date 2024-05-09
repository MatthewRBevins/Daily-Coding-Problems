s = [1, 2, 3, 10]
def findSums(array, curSum, pos):
    if pos == len(array):
        return [curSum]
    sums = []
    for i in range(2):
        c = 0
        c += curSum
        if i == 1:
            c += s[pos]
        f = findSums(array, c, pos+1)
        for j in range(len(f)):
            sums.append(f[j])
    return sums
f = findSums(s, 0, 0)
f.sort()
i = 1
while True:
    if not i in f:
        print(i)
        break
    i += 1