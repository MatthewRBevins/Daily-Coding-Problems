from copy import deepcopy
from typing import Tuple

# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/199.py

class Stack:
    """
    Stack Class for LIFO Structure

    Functions:
    is_empty: Check if the stack is empty
    peek: Get the value at the stack top without removing it
    pop: Pop the object at the top of the stack
         Raises erorr if the stack is empty
    push: Push an object to the top of the stack
    """

    def __init__(self) -> None:
        self.stack = []
        self.rear = -1
        self.top = -1

    def __repr__(self) -> str:
        return str(self.stack)

    def __len__(self) -> int:
        return len(self.stack)

    def __delitem__(self, position: int) -> None:
        del self.stack[position]
        self.rear -= 1

    def __getitem__(self, position: int):
        return self.stack[position]

    def __setitem__(self, position: int, value) -> None:
        self.stack[position] = value

    def is_empty(self) -> bool:
        # Check if the stack is empty
        return not bool(self.stack)

    def peek(self):
        # Get the value at the stack top without removing it
        if self.is_empty():
            raise Exception("Stack Underflow. Cannot peek at an empty stack")
        return self.stack[-1]

    def pop(self):
        # Pop the value at the stack top
        if self.rear == -1:
            raise Exception("Stack Underflow. Cannot pop from an empty stack")
        elif self.top == 0:
            self.rear = -1
            self.top = -1
        else:
            self.top -= 1
        return self.stack.pop()

    def push(self, val) -> None:
        # Push a new value to the stack top
        if self.rear == -1:
            self.stack.append(val)
            self.rear = 0
            self.top = 0
        else:
            self.stack.append(val)
            self.top += 1
def get_min_changes_helper(
    string: str, modifications: int, stack, current: str
) -> Tuple[int, str]:
    if not string and stack.is_empty():
        return modifications, current
    elif not string:
        additions = len(stack)
        return modifications + additions, current + (")" * additions)

    if string[0] == "(":
        stack_added = deepcopy(stack)
        stack_added.push("(")
        modifications1, string1 = get_min_changes_helper(
            string[1:], modifications, stack_added, current + "("
        )  # adding to stack
        modifications2, string2 = get_min_changes_helper(
            string[1:], modifications + 1, stack, current
        )  # removing from string
        return min(
            [(modifications1, string1), (modifications2, string2)],
            key=lambda tup: tup[0],
        )

    if not stack.is_empty():
        stack.pop()
        return get_min_changes_helper(string[1:], modifications, stack, current + ")")
    return get_min_changes_helper(string[1:], modifications + 1, stack, current)


def get_min_changes(string: str) -> str:
    _, res = get_min_changes_helper(string, 0, Stack(), "")
    return res


if __name__ == "__main__":
    print(get_min_changes("(()"))
    print(get_min_changes("))()("))
    print(get_min_changes("()(()"))
    print(get_min_changes("()(()))"))
    print(get_min_changes(")(())"))
    print(get_min_changes("())("))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(2 ^ n)
"""