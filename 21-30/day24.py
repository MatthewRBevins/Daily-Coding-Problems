class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.locked = False
    def is_locked(self):
        return self.locked
    def checkDescendantsLocked(self):
        l = True
        r = True
        if self.left:
            l = self.left.checkDescendantsLocked()
        if self.right:
            r = self.right.checkDescendantsLocked()
        if self.locked or l == False or r == False:
            return False
        return True
    def lock(self):
        # check ancestors
        p = self.parent
        while p != None:
            if p.is_locked():
                return False
            p = p.parent

        # check descendants
        if self.checkDescendantsLocked() == False:
            return False

        self.locked = True
        return True
    def unlock(self):
        # check ancestors
        p = self.parent
        while p != None:
            if p.is_locked():
                return False
            p = p.parent

        # check descendants
        if self.checkDescendantsLocked() == False:
            return False

        self.locked = False
        return True
bt = Node(1,Node(2,Node(3),Node(4)),Node(5,Node(6),Node(7)))

print(bt.left.lock())
print(bt.lock())
