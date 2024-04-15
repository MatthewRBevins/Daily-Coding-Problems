# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/203.py
def find_pivot_helper(arr, low: int, high: int) -> int:
    if low == high:
        return high

    mid = (high + low) // 2
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    elif mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    elif arr[mid] > arr[high]:
        return find_pivot_helper(arr, mid + 1, high)
    return find_pivot_helper(arr, low, mid - 1)


def find_pivot(arr) -> int:
    length = len(arr)
    # the pivot returns the last index of the rotated array
    pivot = find_pivot_helper(arr, 0, length)
    return (pivot + 1) % length

print(find_pivot([5, 7, 10, 3, 4]))