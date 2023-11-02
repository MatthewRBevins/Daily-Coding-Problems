class Node:
    def __init__(value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def findSecondLargest(self, largest, secondLargest):
        if self.left is None and self.right is None:
            if self.value < largest and self.value > secondLargest:
                return self.value
            else:
                return None
        else:
            if self.value > largest:
                largest = self.value
            elif self.value < largest and self.value > secondLargest:
                secondLargest = self.value
            if self.left is not None:
                l = self.left.findSecondLargest(largest, secondLargest)
            if self.right is not None:
                r = self.right.findSecondLargest(largest, secondLargest)
