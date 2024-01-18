class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right


# Should be doing with pointer, not value, so this assumes that every node has a different value
def lca(v, w):
    c = v
    arr = [c.value]
    while c.parent != None:
        c = c.parent
        arr.append(c.value)
    c = w
    while c.parent != None:
        if c.value in arr:
            return c.value
        c = c.parent
    return -1

node = Node(1, Node(2, Node(3, Node(5, Node(6)), Node(4)), Node(9)))
node.left.parent = node
node.left.left.parent = node.left
node.left.right.parent = node.left
node.left.left.right.parent = node.left.left
node.left.left.left.parent = node.left.left
node.left.left.left.left.parent = node.left.left.left
v = node.left.left.right
w = node.left.left.left.left
print(v.value)
print(w.value)
print(lca(v,w))