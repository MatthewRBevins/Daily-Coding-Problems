class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def paths(self, curPath, level):
        paths = []
        curPath.append(self.value)
        if self.left == None and self.right == None:
            return curPath
        if self.left != None:
            paths.append(self.left.paths(curPath, 1))
            if level == 0:
                print(self.left.paths(curPath, 1))
                print(paths)
        if self.right != None:
            if level == 0:
                print(self.right.paths(curPath, 1))
            paths.append(self.right.paths(curPath, 1))
        return paths

t = Node(1, Node(2), Node(3, Node(4), Node(5)))
print(t.paths([], 0))