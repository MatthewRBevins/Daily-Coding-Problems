# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/205.py

def get_next_helper(arr):
    length = len(arr)
    if length < 2:
        return arr
    # finding the last element arranged in ascending order
    for index in range(length - 1, -1, -1):
        if index > 0 and arr[index - 1] < arr[index]:
            break
    # if index is 0, arr is sorted in descending order
    if index == 0:
        arr.reverse()
        return arr
    # finding the next permutation
    for k in range(length - 1, index - 1, -1):
        if arr[k] > arr[index - 1]:
            arr[k], arr[index - 1] = arr[index - 1], arr[k]
            break
    # arranging the other elements in proper order
    size = (length - 1) + index
    for i in range(index, (size + 1) // 2):
        arr[i], arr[size - i] = arr[size - i], arr[i]
    return arr


def get_next(num: int) -> int:
    return int("".join(get_next_helper(list(str(num)))))


if __name__ == "__main__":
    print(get_next(48975))