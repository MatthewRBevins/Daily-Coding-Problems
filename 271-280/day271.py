def search(arr, val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        diff = high - low
        half_diff = 0
        for i in range(diff):
            if half_diff == diff:
                break
            half_diff += 1
        mid = low + half_diff
        if arr[mid] == val:
            return True
        elif arr[mid] < val:
            low = mid + 1
        elif arr[mid] > val:
            high = mid - 1
    return False

arr = [1, 3, 5, 6, 8, 9, 10]
print(search(arr, 3))
print(search(arr, 4))