class Node:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r
    def invert(self):
        temp = self.l
        self.l = self.r
        self.r = temp
        if self.l != None:
            self.l.invert()
        if self.r != None:
            self.r.invert()
    def printTree(self, level, side):
        print(str(level) + ' | ' + side + ' | ' + self.val)
        if self.l != None:
            self.l.printTree(level+1, 'l')
        if self.r != None:
            self.r.printTree(level+1, 'r')
            

n = Node('a', Node('b', Node('d'), Node('e')), Node('c', Node('f')))
n.printTree(1, 'root')
n.invert()
n.printTree(1, 'root')