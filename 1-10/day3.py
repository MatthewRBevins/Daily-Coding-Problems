class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def serialize(self):
        l = '"None"'
        r = '"None"'
        if self.left:
            l = self.left.serialize()
        if self.right:
            r = self.right.serialize()
        return '"' + self.val + '":{' + l + ',' + r + '}'
    
s = '"root":{"left":{"left.left":{"None","None"},"None"},"right":{"None","None"}}'
# ['', 'root', ':{', 'left', ':{', 'left.left', ':{', 'None', ',', 'None', '},', 'None', '},', 'right', ':{', 'None', ',', 'None', '}}']
# :{ before: parent node, after: left node
# , before: left node, after: right node WHEN NONE
# }, before: left node, after: right node
def deserialize(s):
    s = s.split('"')
    n = 'p'
    node = None
    cc = []
    ln = False
    for i in range(len(s)-2):
        if s[i] == ':{':
            n = 'p,l'
        elif s[i] == ',':
            n = 'n,n'
        elif s[i] == '},':
            n = 'l,r'
        elif s[i] == '':
            pass
        else:
            if n == 'p':
                node = Node(s[i])
                c = node
                cc.append(c)
            elif n == 'p,l':
                if s[i] != 'None':
                    c.left = Node(s[i])
                    c = c.left
            elif n == 'n,n':
                c.left = None
                c.right = None
                ln = True
            elif n == 'l,r':
                if ln:
                    ln = False
                else:
                    c = cc[len(cc)-2]
                    c.right = Node(s[i])
    return node

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(deserialize(node.serialize()).left.left.val == 'left.left')
