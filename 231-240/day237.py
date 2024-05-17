from math import floor
import copy


class Kary:
    def __init__(self, value, children):
        self.value = value
        self.children = children
    def reflect(self, level):
        c = copy.deepcopy(self)
        for i in range(floor(len(c.children)/2)):
            temp = c.children[len(c.children)-i-1]
            c.children[len(c.children)-i-1] = c.children[i]
            c.children[i] = temp
            pass
        for i in range(len(c.children)):
            if c.children[i] != None:
                c.children[i] = c.children[i].reflect(1)
        if level == 0:
            print(c.children[0].value)
        return c

def checkEquiv(tree1, tree2):
    if tree1.value != tree2.value:
        return False
    for i in range(len(tree1.children)):
        if tree1.children[i] != None:
            c = checkEquiv(tree1.children[i], tree2.children[i])
            if not c:
                return False
    return True


tree = Kary(4, [Kary(3, [Kary(9, [None, None, None]), None, None]), Kary(5, [None, None, None]), Kary(3, [None, None, Kary(9, [None, None, None])])])
tree2 = tree.reflect(0)