class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def compare(s, t):
    if s.value != t.value:
        return False
    if (s.left != None and t.left == None) or (s.left == None and t.left != None) or (s.right == None and t.right != None) or (s.right != None and t.right == None):
        return False
    if (s.left == None and t.left == None) and (s.right == None and t.right == None):
        return True
    l = -1
    r = -1
    if s.left != None and t.left != None:
        l = compare(s.left, t.left)
    if s.right != None and t.right != None:
        r = compare(s.right, t.right)
    if l == False or r == False:
        return False
    return True

t = Node(1,Node(2,Node(6)),Node(4,Node(5)))
s = Node(1,Node(2,Node(3)),Node(4,Node(5)))
print(compare(s, t))