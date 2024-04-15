# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/200.py
def get_stab(list_of_intervals):
    start, end = zip(*list_of_intervals)
    return min(end), max(start)


if __name__ == "__main__":
    print(get_stab([(1, 4), (4, 5), (7, 9), (9, 12)]))