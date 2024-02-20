# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/148.py
def grayCode(n):
    if n == 0:
        return [""]
    prev = grayCode(n-1)
    base0 = ["0" + val for val in prev]
    base1 = ["1" + val for val in prev[::-1]]
    return base0 + base1
print(grayCode(2))