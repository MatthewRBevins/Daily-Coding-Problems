def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def paths(self, curPath, level):
        curPath = [[self.value]]
        if self.right != None:
            nextStep = self.right.paths([], 1)
            for i in nextStep:
                curPath.append([self.value])
                curPath[len(curPath)-1].append(i)
        if self.left != None:
            nextStep = self.left.paths([], 1)
            for i in nextStep:
                curPath.append([self.value])
                curPath[len(curPath)-1].append(i)
        for i in range(len(curPath)):
            curPath[i] = flatten_list(curPath[i])
        if level == 0:
            newCurPath = []
            for i in curPath:
                searchVal = findNodeFromValue(self, i[len(i)-1])
                if (searchVal.left == None and searchVal.right == None):
                    newCurPath.append(i)
            curPath = newCurPath
        return curPath

def findNodeFromValue(tree, value):
    if tree.value == value:
        return tree
    if tree.left == None and tree.right == None:
        return False
    else:
        l = findNodeFromValue(tree.left, value)
        if l != False:
            return l
        r = findNodeFromValue(tree.right, value)
        if r != False:
            return r

# NOTE - SHOULD WORK WITH POINTERS ETC, RIGHT NOW ONLY WORKS IF EACH NODE HAS DIFFERENT VALUE

t = Node(1, Node(2), Node(3, Node(4), Node(5)))
print(t.paths([], 0))