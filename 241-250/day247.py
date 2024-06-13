class BT:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def checkHeight(bt, h):
    h += 1
    h1 = h
    h2 = h
    if bt.left != None:
        h1 = checkHeight(bt.left, h)
    if bt.right != None:
        h2 = checkHeight(bt.right, h)
    if h1 > h2:
        return h1
    else:
        return h2

b = BT(5, BT(4, BT(3)), BT(6))

def checkBalanced(bt):
    if bt.left != None and bt.right != None:
        if abs(checkHeight(bt.left, 0) - checkHeight(bt.right, 0)) > 1:
            return False
    if bt.left != None and not checkBalanced(bt.left):
        return False
    if bt.right != None and not checkBalanced(bt.right):
        return False
    return True

print(checkBalanced(b))