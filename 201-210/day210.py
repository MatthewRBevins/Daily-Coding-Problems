def collatz(n):
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return n
for i in range(1, 1000):
    print(collatz(i))