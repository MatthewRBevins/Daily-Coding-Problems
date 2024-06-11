def findMin(o, t, th):
    if o <= t and o <= th:
        return o
    elif t <= th:
        return t
    else:
        return th
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def findMinSum(self, min, level):
        l = 0
        ll = [None, 100]
        if self.left:
            l = self.left.val
            ll = self.left.findMinSum(min, level+1)
        r = 0
        rr = [None, 100]
        if self.right:
            r = self.right.val
            rr = self.right.findMinSum(min, level+1)
        s = l + r
        if s == 0:
            s = 100
        m = findMin(ll[1], rr[1], s)
        lol = level
        if m == ll[1]:
            lol = ll[0]
        elif m == rr[1]:
            lol = rr[0]
        return [lol, m]
bt = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7)))
print(bt.findMinSum(100, 0))