# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/230.py
from sys import maxsize


def calculate(eggs: int, floors: int) -> int:
    dp_mat = [[maxsize for _ in range(floors + 1)] for _ in range(eggs + 1)]
    # base cases
    for i in range(floors + 1):
        dp_mat[1][i] = i
        dp_mat[0][i] = 0
    for i in range(eggs + 1):
        dp_mat[i][0] = 0
    # populating the dp matrix
    for egg in range(2, eggs + 1):
        for floor in range(1, floors + 1):
            for i in range(1, floor + 1):
                temp = 1 + max(dp_mat[egg - 1][i - 1], dp_mat[egg][floor - i])
                dp_mat[egg][floor] = min(dp_mat[egg][floor], temp)
    return dp_mat[eggs][floors]


if __name__ == "__main__":
    print(calculate(2, 20))
    print(calculate(3, 15))