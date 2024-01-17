class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right
        