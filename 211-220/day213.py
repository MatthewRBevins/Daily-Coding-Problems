# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/213.py
ACCEPTABLE_NUMBERS = set([str(i) for i in range(256)])


def get_ip_combinations_helper(
    string: str, curr, accumulator
) -> None:
    if not string and len(curr) == 4:
        accumulator.append(list(curr))
        return
    elif len(curr) > 4:
        return

    curr_part = ""
    for char in string:
        curr_part += char
        length = len(curr_part)
        if length > 3:
            return
        if curr_part in ACCEPTABLE_NUMBERS:
            get_ip_combinations_helper(
                string[length:], list(curr) + [curr_part], accumulator
            )


def get_ip_combinations(string: str):
    accumulator = []
    get_ip_combinations_helper(string, [], accumulator)
    return [".".join(combination) for combination in accumulator]


if __name__ == "__main__":
    print(get_ip_combinations("2542540123"))