class BT:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def boustrophedon(self, level, pos, arr):
        arr.append([self.val, level, pos])
        if self.left != None:
            arr = self.left.boustrophedon(level+1, pos-(1/(level+1)), arr)
        if self.right != None:
            arr = self.right.boustrophedon(level+1, pos+(1/(level+1)), arr)
        return arr

t = BT(1, BT(2, BT(4), BT(5)), BT(3, BT(6), BT(7)))
b = t.boustrophedon(0, 0, [])
levels = []
for i in b:
    if i[1] >= len(levels):
        levels.append([i])
    else:
        levels[i[1]].append(i)

for i in levels:
    if i[0][1] % 2 == 0:
        for j in range(len(i)):
            for k in range(len(i)):
                if i[j][2] < i[k][2]:
                    temp = i[j]
                    i[j] = i[k]
                    i[k] = temp
    else:
        for j in range(len(i)):
            for k in range(len(i)):
                if i[j][2] > i[k][2]:
                    temp = i[j]
                    i[j] = i[k]
                    i[k] = temp
finalArr = []
for i in levels:
    for j in i:
        finalArr.append(j[0])
print(finalArr)