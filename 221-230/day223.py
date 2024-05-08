# Morris traversal uses O(1) time for inorder traversal of binary tree
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def morris_inorder_traversal(root):
    current = root
    while current:
        if current.left is None:
            print(current.val)  # Visit the current node
            current = current.right
        else:
            # Find the inorder predecessor of current node
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            # Make current node as the right child of its inorder predecessor
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                # Revert the changes made in if condition to restore the original tree
                predecessor.right = None
                print(current.val)  # Visit the current node
                current = current.right


# Example usage:
# Constructing a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Performing Morris Inorder Traversal
morris_inorder_traversal(root)