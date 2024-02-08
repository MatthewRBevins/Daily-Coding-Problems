import copy
class Iterator:
    def __init__(self, arr):
        self.arr = arr
        self.index = 0
        self.cur = arr[0]

    def next(self):
        self.index += 1
        self.cur = self.arr[self.index]
        return self.cur

    def hasNext(self):
        return self.index + 1 < len(self.arr)-1


class PeekableInterface:
    def __init__(self, iterator):
        self.iterator = iterator

    def peek(self):
        copied = copy.deepcopy(self.iterator)
        return copied.next()

    def next(self):
        return self.iterator.next()

    def hasNext(self):
        return self.iterator.hasNext()


i = PeekableInterface(Iterator([1,2,3,4]))
print(i.next())
print(i.peek())
print(i.next())