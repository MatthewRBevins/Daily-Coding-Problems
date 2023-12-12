# from https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/061.py

def pow(base, power):
    if power == 0:
        return 1

    if power % 2 != 0:
        return pow((base * base), power // 2) * base
    return pow((base * base), power // 2)

print(pow(2,3))
