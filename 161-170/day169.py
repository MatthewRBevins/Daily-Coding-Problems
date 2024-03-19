class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def hasNext(self):
        return self.next != None
    def add(self, val):
        c = self
        while c.hasNext():
            c = c.next
        c.next = LinkedList(val)
    def printList(self):
        c = self
        while c.hasNext():
            print(c.val)
            c = c.next
        print(c.val)

def merge_sort(head):
    if not head or not head.next:
        return head

    # Find the middle of the linked list
    prev = None
    slow = head
    fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None  # Splitting the list into two halves

    # Recursively sort each half
    left_half = merge_sort(head)
    right_half = merge_sort(slow)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    dummy = LinkedList()
    current = dummy

    # Merge the two sorted lists
    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    # Attach remaining elements
    if left:
        current.next = left
    if right:
        current.next = right

    return dummy.next
ll = LinkedList(4)
ll.add(1)
ll.add(-3)
ll.add(99)
ll.printList()
merge_sort(ll).printList()