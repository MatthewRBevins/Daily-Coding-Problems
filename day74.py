n = 6
x = 6
def m1():
    c = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i*j == x:
                c += 1
    return c