preorder = ['a','b','d','e','c','f','g']
inorder = ['d','b','e','a','f','c','g']

class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def construct(head, inorder):
    left = inorder[0:inorder.index(head)]
    right = inorder[inorder.index(head)+1:len(inorder)]
    n = Node(head)
    if len(left) > 1:
        lowest = [100,'']
        for i in left:
            print(i)
            if preorder.index(i) < lowest[0]:
                lowest = [preorder.index(i), i]
        lefthead = lowest[1]
        print('**')
        print(lefthead)
        print('*')
        n.left = construct(lefthead, left)
    else:
        n.left = left[0]

    if len(right) > 1:
        lowest = [100,'']
        for i in right:
            if preorder.index(i) < lowest[0]:
                lowest = [preorder.index(i), i]
        righthead = lowest[1]
        print(righthead)
        n.right = construct(righthead, right)
    else:
        n.right = right[0]
    return n
    
    
nn = construct(preorder[0], inorder)
