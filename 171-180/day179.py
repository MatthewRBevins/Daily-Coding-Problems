traversal = [2, 4, 3, 8, 7, 5]
class BT:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
    def hasParent(self):
        return self.parent != None

b = BT(traversal[len(traversal)-1])
traversal.reverse()
p = b
for i in range(1,len(traversal)):
    if traversal[i] > p.val:
        p.right = BT(traversal[i], parent=p)
        p = p.right
    else:
        c = p
        lowestWithEmptyLeft = None
        while c.hasParent():
            if c.left is None:
                lowestWithEmptyLeft = c
            c = c.parent
        if c.left is None:
            lowestWithEmptyLeft = c
        lowestWithEmptyLeft.left = BT(traversal[i], parent=lowestWithEmptyLeft)
        p = lowestWithEmptyLeft.left
print(b.val)
print(b.right.val)
print(b.right.right.val)
print(b.left.val)
print(b.left.left.val)
print(b.left.right.val)