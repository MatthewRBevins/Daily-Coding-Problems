# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/096.pyfrom copy import deepcopy
def generate_all_permutations(arr, l=0, r=None, res=None):
    if r is None:
        r = len(arr) - 1
    if l == r:
        res.append(list(arr))
        return res
    # generating all permutation using backtracking
    for i in range(l, r + 1):
        arr[l], arr[i] = arr[i], arr[l]
        generate_all_permutations(arr, l + 1, r, res)
        arr[l], arr[i] = arr[i], arr[l]
    return res


if __name__ == "__main__":
    print(generate_all_permutations([1, 2, 3], res=[]))
    print(generate_all_permutations([1, 2], res=[]))
    print(generate_all_permutations([1], res=[]))
    print(generate_all_permutations([], res=[]))