import statistics
class BT:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def calcSubtree(self, sum):
        sum += self.val
        if self.left == None and self.right == None:
            return sum
        if self.left != None:
            sum = self.left.calcSubtree(sum)
        if self.right != None:
            sum = self.right.calcSubtree(sum)
        return sum
    def iterateSubtrees(self, sums):
        sums.append(self.calcSubtree(0))
        if self.left != None:
            sums = self.left.iterateSubtrees(sums)
        if self.right != None:
            sums = self.right.iterateSubtrees(sums)
        return sums

b = BT(5, BT(2), BT(-5))
print(statistics.mode(b.iterateSubtrees([])))
