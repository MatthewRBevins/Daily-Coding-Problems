# Solution from https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/009.py

def max_nonadjacent_sum(arr):
    including = 0
    excluding = 0
    for elem in arr:
        # updating maximum sum including and excluding the current element
        including, excluding = max(excluding + elem, elem), max(excluding, including)
        print(including)
        print(excluding)
        print("***")
    return max(including, excluding)
print(max_nonadjacent_sum([5, 1, 1, 5]))
