def fib(n):
    x = 1
    y = 1
    i = 3
    if n <= 2:
        return 1
    while True:
        temp = y
        y = x + y
        x = temp
        if i == n:
            return y
        i += 1
print(fib(3))