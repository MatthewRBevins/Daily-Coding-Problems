# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/156.py
def min_square_num(num: int, accumulator: int = 0) -> int:
    if num == 0:
        return accumulator
    elif num == 1:
        return accumulator + 1

    largest_square_divisor = int(num ** 0.5) ** 2
    num = num - largest_square_divisor
    accumulator += 1
    return min_square_num(num, accumulator)
print(min_square_num(27))