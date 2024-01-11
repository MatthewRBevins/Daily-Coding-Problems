class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def checkBST(self):
        lOK = False
        rOK = False
        if self.left != None:
            if self.left.val < self.val:
                lOK = True
            if not self.left.checkBST:
                lOK = False
        else:
            lOK = True
        if self.right != None:
            if self.right.val > self.val:
                rOK = True
            if not self.right.checkBST:
                rOK = False
        else:
            rOK = True
        return (lOK and rOK)

t = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, right=Node(14, left=Node(13))))
print(t.checkBST())