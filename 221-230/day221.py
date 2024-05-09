# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/221.py

def get_nth_sevenish_num(number: int) -> int:
    curr = 1
    curr_iteration = 1
    while curr < number:
        curr_iteration += 1
        curr += curr_iteration

    curr -= curr_iteration
    result = 7 ** (curr_iteration - 1)
    curr_to_add = 1
    for _ in range(number - curr - 1):
        result += curr_to_add
        curr_to_add *= 7
    return result
print(get_nth_sevenish_num(5))