class BT:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def bottom(self, horiz, values):
        print(self.value)
        values.append([self.value, horiz])
        v = values.copy()
        if self.left != None:
            a = self.left.bottom(horiz-1, values)
            for i in a:
                v.append(i)
        if self.right != None:
            a = self.right.bottom(horiz + 1, values)
            for i in a:
                v.append(i)
        return v



b = BT(5, BT(3, BT(1, BT(0)), BT(4)), BT(7, BT(6), BT(9, BT(8))))
v = b.bottom(0, [])
def sort_array(arr):
    return sorted(arr, key=lambda x: x[1])
sorted_array = sort_array(v)
bottom = []
current = None
for i in sorted_array:
    if current != i[1]:
        current = i[1]
        bottom.append(i[0])
    else:
        pass
print(bottom)